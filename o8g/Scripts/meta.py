    # Python Scripts for the Star Wards LCG definition for OCTGN
    # Copyright (C) 2012  Konstantine Thoukydides

    # This python script is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this script.  If not, see <http://www.gnu.org/licenses/>.


import re, time
from collections import defaultdict, namedtuple

Automations = {'Play'                   : False, # If True, game will automatically trigger card effects when playing or double-clicking on cards. Requires specific preparation in the sets.
               'HARDCORE'               : True, # If True, game will not anymore display highlights and announcements on card waiting to trigger.
               'Triggers'               : False, # If True, game will search the table for triggers based on player's actions, such as installing a card, or discarding one.
               'WinForms'               : False, # If True, game will use the custom Windows Forms for displaying multiple-choice menus and information pop-ups
               'Placement'              : False, # If True, game will try to auto-place cards on the table after you paid for them.
               'Start/End-of-Turn/Phase': False, # If True, game will automatically trigger effects happening at the start of the player's turn, from cards they control.                
              }


UniCode = True # If True, game will display credits, clicks, trash, memory as unicode characters

debugVerbosity = -1 # At -1, means no debugging messages display

startupMsg = False # Used to check if the player has checked for the latest version of the game.

gameGUID = None # A Unique Game ID that is fetched during game launch.
#totalInfluence = 0 # Used when reporting online
#gameEnded = False # A variable keeping track if the players have submitted the results of the current game already.

CardsAA = {} # Dictionary holding all the AutoAction scripts for all cards
CardsAS = {} # Dictionary holding all the autoScript scripts for all cards
Stored_Keywords = {} # A Dictionary holding all the Keywords a card has.

gatheredCardList = False # A variable used in reduceCost to avoid scanning the table too many times.
costModifiers = [] # used in reduceCost to store the cards that might hold potential cost-modifying effects. We store them globally so that we only scan the table once per execution
#cardAttachementsNR = {} # A dictionary which counts how many attachment each host has
#hostCards = {} # A dictionary which holds which is the host of each attachment
myAllies = []
MPxOffset = 0
MPyOffset = 0
    
def storeSpecial(card): 
# Function stores into a shared variable some special cards that other players might look up.
   debugNotify(">>> storeSpecial(){}".format(extraASDebug())) #Debug
   specialCards = eval(me.getGlobalVariable('specialCards'))
   specialCards[card.Type] = card._id
   me.setGlobalVariable('specialCards', str(specialCards))

def storeObjective(card, GameSetup = False): 
# Function stores into a shared variable the current objectives of the player, so that other players might look them up.
# This function also reorganizes the objectives on the table
   debugNotify(">>> storeObjective(){}") #Debug
   currentObjectives = eval(me.getGlobalVariable('currentObjectives'))
   currentObjectives.append(card._id)
   debugNotify("About to iterate the list: {}".format(currentObjectives))
   if GameSetup:
      for iter in range(len(currentObjectives)):
         Objective = Card(currentObjectives[iter])
         Objective.moveToTable(MPxOffset + (playerside * -310) - 25, MPyOffset + (playerside * 10) + (70 * iter * playerside) + yaxisMove(Objective), True)
         Objective.highlight = ObjectiveSetupColor # During game setup, we put the objectives face down so that the players can draw their hands before we reveal them.
         Objective.orientation = Rot0
         Objective.peek()
   else:
      for iter in range(len(currentObjectives)):
         Objective = Card(currentObjectives[iter])
         Objective.moveToTable( MPxOffset + (playerside * -310) - 25, MPyOffset + (playerside * 10) + (70 * iter * playerside) + yaxisMove(Objective))
         orgAttachments(Objective)
      update() # We put a delay here to allow the table to read the card autoscripts before we try to execute them.
      debugNotify("About to execure play Scripts") #Debug      
      executePlayScripts(card, 'PLAY')
   debugNotify("About to set currentObjectives") #Debug      
   me.setGlobalVariable('currentObjectives', str(currentObjectives))
   debugNotify("<<< storeObjective()") #Debug

def getSpecial(cardType, player = me):
# Functions takes as argument the name of a special card, and the player to whom it belongs, and returns the card object.
   debugNotify(">>> getSpecial(){}".format(extraASDebug())) #Debug
   if cardType == 'BotD':   
      BotD = getGlobalVariable('Balance of the Force')
      debugNotify("<<< getSpecial() by returning: {}".format(Card(num(BotD))))
      return Card(num(BotD))
   else: 
      specialCards = eval(player.getGlobalVariable('specialCards'))
      debugNotify("<<< getSpecial() by returning: {}".format(Card(specialCards[cardType])))
      return Card(specialCards[cardType])

def checkUnique (card):
   debugNotify(">>> checkUnique(){}".format(extraASDebug())) #Debug
   mute()
   if not re.search(r'Unique', getKeywords(card)): 
      debugNotify("<<< checkUnique() - Not a unique card") #Debug
      return True #If the played card isn't unique do nothing.
   ExistingUniques = [ c for c in table
         if c.owner == me and c.isFaceUp and fetchProperty(c, 'name') == fetchProperty(card, 'name') and re.search(r'Unique', getKeywords(c)) ]
   if len(ExistingUniques) != 0 and not confirm("This unique card is already in play. Are you sure you want to play {}?\n\n(If you do, your existing unique card will be Trashed at no cost)".format(fetchProperty(card, 'name'))) : return False
   else:
      for uniqueC in ExistingUniques: trashForFree(uniqueC)
   debugNotify("<<< checkUnique() - Returning True") #Debug
   return True   

def findOpponent(position = '#1', multiText = "Choose which opponent you're targeting with this effect."):
   debugNotify(">>> findOpponent()") #Debug
   opponentList = fetchAllOpponents()
   if len(opponentList) == 1: opponentPL = opponentList[0]
   else:
      if position == 'Ask':
         debugNotify("About to Ask for opponent")
         choice = SingleChoice(multiText, [pl.name for pl in opponentList])
         opponentPL = opponentList[choice]         
      else:
         debugNotify("looking for opponent in position {}".format(position))
         for player in opponentList:
            if player.getGlobalVariable('PLnumber') == position: opponentPL = player
   # Just a quick function to make the code more readable
   debugNotify(">>> findOpponent() returning {}".format(opponentPL.name)) #Debug
   return opponentPL
      
def findAlly(position = '#1', multiText = "Choose which ally you're targeting with this effect."):
   debugNotify(">>> findAlly()") #Debug
   if len(myAllies) == 1: allyPL = myAllies[0]
   else:
      if position == 'Ask':
         debugNotify("About to Ask for ally")
         choice = SingleChoice(multiText, [pl.name for pl in myAllies])
         allyPL = myAllies[choice]         
      else:
         debugNotify("looking for Ally in position {}".format(position))
         for player in myAllies:
            if player.getGlobalVariable('PLnumber') == position: allyPL = player
   # Just a quick function to make the code more readable
   debugNotify(">>> findAlly() returning {}".format(allyPL.name)) #Debug
   return allyPL
      
def ofwhom(Autoscript, controller = me, multiText = None): 
   debugNotify(">>> ofwhom(){}".format(extraASDebug(Autoscript))) #Debug
   targetPLs = []
   playerList = []
   if re.search(r'o[fn]Opponent', Autoscript) or re.search(r'o[fn]AllOpponents', Autoscript):
      if not multiText: multiText = "Choose which opponent you're targeting with this effect."
      if len(getPlayers()) > 1:
         for player in getPlayers():
            if player.getGlobalVariable('Side') == '': 
               debugNotify("ofwhom() -- rejecting {} because they are a spectator".format(player))
               continue # This is a spectator 
            elif player.getGlobalVariable('Side') != controller.getGlobalVariable('Side'): 
               playerList.append(player) # Opponent needs to be not us, and of a different type. 
               debugNotify("ofwhom() -- appending {}".format(player),4)
            else: debugNotify("ofwhom() -- rejecting {} because their side {} matches controller Side ({})".format(player, player.getGlobalVariable('Side'), controller.getGlobalVariable('Side')), 4)
         debugNotify("playerList = {}".format(playerList), 4)
         if len(playerList) == 1: targetPLs.append(playerList[0])
         elif len(playerList) == 0: 
            notify(":::Error::: No Valid Opponents found. Returning Myself as failsafe")
            targetPLs.append(me)
         else:
            if re.search(r'o[fn]AllOpponents', Autoscript): targetPLs = playerList
            else:
               choice = SingleChoice(multiText, [pl.name for pl in playerList])
               targetPLs.append(playerList[choice])
      else: 
         if debugVerbosity >= 1: whisper("There's no valid Opponents! Selecting myself.")
         targetPLs.append(me)
   elif re.search(r'o[fn]Team', Autoscript) or re.search(r'o[fn]Allies', Autoscript) or re.search(r'o[fn]AllAllies', Autoscript):
      if not multiText: multiText = "Choose which allied player you're targeting with this effect."
      if len(getPlayers()) > 1:
         for player in getPlayers():
            if player.getGlobalVariable('Side') == '': 
               debugNotify("ofwhom() -- rejecting {} because they are a spectator".format(player))
               continue # This is a spectator 
            elif player.getGlobalVariable('Side') == controller.getGlobalVariable('Side'):
               if re.search(r'o[fn]Allies', Autoscript) and player == controller: 
                  debugNotify("ofwhom() -- rejecting {} because we're looking only for their allies".format(player, 4))
               else:
                  playerList.append(player) # Opponent needs to be not us, and of a different type. 
                  debugNotify("ofwhom() -- appending {}".format(player),4)
            else: debugNotify("ofwhom() -- rejecting {} because their side {} does not match controller Side ({})".format(player, player.getGlobalVariable('Side'), controller.getGlobalVariable('Side')), 4)
         if len(playerList) == 1: targetPLs.append(playerList[0])
         elif len(playerList) == 0: 
            notify(":::Error::: No Valid Allies found. Returning Myself as failsafe")
            targetPLs.append(me)
         else: 
            if re.search(r'o[fn]AllAllies', Autoscript): targetPLs = playerList
            else:
               choice = SingleChoice(multiText, [pl.name for pl in playerList])
               targetPLs.append(playerList[choice])
      else: 
         if debugVerbosity >= 1: whisper("There's no valid Opponents! Selecting myself.")
         targetPLs.append(me)
   else: targetPLs.append(controller) # If the script does not mention Opponent or Ally, then it's targeting the controller
   debugNotify("<<< ofwhom() returns {}".format([pl.name for pl in targetPLs]))
   return targetPLs

def fetchAllOpponents(targetPL = me):
   debugNotify(">>> fetchAllOpponents()") #Debug
   opponentList = []
   if len(getPlayers()) > 1:
      for player in getPlayers():
         if player.getGlobalVariable('Side') == '': continue # This is a spectator 
         if player != targetPL and player.getGlobalVariable('Side') != targetPL.getGlobalVariable('Side'): opponentList.append(player) # Opponent needs to be not us, and of a different type. 
   else: opponentList = [me] # For debug purposes
   debugNotify("<<< fetchAllOpponents() returning size {} ".format(len(opponentList))) #Debug
   return opponentList   
   
def fetchAllAllies(targetPL = me):
   debugNotify(">>> fetchAllAllies()") #Debug
   alliesList = []
   if len(getPlayers()) > 1:
      for player in getPlayers():
         if player.getGlobalVariable('Side') == '': continue # This is a spectator 
         if player == targetPL or player.getGlobalVariable('Side') == targetPL.getGlobalVariable('Side'): alliesList.append(player) # Opponent needs to be not us, and of a different type. 
   else: alliesList = [me] # For debug purposes
   debugNotify("<<< fetchAllAllies() returning size {} ".format(len(alliesList))) #Debug
   return alliesList   
   
def modifyDial(value):
   debugNotify(">>> modifyDial(). Value = {}".format(value)) #Debug   
   for player in getPlayers(): player.counters['Death Star Dial'].value += value
   if value > 0: autoscriptOtherPlayers('DialIncrease',Affiliation)
   else: autoscriptOtherPlayers('DialDecrease',Affiliation)
   if len(myAllies) == 2: winningValue = 16
   else: winningValue = 12
   if me.counters['Death Star Dial'].value >= winningValue:
      notify("===::: The Dark Side wins the Game! :::====")
      reportGame('DialVictory')   

def resetAll(): # Clears all the global variables in order to start a new game.
   global unpaidCard, edgeRevealed, firstTurn, debugVerbosity
   global Side, Affiliation, limite1dPlayed, myAllies, MPxOffset
   debugNotify(">>> resetAll(){}".format(extraASDebug())) #Debug
   mute()
   if len(table) > 0: 
      for c in table: 
         if c.Type == 'Affiliation' and c.owner == me: reconnect() # Attempting to catch a game reconnecting
      return # This function should only ever run after game start or reset. We abort in case it's a reconnect.
   Side = None
   Affiliation = None
   unpaidCard = None 
   myAllies = []
   MPxOffset = 0
   MPyOffset = 0
   edgeRevealed = False
   firstTurn = True
   limitedPlayed = False
   #cardAttachementsNR.clear()
   #cardAttachementsNR.clear()
   hostCards = eval(getGlobalVariable('Host Cards'))
   hostCards.clear()
   setGlobalVariable('Host Cards',str(hostCards))
   selectedAbility = eval(getGlobalVariable('Stored Effects'))
   selectedAbility.clear()
   setGlobalVariable('Stored Effects',str(selectedAbility))
   if len(getPlayers()) > 1: debugVerbosity = -1 # Reset means normal game.
   elif debugVerbosity != -1 and confirm("Reset Debug Verbosity?"): debugVerbosity = -1 
   capturedCards = eval(getGlobalVariable('Captured Cards')) # This variable is for captured cards.
   capturedCards.clear()
   setGlobalVariable('Captured Cards',str(capturedCards))
   edgeRevealed = eval(getGlobalVariable('Revealed Edge'))
   for plName in edgeRevealed: edgeRevealed[plName] = False # Clearing some variables just in case they were left over. 
   setGlobalVariable('Revealed Edge',str(edgeRevealed))
   setGlobalVariable('Engaged Objective','None')
   setGlobalVariable('Current Attacker','None')
   setGlobalVariable('Engagement Phase','0')
   setGlobalVariable('Turn','0')
   me.setGlobalVariable('freePositions',str([]))
   me.setGlobalVariable('currentObjectives', '[]')
   me.setGlobalVariable('PLnumber', '') 
   me.setGlobalVariable('MPxOffset', '0')    
   me.setGlobalVariable('MPyOffset', '0')    
   me.setGlobalVariable('myAllies', '[]')    
   resetGameStats()
   debugNotify("<<< resetAll()") #Debug
   
def placeCard(card): 
   mute()
   try:
      debugNotify(">>> placeCard() for card: {}".format(card)) #Debug
      if Automations['Placement']:
         debugNotify("We have placement automations",2) #Debug
         if card.Type == 'Unit': # For now we only place Units
            unitAmount = len([c for c in table if c.Type == 'Unit' and c.controller == me and c.highlight != UnpaidColor and c.highlight != EdgeColor and c.highlight != DummyColor]) - 1 # we reduce by 1, because it will always count the unit we're currently putting in the game
            debugNotify("my unitAmount is: {}.".format(unitAmount)) #Debug
            freePositions = eval(me.getGlobalVariable('freePositions')) # We store the currently released position
            debugNotify("my freePositions is: {}.".format(freePositions),2) #Debug
            if freePositions != []: # We use this variable to see if there were any discarded units and we use their positions first.
               positionC = freePositions.pop() # This returns the last position in the list of positions and deletes it from the list.
               debugNotify("positionC is: {}.".format(positionC)) #Debug
               card.moveToTable(positionC[0],positionC[1])
               me.setGlobalVariable('freePositions',str(freePositions))
            else:
               if len(myAllies) == 1:
                  loopsNR = unitAmount / 7 
                  loopback = 7 * loopsNR
               else: 
                  loopsNR = unitAmount / 6 # With multiplayer, we only allow 6 units per player to prevent overlapping
                  loopback = 6 * loopsNR
               if getSetting('Unit Placement', 'Center') == 'Center': # If the unit placement is the default center orientation, then we start placing units from the center outwards
                  if unitAmount == 0: xoffset = MPxOffset + (playerside * 20) - 25
                  else: xoffset = MPxOffset + (-playerside * ((2 * (unitAmount % 2)) - 1) * (((unitAmount - loopback) + 1) / 2) * cheight(card,0)) + (playerside * 20) - 25 # The -25 is an offset to help center the table.
                  debugNotify("xoffset is: {}.".format(xoffset)) #Debug
                  yoffset = MPyOffset + yaxisMove(card) + (cheight(card,3) * (loopsNR) * playerside) + (10 * playerside)
               else:                  
                  xoffset = MPxOffset + (playerside * (-325 + cheight(card,0))) + (playerside * cheight(card,0) * (unitAmount - loopback)) - 25
                  debugNotify("xoffset is: {}.".format(xoffset)) #Debug
                  yoffset = MPyOffset + yaxisMove(card) + (cheight(card,3) * (loopsNR) * playerside) + (10 * playerside)                  
               card.moveToTable(xoffset,yoffset)
            playUnitSound(card)
         if card.Type == 'Enhancement':
            hostType = re.search(r'Placement:([A-Za-z1-9:_ ]+)', CardsAS.get(card.model,''))
            if hostType:
               debugNotify("hostType: {}.".format(hostType.group(1))) #Debug
               host = findTarget('Targeted-at{}'.format(hostType.group(1)))
               if host == []: 
                  whisper(":::ABORTING!:::")
                  return
               else:
                  debugNotify("We have a host") #Debug
                  hostCards = eval(getGlobalVariable('Host Cards'))
                  hostCards[card._id] = host[0]._id
                  setGlobalVariable('Host Cards',str(hostCards))
                  orgAttachments(host[0])
            else: card.moveToTable(MPxOffset + 0, 0 + yaxisMove(card))
      else: debugNotify("No Placement Automations. Doing Nothing",2)
      if card.Type == 'Unit': incrStat('units',me.name) # We store that the player has played a unit
      debugNotify("<<< placeCard()") #Debug
   except: notify("!!! ERROR !!! in placeCard()")

def orgAttachments(card,facing = 'Same'):
# This function takes all the cards attached to the current card and re-places them so that they are all visible
# xAlg, yAlg are the algorithsm which decide how the card is placed relative to its host and the other hosted cards. They are always multiplied by attNR
   debugNotify(">>> orgAttachments()") #Debug
   attNR = 1
   debugNotify("Card Name : {}".format(card.name), 4)
   update()
   x,y = card.position
   if card.controller in myAllies: sideOffset = playerside # If it's our card, we need to assign it towards our side
   else: sideOffset = playerside * -1 # Otherwise we assign it towards the opponent's side
   if card.Type == 'Objective':
      debugNotify("Found specialHostPlacementAlgs", 3)
      xAlg = cwidth() / 2 * sideOffset
      yAlg = 0
      countCaptures = 0
      debugNotify("About to retrieve captured cards") #Debug      
      capturedCards = eval(getGlobalVariable('Captured Cards'))
      for capturedC in capturedCards: # once we move our objectives around, we want to move their captured cards with them as well.
         if capturedCards[capturedC] == card._id:
            debugNotify("Moved Objective has Captured cards. Moving them...")
            countCaptures += 1
            Card(capturedC).moveToTable(x - (xAlg * countCaptures), y, True) # Captures are placed towards the left.
            Card(capturedC).sendToBack()
            Card(capturedC).highlight = CapturedColor
   else:
      xAlg = 0 # The Default placement on the X axis, is to place the attachments at the same X as their parent
      yAlg = -(cwidth() / 4 * sideOffset)
   hostCards = eval(getGlobalVariable('Host Cards'))
   cardAttachements = [Card(att_id) for att_id in hostCards if hostCards[att_id] == card._id]
   for attachment in cardAttachements:
      if facing == 'Faceup': FaceDown = False
      elif facing == 'Facedown': FaceDown = True
      else: # else is the default of 'Same' and means the facing stays the same as before.
         if attachment.isFaceUp: FaceDown = False
         else: FaceDown = True
      if attachment.controller == me:
         attachment.moveToTable(x + (xAlg * attNR), y + (yAlg * attNR),FaceDown)
         if FaceDown: attachment.peek()
      else: remoteCall(attachment.controller, 'moveForeignCard', [attachment, x + (xAlg * attNR), y + (yAlg * attNR), FaceDown])
      attachment.setIndex(len(cardAttachements) - attNR) # This whole thing has become unnecessary complicated because sendToBack() does not work reliably
      debugNotify("{} index = {}".format(attachment,attachment.getIndex), 4) # Debug
      attNR += 1
      debugNotify("Moving {}, Iter = {}".format(attachment,attNR), 4)
   card.sendToFront() # Because things don't work as they should :(
   if debugVerbosity >= 4: # Checking Final Indices
      for attachment in cardAttachements: notify("{} index = {}".format(attachment,attachment.getIndex)) # Debug
   debugNotify("<<< orgAttachments()", 3) #Debug      

def moveForeignCard(card,x,y,faceDown = False): # A remote function to allow other players to move our cards.
   debugNotify(">>> moveForeignCard()") #Debug
   mute()
   card.moveToTable(x, y, faceDown)
   debugNotify("<<< moveForeignCard()") #Debug

def findMarker(card, markerDesc): # Goes through the markers on the card and looks if one exist with a specific description
   debugNotify(">>> findMarker(){}".format(extraASDebug())) #Debug
   foundKey = None
   if markerDesc in mdict: markerDesc = mdict[markerDesc][0] # If the marker description is the code of a known marker, then we need to grab the actual name of that.
   for key in card.markers:
      debugNotify("Key: {}\nmarkerDesc: {}".format(key[0],markerDesc)) # Debug
      if re.search(r'{}'.format(markerDesc),key[0]) or markerDesc == key[0]:
         foundKey = key
         debugNotify("Found {} on {}".format(key[0],card))
         break
   debugNotify("<<< findMarker() by returning: {}".format(foundKey))
   return foundKey

def parseCombatIcons(STRING, dictReturn = False):
   # This function takes the printed combat icons of a card and returns a string that contains only the non-zero ones.
   debugNotify(">>> parseCombatIcons() with STRING: {}".format(STRING)) #Debug
   UD = re.search(r'(?<!-)UD:([1-9])',STRING)
   EEUD = re.search(r'EE-UD:([1-9])',STRING)
   BD = re.search(r'(?<!-)BD:([1-9])',STRING)
   EEBD = re.search(r'EE-BD:([1-9])',STRING)
   T = re.search(r'(?<!-)T:([1-9])',STRING)
   EET = re.search(r'EE-T:([1-9])',STRING)
   if not dictReturn: # without a dictReturn, we compile a human readable string.
      parsedIcons = ''
      if UD: parsedIcons += 'UD:{}. '.format(UD.group(1))
      if EEUD: parsedIcons += 'EE-UD:{}. '.format(EEUD.group(1))
      if BD: parsedIcons += 'BD:{}. '.format(BD.group(1))
      if EEBD: parsedIcons += 'EE-BD:{}. '.format(EEBD.group(1))
      if T: parsedIcons += 'T:{}. '.format(T.group(1))
      if EET: parsedIcons += 'EE-T:{}.'.format(EET.group(1))
      debugNotify("<<< parseCombatIcons() with return: {}".format(parsedIcons)) # Debug
   else: # If we requested a dictReturn, the parsed icons will be returned in the form of a dictionary.
      parsedIcons = {}
      if UD: parsedIcons[UD] = num(UD.group(1))
      else: parsedIcons[UD] = 0
      if EEUD: parsedIcons[EE-UD] = num(EEUD.group(1))
      else: parsedIcons[EE-UD] = 0
      if BD: parsedIcons[BD] = num(BD.group(1))
      else: parsedIcons[BD] = 0
      if EEBD: parsedIcons[EE-BD] = num(EEBD.group(1))
      else: parsedIcons[EE-BD] = 0
      if T: parsedIcons[T] = num(T.group(1))
      else: parsedIcons[T] = 0
      if EET: parsedIcons[EE-T] = num(EET.group(1))
      else: parsedIcons[EE-T] = 0
      debugNotify("<<< parseCombatIcons() with dictReturn: {}".format(parsedIcons)) # Debug      
   return parsedIcons

def calculateCombatIcons(card = None, CIString = None):
   # This function calculates how many combat icons a unit is supposed to have in a battle by adding bonuses from attachments as well.
   debugNotify(">>> calculateCombatIcons()") #Debug
   if card: 
      debugNotify("card = {}".format(card)) #Debug
      combatIcons = card.properties['Combat Icons']
   elif CIString: 
      debugNotify("CIString = {}".format(CIString)) #Debug
      combatIcons = CIString
   else: return
   debugNotify("Setting Variables") #Debug
   LobotBlocked = False
   Unit_Damage = 0
   Blast_Damage = 0
   Tactics = 0
   debugNotify("About to process CI: {}".format(combatIcons)) #Debug
   UD = re.search(r'(?<!-)UD:([1-9])',combatIcons)
   EEUD = re.search(r'EE-UD:([1-9])',combatIcons)
   BD = re.search(r'(?<!-)BD:([1-9])',combatIcons)
   EEBD = re.search(r'EE-BD:([1-9])',combatIcons)
   T = re.search(r'(?<!-)T:([1-9])',combatIcons)
   EET = re.search(r'EE-T:([1-9])',combatIcons)
   debugNotify("Icons Processed. Incrementing variables") #Debug
   if UD: Unit_Damage += num(UD.group(1))
   if EEUD and gotEdge(): Unit_Damage += num(EEUD.group(1))
   if BD: Blast_Damage += num(BD.group(1))
   if EEBD and gotEdge(): Blast_Damage += num(EEBD.group(1))
   if T: Tactics += num(T.group(1))
   if EET and gotEdge(): Tactics += num(EET.group(1))
   if not Automations['Triggers']: # If trigger automations have been disabled, we don't check for extra damage icons.
      whisper("Trigger automations disabled. Calculating only basic icons")
   else:
      if card: # We only check markers if we're checking a host's Combat Icons.
         debugNotify("Checking Markers") #Debug
         for marker in card.markers:
            if re.search(r':UD',marker[0]): Unit_Damage += card.markers[marker]
            if re.search(r':BD',marker[0]): Blast_Damage += card.markers[marker]
            if re.search(r':Tactics',marker[0]): Tactics += card.markers[marker]
            if re.search(r':EE-UD',marker[0]) and gotEdge(): Unit_Damage += card.markers[marker]
            if re.search(r':EE-BD',marker[0]) and gotEdge(): Blast_Damage += card.markers[marker]
            if re.search(r':EE-Tactics',marker[0]) and gotEdge(): Tactics += card.markers[marker]
            if re.search(r':minusUD',marker[0]): Unit_Damage -= card.markers[marker]
            if re.search(r':minusBD',marker[0]): Blast_Damage -= card.markers[marker]
            if re.search(r':minusTactics',marker[0]): Tactics -= card.markers[marker]
            if re.search(r':minusEE-UD',marker[0]) and gotEdge(): Unit_Damage -= card.markers[marker]
            if re.search(r':minusEE-BD',marker[0]) and gotEdge(): Blast_Damage -= card.markers[marker]
            if re.search(r':minusEE-Tactics',marker[0]) and gotEdge(): Tactics -= card.markers[marker]
         Autoscripts = CardsAS.get(card.model,'').split('||')   
         if len(Autoscripts) > 0:
            for autoS in Autoscripts:
               extraRegex = re.search(r'ExtraIcon:(UD|BD|Tactics|EE-UD|EE-BD|EE-T):([0-9])',autoS)
               if extraRegex:
                  debugNotify("extraRegex = {}".format(extraRegex.groups())) #Debug
                  if not chkSuperiority(autoS, card): continue
                  if not checkOriginatorRestrictions(autoS,card): continue
                  if re.search(r'-ifHaveForce', autoS) and not haveForce(): continue
                  if re.search(r'-ifHaventForce', autoS) and haveForce(): continue         
                  targetCards = findTarget(autoS,card = card)
                  multiplier = per(autoS, card, 0, targetCards)               
                  if extraRegex.group(1) == 'UD': Unit_Damage += num(extraRegex.group(2)) * multiplier
                  if extraRegex.group(1) == 'BD': Blast_Damage += num(extraRegex.group(2)) * multiplier
                  if extraRegex.group(1) == 'Tactics': Tactics += num(extraRegex.group(2)) * multiplier
                  if extraRegex.group(1) == 'EE-UD' and gotEdge(): Unit_Damage += num(extraRegex.group(2)) * multiplier
                  if extraRegex.group(1) == 'EE-BD' and gotEdge(): Blast_Damage += num(extraRegex.group(2)) * multiplier
                  if extraRegex.group(1) == 'EE-T' and gotEdge(): Tactics += num(extraRegex.group(2)) * multiplier
               else:
                  debugNotify("No extra combat icons found in {}".format(card))
      debugNotify("Checking Constant Effects on table") #Debug
      for c in table:
         Autoscripts = CardsAS.get(c.model,'').split('||')      
         for autoS in Autoscripts:
            if not chkDummy(autoS, c): continue
            if re.search(r'excludeDummy', autoS) and c.highlight == DummyColor: continue
            if c.highlight == EdgeColor: continue # cards played as edge don't use their effects.
            if not checkOriginatorRestrictions(autoS,c): continue
            if chkPlayer(autoS, c.controller, False): # If the effect is meant for our cards...
               increaseRegex = re.search(r'(Increase|Decrease)(UD|BD|Tactics):([0-9])',autoS)
               if increaseRegex:
                  debugNotify("increaseRegex = {}".format(increaseRegex.groups())) #Debug
                  if checkCardRestrictions(gatherCardProperties(card), prepareRestrictions(autoS,'type')) and checkSpecialRestrictions(autoS,card): # We check that the current card is a valid one for the constant ability.
                     if increaseRegex.group(1) == 'Increase': 
                        if increaseRegex.group(2) == 'UD': Unit_Damage += num(increaseRegex.group(3))
                        if increaseRegex.group(2) == 'BD': Blast_Damage += num(increaseRegex.group(3))
                        if increaseRegex.group(2) == 'Tactics': Tactics += num(increaseRegex.group(3))
                     else: 
                        if increaseRegex.group(2) == 'UD': Unit_Damage -= num(increaseRegex.group(3))
                        if increaseRegex.group(2) == 'BD': Blast_Damage -= num(increaseRegex.group(3))
                        if increaseRegex.group(2) == 'Tactics': Tactics -= num(increaseRegex.group(3))
               else:
                  debugNotify("No constant ability for combat icons found in {}".format(c))
               if c.model == "ff4fb461-8060-457a-9c16-000000000386": # Lobot's ability is pretty unique.
                  LobotBlocked = True
      if card: # We only check attachments if we're checking a host's Combat Icons.
         debugNotify("Checking Attachments") #Debug
         hostCards = eval(getGlobalVariable('Host Cards'))
         for attachment in hostCards:
            if hostCards[attachment] == card._id:
               debugNotify("Found Attachment: {}".format(Card(attachment))) #Debug
               AS = CardsAS.get(Card(attachment).model,'')
               if AS == '': continue
               Autoscripts = AS.split('||')
               for autoS in Autoscripts:
                  if re.search(r'BonusIcons:',autoS):
                     if not checkOriginatorRestrictions(autoS,Card(attachment)): continue
                     UD, BD, T = calculateCombatIcons(CIString = autoS) # Recursion FTW!
                     Unit_Damage += UD
                     Blast_Damage += BD
                     Tactics += T
                     if re.search(r'Double',autoS):
                        Unit_Damage *= 2
                        Blast_Damage *= 2
                        Tactics *= 2
   debugNotify("<<< calculateCombatIcons() with return: {}".format((Unit_Damage,Blast_Damage,Tactics))) # Debug
   if Unit_Damage < 0: Unit_Damage = 0 # We cannot have a negative combat icon.
   if Blast_Damage < 0: Blast_Damage = 0
   if Tactics < 0: Tactics = 0
   if LobotBlocked and not gotEdge(): #If Lobot is taking part and we don't have the edge, then we can't do anything.
      if Unit_Damage > 0 or Blast_Damage > 0 or Tactics > 0: # If we were actually doing anything, then we announce that it was blocked by Lobot, so that they don't get confused.
         if card: notify(":> {}'s combat icons were made edge-enabled by Lobot".format(card))
         else: notify(":> Unit's combat icons were made edge-enabled by Lobot")
      Unit_Damage = 0
      Blast_Damage = 0
      Tactics = 0
   return (Unit_Damage,Blast_Damage,Tactics)

def chkShiiChoTrainnig(card): # Checks if a card or its attachments allow it to split its damage amoing targets
   debugNotify(">>> chkSiiChoTrainnig() with card {}".format(card)) #Debug   
   ShiiCho = False
   Autoscripts = CardsAS.get(card.model,'').split('||')   
   if len(Autoscripts) > 0:
      for autoS in Autoscripts:
         if re.search(r'ConstantAbility:ShiiCho',autoS):
            debugNotify("Found ShiiCho Training in card abilities!") #Debug
            ShiiCho = True
   hostCards = eval(getGlobalVariable('Host Cards'))
   for attachment in hostCards:
      if hostCards[attachment] == card._id:
         debugNotify("Found Attachment: {}".format(Card(attachment)),3) #Debug
         Autoscripts = CardsAS.get(Card(attachment).model,'').split('||')
         for autoS in Autoscripts:
            if re.search(r'ConstantAbility:ShiiCho',autoS): 
               debugNotify("Found ShiiCho Training in card attachments!") #Debug
               ShiiCho = True
   debugNotify("<<< chkSiiChoTrainnig() with return {}".format(ShiiCho)) #Debug   
   return ShiiCho
   
def chkTargetedStrike(card): # Checks if a card or its attachments allow it to split its damage amoing targets
   debugNotify(">>> chkTargetedStrike() with card {}".format(card)) #Debug   
   targetedStrike = False
   Autoscripts = CardsAS.get(card.model,'').split('||')   
   if len(Autoscripts) > 0:
      for autoS in Autoscripts:
         if re.search(r'ConstantAbility:TargetStrike',autoS):
            debugNotify("Found Targeted Strike in card abilities!") #Debug
            targetedStrike = True
   hostCards = eval(getGlobalVariable('Host Cards'))
   debugNotify("About to check attachments for Targeted Strikes")
   for attachment in hostCards:
      if hostCards[attachment] == card._id:
         debugNotify("Found Attachment: {}".format(Card(attachment)),3) #Debug
         Autoscripts = CardsAS.get(Card(attachment).model,'').split('||')
         for autoS in Autoscripts:
            if re.search(r'ConstantAbility:TargetStrike',autoS) and checkCardRestrictions(gatherCardProperties(card), prepareRestrictions(autoS,'hostType')):
               debugNotify("Found Targeted Strike in card attachments!") #Debug
               targetedStrike = True
   debugNotify("<<< chkTargetedStrike() with return {}".format(targetedStrike)) #Debug   
   return targetedStrike
   
def resolveUD(card,Unit_Damage):
   debugNotify(">>> resolveUD()") #Debug   
   targetUnits = {}
   knowsShiiCho = chkShiiChoTrainnig(card)
   targetedStrike = chkTargetedStrike(card)
   targetUnitsList = [c for c in table if (c.controller in fetchAllOpponents() or len(getPlayers()) == 1) and c.targetedBy and c.targetedBy == me and c.Type == 'Unit' and not hasDamageProtection(c,card) and (c.orientation == Rot90 or targetedStrike)]
   if not len(targetUnitsList): # if the player hasn't targeted any units, then we try to figure out which units might be a valid target for the Unit Damage
      targetUnitsList = [c for c in table if (c.orientation == Rot90 or targetedStrike) and (c.controller in fetchAllOpponents() or len(getPlayers()) == 1) and c.Type == 'Unit' and not hasDamageProtection(c,card) and c.isFaceUp and c.highlight != EdgeColor]
      if len(targetUnitsList) and not confirm("You had no valid units targeted for {}'s Unit Damage icons. Attempt to discover targets automatically?".format(card.name)): targetUnitsList = []
   if len(targetUnitsList) > 1:
      unitChoices = makeChoiceListfromCardList(targetUnitsList)
      if Unit_Damage:
         if not knowsShiiCho:
            damagedUnit = SingleChoice('Please select the unit to take {} damage'.format(Unit_Damage), unitChoices, cancelButton = True)
            if damagedUnit != None:
               addMarker(targetUnitsList[damagedUnit], 'Damage',Unit_Damage, True)
               targetUnits[targetUnitsList[damagedUnit].name] = targetUnits.get(targetUnitsList[damagedUnit].name,0) + Unit_Damage
         else:
            damagedUnits = multiChoice("Please assign {} damage tokens among the {} units you've selected".format(Unit_Damage,len(targetUnitsList)), unitChoices)
            if damagedUnits != 'ABORT': 
               while len(damagedUnits) != Unit_Damage:
                  damagedUnits = multiChoice(":::ERROR::: Amount of units chosen does not match your available Unit Damage!\
                                          \n\nPlease assign {} damage tokens among the {} units you've selected".format(Unit_Damage,len(targetUnitsList)), unitChoices)
                  if damagedUnits == 'ABORT': break
            if damagedUnits != 'ABORT':
               for choice in damagedUnits: 
                  addMarker(targetUnitsList[choice], 'Damage',1, True)
                  targetUnits[targetUnitsList[choice].name] = targetUnits.get(targetUnitsList[choice].name,0) + 1
   elif len(targetUnitsList) == 1: 
      addMarker(targetUnitsList[0], 'Damage',Unit_Damage, True)
      targetUnits[targetUnitsList[0].name] = targetUnits.get(targetUnitsList[0].name,0) + Unit_Damage
   else: delayed_whisper(":::WARNING::: No valid units selected as targets for Unit Damage. Please add damage tokens manually as required.")
   debugNotify("<<< resolveUD() with targetUnits: {}".format([targetUnits])) #Debug
   if len(targetUnits): return [targetUnits]
   else: return []

def resolveTactics(card,Tactics):
   debugNotify(">>> resolveTactics()") #Debug   
   targetUnits = {}
   targetUnitsList = [c for c in table if (c.controller in fetchAllOpponents() or len(getPlayers()) == 1) and c.targetedBy and c.targetedBy == me and c.Type == 'Unit' and c.isFaceUp]
   if not len(targetUnitsList): # if the player hasn't targeted any units, then we try to figure out which units might be a valid target for the Unit Damage
      targetUnitsList = [c for c in table if (c.controller in fetchAllOpponents() or len(getPlayers()) == 1) and c.Type == 'Unit' and not hasDamageProtection(c,card) and c.isFaceUp and c.highlight != EdgeColor] # We first make the list, so as to avoid asking if there's not going to be any valid target anyway.
      if len(targetUnitsList) and not confirm("You had no valid units targeted for {}'s Tactics icons. Attempt to discover targets automatically?".format(card.name)): targetUnitsList = []
   if len(targetUnitsList) > 1:
      unitChoices = makeChoiceListfromCardList(targetUnitsList)
      if Tactics:
         focusedUnits = multiChoice("Please assign {} focus tokens among the {} units you've selected".format(Tactics,len(targetUnitsList)), unitChoices)
         if focusedUnits != 'ABORT':
            while len(focusedUnits) != Tactics:
               focusedUnits = multiChoice(":::ERROR::: Amount of units chosen does not match your available tactics!\
                                       \n\nPlease assign {} focus tokens among the {} units you've selected".format(Tactics,len(targetUnitsList)), unitChoices)
               if focusedUnits == 'ABORT': break
         if focusedUnits != 'ABORT':
            for choice in focusedUnits: 
               addMarker(targetUnitsList[choice], 'Focus',1, True)
               targetUnits[targetUnitsList[choice].name] = targetUnits.get(targetUnitsList[choice].name,0) + 1
   elif len(targetUnitsList) == 1: 
      addMarker(targetUnitsList[0], 'Focus',Tactics, True)
      targetUnits[targetUnitsList[0].name] = targetUnits.get(targetUnitsList[0].name,0) + Tactics
   else: delayed_whisper(":::WARNING::: No valid units selected as targets for Tactics. Please add focus tokens manually as required.")
   debugNotify("<<< resolveTactics() with targetUnits: {}".format([targetUnits])) #Debug   
   if len(targetUnits): return [targetUnits]
   else: return []

def chkDummy(Autoscript, card): # Checks if a card's effect is only supposed to be triggered for a (non) Dummy card
   if debugVerbosity >= 4: notify(">>> chkDummy()") #Debug
   if re.search(r'onlyforDummy',Autoscript) and card.highlight != DummyColor: return False
   if re.search(r'excludeDummy', Autoscript) and card.highlight == DummyColor: return False
   return True

def chkParticipants(Autoscript, card):
   # This function check to see if one side of the engagement has the amount of units required for this effect to trigger.
   debugNotify(">>> chkParticipants() with Autoscript = {}".format(Autoscript)) #Debug
   participantRegex = re.search(r'-if(Attackers|Defenders)(Opponents|Allies)(eq|le|ge|gt|lt)([0-9])',Autoscript)
   validCard = True
   if participantRegex:
      if participantRegex.group(1) == 'Attackers': mainPlayer = Player(num(getGlobalVariable('Current Attacker')))
      else: mainPlayer = Card(num(getGlobalVariable('Engaged Objective'))).controller
      if participantRegex.group(2) == 'Opponents': playerTeam = fetchAllOpponents(card.controller)
      else: playerTeam = fetchAllAllies(card.controller)
      participatingUnits = [c for c in table if c.orientation == Rot90 and c.controller in playerTeam and mainPlayer in playerTeam]
      validCard = compareValue(participantRegex.group(3), len(participatingUnits), num(participantRegex.group(4)))
   debugNotify(">>> chkParticipants() with validCard = {}".format(validCard)) #Debug
   return validCard
   
def gotEdge(targetPL = None):
   debugNotify(">>> gotEdge() with targetPL = {}".format(targetPL)) #Debug
   gotIt = False
   if not targetPL: targetPL = me
   for player in fetchAllAllies(targetPL):
      targetAffiliation = getSpecial('Affiliation',targetPL)
      if targetAffiliation.markers[mdict['Edge']] and targetAffiliation.markers[mdict['Edge']] == 1: gotIt = True      
   debugNotify("<<< gotEdge() returns {}".format(gotIt)) #Debug
   return gotIt

def getKeywords(card): # A function which combines the existing card keywords, with markers which give it extra ones.
   debugNotify(">>> getKeywords()") #Debug
   global Stored_Keywords
   #confirm("getKeywords") # Debug
   keywordsList = []
   cKeywords = card.Traits
   strippedKeywordsList = cKeywords.split('-')
   for cardKW in strippedKeywordsList:
      strippedKW = cardKW.strip() # Remove any leading/trailing spaces between traits. We need to use a new variable, because we can't modify the loop iterator.
      if strippedKW: keywordsList.append(strippedKW) # If there's anything left after the stip (i.e. it's not an empty string anymrore) add it to the list.   
   if card.markers:
      for key in card.markers:
         markerKeyword = re.search('Trait:([\w ]+)',key[0])
         if markerKeyword:
            #confirm("marker found: {}\n key: {}".format(markerKeyword.groups(),key[0])) # Debug
            #if markerKeyword.group(1) == 'Barrier' or markerKeyword.group(1) == 'Sentry' or markerKeyword.group(1) == 'Code Gate': #These keywords are mutually exclusive. An Ice can't be more than 1 of these
               #if 'Barrier' in keywordsList: keywordsList.remove('Barrier') # It seems in ANR, they are not so mutually exclusive. See: Tinkering
               #if 'Sentry' in keywordsList: keywordsList.remove('Sentry') 
               #if 'Code Gate' in keywordsList: keywordsList.remove('Code Gate')
            if re.search(r'Breaker',markerKeyword.group(1)):
               if 'Barrier Breaker' in keywordsList: keywordsList.remove('Barrier Breaker')
               if 'Sentry Breaker' in keywordsList: keywordsList.remove('Sentry Breaker')
               if 'Code Gate Breaker' in keywordsList: keywordsList.remove('Code Gate Breaker')
            keywordsList.append(markerKeyword.group(1))
   keywords = ''
   for KW in keywordsList:
      keywords += '{}-'.format(KW)
   Stored_Keywords[card._id] = keywords[:-1] # We also update the global variable for this card, which is used by many functions.
   debugNotify("<<< getKeywords() by returning: {}.".format(keywords[:-1]))
   return keywords[:-1] # We need to remove the trailing dash '-'

def reduceCost(card, action = 'PLAY', fullCost = 0, dryRun = False):
# A Functiona that scours the table for cards which reduce the cost of other cards.
# if dryRun is set to True, it means we're just checking what the total reduction is going to be and are not actually removing or adding any counters.
   type = action.capitalize()
   debugNotify(">>> reduceCost(). Action is: {}. FullCost = {}. dryRyn = {}".format(type,fullCost,dryRun)) #Debug
   fullCost = abs(fullCost)
   reduction = 0
   costReducers = []
   ### First we check if the card has an innate reduction. 
   Autoscripts = CardsAS.get(card.model,'').split('||') 
   debugNotify("About to check if there's any onPay triggers on the card")
   if len(Autoscripts): 
      for autoS in Autoscripts:
         if not re.search(r'onPay', autoS): 
            debugNotify("No onPay trigger found in {}!".format(autoS))
            continue
         else: debugNotify("onPay trigger found in {}!".format(autoS))
         reductionSearch = re.search(r'Reduce([0-9]+)Cost({}|All)'.format(type), autoS)
         if debugVerbosity >= 2: #Debug
            if reductionSearch: notify("!!! self-reduce regex groups: {}".format(reductionSearch.groups()))
            else: notify("!!! No self-reduce regex Match!")
         count = num(reductionSearch.group(1))
         targetCards = findTarget(autoS,card = card)
         multiplier = per(autoS, card, 0, targetCards)
         reduction += (count * multiplier)
         maxRegex = re.search(r'-maxReduce([1-9])', autoS) # We check if the card will only reduce its cast by a specific maximum (e.g. Weequay Elite)
         if maxRegex and reduction > num(maxRegex.group(1)): reduction = num(maxRegex.group(1))
         fullCost -= reduction
         if reduction > 0 and not dryRun: notify("-- {}'s full cost is reduced by {}".format(card,reduction))
   debugNotify("About to gather cards on the table")
   ### Now we check if any card on the table has an ability that reduces costs
   if not gatheredCardList: # A global variable that stores if we've scanned the tables for cards which reduce costs, so that we don't have to do it again.
      global costModifiers
      del costModifiers[:]
      RC_cardList = sortPriority([c for c in table if c.isFaceUp and c.highlight != EdgeColor])
      reductionRegex = re.compile(r'(Reduce|Increase)([0-9#X]+)Cost({}|All)-affects([A-Z][A-Za-z ]+)(-not[A-Za-z_& ]+)?'.format(type)) # Doing this now, to reduce load.
      for c in RC_cardList: # Then check if there's other cards in the table that reduce its costs.
         Autoscripts = CardsAS.get(c.model,'').split('||')
         if len(Autoscripts) == 0: continue
         for autoS in Autoscripts:
            debugNotify("Checking {} with AS: {}".format(c, autoS)) #Debug
            if not chkPlayer(autoS, c.controller, False): continue
            reductionSearch = reductionRegex.search(autoS) 
            if debugVerbosity >= 2: #Debug
               if reductionSearch: notify("!!! Regex is {}".format(reductionSearch.groups()))
               else: notify("!!! No reduceCost regex Match!") 
            #if re.search(r'ifInstalled',autoS) and (card.group != table or card.highlight == RevealedColor): continue
            if reductionSearch: # If the above search matches (i.e. we have a card with reduction for Rez and a condition we continue to check if our card matches the condition)
               debugNotify("Possible Match found in {}".format(c),3) # Debug         
               if not chkDummy(autoS, c): continue   
               if not checkOriginatorRestrictions(autoS,c): continue  
               if not chkSuperiority(autoS, c): continue
               if reductionSearch.group(1) == 'Reduce': 
                  debugNotify("Adding card to cost Reducers list")
                  costReducers.append((c,reductionSearch,autoS)) # We put the costReducers in a different list, as we want it to be checked after all the increasers are checked
               else:
                  debugNotify("Adding card to cost Modifiers list")
                  costModifiers.append((c,reductionSearch,autoS)) # Cost increasing cards go into the main list we'll check in a bit, as we need to check them first. 
                                                                  # In each entry we store a tuple of the card object and the search result for its cost modifying abilities, so that we don't regex again later. 
      if len(costReducers): costModifiers.extend(costReducers)
   for cTuple in costModifiers: # Now we check what kind of cost modification each card provides. First we check for cost increasers and then for cost reducers
      debugNotify("Checking next cTuple",4) # Debug
      c = cTuple[0]
      reductionSearch = cTuple[1]
      autoS = cTuple[2]
      debugNotify("cTuple[0] (i.e. card) is: {}".format(c)) #Debug
      debugNotify("cTuple[2] (i.e. autoS) is: {}".format(autoS),4) # Debug
      if reductionSearch.group(4) == 'All' or checkCardRestrictions(gatherCardProperties(card), prepareRestrictions(autoS,seek = 'reduce')):
         if not checkSpecialRestrictions(autoS,card): continue
         debugNotify("### Search match! Reduction Value is {}".format(reductionSearch.group(2)),3) # Debug
         if re.search(r'onlyOnce',autoS):
            if dryRun: # For dry Runs we do not want to add the "Activated" token on the card. 
               if oncePerTurn(c, act = 'dryRun') == 'ABORT': continue 
            else:
               if oncePerTurn(c, act = 'automatic') == 'ABORT': continue # if the card's effect has already been used, check the next one
         if reductionSearch.group(2) == '#': 
            markersCount = c.markers[mdict['Credits']]
            markersRemoved = 0
            while markersCount > 0:
               debugNotify("Reducing Cost with and Markers from {}".format(c)) # Debug
               if reductionSearch.group(1) == 'Reduce':
                  if fullCost > 0: 
                     reduction += 1
                     fullCost -= 1
                     markersCount -= 1
                     markersRemoved += 1
                  else: break
               else: # If it's not a reduction, it's an increase in the cost.
                  reduction -= 1
                  fullCost += 1                     
                  markersCount -= 1
                  markersRemoved += 1
            if not dryRun and markersRemoved != 0: 
               c.markers[mdict['Credits']] -= markersRemoved # If we have a dryRun, we don't remove any tokens.
               notify(" -- {} credits are used from {}".format(markersRemoved,c))
         elif reductionSearch.group(2) == 'X':
            markerName = re.search(r'-perMarker{([\w ]+)}', autoS)
            try: 
               marker = findMarker(c, markerName.group(1))
               if marker:
                  for iter in range(c.markers[marker]):
                     if reductionSearch.group(1) == 'Reduce':
                        if fullCost > 0:
                           reduction += 1
                           fullCost -= 1
                     else: 
                        reduction -= 1
                        fullCost += 1
            except: notify("!!!ERROR!!! ReduceXCost - Bad Script")
         else:
            orig_reduction = reduction
            for iter in range(num(reductionSearch.group(2))):  # if there is a match, the total reduction for this card's cost is increased.
               if reductionSearch.group(1) == 'Reduce': 
                  if fullCost > 0: 
                     reduction += 1
                     fullCost -= 1
               else: 
                  reduction -= 1
                  fullCost += 1
            if orig_reduction != reduction: # If the current card actually reduced or increased the cost, we want to announce it
               if reduction > 0 and not dryRun: notify(" -- {} reduces cost by {}".format(c,reduction - orig_reduction))
               elif reduction < 0 and dryRun: notify(" -- {} increases cost by {}".format(c,abs(reduction - orig_reduction)))
   debugNotify("<<< reduceCost(). final reduction = {}".format(reduction)) #Debug
   return reduction
   
def haveForce():
   debugNotify(">>> chkForce()") #Debug
   myForce = False
   BotD = getSpecial('BotD')
   if Side == 'Dark': 
      if BotD.alternate == 'DarkSide': myForce = True
   else:
      if BotD.alternate == '': myForce = True
   if debugVerbosity >= 4: notify("<<< chkForce() with return:{}".format(myForce)) #Debug
   return myForce

def compareObjectiveTraits(Trait):
   debugNotify(">>> compareObjectiveTraits(). Checking Trait: {}".format(Trait)) #Debug
   # This function will go through all objectives on the table, count how many of them contain a specific trait
   # and return a list of the player(s) who have the most objectives with that trait.
   playerTraitCounts = {}
   for player in getPlayers(): # We go through all the objectives of each player and count which of them have the relevant trait.
      playerTraitCounts[player.name] = 0
      Objectives = eval(player.getGlobalVariable('currentObjectives'))
      debugNotify("Checking {} Objectives".format(player.name)) # Debug
      for obj in [Card(obj_ID) for obj_ID in Objectives]:
         if re.search(r'{}'.format(Trait),obj.Traits): 
            playerTraitCounts[player.name] += 1
            debugNotify("Found {} Trait in Objective {}. {}'s Counter now {}".format(Trait,obj,player,playerTraitCounts[player.name]),2)
      for card in table: # We check for cards for give bonus objective traits (e.g. Echo Base)
         if card.controller == player and card.highlight != EdgeColor and card.highlight != RevealedColor and card.highlight != UnpaidColor:
            Autoscripts = CardsAS.get(card.model,'').split('||')
            debugNotify("Autoscripts len = {}. Autoscripts = {}".format(len(Autoscripts),Autoscripts),3)
            for autoS in Autoscripts:
               debugNotify("Checking {} for Objective Trait boosting AS: {}".format(card,autoS)) # Debug
               search = 'Trait{Objective_and_' + Trait + '}([0-9])Bonus' # Doing a concatenate because python b0rks if I try to do it with format.
               debugNotify("Finished concatenating",3) # Debug
               TraitBonus = re.search(r'{}'.format(search),autoS)
               if TraitBonus: 
                  playerTraitCounts[player.name] += num(TraitBonus.group(1))
                  debugNotify("Found {} Trait Bonus in Autoscripts of {}. {}'s Counter now {}".format(Trait,card,player,playerTraitCounts[player.name]),2)
   debugNotify("Comparing Objectives count") # Debug
   topPlayers = []
   currentMaxCount = 0
   for player in getPlayers():
      debugNotify("Comparing {} with counter at {}. Current Max at {} ".format(player,playerTraitCounts[player.name],currentMaxCount),2)
      if playerTraitCounts[player.name] > currentMaxCount:
         del topPlayers[:] # If that player has the highest current total, remove all other players from the list.
         topPlayers.append(player)
         currentMaxCount = playerTraitCounts[player.name]
      elif playerTraitCounts[player.name] == currentMaxCount:
         topPlayers.append(player)
   debugNotify("<<< compareObjectiveTraits(). TopPlayers = {}".format([pl.name for pl in topPlayers])) #Debug
   return topPlayers

def chkSuperiority(Autoscript, card):
   debugNotify(">>> chkSuperiority()") #Debug
   debugNotify("AS = {}. Card = {}".format(Autoscript, card),3) # Debug
   haveSuperiority = True # The default is True, which means that if we do not have a relevant autoscript, it's always True
   supRegex = re.search(r'-ifSuperiority([\w ]+)',Autoscript)
   if supRegex:
      supPlayers = compareObjectiveTraits(supRegex.group(1))
      if len(supPlayers) > 1 or supPlayers[0] != card.controller: haveSuperiority = False # If the controller of the card requiring superiority does not have the most objectives with that trait, we return False
   debugNotify("<<< chkSuperiority(). Return: {}".format(haveSuperiority)) #Debug
   return haveSuperiority
   
def calcBonusEdge(card): # This function calculated how much Edge bonus a card is providing
   debugNotify(">>> calcBonusEdge() with card: {}".format(card)) #Debug
   Autoscripts = CardsAS.get(card.model,'').split('||')
   debugNotify("### Split Autoscripts = {}".format(Autoscripts),4)
   edgeBonus = 0
   if len(Autoscripts) > 0:
      for autoS in Autoscripts:
         debugNotify("regex searching on {}".format(autoS),3)
         edgeRegex = re.search(r'Edge([0-9])Bonus',autoS)
         if edgeRegex and debugVerbosity >= 4: notify("#### regex found") # Debug
         if not edgeRegex: 
            debugNotify("regex NOT found",4) # Debug
            continue # If the script doesn't provide edge bonus, ignore it
         if card.orientation != Rot90 and not re.search(r'-isDistributedEffect',autoS): continue  # If the card isn't participating or the script isn't providing a distributed benefit, ignore it
         if not chkSuperiority(autoS, card): continue # If the script requires superiority but we don't have it, ignore it
         if not checkOriginatorRestrictions(autoS,card): continue # If the script's originator has some restrictions we can't pass, we abort.
         # If the card does not provide an edge bonus, or is not participating, then we ignore it.
         # -isDistributedEffect is a hacky modulator I've added to signify that it's not the card itself that provides the Edge, but other card on the table (e.g. see Hoth Operations)                                                                                                
         debugNotify("Found edgeRegex. Checking Values",3)
         bonus = num(edgeRegex.group(1))
         targetCards = findTarget(autoS,card = card)
         multiplier = per(autoS, card, 0, targetCards)
         debugNotify("Multiplier = {}. Bonus = {}".format(multiplier, bonus)) #Debug
         edgeBonus += (multiplier * bonus)
   if edgeBonus: notify("-- {} adds {} force to the edge total".format(card,edgeBonus))
   return edgeBonus

def hasDamageProtection(target,attacker): # A function which checks if the current target of damage has any protection from it.
   debugNotify(">>> hasDamageProtection(){}".format(extraASDebug())) #Debug   
   protected = False
   Autoscripts = CardsAS.get(target.model,'').split('||')
   for autoS in Autoscripts:
      if re.search(r'ConstantEffect:Protection',autoS) and checkCardRestrictions(gatherCardProperties(attacker), prepareRestrictions(autoS, seek = 'type')) and checkSpecialRestrictions(autoS,target): 
         protected = True
         notify(":> {} is protected against {}'s damage".format(target,attacker))
   hostCards = eval(getGlobalVariable('Host Cards'))
   if not protected: # We don't check more if we've found protection already.
      for attachment in hostCards: # We check if any of the card's attachments is providing protection as well (E.g. First Marker)
         if hostCards[attachment] == target._id:
            Autoscripts = CardsAS.get(Card(attachment).model,'').split('||')
            for autoS in Autoscripts:
               if re.search(r'ConstantEffect:Protection',autoS) and re.search(r'-onHost',autoS) and checkCardRestrictions(gatherCardProperties(attacker), prepareRestrictions(autoS, seek = 'type')) and checkSpecialRestrictions(autoS,target): 
                  protected = True
                  notify(":> {} is protected against {}'s damage".format(target,attacker))
   if not protected: # We don't check more if we've found protection already.
      for marker in target.markers: # We also check if there's any special markers providing protection
         debugNotify("Checking marker {} for protection".format(marker[0]))
         if re.search(r':Protection',marker[0]): 
            protected = True
            notify(":> {} is protected against {}'s damage".format(target,attacker))
   debugNotify("<<< hasDamageProtection()") #Debug
   return protected
     
def readyEffect(card,forced = False):
# This function prepares an event for being activated and puts the initial warning out if necessary.
   debugNotify(">>> readyEffect()") #Debug
   hardcoreMode = chkHardcore(card)
   if not hardcoreMode or forced or card.Type == 'Event':
      card.highlight = ReadyEffectColor
      notify(":::NOTICE::: {}'s {} is about to take effect...".format(card.controller,card))
   else: debugNotify("Hardcore mode enabled. Not Highlighting")
   clrResourceMarkers(card)
   warnImminentEffects = getSetting('warnEffect', "An effect is ready to trigger but has not been done automatically in order to allow your opponent to react.\
                                                 \nOnce your opponent had the chance to play any interrupts, double click on the green-highlighted card to finalize it and resolve any effects (remember to target any relevant cards if required).\
                                               \n\n(This message will not appear again)") # Warning about playing events. Only displayed once.
   if (not hardcoreMode or card.type == 'Event' or forced) and card.owner == me and warnImminentEffects != 'Done':
      information(warnImminentEffects)
      setSetting('warnEffect', 'Done')
   debugNotify("<<< readyEffect()") #Debug         
   
def clrResourceMarkers(card):
   for cMarkerKey in card.markers: 
      debugNotify("Checking marker {}.".format(cMarkerKey[0]),3)
      for resdictKey in resdict:
         if resdict[resdictKey] == cMarkerKey or cMarkerKey[0] == 'Ignores Affiliation Match': 
            card.markers[cMarkerKey] = 0
            break

def clearAttachLinks(card):
# This function takes care to discard any attachments of a card that left play (discarded or captured)
# It also clear the card from the host dictionary, if it was itself attached to another card
   debugNotify(">>> clearAttachLinks()") #Debug
   hostCards = eval(getGlobalVariable('Host Cards'))
   cardAttachementsNR = len([att_id for att_id in hostCards if hostCards[att_id] == card._id])
   if cardAttachementsNR >= 1:
      hostCardSnapshot = dict(hostCards)
      for attachment in hostCardSnapshot:
         if hostCardSnapshot[attachment] == card._id:
            attachedCard = Card(attachment)
            if attachedCard in table: 
               if attachedCard.controller == me: discard(attachedCard)
               else: remoteCall(attachedCard.controller, 'discard', [attachedCard,0,0,False,False,me])
            del hostCards[attachment]
   debugNotify("Checking if the card is attached to unlink.")      
   if hostCards.has_key(card._id): del hostCards[card._id] # If the card was an attachment, delete the link
   setGlobalVariable('Host Cards',str(hostCards))
   debugNotify("<<< clearAttachLinks()") #Debug
   
def removeCapturedCard(card): # This function removes a captured card from the dictionary which records which cards are captured at which objective.
   debugNotify(">>> removeCapturedCard()") #Debug
   parentObjective = None
   try: 
      mute()
      capturedCards = eval(getGlobalVariable('Captured Cards'))
      if capturedCards.has_key(card._id):
         debugNotify("{} was in the capturedCards dict.".format(card))
         parentObjective = Card(capturedCards[card._id])
         del capturedCards[card._id]
         if debugVerbosity >= 3: notify("Double Checking if entry exists: {}".format(capturedCards.get(card._id,'DELETED')))
      card.highlight = None
      if debugVerbosity >= 4: 
         notify("Captured Cards: {}".format([Card(id).name for id in capturedCards]))
         rnd(1,10)
      setGlobalVariable('Captured Cards',str(capturedCards))
   except: notify("!!!ERROR!!! in removeCapturedCard()") # Debug
   debugNotify("<<< removeCapturedCard() with return: {}".format(parentObjective)) #Debug
   return parentObjective

def rescueFromObjective(obj): # THis function returns all captured cards from an objective to their owner's hand
   debugNotify(">>> rescueFromObjective()")
   try:
      count = 0
      capturedCards = eval(getGlobalVariable('Captured Cards')) # This is a dictionary holding how many and which cards are captured at each objective.
      for capturedC in capturedCards: # We check each entry in the dictionary. Each entry is a card's unique ID
         if capturedCards[capturedC] == obj._id: # If the value we have for that card's ID is the unique ID of the current dictionary, it means that card is currently being captured at our objective.
            count += 1 # We count how many captured cards we found
            rescuedC = Card(capturedC) # We generate the card object by the card's unique ID
            removeCapturedCard(rescuedC) # We remove the card from the dictionary
            rescuedC.moveTo(rescuedC.owner.hand) # We return the card to its owner's hand
            autoscriptOtherPlayers('CardRescued',rescuedC) # We check if any card on the table has a trigger out of rescued cards.
      return count
   except: notify("!!!ERROR!!! in rescueFromObjective()") # Debug
   debugNotify("<<< rescueFromObjective()")
            
def clearStoredEffects(card, silent = False,continuePath = True, ignoredEffect = False): # A function which clears a card's waiting-to-be-activated scripts
   debugNotify(">>> clearStoredEffects with card: {}".format(card))
   selectedAbility = eval(getGlobalVariable('Stored Effects'))
   forcedTrigger = False
   if selectedAbility.has_key(card._id):
      debugNotify("Card's selectedAbility: {}".format(selectedAbility))
      if re.search(r'-isForced',selectedAbility[card._id][0]):
         if not silent and not confirm("This units effect is forced which means you have to use it if possible. Are you sure you want to ignore it?"): return
         else: forcedTrigger = True
   else: debugNotify("Card has no selectedAbility entry")
   debugNotify("Clearing Highlight",3)
   if card.highlight == ReadyEffectColor or card.highlight == UnpaidAbilityColor: 
      if not selectedAbility.has_key(card._id): card.highlight = None
      else: card.highlight = selectedAbility[card._id][2]  # We don't want to change highlight if it was changed already by another effect.
   debugNotify("Checking Continuing Path")
   if continuePath: continueOriginalEvent(card,selectedAbility, ignoredEffect)
   debugNotify("Deleting selectedAbility tuple",3)
   if selectedAbility.has_key(card._id): del selectedAbility[card._id]
   debugNotify("Uploading selectedAbility tuple",3)
   setGlobalVariable('Stored Effects',str(selectedAbility))
   cardsLeaving(card,'remove')
   if not silent: 
      if forcedTrigger: notify(":::WARNING::: {} has chosen to ignore the FORCED trigger of {}.".format(me,card))
      else: notify("{} chose not to activate {}'s ability".format(me,card))
   debugNotify("<<< clearStoredEffects")

def clearAllEffects(silent = False): # A function which clears all card's waiting-to-be-activated scripts. This is not looping clearStoredEffects() to avoid too many setGlobalVariable calls
   debugNotify(">>> clearAllEffects")
   selectedAbility = eval(getGlobalVariable('Stored Effects'))   
   for cID in selectedAbility:
      debugNotify("Clearing Effects for {}".format(Card(cID)),3)
      debugNotify("selectedAbility[cID] = {}".format(selectedAbility[cID]),3)
      if not re.search(r'-isForced',selectedAbility[cID][0]):
         if Card(cID).highlight == ReadyEffectColor or Card(cID).highlight == UnpaidAbilityColor: Card(cID).highlight = selectedAbility[cID][2] # We do not clear Forced Triggers so that they're not forgotten.
         debugNotify("Sending card to its final destination if it has any",3)
         continueOriginalEvent(Card(cID),selectedAbility)
         debugNotify("Now Deleting card's dictionary entry",4)
         del selectedAbility[cID]
         cardsLeaving(Card(cID),'remove')
      elif Card(cID).group != table:
         debugNotify("Card was not in table. Assuming player monkeyed around and clearing",3)
         del selectedAbility[cID]
         cardsLeaving(Card(cID),'remove')         
      else: 
         notify(":::WARNING::: {}'s FORCED Trigger is still remaining.".format(Card(cID)))
   debugNotify("Clearing all highlights from cards not waiting for their abilities")
   for card in table:
      if card.highlight == ReadyEffectColor and not selectedAbility.has_key(card._id): card.highlight = None # If the card is still in the selectedAbility, it means it has a forced effect we don't want to clear.
   setGlobalVariable('Stored Effects',str(selectedAbility))
   if not silent: notify(":> All existing card effect triggers were ignored.".format(card))
   debugNotify("<<< clearAllEffects")

def continueOriginalEvent(card,selectedAbility,ignoredEffect = False):
   debugNotify(">>> continueOriginalEvent with card: {}".format(card))
   debugNotify("ignoredEffect: {}".format(ignoredEffect))
   if selectedAbility.has_key(card._id):
      debugNotify("selectedAbility action = {}".format(selectedAbility[card._id][3]),2)
      if selectedAbility[card._id][3] == 'STRIKE': 
         if not ignoredEffect and re.search(r'isStrikeAlternative',selectedAbility[card._id][0]): 
            notify(":> {} has opted to use {}'s react instead of resolving its combat icons".format(me,card))
         else: strike(card, Continuing = True)# If the action is a strike, it means we interrupted a strike for this effect, in which case we want to continue with the strike effects now.         
      if re.search(r'LEAVING',selectedAbility[card._id][3]) or selectedAbility[card._id][3] == 'THWART': 
         if re.search(r'-DISCARD',selectedAbility[card._id][3]) or selectedAbility[card._id][3] == 'THWART': discard(card,Continuing = True)
         elif re.search(r'-HAND',selectedAbility[card._id][3]): returnToHand(card,Continuing = True) 
         elif re.search(r'-DECKBOTTOM',selectedAbility[card._id][3]): sendToBottom(Continuing = True) # This is not passed a specific card as it uses a card list, which we've stored in a global variable already
         elif re.search(r'-EXILE',selectedAbility[card._id][3]): exileCard(card, Continuing = True)
         elif re.search(r'-CAPTURE',selectedAbility[card._id][3]): capture(targetC = card, Continuing = True)
   else: debugNotify("No selectedAbility entry")
   debugNotify("<<< continueOriginalEvent with card: {} and selectedAbility {}".format(card,selectedAbility))  

   
def storeCardEffects(card,Autoscript,cost,previousHighlight,actionType,preTargetCard,count = 0):
   debugNotify(">>> storeCardEffects()")
   # A function which store's a bunch of variables inside a shared dictionary
   # These variables are recalled later on, when the player clicks on a triggered card, to recall the script to execute and it's peripheral variables.
   selectedAbility = eval(getGlobalVariable('Stored Effects'))
   if selectedAbility.has_key(card._id): whisper(":::WARNING::: {} already has a triggered ability waiting to be activated. Ignoring latest trigger".format(card))
   else: 
      selectedAbility[card._id] = (Autoscript,cost,previousHighlight,actionType,preTargetCard,count)
      # We set a tuple of variables for when we come back to executre the scripts
      # The first variable is tracking which script is going to be used
      # The Second is the amount of resource payment 
      # The third entry in the tuple is the card's previous highlight if it had any.
      # The fourth entry in the tuple is the type of autoscript this is. In this case it's a 'USE' script, which means it was manually triggered by the player
      # The fifth is used to parse pre-selected targets for the card effects. Primarily used in autoscriptOtherPlayers()
      # The sixth entry is used to pass an amount some scripts require (e.g. the difference in edge ranks for Bounty)
      setGlobalVariable('Stored Effects',str(selectedAbility))
   debugNotify("<<< storeCardEffects()")
   
def freeUnitPlacement(card): # A function which stores a unit's position when it leaves play, so that it can be re-used by a different unit
   if Automations['Placement'] and card.Type == 'Unit':
      if card.owner == me and card.highlight != DummyColor and card.highlight != UnpaidColor and card.highlight != CapturedColor and card.highlight != EdgeColor:
         freePositions = eval(me.getGlobalVariable('freePositions')) # We store the currently released position
         freePositions.append(card.position)
         me.setGlobalVariable('freePositions',str(freePositions))
         
def chkEffectTrigger(card,actionType = 'Discard',silent = False): # Checks if a card has a currently waiting-to-trigger script, in order to avoid removing it from the table.
   debugNotify(">>> chkEffectTrigger()")
   selectedAbility = eval(getGlobalVariable('Stored Effects'))
   if selectedAbility.has_key(card._id):
      if not silent: scriptPostponeNotice(actionType)
      debugNotify("<<< chkEffectTrigger() with True")
      return True # If the unit now has the Ready Effect Highlight, it means we're pausing our attack to allow the player to decide to use the react or not. 
   debugNotify("<<< chkEffectTrigger() with False")
   return False

def scriptPostponeNotice(actionType = None):
   if actionType: delayed_whisper(":::INFO::: {} PAUSED while card's React in progress. Use or ignore the react trigger to continue.".format(actionType.capitalize()))
   else: delayed_whisper(":::INFO::: Script execution PAUSED to allow other players to react.")
   
def chkHardcore(card):
   debugNotify(">>> chkHardcore() for {}".format(card)) #Returns True if the controller of a card has hardcore mode enabled.
   if card.owner == me: hardcoreMode = Automations['HARDCORE']
   else: 
      oppAutomations = eval(card.owner.getGlobalVariable('Switches'))
      hardcoreMode = oppAutomations['HARDCORE']
   debugNotify("<<< chkHardcore() with return {}".format(hardcoreMode))
   return hardcoreMode

def cardsLeaving(card,action = 'chk'):
   debugNotify(">>> modCardsLeaving() for {} with action {}".format(card,action)) #Returns True if the controller of a card has hardcore mode enabled.
   cardsLeavingPlay = eval(getGlobalVariable('Cards Leaving Play'))
   if action == 'remove':
      if card._id in cardsLeavingPlay: 
         debugNotify("Removing from cardsLeavingPlay")
         cardsLeavingPlay.remove(card._id)
         setGlobalVariable('Cards Leaving Play',str(cardsLeavingPlay))
      else: debugNotify("Card ID was not in cardsLeavingPlay")
      cardLeaving = False
   elif action == 'append': 
      if card._id not in cardsLeavingPlay: 
         debugNotify("Adding to cardsLeavingPlay")
         cardsLeavingPlay.append(card._id)
         setGlobalVariable('Cards Leaving Play',str(cardsLeavingPlay))
      else: debugNotify("Card ID already in cardsLeavingPlay")
      cardLeaving = True
   else: # If no action is specified,then we just check if the card is in the array.
      if card._id in cardsLeavingPlay: cardLeaving = True
      else: cardLeaving = False      
   debugNotify("<<< modCardsLeaving with cardLeaving = {}".format(cardLeaving))
   return cardLeaving
   
def setupMultiPlayer():
   debugNotify(">>> setupMultiPlayer()") #Debug
   global MPxOffset, MPyOffset, myAllies
   TwoPlayerPos = {'#1':350, '#2':-350}
   ThreePlayerPos = {'#1':0, '#2':350, '#3':-350}
   for player in getPlayers():
      if len(player.hand) == 0 and not confirm("Have all the players loaded their decks?\
                                            \n\n(If not, the game will not be able to setup correctly. Press 'Yes' only if everyone but spectators have loaded a deck"): 
         return 'ABORT'         
   myAllies = []
   for player in getPlayers():
      if player.getGlobalVariable('Side') == Side:
         myAllies.append(player)
   if len(myAllies) == 1: MPxOffset = 0 # With just one player per side, we just leave them at the default placement
   elif len(myAllies) == 2:
      debugNotify("Starting 2 player MP setup for {}".format(me))
      availablePos = findAvailablePos(myAllies)
      if len(availablePos) == 2:
         debugNotify("Found 2 available positions")
         posChoice = SingleChoice("Select your player position for this game.", availablePos)
         doubleCheckPos = findAvailablePos(myAllies)
         if availablePos[posChoice] in doubleCheckPos: # Double checking to avoid syncronized choices.
            me.setGlobalVariable('PLnumber', availablePos[posChoice]) 
            debugNotify("Just set {} PLnumber shared var to {}".format(me,me.getGlobalVariable('PLnumber')),4)
            MPxOffset = playerside * TwoPlayerPos[availablePos[posChoice]]
         else:
            whisper(":::ERROR::: Oops! It seems the other player was faster than you and already picked the {} position. Automatically setting you as Player {}".format(availablePos[posChoice],doubleCheckPos[0]))
            me.setGlobalVariable('PLnumber', doubleCheckPos[0])        
            MPxOffset = playerside * TwoPlayerPos[doubleCheckPos[0]]
      elif len(availablePos) == 1:
         debugNotify("Found 1 available position")
         me.setGlobalVariable('PLnumber', availablePos[0]) 
         MPxOffset = playerside * TwoPlayerPos[availablePos[0]]
      else: 
         notify(":::ERROR::: 0 Available Player Positions. Something went wrong?")
         return 'ABORT'
   elif len(myAllies) == 3: 
      debugNotify("Starting 3 player MP setup")
      extraTXT = ''
      availablePos = findAvailablePos(myAllies)
      if len(availablePos) == 3:
         debugNotify("Found 3 available positions")
         posChoice = SingleChoice("Select your player position for this game.", availablePos)
         doubleCheckPos = findAvailablePos(myAllies)
         if availablePos[posChoice] in doubleCheckPos:
            me.setGlobalVariable('PLnumber', availablePos[posChoice]) 
            MPxOffset = playerside * ThreePlayerPos[availablePos[posChoice]]      
         else: 
            availablePos = doubleCheckPos
            extraTXT = "Oops! It seems another player was faster than you and already picked the {} position.  Please choose again.\n\n".format(availablePos[posChoice])
      if len(availablePos) == 2:
         debugNotify("Found 2 available positions")
         posChoice = SingleChoice("{}Select your player position for this game.".format(extraTXT), availablePos)
         doubleCheckPos = findAvailablePos(myAllies)
         if availablePos[posChoice] in doubleCheckPos:
            me.setGlobalVariable('PLnumber', availablePos[posChoice]) 
            MPxOffset = playerside * ThreePlayerPos[availablePos[posChoice]]      
         else: 
            whisper(":::ERROR::: Oops! It seems the other player was faster than you and already picked the {} position. Automatically setting you as Player {}".format(availablePos[posChoice],doubleCheckPos[0]))
            me.setGlobalVariable('PLnumber', doubleCheckPos[0])        
            MPxOffset = ThreePlayerPos[doubleCheckPos[0]]
      elif len(availablePos) == 1:
         debugNotify("Found 1 available position")
         me.setGlobalVariable('PLnumber', availablePos[0]) 
         MPxOffset = playerside * ThreePlayerPos[availablePos[0]]
      if MPxOffset == 0: MPyOffset = playerside * 250
   me.setGlobalVariable('MPxOffset', str(MPxOffset))    
   me.setGlobalVariable('MPyOffset', str(MPyOffset))    
   if len(myAllies) > 0: me.setGlobalVariable('myAllies', str([player._id for player in myAllies]))    
   debugNotify("<<< setupMultiPlayer() with MPxOffset = {}".format(MPxOffset)) #Debug
   
def findAvailablePos(myAllies):
   debugNotify(">>> findAvailablePos()") #Debug
   if len(myAllies) == 2: # 2v2 or #2v1
      availablePos = ['#1','#2']
      for player in myAllies:
         PLpos = player.getGlobalVariable('PLnumber')
         debugNotify("Just grabbed {} Shared PLnumber and it is {}".format(player,PLpos),4)
         if PLpos != '': 
            availablePos.remove(PLpos)
            debugNotify("{} position {} removed from list. Current list = {}".format(player, PLpos, availablePos), 4)
         else: debugNotify("{} position not set yet".format(player), 4)
   elif len(myAllies) == 3: # 3v1
      availablePos = ['#1','#2','#3']
      for player in myAllies:
         PLpos = player.getGlobalVariable('PLnumber')
         if PLpos != '': availablePos.remove(PLpos)
   else: availablePos = [] # Single player on that side
   debugNotify("<<< findAvailablePos() with return: {}".format(availablePos)) #Debug
   return availablePos

def clearFirstTurn(Init = True):
   debugNotify(">>> clearFirstTurn()") #Debug
   global firstTurn
   if Init:
      for player in myAllies: 
         if player == me: firstTurn = False
         else: remoteCall(player, 'clearFirstTurn', [False])
   else: firstTurn = False
   debugNotify("<<< clearFirstTurn()") #Debug

def giveBoTD():
   debugNotify(">>> giveBoTD()") #Debug
   mute()
   BotD = getSpecial('BotD')
   if BotD.alternate == 'DarkSide': BotD.switchTo()
   else: BotD.switchTo('DarkSide')
   firstPlayer = findOpponent()
   mainAffiliation = getSpecial('Affiliation',firstPlayer)
   x,y = mainAffiliation.position
   debugNotify("First Affiliation is {} at position {} {}".format(mainAffiliation, x,y,)) #Debug
   BotD.moveToTable(x, y - (playerside * 75))
   giveCard(BotD,firstPlayer)
   debugNotify("<<< giveBoTD()") #Debug

def refreshObjectives():
   debugNotify(">>> refreshObjectives()") #Debug
   mute()
   while len(eval(me.getGlobalVariable('currentObjectives'))) < 3:
      card = me.piles['Objective Deck'].top()
      storeObjective(card)
   debugNotify("<<< refreshObjectives()") #Debug
   
def unsetRefillDone(): # A function that sets a global variable which tracks if each player has refilled their hand this draw phase. 
   global handRefillDone
   handRefillDone = False
   
def chkRefillDone(): # A function that refills the hand of each player who has not done so until now
   if not handRefillDone and Automations['Start/End-of-Turn/Phase']: refillHand()
   
def clearAllParticipations(remoted = False):
   mute()
   debugNotify(">>> clearAllParticipations() with remoted = {}".format(remoted)) #Debug
   if not remoted:
      for player in getPlayers(): 
         debugNotify("Remote sending to {}".format(player),4)
         remoteCall(player,'clearAllParticipations',[True])
   else:
      rnd(1,100) # A small wait to allow all our card controls to return to us.
      for card in table:
         if card.controller == me:
            if card.highlight == DefendColor: card.highlight = None
            if card.orientation == Rot90: 
               card.orientation = Rot0
               returnSupportUnit(card)
   debugNotify("<<< clearAllParticipations() with remoted = {}".format(remoted)) #Debug

def returnSupportUnit(card):
   mute()
   debugNotify(">>> returnSupportUnit()") #Debug
   debugNotify("{} is supporting. Attempting to return".format(card))
   if card.markers[mdict['Support']]: # If the card has the default support marker, we simply return it to its owner
      debugNotify("Default Support marker found")
      card.markers[mdict['Support']] = 0
      claimCard(card, card.owner)
   else:
      for player in getPlayers(): # If the card has a custom support marker, means its current permanent controller is not the owner (e.g. Mara Jade)
         debugNotify("Checking markers for {}".format(player),4)
         customSupportMarker = findMarker(card, "Support:{}".format(player.name)) # So we check each player, to see who's name matches the marker
         if customSupportMarker: # If we find the player, we pass control of the card back to them after this engagement.
            debugNotify("Custom Support marker found: {}".format(customSupportMarker[0]))
            card.markers[customSupportMarker] = 0
            claimCard(card, player)
   debugNotify("<<< returnSupportUnit()") #Debug

#------------------------------------------------------------------------------
# Switches
#------------------------------------------------------------------------------

def switchAutomation(type,command = 'Off'):
   debugNotify(">>> switchAutomation(){}".format(extraASDebug())) #Debug
   global Automations
   if (Automations[type] and command == 'Off') or (not Automations[type] and command == 'Announce'):
      if type == 'HARDCORE': 
         notify ("--> The force is not strong within {}. HARDCORE mode deactivated.".format(me))
         setSetting('HARDCORE', False) # We store the HARDCORE value so that the player doesn't have to set it each time
      else: notify ("--> {}'s {} automations are OFF.".format(me,type))
      if command != 'Announce': Automations[type] = False
   else:
      if type == 'HARDCORE': 
         notify ("--> {} trusts their feelings. HARDCORE mode activated!".format(me))
         setSetting('HARDCORE', True) # We store the HARDCORE value so that the player doesn't have to set it each time
      else: notify ("--> {}'s {} automations are ON.".format(me,type))
      if command != 'Announce': Automations[type] = True
   me.setGlobalVariable('Switches',str(Automations))
   
def switchPlayAutomation(group,x=0,y=0):
   debugNotify(">>> switchPlayAutomation(){}".format(extraASDebug())) #Debug
   switchAutomation('Play')
   
def switchTriggersAutomation(group,x=0,y=0):
   debugNotify(">>> switchTriggersAutomation(){}".format(extraASDebug())) #Debug
   switchAutomation('Triggers')

def switchStartEndAutomation(group,x=0,y=0):
   debugNotify(">>> switchStartEndAutomation(){}".format(extraASDebug())) #Debug
   if Automations['Start/End-of-Turn/Phase'] and not confirm(":::WARNING::: Disabling these automations means that you'll have to do each phase's effects manually.\
                                                            \nThis means removing a focus from each card, increasing the dial and refreshing your hand.\
                                                            \nThis can add a significant amount of time to each turn's busywork.\
                                                            \nAre you sure you want to disable? (You can re-enable again by using the same menu option)"): return
   switchAutomation('Start/End-of-Turn/Phase')
   
def switchWinForms(group,x=0,y=0):
   debugNotify(">>> switchWinForms(){}".format(extraASDebug())) #Debug
   switchAutomation('WinForms')

def switchPlacement(group,x=0,y=0):
   debugNotify(">>> switchPlacement(){}".format(extraASDebug())) #Debug
   switchAutomation('Placement')
   
def switchAll(group,x=0,y=0):
   debugNotify(">>> switchAll(){}".format(extraASDebug())) #Debug
   switchAutomation('Play')
   switchAutomation('Triggers')
   switchAutomation('Start/End-of-Turn/Phase')
   switchAutomation('Placement')
   
def switchHardcore(group,x=0,y=0):
   debugNotify(">>> switchHardcore(){}".format(extraASDebug())) #Debug
   switchAutomation('HARDCORE')
   
def switchUnitLocation(group,x=0,y=0):
   debugNotify(">>> switchUnitLocation(){}".format(extraASDebug())) #Debug
   unitPlacement = getSetting('Unit Placement', 'Center')
   if unitPlacement == 'Center':
      setSetting('Unit Placement', 'Left')
      whisper("Your default unit placement has now been left-aligned")
   else:
      setSetting('Unit Placement', 'Center')
      whisper("Your default unit placement has now been centered")
   
def switchSounds(group,x=0,y=0):
   debugNotify(">>> switchSounds(){}".format(extraASDebug())) #Debug
   if getSetting('Sounds', True):
      setSetting('Sounds', False)
      whisper("Sound effects have been switched off")
   else:
      setSetting('Sounds', True)
      whisper("Sound effects have been switched on")
   
def switchButtons(group,x=0,y=0):
   debugNotify(">>> switchSounds(){}".format(extraASDebug())) #Debug
   mute()
   if getSetting('Buttons', True):
      setSetting('Buttons', False)
      for c in table:
         if c.Type == 'Button' and c.owner == me: c.moveTo(me.piles['Removed from Game'])
      whisper("Buttons have been disabled")
   else:
      setSetting('Buttons', True)
      table.create("eeb4f11c-3bb0-4e84-bc4e-97f51bf2dbdc", (playerside * 340) - 25, (playerside * 20) + yaxisMove(Affiliation), 1, True) # The OK Button
      table.create("92df7072-0613-4e76-9fb0-e1b2b6d46473", (playerside * 340) - 25, (playerside * 60) + yaxisMove(Affiliation), 1, True) # The Wait! Button
      table.create("ef1f6e91-4d7f-4a10-963c-832953f985b8", (playerside * 340) - 25, (playerside * 100) + yaxisMove(Affiliation), 1, True) # The Actions? Button      
      whisper("Buttons have been re-enabled.")
   
def switchUniCode(group,x=0,y=0,command = 'Off'):
   debugNotify(">>> switchUniCode(){}".format(extraASDebug())) #Debug
   global UniCode
   if UniCode and command != 'On':
      whisper("Credits and Clicks will now be displayed as normal ASCII.".format(me))
      UniCode = False
   else:
      whisper("Credits and Clicks will now be displayed as Unicode.".format(me))
      UniCode = True

#------------------------------------------------------------------------------
# Help functions
#------------------------------------------------------------------------------

def HELP_BalancePhase(group,x=0,y=0):
   table.create('d98d94d5-57ef-4616-875d-41224784cb96', x, y, 1)
def HELP_RefreshPhase(group,x=0,y=0):
   table.create('1c13a82f-74f3-40fa-81f3-9b98523acfc3', x, y, 1)
def HELP_DrawPhase(group,x=0,y=0):
   table.create('6b6c8bd3-07ea-4b21-9ced-07562c16e7d7', x, y, 1)
def HELP_DeploymentPhase(group,x=0,y=0):
   table.create('6d18a054-516f-4ce4-aee5-ec22bb1f300f', x, y, 1)
def HELP_ConflictPhase(group,x=0,y=0):
   table.create('987517ed-111d-4ee0-a8a0-66b9f553e0a8', x, y, 1)
def HELP_ForcePhase(group,x=0,y=0):
   table.create('3aaf2774-97e5-4886-8476-49980647ddc1', x, y, 1)
      
#------------------------------------------------------------------------------
#  Online Functions
#------------------------------------------------------------------------------

def versionCheck():
   debugNotify(">>> versionCheck()") #Debug
   global startupMsg
   me.setGlobalVariable('gameVersion',gameVersion)
   if not startupMsg: MOTD() # If we didn't give out any other message , we give out the MOTD instead.
   startupMsg = True
   ### Below code Not needed anymore in 3.1.x
   # if not startupMsg and (len(getPlayers()) > 1 or debugVerbosity == 0): # At debugverbosity 0 I want to try and download the version.
      # try: (url, code) = webRead('https://raw.github.com/db0/Star-Wars-LCG-OCTGN/master/current_version.txt',3000)
      # except: code = url = None
      # debugNotify("url:{}, code: {}".format(url,code)) #Debug
      # if code != 200 or not url:
         # whisper(":::WARNING::: Cannot check version at the moment.")
         # return
      # detailsplit = url.split('||')
      # currentVers = detailsplit[0].split('.')
      # installedVers = gameVersion.split('.')
      # if len(installedVers) < 3:
         # whisper("Your game definition does not follow the correct version conventions. It is most likely outdated or modified from its official release.")
         # startupMsg = True
      # elif num(currentVers[0]) > num(installedVers[0]) or num(currentVers[1]) > num(installedVers[1]) or num(currentVers[2]) > num(installedVers[2]):
         # notify("{}'s game definition ({}) is out-of-date!".format(me, gameVersion))
         # if confirm("There is a new game definition available!\nYour version: {}.\nCurrent version: {}\n{}\
                     # {}\
                 # \n\nDo you want to be redirected to download the latest version?.\
                   # \n(You'll have to download the game definition, any patch for the current version and the markers if they're newer than what you have installed)\
                     # ".format(gameVersion, detailsplit[0],detailsplit[2],detailsplit[1])):
            # openUrl('http://octgn.gamersjudgement.com/viewtopic.php?f=55&t=581')
         # startupMsg = True
   debugNotify("<<< versionCheck()") #Debug
      
      
def MOTD():
   debugNotify(">>> MOTD()") #Debug
   (MOTDurl, MOTDcode) = webRead('https://raw.github.com/db0/Star-Wars-LCG-OCTGN/master/MOTD.txt',3000)
   if MOTDcode != 200 or not MOTDurl:
      whisper(":::WARNING::: Cannot fetch MOTD info at the moment.")
      return
   if getSetting('MOTD', 'UNSET') != MOTDurl: # If we've already shown the player the MOTD already, we don't do it again.
      setSetting('MOTD', MOTDurl) # We store the current MOTD so that we can check next time if it's the same.
      (DYKurl, DYKcode) = webRead('https://raw.github.com/db0/Star-Wars-LCG-OCTGN/master/DidYouKnow.txt',3000)
      if DYKcode !=200 or not DYKurl:
         whisper(":::WARNING::: Cannot fetch DYK info at the moment.")
         return
      DYKlist = DYKurl.split('||')
      DYKrnd = rnd(0,len(DYKlist)-1)
      while MOTDdisplay(MOTDurl,DYKlist[DYKrnd]) == 'MORE': 
         MOTDurl = '' # We don't want to spam the MOTD for the further notifications
         DYKrnd += 1
         if DYKrnd == len(DYKlist): DYKrnd = 0
   debugNotify("<<< MOTD()") #Debug
   
def MOTDdisplay(MOTD,DYK):
   debugNotify(">>> MOTDdisplay()") #Debug
   if re.search(r'http',MOTD): # If the MOTD has a link, then we do not sho DYKs, so that they have a chance to follow the URL
      MOTDweb = MOTD.split('&&')      
      if confirm("{}".format(MOTDweb[0])): openUrl(MOTDweb[1].strip())
   elif re.search(r'http',DYK):
      DYKweb = DYK.split('&&')
      if confirm("{}\
              \n\nDid You Know?:\
                \n------------------\
                \n{}".format(MOTD,DYKweb[0])):
         openUrl(DYKweb[1].strip())
   elif confirm("{}\
              \n\nDid You Know?:\
                \n-------------------\
                \n{}\
                \n-------------------\
              \n\nWould you like to see the next tip?".format(MOTD,DYK)): return 'MORE'
   return 'STOP'

def initGame(): # A function which prepares the game for online submition
   debugNotify(">>> initGame()") #Debug
   if getGlobalVariable('gameGUID') != 'None': return #If we've already grabbed a GUID, then just use that.
   (gameInit, initCode) = webRead('http://84.205.248.92/slaghund/init.swlcg',3000)
   if initCode != 200:
      #whisper("Cannot grab GameGUID at the moment!") # Maybe no need to inform players yet.
      return
   debugNotify("{}".format(gameInit), 2) #Debug
   GUIDregex = re.search(r'([0-9a-f-]{36}).*?',gameInit)
   if GUIDregex: setGlobalVariable('gameGUID',GUIDregex.group(1))
   else: setGlobalVariable('gameGUID','None') #If for some reason the page does not return a propert GUID, we won't record this game.
   setGlobalVariable('gameEnded','False')
   debugNotify("<<< initGame()", 3) #Debug
   
def reportGame(result = 'DialVictory'): # This submits the game results online.
   if len(myAllies) > 1 or len(fetchAllOpponents()) > 1:
      notify("Thanks for playing. Please submit any bugs or feature requests on github.\n-- https://github.com/db0/Star-Wars-LCG-OCTGN/issues")
      return # We currently do not record multiplayer stats
   delayed_whisper("Please wait. Submitting Game Stats...")     
   debugNotify(">>> reportGame()") #Debug
   if not Automations['Play'] or not Automations['Triggers'] or not Automations['Start/End-of-Turn/Phase']:
      notify(":::INFO::: Aborting Stat Submission because automations are disabled")
      return
   GUID = getGlobalVariable('gameGUID')
   if GUID == 'None' and debugVerbosity < 0: return # If we don't have a GUID, we can't submit. But if we're debugging, we go through.
   gameEnded = getGlobalVariable('gameEnded')
   if gameEnded == 'True':
     if not confirm("Your game already seems to have finished once before. Do you want to change the results to '{}' for {}?".format(result,me.name)): return
   GNAME = currentGameName()
   LEAGUE = getGlobalVariable('League')
   TURNS = turnNumber()
   VERSION = gameVersion
   RESULT = result
   gameStats = eval(getGlobalVariable('Game Stats'))
   debugNotify("Retrieved gameStats ") #Debug
   debugNotify("gameStats = {}".format(gameStats), 4) #Debug
   PLAYER = me.name # Seeting some variables for readability in the URL
   AFFILIATION = Affiliation.Affiliation
   if result == 'DeckDefeat' or result == 'DialDefeat' or result == 'ObjectiveDefeat' or result == 'SpecialDefeat' or result == 'Conceded': WIN = 0
   else: WIN = 1
   DIAL = me.counters['Death Star Dial'].value
   if DIAL > 12: DIAL = 12
   OBJECTIVES = me.counters['Objectives Destroyed'].value
   PODS = me.getGlobalVariable('Pods')
   UNITS = gameStats[me.name]['units'] # How many units the player brought into play
   RESOURCES = gameStats[me.name]['resources'] # How many Resources that player generated
   ATTACKS = gameStats[me.name]['attacks'] # How many objectives that player engaged
   EDGEVICTORIES = gameStats[me.name]['edgev'] # How many edge battles the player won
   FORCEVICTORIES = gameStats[me.name]['forcev'] # How many force struggles the player won
   FORCETURNS = gameStats[me.name]['forceturns'] # How many balance phases the player started with the force.
   debugNotify("About to report player results online.", 2) #Debug
   if (TURNS < 1 or len(getPlayers()) == 1) and debugVerbosity < 1:
      notify(":::ATTENTION:::Game stats submit aborted due to number of players ( less than 2 ) or turns played (less than 1)")
      return # You can never win before the first turn is finished and we don't want to submit stats when there's only one player.
   reportURL = 'http://84.205.248.92/slaghund/game.swlcg?g={}&u={}&r={}&w={}&aff={}&p={}&d={}&o={}&t={}&v={}&lid={}&gname={}&stu={}&str={}&sta={}&ste={}&stf={}&stb={}'.format(GUID,PLAYER,RESULT,WIN,AFFILIATION,PODS,DIAL,OBJECTIVES,TURNS,VERSION,LEAGUE,GNAME,UNITS,RESOURCES,ATTACKS,EDGEVICTORIES,FORCEVICTORIES,FORCETURNS)
   if debugVerbosity < 1: # We only submit stats if we're not in debug mode
      (reportTXT, reportCode) = webRead(reportURL,10000)
   else: 
      if confirm('Report URL: {}\n\nSubmit?'.format(reportURL)):
         (reportTXT, reportCode) = webRead(reportURL,10000)
         notify('Report URL: {}'.format(reportURL))
   try:
      if (reportTXT != "Adding result...Ok!" and reportTXT != "Updating result...Ok!") and debugVerbosity >=0: notify("Failed to submit match results. Sorry.") 
   except: pass
   # The victorious player also reports for their enemy
   enemyPLs = ofwhom('-ofOpponent')
   enemyPL = enemyPLs[0]
   ENEMY = enemyPL.name
   enemyAff = getSpecial('Affiliation',enemyPL)
   E_AFFILIATION = enemyAff.Affiliation
   debugNotify("Enemy Affiliation: {}".format(E_AFFILIATION), 2) #Debug
   if result == 'DialVictory': 
      E_RESULT = 'DialDefeat'
      E_WIN = 0
   elif result == 'DialDefeat': 
      E_RESULT = 'DealVictory'
      E_WIN = 1
   elif result == 'ObjectiveVictory': 
      E_RESULT = 'ObjectiveDefeat'
      E_WIN = 0
   elif result == 'ObjectiveDefeat': 
      E_RESULT = 'ObjectiveVictory'
      E_WIN = 1
   elif result == 'SpecialVictory': 
      E_RESULT = 'SpecialDefeat'
      E_WIN = 0
   elif result == 'SpecialDefeat': 
      E_RESULT = 'SpecialVictory'
      E_WIN = 1
   elif result == 'DeckDefeat':
      E_RESULT = 'DeckVictory'
      E_WIN = 1  
   elif result == 'Conceded':
      E_RESULT = 'ConcedeVictory'
      E_WIN = 1  
   else: 
      E_RESULT = 'Unknown'
      E_WIN = 0
   E_DIAL = enemyPL.counters['Death Star Dial'].value
   if E_DIAL > 12: E_DIAL = 12
   E_OBJECTIVES = enemyPL.counters['Objectives Destroyed'].value
   E_PODS = enemyPL.getGlobalVariable('Pods')
   E_UNITS = gameStats[enemyPL.name]['units'] # How many units the player brought into play
   E_RESOURCES = gameStats[enemyPL.name]['resources'] # How many Resources that player generated
   E_ATTACKS = gameStats[enemyPL.name]['attacks'] # How many objectives that player engaged
   E_EDGEVICTORIES = gameStats[enemyPL.name]['edgev'] # How many edge battles the player won
   E_FORCEVICTORIES = gameStats[enemyPL.name]['forcev'] # How many force struggles the player won
   E_FORCETURNS = gameStats[enemyPL.name]['forceturns'] # How many balance phases the player started with the force.
   debugNotify("About to report enemy results online.", 2) #Debug
   E_reportURL = 'http://84.205.248.92/slaghund/game.swlcg?g={}&u={}&r={}&w={}&aff={}&p={}&d={}&o={}&t={}&v={}&lid={}&gname={}&stu={}&str={}&sta={}&ste={}&stf={}&stb={}'.format(GUID,ENEMY,E_RESULT,E_WIN,E_AFFILIATION,E_PODS,E_DIAL,E_OBJECTIVES,TURNS,VERSION,LEAGUE,GNAME,E_UNITS,E_RESOURCES,E_ATTACKS,E_EDGEVICTORIES,E_FORCEVICTORIES,E_FORCETURNS)
   if debugVerbosity < 1: # We only submit stats if we're not debugging
      (EreportTXT, EreportCode) = webRead(E_reportURL,10000)
   setGlobalVariable('gameEnded','True')
   notify("Thanks for playing. Please submit any bugs or feature requests on github.\n-- https://github.com/db0/Star-Wars-LCG-OCTGN/issues")
   notify("\n =+= Please consider supporting the development of this plugin\n =+= http://www.patreon.com/db0\n")
   debugNotify("<<< reportGame()", 3) #Debug

def setleague(group = table, x=0,y=0, manual = True):
   debugNotify(">>> setleague()") #Debug
   mute()
   league = getGlobalVariable('League')
   origLeague = league
   debugNotify("global var = {}".format(league))
   if league == '': # If there is no league set, we attempt to find out the league name from the game name
      for leagueTag in knownLeagues:
         if re.search(r'{}'.format(leagueTag),currentGameName()): league = leagueTag
   debugNotify("League after automatic check: {}".format(league))
   if manual:
      if not confirm("Do you want to set this match to count for an active league\n(Pressing 'No' will unset this match from all leagues)"): league = ''
      else:
         choice = SingleChoice('Please Select One the Active Leagues', [knownLeagues[leagueTag] for leagueTag in knownLeagues])
         if choice != None: league = [leagueTag for leagueTag in knownLeagues][choice]
   debugNotify("League after manual check: {}".format(league))
   debugNotify("Comparing with origLeague: {}".format(origLeague))
   if origLeague != league:
      if manual: 
         if league ==  '': notify("{} sets this match as casual".format(me))
         else: notify("{} sets this match to count for the {}".format(me,knownLeagues[league]))
      elif league != '': notify(":::LEAGUE::: This match will be recorded for the the {}. (press Ctrl+Alt+L to unset)".format(knownLeagues[league]))
   elif manual: 
         if league == '': delayed_whisper("Game is already casual.")
         else: delayed_whisper("Game already counts for the {}".format(me,knownLeagues[league]))
   setGlobalVariable('League',league)
   debugNotify(">>> setleague() with league: {}".format(league)) #Debug
   
   
def incrStat(stat,playerName):
   # This command increments one of the player's game stats by one. The available stats are:
   # 'units'         : How many units the player brought into play
   # 'resources'     : How many Resources that player generated
   # 'attacks'       : How many objectives that player engaged
   # 'edgev'         : How many edge battles the player won
   # 'forcev'        : How many force struggles the player won
   # 'forceturns'    : How many balance phases the player started with the force.
   # These are then stored into a global variable which is a nested dictionary. First dictionary contains a dictionaty for each player's name with their individual stats.
   debugNotify(">>> incrStat() - {} for {}".format(stat,playerName)) #Debug
   if len(myAllies) > 1 or len(fetchAllOpponents()) > 1: return # We currently do not record multiplayer stats
   try: # Just in case. We don't want to break the whole game.
      gameStats = eval(getGlobalVariable('Game Stats'))
      debugNotify("gameStats = {}".format(gameStats), 4) #Debug
      if not gameStats[playerName][stat]: gameStats[playerName][stat] = 1 # If we haven't put a value in this dictionary key for some reason yet, then set it to 1 now.
      else: gameStats[playerName][stat] += 1
      setGlobalVariable('Game Stats', str(gameStats))
   except: notify(":::ERROR::: When trying to increment game stats")
   debugNotify("<<< incrStat()") #Debug
   
def resetGameStats():
   debugNotify(">>> resetGameStats()") #Debug
   gameStats = eval(getGlobalVariable('Game Stats'))
   if gameStats == '': 
      debugNotify("Gamestats NULL")
      gameStats = {}
   debugNotify("gameStats = {}".format(gameStats), 4) #Debug
   for player in getPlayers():
      debugNotify("Resetting for {}".format(player))
      gameStats[player.name] = {}
      gameStats[player.name]['units'] = 0      
      gameStats[player.name]['resources'] = 0      
      gameStats[player.name]['attacks'] = 0      
      gameStats[player.name]['edgev'] = 0      
      gameStats[player.name]['forcev'] = 0      
      gameStats[player.name]['forceturns'] = 0      
   setGlobalVariable('Game Stats', str(gameStats))
   debugNotify("<<< resetGameStats()") #Debug
   
   
def fetchCardScripts(group = table, x=0, y=0, silent = False): # Creates 2 dictionaries with all scripts for all cards stored, based on a web URL or the local version if that doesn't exist.
   debugNotify(">>> fetchCardScripts()") #Debug
   ### Note to self. Switching on Debug Verbosity here tends to crash the game.probably because of bug #596
   global CardsAA, CardsAS # Global dictionaries holding Card AutoActions and Card autoScripts for all cards.
   if not silent: whisper("+++ Fetching fresh scripts. Please Wait...")
   if len(getPlayers()) > 1 and debugVerbosity < 0:
      try: (ScriptsDownload, code) = webRead('https://raw.github.com/db0/Star-Wars-LCG-OCTGN/master/o8g/Scripts/CardScripts.py',5000)
      except: 
         if debugVerbosity >= 0: notify("Timeout Error when trying to download scripts")
         code = ScriptsDownload = None
   else: # If we have only one player, we assume it's a debug game and load scripts from local to save time.
      if debugVerbosity >= 0: notify("Skipping Scripts Download for faster debug")
      code = 0
      ScriptsDownload = None
   debugNotify("code: {}, text: {}".format(code, ScriptsDownload)) #Debug
   if code != 200 or not ScriptsDownload or (ScriptsDownload and not re.search(r'ANR CARD SCRIPTS', ScriptsDownload)): 
      whisper(":::WARNING::: Cannot download card scripts at the moment. Will use locally stored ones.")
      Split_Main = ScriptsLocal.split('=====') # Split_Main is separating the file description from the rest of the code
   else: 
      #WHAT THE FUUUUUCK? Why does it gives me a "value cannot be null" when it doesn't even come into this path with a broken connection?!
      #WHY DOES IT WORK IF I COMMENT THE NEXT LINE. THIS MAKES NO SENSE AAAARGH!
      #ScriptsLocal = ScriptsDownload #If we found the scripts online, then we use those for our scripts
      Split_Main = ScriptsDownload.split('=====')
   if debugVerbosity >= 5:  #Debug
      notify(Split_Main[1])
      notify('=====')
   Split_Cards = Split_Main[1].split('.....') # Split Cards is making a list of a different cards
   if debugVerbosity >= 5: #Debug
      notify(Split_Cards[0]) 
      notify('.....')
   for Full_Card_String in Split_Cards:
      if re.search(r'ENDSCRIPTS',Full_Card_String): break # If we have this string in the Card Details, it means we have no more scripts to load.
      Split_Details = Full_Card_String.split('-----') # Split Details is splitting the card name from its scripts
      if debugVerbosity >= 5:  #Debug
         notify(Split_Details[0])
         notify('-----')
      # A split from the Full_Card_String always should result in a list with 2 entries.
      if debugVerbosity >= 5: notify(Split_Details[0].strip()) # If it's the card name, notify us of it.
      Split_Scripts = Split_Details[2].split('+++++') # List item [1] always holds the two scripts. autoScripts and AutoActions.
      CardsAS[Split_Details[1].strip()] = Split_Scripts[0].strip()
      CardsAA[Split_Details[1].strip()] = Split_Scripts[1].strip()
      if debugVerbosity >= 5: notify(Split_Details[0].strip() + "-- STORED")
   if num(getGlobalVariable('Turn')) > 0: whisper("+++ All card scripts refreshed!")
   if debugVerbosity >= 5: # Debug
      notify("CardsAS Dict:\n{}".format(str(CardsAS)))
      notify("CardsAA Dict:\n{}".format(str(CardsAA))) 
   debugNotify("<<< fetchCardScripts()") #Debug
   
#------------------------------------------------------------------------------
# Debugging
#------------------------------------------------------------------------------
   
def TrialError(group, x=0, y=0): # Debugging
   global Side, debugVerbosity
   mute()
   ######## Testing Corner ########
   # for i in range(4):
      # time.sleep(1)
      # update()
      # notify("i = {}".format(i))
   ###### End Testing Corner ######
   #notify("### Setting Debug Verbosity")
   if debugVerbosity >=0: 
      if debugVerbosity == 0: 
         debugVerbosity = 1
         #ImAProAtThis() # At debug level 1, we also disable all warnings
      elif debugVerbosity == 1: debugVerbosity = 2
      elif debugVerbosity == 2: debugVerbosity = 3
      elif debugVerbosity == 3: debugVerbosity = 4
      else: debugVerbosity = 0
      notify("Debug verbosity is now: {}".format(debugVerbosity))
      return
   notify("### Checking Players")
   for player in getPlayers():
      if player.name == 'db0' or player.name == 'dbzer0': debugVerbosity = 0
   notify("### Checking Debug Validity")
   if not (len(getPlayers()) == 1 or debugVerbosity >= 0): 
      whisper("This function is only for development purposes")
      return
   notify("### Checking Side")
   if not Side: 
      if confirm("Dark Side?"): Side = "Dark"
      else: Side = "Light"
   notify("### Setting Side")
   me.setGlobalVariable('Side', Side) 
   notify("### Setting Table Side")
   if not playerside:  # If we've already run this command once, don't recreate the cards.
      chooseSide()
      #createStartingCards()
   if confirm("Spawn Test Cards?"):
      spawnTestCards()
      spawnSetCards()

def spawnTestCards():
   testcards = [  
                "ff4fb461-8060-457a-9c16-000000000446",
                "ff4fb461-8060-457a-9c16-000000000496"
                ]
   for idx in range(len(testcards)):
      test = table.create(testcards[idx], (70 * idx) - 300, 0, 1, True)
      
def spawnSetCards():
   setCards = []    ### BOTF Set 547 - 636 ###
   for signi in range(547,582 + 1): # We need the +1 in the end to get the last Card ID in the set.
      cID = "ff4fb461-8060-457a-9c16-000000000{}".format(signi)
      try:
         test = table.create(cID, 0, 0, 1, True)
         test.moveTo(me.piles['Removed from Game'])
      except: notify(":::MISSING::: {}".format(cID))

def flipcard(card,x,y):
   card.switchImage
   if card.isAlternateImage: notify("is Alternate")
   elif not card.isAlternateImage: notify("is not Alternate")
   
def extraASDebug(Autoscript = None):
   if Autoscript and debugVerbosity >= 3: return ". Autoscript:{}".format(Autoscript)
   else: return ''

def ShowPos(group, x=0,y=0):
   if debugVerbosity >= 1: 
      notify('x={}, y={}'.format(x,y))
      
def ShowPosC(card, x=0,y=0):
   if debugVerbosity >= 1: 
      notify(">>> ShowPosC(){}".format(extraASDebug())) #Debug
      x,y = card.position
      notify('card x={}, y={}'.format(x,y))
      
def soundTest(group,x,y):
   return
   
def debugPLPos(group = table,x = 0,y = 0):
   mute()
   if confirm("2 allies setup test"):
      for MPxOffset in [350 * playerside, -350 * playerside]:
         Affiliation = table.create("ff4fb461-8060-457a-9c16-000000000095", 0, 0, 1, True) 
         Affiliation.moveToTable(MPxOffset + (playerside * -380) - 25, (playerside * 20) + yaxisMove(Affiliation))
         table.create("eeb4f11c-3bb0-4e84-bc4e-97f51bf2dbdc", MPxOffset + (playerside * -340) - 25, (playerside * 130) + yaxisMove(Affiliation), 1, True) # The OK Button
         table.create("92df7072-0613-4e76-9fb0-e1b2b6d46473", MPxOffset + (playerside * -390) - 25, (playerside * 130) + yaxisMove(Affiliation), 1, True) # The Wait! Button
         table.create("ef1f6e91-4d7f-4a10-963c-832953f985b8", MPxOffset + (playerside * -440) - 25, (playerside * 130) + yaxisMove(Affiliation), 1, True) # The Actions? Button
   else:
      for MPxOffset in [350 * playerside, 0, -350 * playerside]:
         Affiliation = table.create("ff4fb461-8060-457a-9c16-000000000095", 0, 0, 1, True) 
         if MPxOffset == 0: MPyOffset = playerside * 250
         else: MPyOffset = 0
         Affiliation.moveToTable(MPxOffset + (playerside * -380) - 25, MPyOffset + (playerside * 20) + yaxisMove(Affiliation))
         table.create("eeb4f11c-3bb0-4e84-bc4e-97f51bf2dbdc", MPxOffset + (playerside * -340) - 25, MPyOffset + (playerside * 130) + yaxisMove(Affiliation), 1, True) # The OK Button
         table.create("92df7072-0613-4e76-9fb0-e1b2b6d46473", MPxOffset + (playerside * -390) - 25, MPyOffset + (playerside * 130) + yaxisMove(Affiliation), 1, True) # The Wait! Button
         table.create("ef1f6e91-4d7f-4a10-963c-832953f985b8", MPxOffset + (playerside * -440) - 25, MPyOffset + (playerside * 130) + yaxisMove(Affiliation), 1, True) # The Actions? Button
   
def switchPLPos(group = table,x = 0,y = 0):
   global MPxOffset, myAllies, MPyOffset
   mute()
   posChoice = SingleChoice("Switch to which pos?", ['2pl #1','2pl #2','3pl #1','3pl #2','3pl #3'])
   if posChoice == 0: 
      myAllies = [me,me]
      MPxOffset = 350 * playerside
   if posChoice == 1: 
      myAllies = [me,me]
      MPxOffset = -350 * playerside
   if posChoice == 2: 
      myAllies = [me,me,me]
      MPxOffset = 0
      MPyOffset = playerside * 250
   if posChoice == 3: 
      myAllies = [me,me,me]
      MPxOffset = 600 * playerside
   if posChoice == 4: 
      myAllies = [me,me,me]
      MPxOffset = -600 * playerside

def addC(cardModel,count = 1): # Quick function to add custom cards to your hand depending on their GUID
# Use the following to spawn a card
# remoteCall(me,'addC',['<cardGUID>'])
   card = table.create(cardModel, 0,0, count, True)
   returnToHand(card,0,0,True,False)
#   if card.Type == 'ICE' or card.Type == 'Agenda' or card.Type == 'Asset': card.isFaceUp = False   	  
   
