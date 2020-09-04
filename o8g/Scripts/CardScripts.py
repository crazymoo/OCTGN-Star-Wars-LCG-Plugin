### SWLCG CARD SCRIPTS ###
# 5 Equal Signs (=) signifiies a break between the description (what you're currently reading) and the code
# 5 Dashes  (-) signifies a break between the card name, the GUID and the card scripts. The card name is ignored by the code, only the GUID and Scripts are used.
# 5 Plus Signs (+) signifies a break between AutoActions and AutoScripts for the same card
# 5 Dots (.) signifies a break between different cards.
# Card names which start with * have special custom code just for them (cards which use CustomScript or useCustomAbility don't have *)
# Do not edit below the line
ScriptsLocal = '''
=====
"Backstabber"
-----
ff4fb461-8060-457a-9c16-000000000050
-----
onPlay:Deal1Damage-AutoTargeted-atObjective-isCurrentObjective-onlyDuringEngagement-isReact||DeployAllowance:Conflict
+++++

.....
A Disturbance In the Force
-----
ff4fb461-8060-457a-9c16-000000000113
-----
onPlay:Put1Focus-AutoTargeted-atUnit-isCommited-targetOpponents
+++++

.....
A Hero's Journey
-----
ff4fb461-8060-457a-9c16-000000000063
-----

+++++

.....
A Journey to Dagobah
-----
ff4fb461-8060-457a-9c16-000000000149
-----
onThwart:CustomScript-isReact
+++++

.....
A New Hope
-----
ff4fb461-8060-457a-9c16-000000000197
-----

+++++

.....
A-Wing
-----
ff4fb461-8060-457a-9c16-000000000012
-----
onStrike:Draw1Card-isReact
+++++

.....
Admiral Ackbar
-----
ff4fb461-8060-457a-9c16-000000000187
-----
onPlay:Deal1Damage-AutoTargeted-atUnit-targetOpponents-isParticipating-onlyDuringEngagement-isReact||DeployAllowance:Conflict
+++++

.....
Admiral Motti
-----
ff4fb461-8060-457a-9c16-000000000070
-----
afterCardRefreshing:Remove1Focus-AutoTargeted-atUnit-targetMine-choose1-hasMarker{Focus}-duringMyTurn-isReact
+++++

.....
Advisor to the Emperor
-----
ff4fb461-8060-457a-9c16-000000000115
-----

+++++

.....
Aft Armor Plating
-----
ff4fb461-8060-457a-9c16-000000000061
-----
Placement:Vehicle_and_Unit||onHostParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Ancient Monument
-----
ff4fb461-8060-457a-9c16-000000000170
-----
ConstantEffect:Force1Bonus
+++++

.....
Astromech Droid Upgrade
-----
ff4fb461-8060-457a-9c16-000000000175
-----
Placement:Vehicle_and_Unit||BonusIcons:UD:1, BD:1
+++++

.....
AT-ST
-----
ff4fb461-8060-457a-9c16-000000000002
-----
onPlay:Draw1Card-isReact
+++++

.....
AT-ST
-----
ff4fb461-8060-457a-9c16-000000000060
-----
onPlay:Draw1Card-isReact
+++++

.....
AT-ST Commander
-----
ff4fb461-8060-457a-9c16-000000000059
-----

+++++
R1:Put1Shield-AutoTargeted-atUnit_and_Vehicle-isParticipating-targetAllied-choose1-hasntMarker{Shield}
.....
Battlefield Engineers
-----
ff4fb461-8060-457a-9c16-000000000015
-----
onAttack:Remove1Focus-AutoTargeted-atEnhancement-choose1-hasMarker{Focus}-isReact
+++++

.....
Believer in the Old Ways
-----
ff4fb461-8060-457a-9c16-000000000141
-----

+++++

.....
Believer in the Old Ways
-----
ff4fb461-8060-457a-9c16-000000000169
-----

+++++

.....
Black Squadron Assault
-----
ff4fb461-8060-457a-9c16-000000000126
-----

+++++
R0:Put1Focus-isCost$$Remove1Focus-Targeted-atBlack Squadron
.....
Black Squadron Pilot
-----
ff4fb461-8060-457a-9c16-000000000129
-----
onPlay:CustomScript||BonusIcons:UD:1, BD:1
+++++

.....
Blaster Pistol
-----
ff4fb461-8060-457a-9c16-000000000079
-----
Placement:Character_and_Unit||BonusIcons:UD:1
+++++

.....
Boba Fett
-----
ff4fb461-8060-457a-9c16-000000000076
-----

+++++
R0:CaptureTarget-Targeted-atCharacter
.....
Bounty Collection
-----
ff4fb461-8060-457a-9c16-000000000080
-----
onPlay:Remove1Focus-DemiAutoTargeted-atnonUnit-choose3
+++++

.....
C-3PO
-----
ff4fb461-8060-457a-9c16-000000000156
-----

+++++
R0:DestroyMyself$$SimplyAnnounce{cancel the effects of the event card}$$Put1Effects Cancelled-DemiAutoTargeted-atEvent-isReady-choose1-isSilent
.....
Cloud City Casino
-----
ff4fb461-8060-457a-9c16-000000000019
-----

+++++

.....
Common Ground
-----
ff4fb461-8060-457a-9c16-000000000201
-----
Placement:Objective||onHostGenerate:Put1Ignores Affiliation Match-AutoTargeted-isUnpaid
+++++

.....
Control Room
-----
ff4fb461-8060-457a-9c16-000000000032
-----

+++++

.....
Control Room
-----
ff4fb461-8060-457a-9c16-000000000037
-----

+++++

.....
Corellian Engineer
-----
ff4fb461-8060-457a-9c16-000000000163
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Corporate Exploitation
-----
ff4fb461-8060-457a-9c16-000000000081
-----

+++++
R0:Put1Focus-isCost$$BringToPlayTarget-Targeted-atUnit-fromHand
.....
Coruscant Defense Fleet
-----
ff4fb461-8060-457a-9c16-000000000023
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++
R0:Remove1Damage-DemiAutoTargeted-atCoruscant-hasMarker{Damage}-choose1-isCost$$Put1Damage
.....
Counsel of the Sith
-----
ff4fb461-8060-457a-9c16-000000000114
-----
atTurnStart:Draw1Card-duringOpponentTurn-isReact
+++++

.....
Counter-stroke
-----
ff4fb461-8060-457a-9c16-000000000142
-----
onPlay:SimplyAnnounce{cancel the effects of the event}$$Put1Effects Cancelled-Targeted-atEvent-isReady-choose1-isSilent
+++++

.....
Covering Fire
-----
ff4fb461-8060-457a-9c16-000000000007
-----
onPlay:SacrificeTarget-DemiAutoTargeted-atUnit-targetMine-choose1$$Put1Shield-AutoTargeted-atUnit-targetMine-isParticipating-hasntMarker{Shield}
+++++

.....
Crossfire
-----
ff4fb461-8060-457a-9c16-000000000021
-----
onPlay:Put1Crossfire:UD-Targeted-atCharacter||onPlay:Put1Crossfire:BD-Targeted-atCharacter||onPlay:Put1Crossfire:Tactics-Targeted-atCharacter
+++++

.....
Cruel Interrogations
-----
ff4fb461-8060-457a-9c16-000000000120
-----
onPlay:CustomScript-isReact
+++++

.....
Dagobah Training Grounds
-----
ff4fb461-8060-457a-9c16-000000000068
-----

+++++

.....
Dagobah Training Grounds
-----
ff4fb461-8060-457a-9c16-000000000139
-----

+++++

.....
Dark Alliance
-----
ff4fb461-8060-457a-9c16-000000000220
-----
whileInPlay:IgnoreAffiliationMatch
+++++

.....
Dark Alliance
-----
ff4fb461-8060-457a-9c16-000000000221
-----
whileInPlay:IgnoreAffiliationMatch
+++++

.....
Dark Precognition
-----
ff4fb461-8060-457a-9c16-000000000118
-----
onPlay:Draw2Cards
+++++

.....
Dark Side Apprentice
-----
ff4fb461-8060-457a-9c16-000000000104
-----

+++++

.....
Darth Vader
-----
ff4fb461-8060-457a-9c16-000000000103
-----
whileInPlay:Deal1Damage-foreachCardPlayed-byMe-typeEvent_and_Sith-DemiAutoTargeted-atUnit-choose1-targetOpponents-onlyOnce-isReact
+++++

.....
Death and Despayre
-----
ff4fb461-8060-457a-9c16-000000000034
-----

+++++

.....
Death from Above
-----
ff4fb461-8060-457a-9c16-000000000044
-----
onPlay:Put1Death from Above:BD-Targeted-atVehicle_and_Unit
+++++

.....
Death from Above
-----
ff4fb461-8060-457a-9c16-000000000049
-----

+++++

.....
Death Star Trooper
-----
ff4fb461-8060-457a-9c16-000000000053
-----

+++++

.....
Death Star Trooper
-----
ff4fb461-8060-457a-9c16-000000000054
-----

+++++

.....
Decoy at Dantooine
-----
ff4fb461-8060-457a-9c16-000000000192
-----
whileInPlay:Lose1Dial-foreachObjectiveThwarted-byOpponent-isReact
+++++

.....
Defense Protocol
-----
ff4fb461-8060-457a-9c16-000000000040
-----
afterRefresh:Lose1Reserves-duringMyTurn-isReact$$Put1Activation-isSilent$$Deal1Damage-AutoTargeted-atUnit-choose1-targetOpponents||afterDraw:Remove1Activation-duringMyTurn-isCost-isSilent$$Gain1Reserves
+++++

.....
Defense Upgrade
-----
ff4fb461-8060-457a-9c16-000000000038
-----
Placement:Objective
+++++

.....
Detained
-----
ff4fb461-8060-457a-9c16-000000000055
-----
onPlay:CaptureTarget-Targeted-atCharacter_or_Droid
+++++

.....
Devastator
-----
ff4fb461-8060-457a-9c16-000000000035
-----

+++++
R1:Gain1Dial
.....
Double Strike
-----
ff4fb461-8060-457a-9c16-000000000153
-----
onPlay:Remove1Focus-Targeted-atCharacter-hasMarker{Focus}
+++++

.....
Draw Their Fire
-----
ff4fb461-8060-457a-9c16-000000000186
-----

+++++

.....
Duty Officer
-----
ff4fb461-8060-457a-9c16-000000000071
-----

+++++

.....
Emergency Repair
-----
ff4fb461-8060-457a-9c16-000000000165
-----
onPlay:Remove999Damage-Targeted-atObjective
+++++

.....
Emperor Palpatine
-----
ff4fb461-8060-457a-9c16-000000000097
-----
whileInPlay:Retrieve1Card-grabEvent_and_Sith-fromDiscard-foreachObjectiveThwarted-isReact
+++++

.....
Emperor's Royal Guard
-----
ff4fb461-8060-457a-9c16-000000000098
-----

+++++
R0:Remove1Damage-DemiAutoTargeted-atCharacter-hasMarker{Damage}-choose1-isCost$$Put1Damage
.....
Espo Trooper
-----
ff4fb461-8060-457a-9c16-000000000082
-----

+++++

.....
Espo Trooper
-----
ff4fb461-8060-457a-9c16-000000000083
-----

+++++

.....
Espo Trooper
-----
ff4fb461-8060-457a-9c16-000000000084
-----

+++++

.....
Espo Trooper
-----
ff4fb461-8060-457a-9c16-000000000085
-----

+++++

.....
Espo Trooper
-----
ff4fb461-8060-457a-9c16-000000000086
-----

+++++

.....
Ewok Scout
-----
ff4fb461-8060-457a-9c16-000000000205
-----
onAttack:Put1Ewok Scouted-DemiAutoTargeted-atUnit-hasntMarker{Focus}-targetOpponents-choose1
+++++

.....
Ewok Scout
-----
ff4fb461-8060-457a-9c16-000000000206
-----
onAttack:Put1Ewok Scouted-DemiAutoTargeted-atUnit-hasntMarker{Focus}-targetOpponents-choose1-isReact
+++++

.....
Fall Back!
-----
ff4fb461-8060-457a-9c16-000000000196
-----
onPlay:ReturnTarget-Targeted-atUnit-targetAllied
+++++

.....
Fall of the Jedi
-----
ff4fb461-8060-457a-9c16-000000000102
-----
afterRefresh:SendToBottomTarget-Targeted-fromHand-duringMyTurn-isReact
+++++

.....
False Lead
-----
ff4fb461-8060-457a-9c16-000000000195
-----
Placement:Objective||onHostObjectiveThwarted:Lose1Dial-isReact
+++++

.....
Fleeing the Empire
-----
ff4fb461-8060-457a-9c16-000000000132
-----
afterRefresh:Put1Shield-DemiAutoTargeted-atUnit_or_Objective-targetMine-choose1-hasntMarker{Shield}-duringMyTurn-isReact
+++++

.....
Fleet Command Center
-----
ff4fb461-8060-457a-9c16-000000000190
-----
afterRefresh:Put1Shield-DemiAutoTargeted-atUnit-hasntMarker{Shield}-targetAllied-choose1-duringMyTurn-isReact
+++++

.....
Fleet Officer
-----
ff4fb461-8060-457a-9c16-000000000134
-----

+++++

.....
Force Choke
-----
ff4fb461-8060-457a-9c16-000000000101
-----
onPlay:Deal1Damage-Targeted-atCharacter_or_Creature
+++++

.....
Force Choke
-----
ff4fb461-8060-457a-9c16-000000000106
-----
onPlay:Deal1Damage-Targeted-atCharacter_or_Creature
+++++

.....
Force Lightning
-----
ff4fb461-8060-457a-9c16-000000000100
-----
onPlay:DestroyTarget-Targeted-atUnit-hasMarker{Focus}
+++++

.....
Force Rejuvenation
-----
ff4fb461-8060-457a-9c16-000000000166
-----
onPlay:Remove999Focus$$Remove999Damage-Targeted-atCharacter-targetAllied
+++++

.....
Force Stasis
-----
ff4fb461-8060-457a-9c16-000000000026
-----
onPlay:Put1Force Stasis-Targeted-atCharacter_or_Creature
+++++

.....
Forgotten Heroes
-----
ff4fb461-8060-457a-9c16-000000000144
-----
whileInPlay:Draw1Card-foreachCardPlayed-byMe-typeForce User-isReact
+++++

.....
Grand Moff Tarkin
-----
ff4fb461-8060-457a-9c16-000000000029
-----

+++++

.....
Guardian of Peace
-----
ff4fb461-8060-457a-9c16-000000000158
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++
R0:Remove1Damage-DemiAutoTargeted-atCharacter-hasMarker{Damage}-choose1-isCost$$Put1Damage
.....
Guardian of Peace
-----
ff4fb461-8060-457a-9c16-000000000159
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++
R0:Remove1Damage-DemiAutoTargeted-atCharacter-hasMarker{Damage}-choose1-isCost$$Put1Damage
.....
Han Solo
-----
ff4fb461-8060-457a-9c16-000000000017
-----
onParticipation:Deal1Damage-DemiAutoTargeted-atUnit-targetOpponents-choose1-isReact||ConstantAbility:TargetStrike
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000011
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000039
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000090
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000107
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000148
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000213
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Heavy Blaster Emplacement
-----
ff4fb461-8060-457a-9c16-000000000014
-----

+++++
R0:Put1Focus-isCost$$SimplyAnnounce{force the Dark Side to deal 1 damage to a unit they control.}
.....
Heavy Stormtrooper Squad
-----
ff4fb461-8060-457a-9c16-000000000072
-----

+++++

.....
Heavy Stormtrooper Squad
-----
ff4fb461-8060-457a-9c16-000000000073
-----

+++++

.....
Heroic Sacrifice
-----
ff4fb461-8060-457a-9c16-000000000191
-----
onPlay:SacrificeTarget-Targeted-atVehicle-targetMine$$DestroyTarget-Targeted-atVehicle-hasProperty{Cost}le4-targetOpponents
+++++

.....
Hidden Outpost
-----
ff4fb461-8060-457a-9c16-000000000179
-----

+++++

.....
Hidden Outpost
-----
ff4fb461-8060-457a-9c16-000000000184
-----

+++++

.....
Hit and Run
-----
ff4fb461-8060-457a-9c16-000000000210
-----
whileInPlay:Deal1Damage-AutoTargeted-atObjective-isParticipating-foreachAttackerEdgeWin-ifOrigPlayerAttacker-onlyOnce-isReact
+++++

.....
Home One
-----
ff4fb461-8060-457a-9c16-000000000181
-----
onStrike:Deal1Damage-AutoTargeted-atObjective-isNotParticipating-targetOpponents-ifOrigAttacking-isReact
+++++

.....
Human Replica Droid
-----
ff4fb461-8060-457a-9c16-000000000088
-----
DeployAllowance:Conflict
+++++

.....
Human Replica Droid
-----
ff4fb461-8060-457a-9c16-000000000089
-----
DeployAllowance:Conflict
+++++

.....
I'm On the Leader
-----
ff4fb461-8060-457a-9c16-000000000130
-----
onPlay:Put1Focus-Targeted-atFighter
+++++

.....
Imperial Command
-----
ff4fb461-8060-457a-9c16-000000000069
-----

+++++

.....
Imperial Navy
-----
ff4fb461-8060-457a-9c16-000000000095
-----

+++++

.....
Imperial Officer
-----
ff4fb461-8060-457a-9c16-000000000036
-----

+++++
R2:Gain1Dial
.....
In You Must Go
-----
ff4fb461-8060-457a-9c16-000000000137
-----
whileInPlay:Reduce1CostPlay-affectsEnhancement-onlyOnce-forMe
+++++

.....
Interrogation
-----
ff4fb461-8060-457a-9c16-000000000121
-----
onPlay:SimplyAnnounce{look at opponent's hand and discard 1 card}
+++++

.....
Interrogation Droid
-----
ff4fb461-8060-457a-9c16-000000000122
-----
onPlay:Discard1Card-ofAllOpponents-isRandom-isReact
+++++

.....
Interrogation Droid
-----
ff4fb461-8060-457a-9c16-000000000123
-----
onPlay:Discard1Card-ofAllOpponents-isRandom-isReact
+++++

.....
Intimidated
-----
ff4fb461-8060-457a-9c16-000000000124
-----
Placement:Character_and_Unit-byOpponent||onHostStrike:Put1Focus-atHost-isReact-isForced
+++++

.....
ISB Interrogators
-----
ff4fb461-8060-457a-9c16-000000000125
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
It Binds All Things
-----
ff4fb461-8060-457a-9c16-000000000172
-----
onPlay:Draw1Card-fromDiscard-ifHaventForce$$Draw2Card-fromDiscard-ifHaveForce
+++++

.....
It Could Be Worse
-----
ff4fb461-8060-457a-9c16-000000000203
-----
onPlay:Remove1Damage-Targeted-atUnit_or_Objective
+++++

.....
It's Worse
-----
ff4fb461-8060-457a-9c16-000000000222
-----
onPlay:Deal1Damage-Targeted-atUnit
+++++

.....
Jedi
-----
ff4fb461-8060-457a-9c16-000000000143
-----

+++++

.....
Jedi in Hiding
-----
ff4fb461-8060-457a-9c16-000000000147
-----

+++++

.....
Jedi in Hiding
-----
ff4fb461-8060-457a-9c16-000000000168
-----

+++++

.....
Jedi Lightsaber
-----
ff4fb461-8060-457a-9c16-000000000066
-----
Placement:Force User_or_Force Sensitive||BonusIcons:UD:1, BD:1
+++++

.....
Jedi Mind Trick
-----
ff4fb461-8060-457a-9c16-000000000003
-----
onPlay:Put2Focus-Targeted-atCharacter_or_Creature-ifHaveForce$$Put1Focus-Targeted-atCharacter_or_Creature-ifHaventForce
+++++

.....
Jedi Mind Trick
-----
ff4fb461-8060-457a-9c16-000000000171
-----
onPlay:Put2Focus-Targeted-atCharacter_or_Creature-ifHaveForce$$Put1Focus-Targeted-atCharacter_or_Creature-ifHaventForce
+++++

.....
Jedi Training
-----
ff4fb461-8060-457a-9c16-000000000167
-----
whileInPlay:Force1Bonus
+++++

.....
Kuat Reinforcements
-----
ff4fb461-8060-457a-9c16-000000000046
-----

+++++
R0:Discard0Card-Targeted-fromHand$$Put1Resource:Neutral-AutoTargeted-isUnpaid-perX
.....
Kuati Security Team
-----
ff4fb461-8060-457a-9c16-000000000024
-----

+++++

.....
Kuati Security Team
-----
ff4fb461-8060-457a-9c16-000000000116
-----

+++++

.....
Last Minute Rescue
-----
ff4fb461-8060-457a-9c16-000000000161
-----
afterCardRefreshing:Remove1Damage-DemiAutoTargeted-atUnit-hasMarker{Damage}-choose1-targetAllied-noTargetingError-duringMyTurn-isReact
+++++

.....
Leia Organa
-----
ff4fb461-8060-457a-9c16-000000000001
-----
onLeaving:Remove999Focus-AutoTargeted-targetMine-hasMarker{Focus}-isReact$$Remove999Focus-AutoTargeted-targetMine-hasMarker{Focus}$$CaptureMyself
+++++

.....
Lightsaber Deflection
-----
ff4fb461-8060-457a-9c16-000000000157
-----
onPlay:Transfer1Damage-Targeted-atUnit-sourceUnit_and_nonVehicle-targetMine-hasMarker{Damage}-destinationUnit
+++++

.....
Log Trap
-----
ff4fb461-8060-457a-9c16-000000000207
-----

+++++
R0:Put1Focus-isCost$$SimplyAnnounce{force opponent to put 1 focus one 1 attacking unit}
.....
Looking for Droids
-----
ff4fb461-8060-457a-9c16-000000000217
-----
whileInPlay:IgnoreAffiliationMatch
+++++

.....
Luke Skywalker
-----
ff4fb461-8060-457a-9c16-000000000064
-----
atTurnStart:Remove1Focus-duringOpponentTurn-isReact||ConstantAbility:TargetStrike
+++++

.....
Mandalorian Armor
-----
ff4fb461-8060-457a-9c16-000000000078
-----
Placement:Character_and_Unit||ConstantAbility:TargetStrike-ifHostBoba Fett
+++++

.....
Mission Briefing
-----
ff4fb461-8060-457a-9c16-000000000010
-----
atTurnStart:Draw1Card-duringOpponentTurn-isReact
+++++

.....
Mobilize the Squadrons
-----
ff4fb461-8060-457a-9c16-000000000004
-----
afterCardRefreshing:Remove1Focus-AutoTargeted-atEnhancement_or_Objective-hasMarker{Focus}-targetMine-choose1-duringMyTurn-isReact
+++++

.....
Mon Mothma
-----
ff4fb461-8060-457a-9c16-000000000013
-----
ConstantEffect:Edge1Bonus
+++++

.....
Nightsister
-----
ff4fb461-8060-457a-9c16-000000000109
-----
onCommit:Deal1Damage-DemiAutoTargeted-atObjective-targetOpponents-choose1-isReact
+++++

.....
Nightsister
-----
ff4fb461-8060-457a-9c16-000000000110
-----
onCommit:Deal1Damage-DemiAutoTargeted-atObjective-targetOpponents-choose1-isReact
+++++

.....
Obi-Wan Kenobi
-----
ff4fb461-8060-457a-9c16-000000000145
-----

+++++

.....
Orbital Bombardment
-----
ff4fb461-8060-457a-9c16-000000000074
-----
whileInPlay:IncreaseBD:1-forMe-typeUnit
+++++

.....
Our Most Desperate Hour
-----
ff4fb461-8060-457a-9c16-000000000146
-----
onPlay:Put1Shield-Targeted-atCharacter
+++++

.....
Outer Rim Hunter
-----
ff4fb461-8060-457a-9c16-000000000077
-----
onAttack:SimplyAnnounce{force opponent to deal 1 damage to one of their objectives}-isReact
+++++

.....
Questionable Contacts
-----
ff4fb461-8060-457a-9c16-000000000016
-----
afterCardRefreshing:Put1Damage-duringMyTurn-isReact$$Remove1Damage-DemiAutoTargeted-atUnit-hasMarker{Damage}-targetAllied-choose1-isCost$$Deal1Damage-DemiAutoTargeted-atUnit-targetOpponents-choose1
+++++

.....
R2-D2
-----
ff4fb461-8060-457a-9c16-000000000151
-----

+++++

.....
Rancor
-----
ff4fb461-8060-457a-9c16-000000000111
-----
afterCardRefreshing:CustomScript-isReact-isForced-duringMyTurn
+++++

.....
Rebel Alliance
-----
ff4fb461-8060-457a-9c16-000000000173
-----

+++++

.....
Rebel Assault
-----
ff4fb461-8060-457a-9c16-000000000005
-----
onPlay:Deal2Damage-Targeted-atUnit_or_Objective
+++++

.....
Rebel Assault
-----
ff4fb461-8060-457a-9c16-000000000178
-----
onPlay:Deal2Damage-Targeted-atUnit_or_Objective
+++++

.....
Rebel Sympathizer
-----
ff4fb461-8060-457a-9c16-000000000199
-----
whileInPlay:IgnoreAffiliationMatch-onlyforDummy||Reduce1CostPlay-affectsAll-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-onlyforDummy-isSilent
+++++
R0:DestroyMyself-isSilent$$SimplyAnnounce{reduce the cost of the next card they play this phase by 1 and ignore its resource match requirement}$$CreateDummy-isSilent-nonUnique
.....
Rebel Sympathizer
-----
ff4fb461-8060-457a-9c16-000000000200
-----
whileInPlay:IgnoreAffiliationMatch-onlyforDummy||Reduce1CostPlay-affectsAll-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-onlyforDummy-isSilent
+++++
R0:DestroyMyself-isSilent$$SimplyAnnounce{reduce the cost of the next card they play this phase by 1 and ignore its resource match requirement}$$CreateDummy-isSilent-nonUnique
.....
Rebel Trooper
-----
ff4fb461-8060-457a-9c16-000000000194
-----

+++++

.....
Reconnaissance Mission
-----
ff4fb461-8060-457a-9c16-000000000087
-----
onPlay:Gain1Reserves||onThwart:Lose1Reserves
+++++

.....
Red Five
-----
ff4fb461-8060-457a-9c16-000000000150
-----

+++++

.....
Red Two
-----
ff4fb461-8060-457a-9c16-000000000177
-----
whileInPlay:Remove1Focus-foreachObjectiveThwarted-isReact
+++++

.....
Redemption
-----
ff4fb461-8060-457a-9c16-000000000162
-----

+++++
R0:ReturnTarget-Targeted-atUnit-onlyOnce
.....
Repair Droid
-----
ff4fb461-8060-457a-9c16-000000000183
-----

+++++
R0:Remove1Damage-DemiAutoTargeted-atVehicle-targetAllied-choose1-onlyOnce
.....
Rescue Mission
-----
ff4fb461-8060-457a-9c16-000000000202
-----
onPlay:CustomScript
+++++

.....
Return of the Jedi
-----
ff4fb461-8060-457a-9c16-000000000164
-----
onPlay:CustomScript
+++++

.....
Rookie Pilot
-----
ff4fb461-8060-457a-9c16-000000000006
-----

+++++

.....
Rumors at the Cantina
-----
ff4fb461-8060-457a-9c16-000000000198
-----
whileInPlay:IgnoreAffiliationMatch
+++++

.....
Scum and Villainy
-----
ff4fb461-8060-457a-9c16-000000000093
-----

+++++

.....
Secret Informant
-----
ff4fb461-8060-457a-9c16-000000000211
-----

+++++
R0:CustomScript
.....
Secret Informant
-----
ff4fb461-8060-457a-9c16-000000000212
-----

+++++
R0:CustomScript
.....
Shadows of Dathomir
-----
ff4fb461-8060-457a-9c16-000000000108
-----

+++++

.....
Shii-Cho-Training
-----
ff4fb461-8060-457a-9c16-000000000140
-----
Placement:Force User_and_Unit||ConstantAbility:ShiiCho
+++++

.....
Sith
-----
ff4fb461-8060-457a-9c16-000000000094
-----

+++++

.....
Sith Library
-----
ff4fb461-8060-457a-9c16-000000000025
-----

+++++

.....
Sith Library
-----
ff4fb461-8060-457a-9c16-000000000099
-----

+++++

.....
Sith Library
-----
ff4fb461-8060-457a-9c16-000000000117
-----

+++++

.....
Smugglers and Spies
-----
ff4fb461-8060-457a-9c16-000000000216
-----

+++++

.....
Stolen Plans
-----
ff4fb461-8060-457a-9c16-000000000133
-----
Placement:Objective-targetOpponents||onHostGenerate:Draw1Card-isReact
+++++

.....
Stormtrooper Elite
-----
ff4fb461-8060-457a-9c16-000000000031
-----

+++++

.....
Superlaser Blast
-----
ff4fb461-8060-457a-9c16-000000000033
-----
onPlay:DestroyTarget-Targeted-atObjective
+++++

.....
Superlaser Engineer
-----
ff4fb461-8060-457a-9c16-000000000030
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough||onPlay:CustomScript-isReact
+++++

.....
Swindled
-----
ff4fb461-8060-457a-9c16-000000000020
-----
onPlay:ReturnTarget-Targeted-atUnit-hasProperty{Cost}le2
+++++

.....
Take Them Prisoner
-----
ff4fb461-8060-457a-9c16-000000000052
-----
onPlay:CustomScript-isReact
+++++

.....
Tallon Roll
-----
ff4fb461-8060-457a-9c16-000000000043
-----
onPlay:Remove1Focus-Targeted-atFighter
+++++

.....
Tallon Roll
-----
ff4fb461-8060-457a-9c16-000000000051
-----
onPlay:Remove1Focus-Targeted-atFighter
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000062
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000091
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000131
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000154
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000185
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000215
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Tear This Ship Apart
-----
ff4fb461-8060-457a-9c16-000000000057
-----
onPlay:DestroyTarget-Targeted-atEnhancement
+++++

.....
The Bespin Exchange
-----
ff4fb461-8060-457a-9c16-000000000075
-----
whileInPlay:Remove1Focus-AutoTargeted-atObjective-hasMarker{Focus}-choose1-foreachUnitCardCapturedFromTable-isReact
+++++

.....
The Defense of Yavin 4
-----
ff4fb461-8060-457a-9c16-000000000174
-----

+++++
R0:Discard0Card-Targeted-fromHand$$Put1Resource:Neutral-AutoTargeted-isUnpaid-perX
.....
The Emperor's Web
-----
ff4fb461-8060-457a-9c16-000000000096
-----
whileInPlay:Reduce1CostPlay-affectsEvent_and_Sith-onlyOnce
+++++

.....
The Endor Gambit
-----
ff4fb461-8060-457a-9c16-000000000058
-----
afterCardRefreshing:Remove1Focus-AutoTargeted-atVehicle-hasMarker{Focus}-choose1-duringMyTurn-targetAllied-isReact
+++++

.....
The Hand's Blessing
-----
ff4fb461-8060-457a-9c16-000000000112
-----
Placement:Character_and_Unit||afterCardRefreshing:Remove999Focus-AutoTargeted-onHost-duringMyTurn-isReact
+++++

.....
The Heart of the Empire
-----
ff4fb461-8060-457a-9c16-000000000022
-----
onThwart:LoseGame-forOwner
+++++

.....
The Rebel Fleet
-----
ff4fb461-8060-457a-9c16-000000000180
-----

+++++

.....
The Secret of Yavin 4
-----
ff4fb461-8060-457a-9c16-000000000155
-----

+++++
R0:CustomScript-isReact-onlyOnce
.....
The Ultimate Power
-----
ff4fb461-8060-457a-9c16-000000000028
-----

+++++

.....
There Is No Escape
-----
ff4fb461-8060-457a-9c16-000000000027
-----
onPlay:SendToBottomMulti-AutoTargeted-atUnit-warnLotsofStuff
+++++

.....
TIE Advanced
-----
ff4fb461-8060-457a-9c16-000000000128
-----
whileInPlay:Deal1Damage-foreachUnopposedEngagement-onTriggerCard-ifOrigAttacking-ifOrigParticipating-isReact
+++++

.....
TIE Attack Squadron
-----
ff4fb461-8060-457a-9c16-000000000041
-----
whileInPlay:Put1TIE Attack Squadron:UD-foreachResolveFate-byMe-onlyOnce-ifOrigParticipating||afterEngagement:Remove999TIE Attack Squadron:UD-isSilent$$Remove999Activation-isSilent
+++++

.....
TIE Bomber
-----
ff4fb461-8060-457a-9c16-000000000047
-----

+++++

.....
TIE Fighter
-----
ff4fb461-8060-457a-9c16-000000000042
-----

+++++

.....
TIE Fighter
-----
ff4fb461-8060-457a-9c16-000000000048
-----

+++++

.....
Trench Run
-----
ff4fb461-8060-457a-9c16-000000000009
-----
EngagedAsObjective||onPlay:CustomScript
+++++

.....
Tribal Support
-----
ff4fb461-8060-457a-9c16-000000000204
-----
afterCardRefreshing:Discard1Card-Targeted-fromHand-duringMyTurn-isCost-isReact$$Retrieve1Card-fromDiscard-grabEwok
+++++

.....
Trooper Assault
-----
ff4fb461-8060-457a-9c16-000000000056
-----
onPlay:CreateDummy-nonUnique||whileInPlay:IncreaseBD:1-forMe-typeTrooper-isAttacking-onlyforDummy||whileInPlay:IncreaseUD:1-forMe-typeTrooper-isAttacking-onlyforDummy||afterEngagement:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Trust Your Feelings
-----
ff4fb461-8060-457a-9c16-000000000065
-----
Placement:Character_and_Unit
+++++
R0:Put1Focus-isCost$$Remove1Focus-AutoTargeted-onHost
.....
Twi'lek Loyalist
-----
ff4fb461-8060-457a-9c16-000000000067
-----

+++++

.....
Twi'lek Loyalist
-----
ff4fb461-8060-457a-9c16-000000000152
-----

+++++

.....
Twi'lek Smuggler
-----
ff4fb461-8060-457a-9c16-000000000018
-----

+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000045
-----
onResolveFate:CustomScript
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000092
-----
onResolveFate:CustomScript
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000119
-----
onResolveFate:CustomScript
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000136
-----
onResolveFate:CustomScript
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000160
-----
onResolveFate:CustomScript
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000214
-----
onResolveFate:CustomScript
+++++

.....
Vader's Lightsaber
-----
ff4fb461-8060-457a-9c16-000000000105
-----
Placement:Force User_or_Force Sensitive|||BonusIcons:UD:1||ConstantAbility:TargetStrike-ifHostDarth Vader
+++++

.....
Vader's TIE Advanced
-----
ff4fb461-8060-457a-9c16-000000000127
-----
onStrike:CustomScript-isReact
+++++

.....
Viper Probe Droid
-----
ff4fb461-8060-457a-9c16-000000000218
-----

+++++

.....
Viper Probe Droid
-----
ff4fb461-8060-457a-9c16-000000000219
-----

+++++

.....
Wookiee Navigator
-----
ff4fb461-8060-457a-9c16-000000000193
-----
whileInPlay:AttackTarget-ifOrigAttacking-ifOrigParticipating-foreachFinishedEngagement-onTriggerCard-isReact
+++++

.....
X-Wing
-----
ff4fb461-8060-457a-9c16-000000000008
-----

+++++

.....
X-Wing
-----
ff4fb461-8060-457a-9c16-000000000189
-----

+++++

.....
X-Wing Escort
-----
ff4fb461-8060-457a-9c16-000000000188
-----
onLeaving:SimplyAnnounce{force opponent to sacrifice a Vehicle unit they control}-isReact
+++++

.....
Y-Wing
-----
ff4fb461-8060-457a-9c16-000000000176
-----

+++++

.....
Y-Wing
-----
ff4fb461-8060-457a-9c16-000000000182
-----

+++++

.....
Yoda
-----
ff4fb461-8060-457a-9c16-000000000138
-----
onStrike:CustomScript
+++++

.....
You're My Only Hope
-----
ff4fb461-8060-457a-9c16-000000000135
-----
onPlay:DestroyTarget-Targeted-atUnit$$Draw2Cards
+++++

.....
Yub Yub!
-----
ff4fb461-8060-457a-9c16-000000000208
-----
onPlay:Put1Focus-Targeted-onEwok-hasntMarker{Focus}$$DestroyTarget-Targeted-atEnhancement
+++++

.....
Yub Yub!
-----
ff4fb461-8060-457a-9c16-000000000209
-----
onPlay:Put1Focus-Targeted-onEwok-hasntMarker{Focus}$$DestroyTarget-Targeted-atEnhancement
+++++

.....
A Message from Beyond
-----
ff4fb461-8060-457a-9c16-000000000223
-----
afterCardRefreshing:Put1Damage$$Retrieve1Card-grabEnhancement-fromDiscard-isTopmost-duringMyTurn-isReact
+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000258
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

.....
Calm
-----
ff4fb461-8060-457a-9c16-000000000227
-----
onPlay:Remove999Focus-Targeted-atCharacter
+++++

.....
Communications Officer
-----
ff4fb461-8060-457a-9c16-000000000249
-----

+++++

.....
Darth Vader
-----
ff4fb461-8060-457a-9c16-000000000248
-----
whileInPlay:IncreaseBD:1-forAlly-typeUnit-isAttacking-ifOrigParticipating
+++++

.....
Echo Base Defense
-----
ff4fb461-8060-457a-9c16-000000000229
-----

+++++

.....
Fear
-----
ff4fb461-8060-457a-9c16-000000000244
-----
Placement:Character_and_Unit||onPlay:UncommitTarget-Targeted-atCharacter
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000228
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Hoth Operations
-----
ff4fb461-8060-457a-9c16-000000000235
-----
ConstantEffect:Edge1Bonus-perEverySpeeder-AutoTargeted-atSpeeder-targetMine-isParticipating-isDistributedEffect-ifSuperiorityHoth
+++++

.....
Hoth Survival Gear
-----
ff4fb461-8060-457a-9c16-000000000239
-----
Placement:Character_and_Unit
+++++

.....
Icetromper
-----
ff4fb461-8060-457a-9c16-000000000242
-----

+++++
R0:SacrificeMyself$$DisengageTarget-Targeted-atUnit_and_nonVehicle$$Deal1Damage-Targeted-atUnit_and_nonVehicle
.....
Icetromper
-----
ff4fb461-8060-457a-9c16-000000000243
-----

+++++
R0:SacrificeMyself$$DisengageTarget-Targeted-atUnit_and_nonVehicle$$Deal1Damage-Targeted-atUnit_and_nonVehicle
.....
Imperial Suppression
-----
ff4fb461-8060-457a-9c16-000000000252
-----
onPlay:SimplyAnnounce{cancel the effects of the event card and return it to the top of its owners command deck}$$Put1Effects Cancelled-Targeted-atEvent-isReady-isSilent$$Put1Destination:Command Deck-Targeted-atEvent-isReady-isSilent
+++++

.....
Lord Vader's Command
-----
ff4fb461-8060-457a-9c16-000000000247
-----
whileInPlay:Increase1CostPlay-affectsEvent-byOpponent-ifOrigHasntMarker{Damage}
+++++

.....
Old Ben's Spirit
-----
ff4fb461-8060-457a-9c16-000000000224
-----
Placement:Character_and_Unit
+++++
R0:Remove999Damage-AutoTargeted-onHost-isReact$$DestroyMyself
.....
Old Ben's Spirit
-----
ff4fb461-8060-457a-9c16-000000000225
-----
Placement:Character_and_Unit
+++++
R0:Remove999Damage-AutoTargeted-onHost$$DestroyMyself
.....
Probe Droid
-----
ff4fb461-8060-457a-9c16-000000000250
-----
onLeaving:Deal1Damage-DemiAutoTargeted-atObjective-choose1-targetOpponents-isReact
+++++

.....
Probe Droid
-----
ff4fb461-8060-457a-9c16-000000000251
-----
onLeaving:Deal1Damage-DemiAutoTargeted-atObjective-choose1-targetOpponents-isReact
+++++

.....
Rogue Three
-----
ff4fb461-8060-457a-9c16-000000000237
-----
onStrike:CustomScript
+++++

.....
Shadows on the Ice
-----
ff4fb461-8060-457a-9c16-000000000253
-----

+++++

.....
Snowspeeder
-----
ff4fb461-8060-457a-9c16-000000000238
-----

+++++

.....
Subzero Defenses
-----
ff4fb461-8060-457a-9c16-000000000233
-----

+++++
R0:DestroyTarget-Targeted-atUnit
.....
Subzero Defenses
-----
ff4fb461-8060-457a-9c16-000000000234
-----

+++++
R0:DestroyTarget-Targeted-atUnit
.....
Succumb to the Cold!
-----
ff4fb461-8060-457a-9c16-000000000256
-----
onPlay:Put1Focus-Targeted-atUnit-targetOpponents
+++++

.....
Succumb to the Cold!
-----
ff4fb461-8060-457a-9c16-000000000257
-----
onPlay:Put1Focus-Targeted-atUnit-targetOpponents
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000240
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
The Desolation of Hoth
-----
ff4fb461-8060-457a-9c16-000000000245
-----
onPlay:RequestInt-Msg{How many damage do you want to move to the enemy unit or objective?}$$Remove1Damage-perX-Targeted-atObjective_and_Hoth-targetMine-isCost$$Put1Damage-perX-Targeted-atObjective_and_Hoth_or_Unit-targetOpponents
+++++

.....
The Killing Cold
-----
ff4fb461-8060-457a-9c16-000000000241
-----

+++++
R0:SacrificeTarget-Targeted-atUnit$$Remove1Damage-Targeted-atObjective_and_Hoth-targetMine
.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000246
-----
onResolveFate:CustomScript
+++++

.....
Wampa
-----
ff4fb461-8060-457a-9c16-000000000254
-----
onPay:Reduce2CostPlay-perEveryHoth-AutoTargeted-atObjective_and_Hoth
+++++

.....
Wampa
-----
ff4fb461-8060-457a-9c16-000000000255
-----
onPay:Reduce2CostPlay-perEveryHoth-AutoTargeted-atObjective_and_Hoth
+++++

.....
Weapon Mastery
-----
ff4fb461-8060-457a-9c16-000000000226
-----
onPlay:RequestInt-Msg{How many enhancements does the target unit have?}$$Put1Weapon Mastery:UD-perX-Targeted-atCharacter$$CreateDummy-nonUnique-isSilent||afterConflict:Remove999Weapon Mastery:UD-AutoTargeted-hasMarker{Weapon Mastery:UD}-isSilent-onlyforDummy$$DestroyMyself-onlyforDummy-isSilent
+++++

.....
Wedge Antilles
-----
ff4fb461-8060-457a-9c16-000000000236
-----
onPlay:CustomScript
+++++
R0:Put1Focus-isCost$$Remove1Focus-AutoTargeted-onHost
.....
Wilderness Fighters
-----
ff4fb461-8060-457a-9c16-000000000230
-----
ExtraIcon:UD:1-perEveryHoth-AutoTargeted-atObjective_and_Hoth-targetMine
+++++

.....
Wilderness Fighters
-----
ff4fb461-8060-457a-9c16-000000000231
-----
ExtraIcon:UD:1-perEveryHoth-AutoTargeted-atObjective_and_Hoth-targetMine
+++++

.....
Wilderness Fighters
-----
ff4fb461-8060-457a-9c16-000000000232
-----
ExtraIcon:UD:1-perEveryHoth-AutoTargeted-atObjective_and_Hoth-targetMine
+++++

.....
AAC-1 Speeder Tank
-----
ff4fb461-8060-457a-9c16-000000000279
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
AAC-1 Speeder Tank
-----
ff4fb461-8060-457a-9c16-000000000280
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Admiral's Orders
-----
ff4fb461-8060-457a-9c16-000000000288
-----
onPlay:SimplyAnnounce{reduce the cost of the next capital ship they play this phase by 2}$$CreateDummy-nonUnique-isSilent||whileInPlay:Reduce2CostPlay-affectsCapital Ship-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeCapital Ship-onlyforDummy-isSilent
+++++

.....
Death Squadron Command
-----
ff4fb461-8060-457a-9c16-000000000287
-----
whileInPlay:Remove1Focus-foreachObjectiveThwarted-isReact
+++++

.....
Death Squadron Star Destroyer
-----
ff4fb461-8060-457a-9c16-000000000284
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Death Squadron Star Destroyer
-----
ff4fb461-8060-457a-9c16-000000000285
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Deploy the Fleet
-----
ff4fb461-8060-457a-9c16-000000000283
-----
whileInPlay:Reduce1CostPlay-affectsCapital Ship-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeCapital Ship-onlyforDummy-isSilent
+++++
R0:SimplyAnnounce{damage it in order to reduce the cost of the next capital ship they play this phase by 1}$$CreateDummy-nonUnique-isSilent-doNotDiscard$$Deal1Damage-isSilent
.....
Echo Base
-----
ff4fb461-8060-457a-9c16-000000000262
-----
ConstantEffect:Trait{Objective_and_Hoth}1Bonus
+++++

.....
Echo Base Shield Generator
-----
ff4fb461-8060-457a-9c16-000000000263
-----

+++++
R0:Put1Damage-onlyOnce$$Put1Shield-Targeted-atUnit_or_Objective_and_Hoth$$ReturnMyself-ifMarkers{Damage}eq3$$Remove999Damage-ifMarkers{Damage}eq3
.....
Echo Caverns
-----
ff4fb461-8060-457a-9c16-000000000269
-----

+++++
R0:CustomScript
.....
Echo Defender
-----
ff4fb461-8060-457a-9c16-000000000260
-----
ExtraIcon:EE-UD:1-perEveryHoth-AutoTargeted-atObjective_and_Hoth-targetMine
+++++

.....
Echo Defender
-----
ff4fb461-8060-457a-9c16-000000000261
-----
ExtraIcon:EE-UD:1-perEveryHoth-AutoTargeted-atObjective_and_Hoth-targetMine
+++++

.....
First Marker
-----
ff4fb461-8060-457a-9c16-000000000264
-----
Placement:Objective_and_Hoth||ConstantEffect:Protection-typeVehicle-onHost
+++++

.....
Fleet Navigator
-----
ff4fb461-8060-457a-9c16-000000000286
-----

+++++

.....
Get Me Solo!
-----
ff4fb461-8060-457a-9c16-000000000276
-----
onPlay:CaptureTarget-Targeted-atUnit-fromHand
+++++

.....
Hoth Scout
-----
ff4fb461-8060-457a-9c16-000000000278
-----

+++++
R0:SacrificeMyself$$Put1Shield-Targeted-atUnit_or_Objective
.....
Jabba's Orders
-----
ff4fb461-8060-457a-9c16-000000000271
-----
onPlay:SimplyAnnounce{look at opponent's hand}-isReact
+++++

.....
Jabba's Palace
-----
ff4fb461-8060-457a-9c16-000000000275
-----

+++++

.....
Jawa Trading Crawler
-----
ff4fb461-8060-457a-9c16-000000000274
-----

+++++

.....
Munitions Expert
-----
ff4fb461-8060-457a-9c16-000000000268
-----

+++++
R0:Put1Focus$$Put1Munitions Expert:UD-Targeted-atUnit
.....
Preparation for Battle
-----
ff4fb461-8060-457a-9c16-000000000277
-----
whileInPlay:IncreaseBD:1-forMe-typeUnit-hasMarker{Shield}-ifDialge8
+++++

.....
Renegade Squadron
-----
ff4fb461-8060-457a-9c16-000000000266
-----
onStrike:Put1Damage-isReact$$RescueTarget-Targeted-isCaptured
+++++

.....
Renegade Squadron Mobilization
-----
ff4fb461-8060-457a-9c16-000000000265
-----
whileInPlay:Draw1Card-foreachCardLeavingPlay-typeUnit-byOpposingOriginController-isReact
+++++

.....
Renegade Squadron Operative
-----
ff4fb461-8060-457a-9c16-000000000267
-----

+++++

.....
Sensors Are Placed
-----
ff4fb461-8060-457a-9c16-000000000259
-----

+++++

.....
Shelter from the Storm
-----
ff4fb461-8060-457a-9c16-000000000282
-----
onPlay:Put1Shield-Targeted-atCharacter-targetMine$$Put1Shelter from the Storm:Protection-Targeted-atCharacter-targetMine
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000270
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Tauntaun
-----
ff4fb461-8060-457a-9c16-000000000281
-----

+++++

.....
Weequay Elite
-----
ff4fb461-8060-457a-9c16-000000000272
-----
onPay:Reduce2CostPlay-perEveryCard-AutoTargeted-isCaptured-maxReduce2
+++++

.....
Weequay Elite
-----
ff4fb461-8060-457a-9c16-000000000273
-----
onPay:Reduce2CostPlay-perEveryCard-AutoTargeted-isCaptured-maxReduce2
+++++

.....
A Dark Time for the Rebellion
-----
ff4fb461-8060-457a-9c16-000000000307
-----
afterCardRefreshing:SimplyAnnounce{force each opponent to deal 1 damage to a unit or objective they control}-duringMyTurn-isReact
+++++

.....
Action-series Bulk Transport
-----
ff4fb461-8060-457a-9c16-000000000298
-----
onStrike:Retrieve1Card-grabCharacter-hasProperty{Cost}le2-toTable-onTop5Cards-isReact$$ShuffleDeck
+++++

.....
Anger
-----
ff4fb461-8060-457a-9c16-000000000305
-----
Placement:Character||whileInPlay:SacrificeTarget-AutoTargeted-onHost-foreachForceStruggleDark-duringOpponentTurn-isReact-isForced
+++++

.....
Anzati Elite
-----
ff4fb461-8060-457a-9c16-000000000304
-----

+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000300
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

.....
Carbonite Chamber Activation
-----
ff4fb461-8060-457a-9c16-000000000318
-----
onPlay:Put1Focus-Targeted-atUnit_and_nonVehicle
+++++

.....
Cloud City Incinerator
-----
ff4fb461-8060-457a-9c16-000000000317
-----
whileInPlay:DestroyTarget-Targeted-isCaptured-onlyOnce-foreachCardCaptured-ifHaveForce-isReact
+++++

.....
Colonel Starck
-----
ff4fb461-8060-457a-9c16-000000000308
-----
ExtraIcon:UD:2-ifOrigAttacking-isDamagedObjective||ExtraIcon:BD:2-ifOrigAttacking-isDamagedObjective
+++++

.....
Force Push
-----
ff4fb461-8060-457a-9c16-000000000306
-----
onPlay:Put2Focus-Targeted-atUnit_and_nonUnique
+++++

.....
Gotal Outcast
-----
ff4fb461-8060-457a-9c16-000000000290
-----
ExtraIcon:BD:2-ifHaveForce
+++++

.....
Gotal Outcast
-----
ff4fb461-8060-457a-9c16-000000000291
-----
ExtraIcon:BD:2-ifHaveForce
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000294
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Heavy Fire
-----
ff4fb461-8060-457a-9c16-000000000312
-----
onPlay:Put1Heavy Fire:UD-Targeted-atUnit||onPlay:Put1Heavy Fire:BD-Targeted-atUnit
+++++

.....
Ion Cannon Burst
-----
ff4fb461-8060-457a-9c16-000000000299
-----
onPlay:Put1Ion Damaged-Targeted-atUnit_and_Vehicle_or_Unit_and_Droid
+++++

.....
MTV-7
-----
ff4fb461-8060-457a-9c16-000000000309
-----
ExtraIcon:BD:1-ifOrigAttacking-isDamagedObjective
+++++

.....
MTV-7
-----
ff4fb461-8060-457a-9c16-000000000310
-----
ExtraIcon:BD:1-ifOrigAttacking-isDamagedObjective
+++++

.....
Prepare for Evacuation
-----
ff4fb461-8060-457a-9c16-000000000295
-----
whileInPlay:ReturnTarget-Targeted-atUnit-foreachObjectiveThwarted-typeHoth-isReact
+++++

.....
Prophet of the Dark Side
-----
ff4fb461-8060-457a-9c16-000000000302
-----
onPlay:CustomScript-isReact
+++++

.....
Prophet of the Dark Side
-----
ff4fb461-8060-457a-9c16-000000000303
-----
onPlay:CustomScript-isReact
+++++

.....
Renegade Squadron Escort
-----
ff4fb461-8060-457a-9c16-000000000296
-----

+++++
R0:Remove1Damage-DemiAutoTargeted-atVehicle-hasMarker{Damage}-choose1-isCost$$Put1Damage
.....
Renegade Squadron Escort
-----
ff4fb461-8060-457a-9c16-000000000297
-----

+++++
R0:Remove1Damage-DemiAutoTargeted-atVehicle-hasMarker{Damage}-choose1-isCost$$Put1Damage
.....
Self Preservation
-----
ff4fb461-8060-457a-9c16-000000000289
-----
ConstantEffect:Force1Bonus-AutoTargeted-atUnit-hasntMarker{Focus}-isCommited-targetMine-perEveryUnit
+++++

.....
Serve the Emperor
-----
ff4fb461-8060-457a-9c16-000000000301
-----
ConstantEffect:Force1Bonus
+++++

.....
Soresu Training
-----
ff4fb461-8060-457a-9c16-000000000292
-----
Placement:Force User_and_Unit||onHostParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
The Hunt for Han Solo
-----
ff4fb461-8060-457a-9c16-000000000313
-----
whileInPlay:Remove1Focus-DemiAutoTargeted-atScum and Villainy-choose1-hasMarker{Focus}-foreachUnitCardCaptured-ifCapturingObjective-isReact
+++++

.....
The Moorsh Moraine
-----
ff4fb461-8060-457a-9c16-000000000311
-----
ConstantEffect:Unopposed2Raise-forMe
+++++

.....
Ugnaught
-----
ff4fb461-8060-457a-9c16-000000000314
-----
whileInPlay:Remove1Damage-DemiAutoTargeted-atUnit_and_Vehicle_or_Unit_and_Droid-targetMine-choose1-hasMarker{Damage}-foreachCardCaptured-isReact
+++++

.....
Unwavering Resolve
-----
ff4fb461-8060-457a-9c16-000000000293
-----
onPlay:Put1Unwavering Resolve-Targeted-atUnit-targetMine
+++++

.....
Z-95 Headhunter
-----
ff4fb461-8060-457a-9c16-000000000315
-----
onStrike:CustomScript-isReact
+++++

.....
Z-95 Headhunter
-----
ff4fb461-8060-457a-9c16-000000000316
-----
onStrike:CustomScript-isReact
+++++

.....
A Stinging Insult
-----
ff4fb461-8060-457a-9c16-000000000329
-----
onPlay:EngageTarget-Targeted-atUnit-targetOpponents-hasntMarker{Focus}
+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000336
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000342
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000354
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

.....
Blizzard Force AT-ST
-----
ff4fb461-8060-457a-9c16-000000000339
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Blizzard Force AT-ST
-----
ff4fb461-8060-457a-9c16-000000000340
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Col Serra
-----
ff4fb461-8060-457a-9c16-000000000326
-----
ConstantEffect:Edge1Bonus||ConstantEffect:Protection-ifhasEdge
+++++

.....
Daughters of Allya
-----
ff4fb461-8060-457a-9c16-000000000320
-----
onCommit:Remove1Damage-AutoTargeted-atObjective-hasMarker{Damage}-targetMine-isReact
+++++

.....
Daughters of Allya
-----
ff4fb461-8060-457a-9c16-000000000321
-----
onCommit:Remove1Damage-AutoTargeted-atObjective-hasMarker{Damage}-targetMine-isReact
+++++

.....
Don't Get Cocky
-----
ff4fb461-8060-457a-9c16-000000000330
-----
onPlay:Put2Cocky:BD-Targeted-atUnit-isParticipating
+++++

.....
Explosive Charge
-----
ff4fb461-8060-457a-9c16-000000000347
-----
onPlay:DestroyTarget-Targeted-atEnhancement
+++++

.....
Forward Command Post
-----
ff4fb461-8060-457a-9c16-000000000352
-----
whileInPlay:IncreaseBD:1-forAlly-typeUnit-hasMarker{Shield}
+++++

.....
Forward Command Post
-----
ff4fb461-8060-457a-9c16-000000000353
-----
whileInPlay:IncreaseBD:1-forAlly-typeUnit-hasMarker{Shield}
+++++

.....
FX-7 Medical Assistant
-----
ff4fb461-8060-457a-9c16-000000000333
-----
onStrike:Remove1AnyTokenType-AutoTargeted-atEnhancement_or_Character-hasMarker{AnyTokenType}-choose1-isReact
+++++

.....
General Veers
-----
ff4fb461-8060-457a-9c16-000000000338
-----
whileInPlay:IncreaseUD:1-forMe-typeWalker_or_Trooper
+++++

.....
Knowledge and Defense
-----
ff4fb461-8060-457a-9c16-000000000319
-----

+++++
R0:ReturnTarget-Targeted-atUnit-byAlly
.....
Last Defense of Hoth
-----
ff4fb461-8060-457a-9c16-000000000325
-----
afterEngagement:Remove999Activation-isSilent
+++++
R0:CustomScript
.....
Lucrative Contract
-----
ff4fb461-8060-457a-9c16-000000000343
-----
afterCardRefreshing:Remove1Focus-AutoTargeted-atUnit_and_Mercenary_or_Unit_and_Bounty Hunter-targetAllied-choose1-hasMarker{Focus}-duringMyTurn-isReact
+++++

.....
Outer Rim Space Pirates
-----
ff4fb461-8060-457a-9c16-000000000344
-----
+++++

.....
Corrupt Official
-----
ff4fb461-8060-457a-9c16-000000000345
-----
+++++

.....
Corrupt Official
-----
ff4fb461-8060-457a-9c16-000000000346
-----
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000000324
-----
onResolveFate:Put1Shield-Targeted-atUnit_or_Objective
+++++

.....
Renegade Squadron X-Wing
-----
ff4fb461-8060-457a-9c16-000000000327
-----

+++++
R0:SacrificeMyself$$ReturnTarget-Targeted-atUnit-hasProperty{Cost}le2
.....
Sabotage in the Snow
-----
ff4fb461-8060-457a-9c16-000000000349
-----
afterDeployment:Transfer1Shield-Targeted-sourceAny-hasMarker{Shield}-targetOpponents-destinationAny-hasntMarker{Shield}-targetAllied-duringMyTurn-isReact
+++++

.....
Snowtrooper Vanguard
-----
ff4fb461-8060-457a-9c16-000000000351
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
The General's Imperative
-----
ff4fb461-8060-457a-9c16-000000000337
-----
onPlay:Gain1Reserves||onDamage:Lose1Reserves||onHeal:Gain1Reserves||onThwart:Lose1Reserves-ifOrigHasntMarker{Damage}
+++++

.....
Turbolaser Battery
-----
ff4fb461-8060-457a-9c16-000000000341
-----
whileInPlay:SacrificeMyself-foreachObjectiveThwarted-byMe-isReact$$DestroyMulti-AutoTargeted-atEnhancement
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000348
-----
onResolveFate:CustomScript-isReact
+++++

.....
WED-15-1016
-----
ff4fb461-8060-457a-9c16-000000000332
-----
afterCardRefreshing:Remove1AnyTokenType-AutoTargeted-atObjective_and_Hoth-hasMarker{AnyTokenType}-choose1-duringMyTurn
+++++

.....
Yoda's Protection
-----
ff4fb461-8060-457a-9c16-000000000322
-----
Placement:Objective||whileInPlay:Put1Shield-AutoTargeted-onHost-hasntMarker{Shield}-foreachEngagedObjective-ifOrigCurrentObjectiveHost-isReact
+++++

.....
Confronting The Terror
-----
ff4fb461-8060-457a-9c16-000000000323
-----
onPlay:SimplyAnnounce{force their opponent to instead divide the damage among any number of units and objectives they control}
+++++

.....
Chewbacca
-----
ff4fb461-8060-457a-9c16-000000000356
-----
onDamage:SimplyAnnounce{deals twice that much damage to a target participating enemy unit}-onlyDuringEngagement-isReact
+++++

.....
Wookiee Warrior
-----
ff4fb461-8060-457a-9c16-000000000357
-----
ExtraIcon:BD:1-ifOrigHasMarker{Damage}||ExtraIcon:UD:1-ifOrigHasMarker{Damage}
+++++

.....
Wookiee Warrior
-----
ff4fb461-8060-457a-9c16-000000000358
-----
ExtraIcon:BD:1-ifOrigHasMarker{Damage}||ExtraIcon:UD:1-ifOrigHasMarker{Damage}
+++++

.....
Let the Wookiee Win
-----
ff4fb461-8060-457a-9c16-000000000359
-----
onPlay:Deal1Damage-DemiAutoTargeted-atUnit-targetMine-choose1$$Deal1Damage-DemiAutoTargeted-atUnit_and_nonVehicle-choose1
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000360
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Raise the Stakes
-----
ff4fb461-8060-457a-9c16-000000000361
-----
ConstantEffect:Unopposed2Raise-forMe-ifOrigHasntMarker{Damage}
+++++

.....
Blockade Runner
-----
ff4fb461-8060-457a-9c16-000000000362
-----

+++++

.....
Cloud City Operative
-----
ff4fb461-8060-457a-9c16-000000000363
-----
onPlay:Transfer1Focus-Targeted-atUnit-sourceUnit-hasMarker{Focus}-destinationUnit-hasProperty{Cost}le2-isReact
+++++

.....
Bothan Spy
-----
ff4fb461-8060-457a-9c16-000000000364
-----
onPlay:SimplyAnnounce{look at opponent's hand}-isReact
+++++

.....
Smuggling Compartment
-----
ff4fb461-8060-457a-9c16-000000000365
-----
Placement:Vehicle
+++++
R0:Draw1Card
.....
Swindled
-----
ff4fb461-8060-457a-9c16-000000000366
-----
onPlay:ReturnTarget-Targeted-atUnit-hasProperty{Cost}le2
+++++

.....
Trust Me
-----
ff4fb461-8060-457a-9c16-000000000367
-----

+++++
Put2Damage$$SimplyAnnounce{cancel the effects of the event card}$$Put1Effects Cancelled-DemiAutoTargeted-atEvent-isReady-choose1-isSilent
.....
Lando Calrissian
-----
ff4fb461-8060-457a-9c16-000000000368
-----

+++++
R1:DisengageTarget-DemiAutoTargeted-atUnit-isParticipating-choose1-onlyOnce
.....
Saboteur
-----
ff4fb461-8060-457a-9c16-000000000369
-----
onPlay:DestroyTarget-Targeted-atEnhancement-hasProperty{Cost}le2-choose1-isReact
+++++

.....
Sabotage
-----
ff4fb461-8060-457a-9c16-000000000371
-----
onPlay:DestroyMultiple-AutoTargeted-atUnit-isParticipating
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000372
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Asteroid Sanctuary
-----
ff4fb461-8060-457a-9c16-000000000373
-----
whileInPlay:Draw1Card-foreachEdgeWin-ifOrigEdgeWinner-isReact
+++++

.....
Millennium Falcon
-----
ff4fb461-8060-457a-9c16-000000000374
-----
ConstantEffect:Edge1Bonus
+++++
R0:ReturnMyself$$BringToPlayTarget-Targeted-atCharacter_or_Droid-fromHand
.....
Cloud City Operative
-----
ff4fb461-8060-457a-9c16-000000000375
-----
onPlay:Transfer1Focus-Targeted-atUnit-sourceUnit-hasMarker{Focus}-destinationUnit-hasProperty{Cost}le2-isReact
+++++

.....
Bamboozle
-----
ff4fb461-8060-457a-9c16-000000000377
-----
onPlay:Transfer1Focus-Targeted-atCharacter-sourceCharacter-hasMarker{Focus}-destinationCharacter
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000378
-----
onResolveFate:CustomScript
+++++

.....
Escape from Ord Mantell
-----
ff4fb461-8060-457a-9c16-000000000379
-----
whileInPlay:Remove1Damage-DemiAutoTargeted-atObjective-hasMarker{Damage}-choose1-foreachCardPlayed-typeEvent-isReact
+++++

.....
Mission Commander
-----
ff4fb461-8060-457a-9c16-000000000380
-----
onStrike:Put1Damage-isReact$$RescueTarget-Targeted-isCapturedCurrentObjective
+++++

.....
Covert Sniper
-----
ff4fb461-8060-457a-9c16-000000000381
-----
afterCardRefreshing:Deal1Damage-DemiAutoTargeted-atUnit-targetOpponents-isCommited-choose1-duringMyTurn-isReact
+++++

.....
Short Range Hauler
-----
ff4fb461-8060-457a-9c16-000000000382
-----

+++++

.....
Bring 'Em On
-----
ff4fb461-8060-457a-9c16-000000000383
-----
onPlay:Put2Bring Em On:UD-Targeted-atUnit-isParticipating
+++++

.....
Over My Dead Body
-----
ff4fb461-8060-457a-9c16-000000000384
-----
onPlay:SimplyAnnounce{cancel the effects of the unit's ability}$$Put1Effects Cancelled-Targeted-atUnit-isReady-isSilent
+++++

.....
Lobot
-----
ff4fb461-8060-457a-9c16-000000000386
-----
whileInPlay:CustomScript-ifOrigParticipating
+++++

.....
Security Control Center
-----
ff4fb461-8060-457a-9c16-000000000389
-----
whileInPlay:Put1Shield-foreachCardPlayed-byMe-onTriggerCard-typeUnit-isReact
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000000390
-----
onResolveFate:Put1Shield-Targeted-atUnit_or_Objective
+++++

.....
Across the Anoat Sector
-----
ff4fb461-8060-457a-9c16-000000000391
-----
whileInPlay:IncreaseBD:1-forMe-typeSmugglers and Spies-isAttacking-isAlone
+++++

.....
Undercover Operative
-----
ff4fb461-8060-457a-9c16-000000000394
-----

+++++

.....
Smuggler's Run
-----
ff4fb461-8060-457a-9c16-000000000395
-----
onPlay:TakeoverTarget-Targeted-atEnhancement-targetOpponents
+++++

.....
Over My Dead Body
-----
ff4fb461-8060-457a-9c16-000000000396
-----
onPlay:SimplyAnnounce{cancel the effects of the unit's ability}$$Put1Effects Cancelled-Targeted-atUnit-isReady-isSilent
+++++

.....
Embers of Hope
-----
ff4fb461-8060-457a-9c16-000000000397
-----
ConstantEffect:PreventDraw-forOpponent-ifOrigHasntMarker{Damage}
+++++

.....
Moisture Farmer
-----
ff4fb461-8060-457a-9c16-000000000398
-----

+++++
R0:Remove1Damage-DemiAutoTargeted-atTatooine-hasMarker{Damage}-choose1-isCost$$Put1Damage
.....
Moisture Farmer
-----
ff4fb461-8060-457a-9c16-000000000399
-----

+++++
R0:Remove1Damage-DemiAutoTargeted-atTatooine-hasMarker{Damage}-choose1-isCost$$Put1Damage
.....
Makashi Training
-----
ff4fb461-8060-457a-9c16-000000000400
-----
Placement:Force User||ConstantAbility:TargetStrike
+++++

.....
Force Precognition
-----
ff4fb461-8060-457a-9c16-000000000401
-----
Placement:Force User
+++++

.....
Secret Guardian ### We use this weird 'whileInPlay' trick because you cannot put markers on cards in your hand, and targeting is wiped when the card is moved by the previous script.
-----
ff4fb461-8060-457a-9c16-000000000402
-----
onPlay:BringToPlayTarget-Targeted-atCharacter-fromHand||whileInPlay:Put1Secret Guardian-foreachCardPlayed-onTriggerCard-typeCharacter-isSilent
+++++

.....
Alderaan's Promise
-----
ff4fb461-8060-457a-9c16-000000000403
-----
onThwart:Gain1Dial-isReact-isForced
+++++

.....
Bail Organa
-----
ff4fb461-8060-457a-9c16-000000000404
-----
ExtraIcon:Tactics:1-perEveryAlderaan-max1-AutoTargeted-atAlderaan_and_Objective||whileInPlay:SacrificeMyself-foreachObjectiveThwarted-typeAlderaan's Promise-isReact-isForced
+++++

.....
Tantive IV
-----
ff4fb461-8060-457a-9c16-000000000405
-----
onPlay:Retrieve1Card-grabUnique-onTop5Cards-isReact$$ShuffleDeck
+++++

.....
Alderaanian Artist
-----
ff4fb461-8060-457a-9c16-000000000406
-----
whileInPlay:SacrificeMyself-foreachObjectiveThwarted-typeAlderaan's Promise-isReact-isForced
+++++

.....
Diplomatic Presence
-----
ff4fb461-8060-457a-9c16-000000000407
-----
Placement:Objective-targetMine
+++++

.....
Misdirection
-----
ff4fb461-8060-457a-9c16-000000000408
-----
onPlay:Transfer1Damage-Targeted-atObjective-targetMine-sourceObjective-targetMine-hasMarker{Damage}-destinationObjective-targetMine
+++++

.....
To Arms!
-----
ff4fb461-8060-457a-9c16-000000000409
-----
whileInPlay:Reduce2CostPlay-affectsEnhancement_and_Weapon-onlyOnce-forMe
+++++

.....
Sullustan Weapon Tech
-----
ff4fb461-8060-457a-9c16-000000000410
-----
whileInPlay:Draw1Card-foreachCardPlayed-typeEnhancement_and_Weapon-forMe-isReact
+++++

.....
Sullustan Weapon Tech
-----
ff4fb461-8060-457a-9c16-000000000411
-----
whileInPlay:Draw1Card-foreachCardPlayed-typeEnhancement_and_Weapon-byMe-isReact
+++++

.....
Han's Heavy Blaster Pistol
-----
ff4fb461-8060-457a-9c16-000000000412
-----
Placement:Character||BonusIcons:UD:1, BD:1||ConstantEffect:Edge1Bonus-perEveryUnit-AutoTargeted-onHost-atHan Solo-isDistributedEffect
+++++

.....
Chewbacca's Bowcaster
-----
ff4fb461-8060-457a-9c16-000000000413
-----
Placement:Character||BonusIcons:UD:1, BD:1
+++++

.....
Hidden Cache
-----
ff4fb461-8060-457a-9c16-000000000414
-----
onPlay:Retrieve1Card-grabEnhancement_and_Weapon$$ShuffleDeck
+++++

.....
Massassi Temple Lookout
-----
ff4fb461-8060-457a-9c16-000000000416
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough-onlyOnce-failSilently||afterEngagement:Pass-onlyOnce-failSilently
+++++

.....
Massassi Temple Lookout
-----
ff4fb461-8060-457a-9c16-000000000417
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough-onlyOnce-failSilently||afterEngagement:Pass-onlyOnce-failSilently
+++++

.....
Ion Cannon Barrage
-----
ff4fb461-8060-457a-9c16-000000000418
-----
onPlay:Remove999Shield-AutoTargeted-hasMarker{Shield}
+++++

.....
Proximity Mine
-----
ff4fb461-8060-457a-9c16-000000000419
-----

+++++
R0:SacrificeMyself$$Deal2Damage-AutoTargeted-atUnit-isAttacking-targetOpponents-isParticipating
.....
Protection
-----
ff4fb461-8060-457a-9c16-000000000420
-----
onResolveFate:Put1Shield-Targeted-atUnit_or_Objective
+++++

.....
Hive of Scum and Villainy
-----
ff4fb461-8060-457a-9c16-000000000421
-----
whileInPlay:DecreaseUD:1-typeUnit-isAttacking-ifOrigCurrentObjective
+++++

.....
Greedo
-----
ff4fb461-8060-457a-9c16-000000000422
-----
whileInPlay:Deal1Damage-foreachEdgeWin-ifOrigEdgeLoser-ifOrigParticipating-isReact-isForced
+++++

.....
Bounty
-----
ff4fb461-8060-457a-9c16-000000000425
-----
Placement:Unit-targetOpponents||whileInPlay:SacrificeMyself-foreachAttackerEdgeWin-ifOrigDefending-ifEdgeDiffge3||whileInPlay:SacrificeMyself-foreachDefenderEdgeWin-ifOrigAttacking-ifEdgeDiffge3||afterCardRefreshing:CaptureHost-duringMyTurn
+++++

.....
Captured
-----
ff4fb461-8060-457a-9c16-000000000426
-----
onPlay:CaptureTarget-Targeted-atUnit
+++++

.....
Jabba's Reach
-----
ff4fb461-8060-457a-9c16-000000000427
-----
whileInPlay:Gain1Reserves-foreachCardCaptured-ifCapturingObjective||whileInPlay:Lose1Reserves-foreachCardRescued-ifCapturingObjective||onThwart:Lose1Reserves-perEveryCard-AutoTargeted-isCaptured-isJailer-noTargetingError
+++++

.....
Jabba the Hutt
-----
ff4fb461-8060-457a-9c16-000000000428
-----

+++++
R0:Put1Focus-isCost$$BringToPlayTarget-Targeted-atUnit_or_Enhancement-hasProperty{Cost}le2-fromHand
.....
Jabba's Pleasure Barge
-----
ff4fb461-8060-457a-9c16-000000000429
-----
afterDeployment:Remove1Focus-DemiAutoTargeted-atCharacter-hasMarker{Focus}-targetMine-choose1-isCost-duringMyTurn-isReact$$Put1Focus
+++++

.....
Reversal of Fate
-----
ff4fb461-8060-457a-9c16-000000000432
-----

+++++

.....
The Tatooine Crash
-----
ff4fb461-8060-457a-9c16-000000000433
-----
afterCardRefreshing:CaptureTarget-AutoTargeted-fromTopDeckOpponents-captureOnMyself-duringMyTurn-isReact
+++++

.....
Jawa Scavenger
-----
ff4fb461-8060-457a-9c16-000000000434
-----
whileInPlay:ReturnMyself-foreachEdgeWin-ifOrigEdgeLoser-isReact-isForced
+++++

.....
Jawa Scavenger
-----
ff4fb461-8060-457a-9c16-000000000435
-----
whileInPlay:ReturnMyself-foreachEdgeWin-ifOrigEdgeLoser-isReact-isForced
+++++

.....
Sandcrawler
-----
ff4fb461-8060-457a-9c16-000000000436
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough||onLeaving:Put1Focus-AutoTargeted-atCharacter_or_Droid-isReact-isForced
+++++

.....
Utinni!
-----
ff4fb461-8060-457a-9c16-000000000437
-----
onPlay:CaptureTarget-Targeted-atEnhancement-targetOpponents
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000438
-----
onResolveFate:CustomScript
+++++

.....
The Shadow of Nar Shaddaa
-----
ff4fb461-8060-457a-9c16-000000000439
-----

+++++
R0:Put2Focus-isCost$$Put1Focus-DemiAutoTargeted-atUnit-isAttacking-choose1
.....
Assassin Droid
-----
ff4fb461-8060-457a-9c16-000000000440
-----

+++++
R0:Remove1Focus
.....
Aqualish Thug
-----
ff4fb461-8060-457a-9c16-000000000441
-----
onPlay:SimplyAnnounce{force each opponent to deal 2 damage divided among any number of objectives they controls.}-isReact
+++++

.....
Aqualish Thug
-----
ff4fb461-8060-457a-9c16-000000000442
-----
onPlay:SimplyAnnounce{force each opponent to deal 2 damage divided among any number of objectives they controls.}-isReact
+++++

.....
Spice Visions
-----
ff4fb461-8060-457a-9c16-000000000443
-----
onPlay:Remove1Focus-Targeted-atCharacter_or_Creature$$Put1Damage-Targeted-atCharacter_or_Creature
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000000444
-----
onResolveFate:Put1Shield-Targeted-atUnit_or_Objective
+++++

.....
Carbonite Transport
-----
ff4fb461-8060-457a-9c16-000000000445
-----
afterCardRefreshing:CaptureTarget-Targeted-isCaptured-duringMyTurn-isReact
+++++

.....
Slave I
-----
ff4fb461-8060-457a-9c16-000000000446
-----
ExtraIcon:BD:1-perEveryObjective-AutoTargeted-atObjective-hasCaptures-targetMine
+++++

.....
Traitorous Wing Guard
-----
ff4fb461-8060-457a-9c16-000000000447
-----
ExtraIcon:BD:1-perEveryObjective-AutoTargeted-atObjective-hasCaptures-max1-targetAllied
+++++

.....
Tractor Beam
-----
ff4fb461-8060-457a-9c16-000000000449
-----
onPlay:Transfer1Focus-Targeted-atVehicle-sourceVehicle-hasMarker{Focus}-destinationVehicle
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000450
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Trandoshan Terror
-----
ff4fb461-8060-457a-9c16-000000000451
-----
+++++

.....
Bossk
-----
ff4fb461-8060-457a-9c16-000000000452
-----
onPlay:Put2Focus-isCost-isReact$$CaptureTarget-DemiAutoTargeted-atCharacter-hasMarker{Focus}-choose1
+++++

.....
Trandoshan Hunter
-----
ff4fb461-8060-457a-9c16-000000000453
-----

+++++

.....
Trandoshan Hunter
-----
ff4fb461-8060-457a-9c16-000000000454
-----

+++++

.....
Bounty
-----
ff4fb461-8060-457a-9c16-000000000455
-----
Placement:Unit-targetOpponents||whileInPlay:SacrificeMyself-foreachAttackerEdgeWin-ifOrigDefending-ifEdgeDiffge3||whileInPlay:SacrificeMyself-foreachDefenderEdgeWin-ifOrigAttacking-ifEdgeDiffge3||afterCardRefreshing:CaptureHost-duringMyTurn
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000456
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Feeding the Pit
-----
ff4fb461-8060-457a-9c16-000000000457
-----

+++++
R0:DestroyTarget-Targeted-isCaptured$$Remove1Damage$$Draw1Card
.....
Spice Visions
-----
ff4fb461-8060-457a-9c16-000000000461
-----
onPlay:Remove1Focus-Targeted-atCharacter_or_Creature$$Put1Damage-Targeted-atCharacter_or_Creature
+++++

.....
The Almighty Sarlacc
-----
ff4fb461-8060-457a-9c16-000000000462
-----
Placement:Objective_and_Tatooine-targetMine
+++++
R0:Put1Damage-AutoTargeted-onHost$$Remove1Focus-AutoTargeted-onHost
.....
The Ghosts of the Dark Side
-----
ff4fb461-8060-457a-9c16-000000000463
-----
ConstantEffect:Force1Bonus
+++++

.....
Force Wraith
-----
ff4fb461-8060-457a-9c16-000000000464
-----
ConstantEffect:Unwavering
+++++

.....
Force Wraith
-----
ff4fb461-8060-457a-9c16-000000000465
-----
ConstantEffect:Unwavering
+++++

.....
Dark Memories
-----
ff4fb461-8060-457a-9c16-000000000466
-----
Placement:Character-targetOpponents||onHostMarkerAddFocus:Deal1Damage-AutoTargeted-onHost-isReact
+++++

.....
Dark Memories
-----
ff4fb461-8060-457a-9c16-000000000467
-----
Placement:Character-targetOpponents||onHostMarkerAddFocus:Deal1Damage-AutoTargeted-onHost-isReact
+++++

.....
Force Shockwave
-----
ff4fb461-8060-457a-9c16-000000000468
-----
onPlay:Deal1Damage-AutoTargeted-atUnit-isNotCommited-targetOpponents
+++++

.....
Imperial Blockade
-----
ff4fb461-8060-457a-9c16-000000000469
-----
whileInPlay:Increase1CostPlay-affectsUnit-byOpponent-ifOrigHasntMarker{Damage}-onlyOnce
+++++

.....
Captain Needa
-----
ff4fb461-8060-457a-9c16-000000000470
-----
whileInPlay:Reduce2CostPlay-affectsCapital Ship-onlyOnce-forMe
+++++

.....
Apology Accepted
-----
ff4fb461-8060-457a-9c16-000000000473
-----
onPlay:SacrificeTarget-Targeted-atUnit_and_Imperial Navy_and_Officer$$Remove999Focus-Targeted-atUnit_and_Imperial Navy_and_Vehicle
+++++

.....
Tractor Beam
-----
ff4fb461-8060-457a-9c16-000000000474
-----
onPlay:Transfer1Focus-Targeted-atVehicle-sourceVehicle-hasMarker{Focus}-destinationVehicle
+++++

.....
Across the Jundland Wastes
-----
ff4fb461-8060-457a-9c16-000000000475
-----
whileInPlay:Put1Focus-foreachUnitStrike-onTriggerCard-typeCharacter-isReact-isForced
+++++

.....
Bantha
-----
ff4fb461-8060-457a-9c16-000000000476
-----
whileInPlay:Retrieve1Card-grabEnhancement-fromDiscard-isTopmost-foreachCardPlayed-typeScavenger-isReact
+++++

.....
Tusken Raider
-----
ff4fb461-8060-457a-9c16-000000000477
-----
onStrike:ReturnMyself-isReact
+++++

.....
Tusken Raider
-----
ff4fb461-8060-457a-9c16-000000000478
-----
onStrike:ReturnMyself-isReact
+++++

.....
Tusken Raider
-----
ff4fb461-8060-457a-9c16-000000000479
-----
onStrike:ReturnMyself-isReact
+++++

.....
Gaffi Stick
-----
ff4fb461-8060-457a-9c16-000000000480
-----
Placement:Scavenger||ConstantEffect:Edge1Bonus-perEveryUnit-AutoTargeted-atUnit-targetAllied-isParticipating-isDistributedEffect-ignore1-ifOrigParticipatingHost
+++++

.....
Asteroid Pursuit
-----
ff4fb461-8060-457a-9c16-000000000481
-----
afterCardRefreshing:Deal1Damage-duringMyTurn-isReact-isForced
+++++

.....
Lictor-class Dungeon Ship
-----
ff4fb461-8060-457a-9c16-000000000482
-----
ExtraIcon:UD:1-perEveryObjective-AutoTargeted-atObjective-hasCaptures-max1-targetMine||ExtraIcon:BD:1-perEveryObjective-AutoTargeted-atObjective-hasCaptures-max1-targetMine
+++++

.....
Trooper Sentry
-----
ff4fb461-8060-457a-9c16-000000000483
-----
onPlay:Put1Shield-DemiAutoTargeted-atUnit_or_Objective-choose1-isReact
+++++

.....
Trooper Sentry
-----
ff4fb461-8060-457a-9c16-000000000484
-----
onPlay:Put1Shield-DemiAutoTargeted-atUnit_or_Objective-choose1-isReact
+++++

.....
Armed and Ready
-----
ff4fb461-8060-457a-9c16-000000000485
-----
onPlay:CreateDummy-nonUnique||whileInPlay:IncreaseBD:1-forMe-typeUnit-hasMarker{Shield}-onlyforDummy||whileInPlay:IncreaseUD:1-forMe-typeUnit-hasMarker{Shield}-onlyforDummy||afterPhase:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000000486
-----
onResolveFate:Put1Shield-Targeted-atUnit_or_Objective
+++++

.....
501st Trooper
-----
ff4fb461-8060-457a-9c16-000000000506
-----
ExtraIcon:BD:1-ifOrigAttacking-hasObjectiveTrait-typeHoth
+++++

.....
501st Trooper
-----
ff4fb461-8060-457a-9c16-000000000507
-----
ExtraIcon:BD:1-ifOrigAttacking-hasObjectiveTrait-typeHoth
+++++

.....
Aggressive Assault
-----
ff4fb461-8060-457a-9c16-000000000516
-----
onPlay:Deal1Damage-AutoTargeted-atObjective-targetOpponents
+++++

.....
AT-AT
-----
ff4fb461-8060-457a-9c16-000000000512
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough||onStrike:DestroyTarget-Targeted-atEnhancement-isStrikeAlternative-isReact
+++++

.....
AT-AT
-----
ff4fb461-8060-457a-9c16-000000000513
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough||onStrike:DestroyTarget-Targeted-atEnhancement-isStrikeAlternative-isReact
+++++

.....
AT-AT Assault Formation
-----
ff4fb461-8060-457a-9c16-000000000514
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough||onStrike:Deal1Damage-AutoTargeted-atObjective_and_Hoth-targetOpponents-isReact
+++++

.....
Attack Pattern Delta
-----
ff4fb461-8060-457a-9c16-000000000487
-----
   
+++++
R0:Retrieve1Card-grabVehicle-hasProperty{Cost}le2-toTable-onTop1Cards-tellPlayer-isReact-onlyOnce
.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000492
-----

+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000504
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000510
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

.....
Coordinated Strike
-----
ff4fb461-8060-457a-9c16-000000000503
-----
onPlay:SimplyAnnounce{immediately strike again with another ready participating unit they control}
+++++

.....
E-Web Heavy Repeating Blaster
-----
ff4fb461-8060-457a-9c16-000000000509
-----

+++++
R0:Put1Focus-isCost-isSilent$$Put1EWeb Heavy Repeating Blaster:BD-Targeted-atTrooper-isSilent
.....
Hold-out Blaster
-----
ff4fb461-8060-457a-9c16-000000000496
-----
Placement:Smugglers and Spies_and_Character||BonusIcons:Double-ifOrigHasLess-typeUnit
+++++

.....
Hoth Rearguard
-----
ff4fb461-8060-457a-9c16-000000000500
-----

+++++
R0:Remove1Damage-DemiAutoTargeted-atHoth-hasMarker{Damage}-choose1-isCost$$Put1Damage
.....
Hoth Rearguard
-----
ff4fb461-8060-457a-9c16-000000000501
-----

+++++
R0:Remove1Damage-DemiAutoTargeted-atHoth-hasMarker{Damage}-choose1-isCost$$Put1Damage
.....
Hoth Rearguard
-----
ff4fb461-8060-457a-9c16-000000000502
-----

+++++

.....
Narrow Escape
-----
ff4fb461-8060-457a-9c16-000000000497
-----
onPlay:SimplyAnnounce{choose a new target for the effect}
+++++

.....
Orbital Resupply Station
-----
ff4fb461-8060-457a-9c16-000000000515
-----
whileInPlay:Reduce1CostPlay-affectsUnit_and_Vehicle_and_Imperial Navy-hasProperty{Cost}ge4-forMe
+++++

.....
Rogue Leader
-----
ff4fb461-8060-457a-9c16-000000000488
-----
ExtraIcon:Tactics:1-perEveryRogueTwo-AutoTargeted-atRogue Two-targetMine
+++++

.....
Rogue Two
-----
ff4fb461-8060-457a-9c16-000000000489
-----
ExtraIcon:EE-BD:1-perEverySpeeder-AutoTargeted-atSpeeder-targetMine-isAttacking-isParticipating
+++++

.....
Shadow Operative
-----
ff4fb461-8060-457a-9c16-000000000494
-----

+++++
R0:ReturnMyself
.....
Shadow Operative
-----
ff4fb461-8060-457a-9c16-000000000495
-----

+++++
R0:ReturnMyself
.....
Snowspeeder Launch Bay
-----
ff4fb461-8060-457a-9c16-000000000491
-----
whileInPlay:Deal1Damage-Targeted-atVehicle-targetOpponents-foreachUnitStrike-typeSpeeder-isReact-onlyOnce$$Put1Focus-Targeted-atVehicle_and_Walker-targetOpponents
+++++

.....
Tactical Retreat
-----
ff4fb461-8060-457a-9c16-000000000498
-----
onPlay:ReturnMulti-Targeted-atUnit-targetMine
+++++

.....
Undercover Dealings
-----
ff4fb461-8060-457a-9c16-000000000493
-----
afterCardRefreshing:Draw999Cards-ifOrigHasLess-typeUnit-duringOpponentTurn-isReact
+++++

.....
Vader's Fist
-----
ff4fb461-8060-457a-9c16-000000000505
-----
onPlay:Lose1Reserves-onAllOpponents||onDamage:Gain1Reserves-onAllOpponents||onHeal:Lose1Reserves-onAllOpponents||onThwart:Gain1Reserves-onAllOpponents-ifOrigHasntMarker{Damage}
+++++

.....
A Hero's Resolve
-----
ff4fb461-8060-457a-9c16-000000000517
-----
ConstantEffect:Edge1Bonus-perEveryCard-AutoTargeted-targetMine-isEdgeCard-isDistributedEffect-ifOrigHasntMarker{Damage}
+++++

.....
Luke Skywalker
-----
ff4fb461-8060-457a-9c16-000000000518
-----
onPlay:CustomScript||BonusIcons:UD:1, T:1||onPay:Reduce2CostPlay-perEveryVehicle-Targeted-atSpeeder_or_Fighter-noTargetingError-maxReduce2||onHostLeaving:CustomScript
+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000521
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000522
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Evacuation Procedure
-----
ff4fb461-8060-457a-9c16-000000000523
-----
atTurnStart:SacrificeTarget-DemiAutoTargeted-atUnit-targetMine-choose1-duringOpponentTurn-isReact$$Remove999Focus-DemiAutoTargeted-atEnhancement_or_Objective_and_Hoth-hasMarker{Focus}-choose1
+++++

.....
Han Solo
-----
ff4fb461-8060-457a-9c16-000000000524
-----
onLeaving:Retrieve1Card-grabRebel Alliance-isReact$$ShuffleDeck
+++++

.....
Toryn Farr
-----
ff4fb461-8060-457a-9c16-000000000525
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough||onLeaving:Put1Focus-DemiAutoTargeted-atEnhancement-choose1-targetOpponents-isReact
+++++

.....
Bright Hope
-----
ff4fb461-8060-457a-9c16-000000000526
-----
whileInPlay:Remove1AnyTokenType-foreachCardLeavingPlay-typeUnit-byFriendlyOriginController-isReact
+++++

.....
Buried Outpost
-----
ff4fb461-8060-457a-9c16-000000000527
-----
onPlay:Put1Focus||onPlay:SacrificeTarget-DemiAutoTargeted-atUnit-targetMine-choose1
+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000528
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

.....
Executor
-----
ff4fb461-8060-457a-9c16-000000000530
-----
whileInPlay:Deal1Damage-DemiAutoTargeted-atUnit_or_Objective-targetOpponents-choose1-foreachCardSacrificed-isReact
+++++
R0:Deal1Damage-DemiAutoTargeted-atUnit_or_Objective-targetOpponents-choose1
.....
ISB Liaison
-----
ff4fb461-8060-457a-9c16-000000000531
-----

+++++
R0:SacrificeMyself$$SimplyAnnounce{look at the top card of a deck and then draw a card}
.....
ISB Liaison
-----
ff4fb461-8060-457a-9c16-000000000532
-----

+++++
R0:SacrificeMyself$$SimplyAnnounce{look at the top card of a deck and then draw a card}
.....
Sith Holocron
-----
ff4fb461-8060-457a-9c16-000000000533
-----
whileInPlay:Reduce3CostPlay-affectsSith-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeSith-onlyforDummy-isSilent
+++++
R0:SacrificeMyself$$SimplyAnnounce{reduce the cost of the next Sith card they play this phase by 3}$$CreateDummy-nonUnique-isSilent-doNotDiscard
.....
Aggression
-----
ff4fb461-8060-457a-9c16-000000000534
-----
onPlay:SimplyAnnounce{force each player to sacrifice a unit if able}
+++++

.....
Hunt Them Down
-----
ff4fb461-8060-457a-9c16-000000000535
-----

+++++

.....
Dengar
-----
ff4fb461-8060-457a-9c16-000000000536
-----
ConstantAbility:CanCapture-ifInPlay-typeUnit||onStrike:CustomScript
+++++

.....
Kihraxz-class Assault Fighter
-----
ff4fb461-8060-457a-9c16-000000000537
-----
onStrike:CaptureTarget-DemiAutoTargeted-atUnit-hasProperty{Cost}le1-targetOpponents-choose1-ifOrighasEdge-isReact
+++++

.....
Kihraxz-class Assault Fighter
-----
ff4fb461-8060-457a-9c16-000000000538
-----
onStrike:CaptureTarget-DemiAutoTargeted-atUnit-hasProperty{Cost}le1-targetOpponents-choose1-ifOrighasEdge-isReact
+++++

.....
Remote Hideout
-----
ff4fb461-8060-457a-9c16-000000000539
-----
whileInPlay:Put1Focus-foreachCardPlayed-byMe-onTriggerCard-typeUnit-onlyOnce
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000540
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Endless Reserves
-----
ff4fb461-8060-457a-9c16-000000000541
-----
ConstantEffect:Edge1Bonus-perEveryEvent-AutoTargeted-atEvent-targetMine-isEdgeCard-isDistributedEffect-ifOrigHasntMarker{Damage}
+++++

.....
Vast Resources
-----
ff4fb461-8060-457a-9c16-000000000542
-----
onPlay:SimplyAnnounce{reduce the cost of the next card they play this phase by 1}$$CreateDummy-isSilent-nonUnique-doNotDiscard||whileInPlay:Reduce1CostPlay-affectsAll-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typenotVast Resources-onlyforDummy-isSilent
+++++

.....
Vast Resources
-----
ff4fb461-8060-457a-9c16-000000000543
-----
onPlay:SimplyAnnounce{reduce the cost of the next card they play this phase by 1}$$CreateDummy-isSilent-nonUnique-doNotDiscard||whileInPlay:Reduce1CostPlay-affectsAll-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typenotVast Resources-onlyforDummy-isSilent
+++++

.....
Vast Resources
-----
ff4fb461-8060-457a-9c16-000000000544
-----
onPlay:SimplyAnnounce{reduce the cost of the next card they play this phase by 1}$$CreateDummy-isSilent-nonUnique-doNotDiscard||whileInPlay:Reduce1CostPlay-affectsAll-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typenotVast Resources-onlyforDummy-isSilent
+++++

.....
Vast Resources
-----
ff4fb461-8060-457a-9c16-000000000545
-----
onPlay:SimplyAnnounce{reduce the cost of the next card they play this phase by 1}$$CreateDummy-isSilent-nonUnique-doNotDiscard||whileInPlay:Reduce1CostPlay-affectsAll-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typenotVast Resources-onlyforDummy-isSilent
+++++

.....
Vast Resources
-----
ff4fb461-8060-457a-9c16-000000000546
-----
onPlay:SimplyAnnounce{reduce the cost of the next card they play this phase by 1}$$CreateDummy-isSilent-nonUnique-doNotDiscard||whileInPlay:Reduce1CostPlay-affectsAll-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typenotVast Resources-onlyforDummy-isSilent
+++++

.....
Watchers in the Wasteland
-----
ff4fb461-8060-457a-9c16-000000000547
-----
ConstantEffect:Force1Bonus-perReservesTeam
+++++

.....
Obi-Wan Kenobi
-----
ff4fb461-8060-457a-9c16-000000000548
-----
whileInPlay:CustomScript-foreachForceStruggleLight-isReact
+++++

.....
Shistavanen Wolfman
-----
ff4fb461-8060-457a-9c16-000000000549
-----
ConstantEffect:Edge1Bonus
+++++

.....
Shistavanen Wolfman
-----
ff4fb461-8060-457a-9c16-000000000550
-----
ConstantEffect:Edge1Bonus
+++++

.....
Force Cleansing
-----
ff4fb461-8060-457a-9c16-000000000551
-----
Placement:Character-byAlly||whileInPlay:Remove1Focus-AutoTargeted-onHost-foreachDialIncrease-isReact-isForced$$Remove1Damage-AutoTargeted-onHost
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000000552
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
Blue Squadron Support
-----
ff4fb461-8060-457a-9c16-000000000553
-----

+++++
R0:Put1Focus-isCost$$CustomScript
.....
Blue Leader
-----
ff4fb461-8060-457a-9c16-000000000554
-----
onStrike:Deal1Damage-DemiAutoTargeted-atObjective-isNotParticipating-targetOpponents-choose1-ifOrigAttacking-isReact
+++++

.....
B-Wing
-----
ff4fb461-8060-457a-9c16-000000000555
-----
onStrike:Draw1Card-onAllies-isReact
+++++

.....
B-Wing
-----
ff4fb461-8060-457a-9c16-000000000556
-----
onStrike:Draw1Card-onAllies-isReact
+++++

.....
Rapid Fire
-----
ff4fb461-8060-457a-9c16-000000000557
-----
onPlay:Deal1Damage-Targeted-atUnit-targetOpponents
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000000558
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
Rendar's Wrath
-----
ff4fb461-8060-457a-9c16-000000000559
-----
whileInPlay:Deal1Damage-AutoTargeted-atUnit-isDefending-isAlone-foreachDefendersDeclared-ifDefendersOpponentseq1-isReact
+++++

.....
Dash Rendar
-----
ff4fb461-8060-457a-9c16-000000000560
-----

+++++
R1:Put1Allied Boost:UD-allyPayable
.....
Arcona Rumor Monger
-----
ff4fb461-8060-457a-9c16-000000000561
-----

+++++

.....
Arcona Rumor Monger
-----
ff4fb461-8060-457a-9c16-000000000562
-----

+++++

.....
Smuggling Shipment
-----
ff4fb461-8060-457a-9c16-000000000563
-----
onPlay:Remove1Focus-Targeted-hasProperty{Resources}ge1-targetAllied
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000000564
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
The Emperor's Hand
-----
ff4fb461-8060-457a-9c16-000000000565
-----
ConstantEffect:Force1Bonus-perReservesTeam
+++++

.....
Mara Jade
-----
ff4fb461-8060-457a-9c16-000000000566
-----
ConstantAbility:TargetStrike||atTurnEnd:Remove1Focus-isSilent-isReact$$UseCustomAbility
+++++

.....
*Agent of the Hand
-----
ff4fb461-8060-457a-9c16-000000000567
-----
whileInPlay:Remove1Focus-foreachCardTakeover-isReact||whileInPlay:Remove1Focus-foreachReservesPlayed-isReact
+++++

.....
*Agent of the Hand
-----
ff4fb461-8060-457a-9c16-000000000568
-----
whileInPlay:Remove1Focus-foreachCardTakeover-isReact||whileInPlay:Remove1Focus-foreachReservesPlayed-isReact
+++++

.....
Join Me
-----
ff4fb461-8060-457a-9c16-000000000569
-----
onPlay:TakeoverTarget-Targeted-atUnit_and_Character_and_nonUnique
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000000570
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
Repair and Refurbish
-----
ff4fb461-8060-457a-9c16-000000000571
-----
atTurnStart:CustomScript-isReact-duringMyTurn
+++++

.....
Thunderflare
-----
ff4fb461-8060-457a-9c16-000000000572
-----
onStrike:Remove1Damage-DemiAutoTargeted-atObjective-hasMarker{Damage}-targetAllied-choose1-isCost-isReact$$Deal1Damage-DemiAutoTargeted-atObjective-targetOpponents-choose1
+++++

.....
Logistics Officer
-----
ff4fb461-8060-457a-9c16-000000000573
-----
onPlay:TakeoverMyself-onAllies-isOptional$$Remove1Damage-DemiAutoTargeted-atObjective-hasMarker{Damage}-targetAllied-choose1-noTargetingError
+++++

.....
Logistics Officer
-----
ff4fb461-8060-457a-9c16-000000000574
-----
onPlay:TakeoverMyself-onAllies-isOptional$$Remove1Damage-DemiAutoTargeted-atObjective-hasMarker{Damage}-targetAllied-choose1-noTargetingError
+++++

.....
Weapons Upgrade
-----
ff4fb461-8060-457a-9c16-000000000575
-----
Placement:Vehicle_and_Unit||BonusIcons:BD:1||onPlay:CustomScript
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000000576
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
Mercenary Support
-----
ff4fb461-8060-457a-9c16-000000000577
-----
whileInPlay:Put1Mercenary Support-foreachCardPlayed-onTriggerCard-typeMercenary_or_Bounty Hunter-isSilent-onlyforDummy$$TakeoverTarget-onTeam-isSilent$$DestroyMyself-isSilent
+++++
R0:Put1Focus-isCost$$CreateDummy-isSilent-doNotDiscard$$BringToPlayTarget-Targeted-atMercenary_or_Bounty Hunter-fromHand

.....
Punishing One
-----
ff4fb461-8060-457a-9c16-000000000578
-----
afterDraw:CaptureTarget-onAnyAlliedObjective-Targeted-isCaptured-duringMyTurn-isReact-isSilent
+++++

.....
Trandoshan Security Team
-----
ff4fb461-8060-457a-9c16-000000000579
-----

+++++

.....
Trandoshan Security Team
-----
ff4fb461-8060-457a-9c16-000000000580
-----

+++++

.....
A Price on Their Heads
-----
ff4fb461-8060-457a-9c16-000000000581
-----
onPlay:CaptureMulti-Targeted-atUnit-targetOpponents
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000000582
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
Death Star II
-----
ff4fb461-8060-457a-9c16-000000000583
-----

+++++

.....
Lemelisk's Ambition
-----
ff4fb461-8060-457a-9c16-000000000584
-----
onPlay:Gain1Reserves-perOpponent||onThwart:Lose1Reserves-perOpponent
+++++

.....
Along the Sanctuary Pipeline
-----
ff4fb461-8060-457a-9c16-000000000585
-----
afterCardRefreshing:Remove1Focus-AutoTargeted-atObjective-hasMarker{Focus}-targetMine-duringMyTurn-isReact
+++++

.....
Heightened Security
-----
ff4fb461-8060-457a-9c16-000000000586
-----

+++++
R0:Remove1Damage-Targeted-atObjective-hasMarker{Damage}-targetMine-isCost-onlyOnce$$Refill1Shield-Targeted-atObjective-targetMine
.....
Jerjerrod's Task
-----
ff4fb461-8060-457a-9c16-000000000587
-----

+++++

.....
Construction Droid
-----
ff4fb461-8060-457a-9c16-000000000588
-----

+++++

.....
Death Star Guards
-----
ff4fb461-8060-457a-9c16-000000000589
-----

+++++

.....
TIE Interceptor
-----
ff4fb461-8060-457a-9c16-000000000590
-----

+++++

.....
Destroyer Defense Fleet
-----
ff4fb461-8060-457a-9c16-000000000591
-----

+++++

.....
Lambda-class Shuttle
-----
ff4fb461-8060-457a-9c16-000000000592
-----

+++++

.....
Darth Vader
-----
ff4fb461-8060-457a-9c16-000000000593
-----

+++++

.....
Moff Jerjerrod
-----
ff4fb461-8060-457a-9c16-000000000594
-----

+++++

.....
Admiral Piett
-----
ff4fb461-8060-457a-9c16-000000000595
-----

+++++

.....
Emperor Palpatine
-----
ff4fb461-8060-457a-9c16-000000000596
-----

+++++

.....
Orbital Construction Yard
-----
ff4fb461-8060-457a-9c16-000000000597
-----

+++++

.....
Tactical Command Center
-----
ff4fb461-8060-457a-9c16-000000000598
-----

+++++

.....
Strategic Command Center
-----
ff4fb461-8060-457a-9c16-000000000599
-----

+++++

.....
Endor Shield Generator
-----
ff4fb461-8060-457a-9c16-000000000600
-----

+++++

.....
Signal Jam
-----
ff4fb461-8060-457a-9c16-000000000601
-----

+++++

.....
We Shall Double Our Efforts
-----
ff4fb461-8060-457a-9c16-000000000602
-----

+++++

.....
Fleet Ambush
-----
ff4fb461-8060-457a-9c16-000000000603
-----

+++++

.....
Fully Armed
-----
ff4fb461-8060-457a-9c16-000000000604
-----

+++++

.....
Change of Plan
-----
ff4fb461-8060-457a-9c16-000000000605
-----

+++++

.....
The Mines
-----
ff4fb461-8060-457a-9c16-000000000606
-----

+++++

.....
The Final Ship
-----
ff4fb461-8060-457a-9c16-000000000607
-----

+++++

.....
Dagobah Refuge
-----
ff4fb461-8060-457a-9c16-000000000608
-----

+++++

.....
The Coruscant Rescue
-----
ff4fb461-8060-457a-9c16-000000000609
-----

+++++

.....
Rebel Command
-----
ff4fb461-8060-457a-9c16-000000000610
-----

+++++

.....
The Ruins of Alderaan
-----
ff4fb461-8060-457a-9c16-000000000611
-----

+++++

.....
Front Line Reinforcements
-----
ff4fb461-8060-457a-9c16-000000000612
-----

+++++

.....
Mission at Kothlis
-----
ff4fb461-8060-457a-9c16-000000000613
-----

+++++

.....
Return to Tatooine
-----
ff4fb461-8060-457a-9c16-000000000614
-----

+++++

.....
Luke Skywalker
-----
ff4fb461-8060-457a-9c16-000000000615
-----

+++++

.....
Rebel Sentry
-----
ff4fb461-8060-457a-9c16-000000000616
-----

+++++

.....
Bothan Facilitator
-----
ff4fb461-8060-457a-9c16-000000000617
-----

+++++

.....
Tatooine Sympathizer
-----
ff4fb461-8060-457a-9c16-000000000618
-----

+++++

.....
Rogue Squadron Backup
-----
ff4fb461-8060-457a-9c16-000000000619
-----

+++++

.....
SpecForces Commando
-----
ff4fb461-8060-457a-9c16-000000000620
-----

+++++

.....
Rebel Ambush Team
-----
ff4fb461-8060-457a-9c16-000000000621
-----

+++++

.....
Decoy Wing
-----
ff4fb461-8060-457a-9c16-000000000622
-----

+++++

.....
R2-D2
-----
ff4fb461-8060-457a-9c16-000000000623
-----

+++++

.....
"Boushh"
-----
ff4fb461-8060-457a-9c16-000000000624
-----

+++++

.....
Wedge Antilles
-----
ff4fb461-8060-457a-9c16-000000000625
-----

+++++

.....
Red Five
-----
ff4fb461-8060-457a-9c16-000000000626
-----

+++++

.....
Secret Hideout
-----
ff4fb461-8060-457a-9c16-000000000627
-----

+++++

.....
Command Center
-----
ff4fb461-8060-457a-9c16-000000000628
-----

+++++

.....
Entrenched Position
-----
ff4fb461-8060-457a-9c16-000000000629
-----

+++++

.....
Rebel Honor Guard
-----
ff4fb461-8060-457a-9c16-000000000630
-----

+++++

.....
Rigged to Explode
-----
ff4fb461-8060-457a-9c16-000000000631
-----

+++++

.....
The Force Is Strong
-----
ff4fb461-8060-457a-9c16-000000000632
-----

+++++

.....
Run Luke&#33; Run&#33;
-----
ff4fb461-8060-457a-9c16-000000000633
-----

+++++

.....
Premonitions of the Future
-----
ff4fb461-8060-457a-9c16-000000000634
-----

+++++

.....
Evading Pursuit
-----
ff4fb461-8060-457a-9c16-000000000635
-----

+++++

.....
Change of Plan
-----
ff4fb461-8060-457a-9c16-000000000636
-----

+++++

.....
Heroes and Legends
-----
ff4fb461-8060-457a-9c16-000000000637
-----

+++++
R0:BringToPlayTarget-Targeted-fromHand$$ReturnTarget-Targeted
.....
Kyle Katarn
-----
ff4fb461-8060-457a-9c16-000000000638
-----
onPlay:Put1Focus-DemiAutoTargeted-atUnit-isCommited||onPlay:Remove1Focus-DemiAutoTargeted-atUnit-isCommited-isReact
+++++

.....
Kyle Katarn
-----
ff4fb461-8060-457a-9c16-000000000639
-----
onPlay:Put1Focus-DemiAutoTargeted-atUnit-isCommited||onPlay:Remove1Focus-DemiAutoTargeted-atUnit-isCommited-isReact
+++++

.....
Ataru Training
-----
ff4fb461-8060-457a-9c16-000000000640
-----
Placement:Force User||whileInPlay:DestroyTarget-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-foreachDefenderEdgeWin-ifOrigDefending-ifEdgeDiffge2-isReact||whileInPlay:DestroyTarget-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-foreachAttackerEdgeWin-ifOrigAttacking-ifEdgeDiffge2-isReact
+++++

.....
Rahn's Guidance
-----
ff4fb461-8060-457a-9c16-000000000641
-----

+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000000642
-----
onResolveFate:CommitTarget-Targeted-atUnit-isNotCommited||UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
Forward Reconnaissance
-----
ff4fb461-8060-457a-9c16-000000000643
-----

+++++

.....
Jan Ors
-----
ff4fb461-8060-457a-9c16-000000000644
-----
onStrike:ReturnTarget-Targeted-atUnit-targetAllied-onlyOnce-isReact$$Remove1Focus
+++++

.....
Intel Operative
-----
ff4fb461-8060-457a-9c16-000000000645
-----
onLeaving:Draw1Card-isReact
+++++

.....
Intel Operative
-----
ff4fb461-8060-457a-9c16-000000000646
-----
onLeaving:Draw1Card-isReact
+++++

.....
Safe House
-----
ff4fb461-8060-457a-9c16-000000000647
-----
whileInPlay:Remove1Focus-foreachForceStruggleLight-isReact
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000000648
-----
onResolveFate:CustomScript
+++++

.....
The False Report
-----
ff4fb461-8060-457a-9c16-000000000649
-----
onPlay:ReturnMulti-AutoTargeted-atUnit-isReact
+++++

.....
Aquaris Freeholders
-----
ff4fb461-8060-457a-9c16-000000000650
-----

+++++

.....
Aquaris Freeholders
-----
ff4fb461-8060-457a-9c16-000000000651
-----

+++++

.....
Clearing House
-----
ff4fb461-8060-457a-9c16-000000000652
-----

+++++

.....
Outmaneuver
-----
ff4fb461-8060-457a-9c16-000000000653
-----
onPlay:ReturnTarget-Targeted-atUnit-targetMine$$ReturnTarget-Targeted-atUnit-targetOpponents
+++++

.....
Slicing In
-----
ff4fb461-8060-457a-9c16-000000000654
-----

+++++

.....
Scouring the Empire
-----
ff4fb461-8060-457a-9c16-000000000655
-----

+++++

.....
Jerec
-----
ff4fb461-8060-457a-9c16-000000000656
-----
onStrike:UncommitTarget-DemiAutoTargeted-atUnit-isCommited-isReact
+++++

.....
Imperial Inquisitor
-----
ff4fb461-8060-457a-9c16-000000000657
-----

+++++
R0:Remove1Focus
.....
Imperial Inquisitor
-----
ff4fb461-8060-457a-9c16-000000000658
-----

+++++
R0:Remove1Focus
.....
Force Storm
-----
ff4fb461-8060-457a-9c16-000000000659
-----

+++++
onPlay:Put2Damage-AutoTargeted-atUnit-isNotCommited
.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000000660
-----
onResolveFate:CommitTarget-Targeted-atUnit-isNotCommited||UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
The Dark Trooper Project
-----
ff4fb461-8060-457a-9c16-000000000661
-----
afterRefresh:Remove1Focus-AutoTargeted-atUnit-isCommited-targetMine
+++++

.....
General Mohc
-----
ff4fb461-8060-457a-9c16-000000000662
-----
whileInPlay:IncreaseBD:1-forMe-typeUnit-isCommited
+++++

.....
Phase I Dark Trooper
-----
ff4fb461-8060-457a-9c16-000000000663
-----
onPlay:CommitMyself
+++++

.....
Phase I Dark Trooper
-----
ff4fb461-8060-457a-9c16-000000000664
-----
onPlay:CommitMyself
+++++

.....
Experimental Tech Lab
-----
ff4fb461-8060-457a-9c16-000000000665
-----
whileInPlay:Remove1Focus-foreachForceStruggleDark-isReact
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000666
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Commando Operations
-----
ff4fb461-8060-457a-9c16-000000000667
-----

+++++

.....
General Crix Madine
-----
ff4fb461-8060-457a-9c16-000000000668
-----

+++++
R0:Remove1Focus
.....
Rebel Commando
-----
ff4fb461-8060-457a-9c16-000000000669
-----

+++++

.....
Rebel Commando
-----
ff4fb461-8060-457a-9c16-000000000670
-----

+++++

.....
Adaptive Strategy
-----
ff4fb461-8060-457a-9c16-000000000671
-----
onPlay:SimplyAnnounce{resolve that fate effect again as if that card were in their edge stack}
+++++

.....
Seeds of Decay
-----
ff4fb461-8060-457a-9c16-000000000672
-----
onResolveFate:Put1Focus-DemiAutoTargeted-atUnit-isCommited-hasntMarker{Focus}-choose1
+++++

.....
Against All Odds
-----
ff4fb461-8060-457a-9c16-000000000673
-----

+++++

.....
Dash Rendar
-----
ff4fb461-8060-457a-9c16-000000000674
-----

+++++

.....
Shifty Lookout
-----
ff4fb461-8060-457a-9c16-000000000675
-----

+++++

.....
Holding All the Cards
-----
ff4fb461-8060-457a-9c16-000000000676
-----
onPlay:Draw2Cards$$Draw2Cards-onOpponent
+++++

.....
Holding All the Cards
-----
ff4fb461-8060-457a-9c16-000000000677
-----
onPlay:Draw2Cards$$Draw2Cards-onOpponent
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000678
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Agent of the Emperor
-----
ff4fb461-8060-457a-9c16-000000000679
-----

+++++
R0:Put1Focus-Targetet-atUnit-targetOpponents
.....
Mara Jade
-----
ff4fb461-8060-457a-9c16-000000000680
-----

+++++

.....
Imperial Shadow Guard
-----
ff4fb461-8060-457a-9c16-000000000681
-----

+++++
R0:Remove1Damage-DemiAutoTargeted-atUnit-hasMarker{Damage}-isCommited-choose1-isCost$$Put1Damage
.....
Mara Jade's Lightsaber
-----
ff4fb461-8060-457a-9c16-000000000682
-----
Placement:Force User_or_Force Sensitive||BonusIcons:UD:1
+++++

.....
Sith Library
-----
ff4fb461-8060-457a-9c16-000000000683
-----

+++++

.....
Rage
-----
ff4fb461-8060-457a-9c16-000000000684
-----
onPlay:Remove2Focus-Targeted-atUnit-isCommited
+++++

.....
Victory or Death
-----
ff4fb461-8060-457a-9c16-000000000685
-----

+++++

.....
Victory-class Star Destroyer
-----
ff4fb461-8060-457a-9c16-000000000686
-----
ExtraIcon:BD:2-ifHaveForce
+++++

.....
Victory-class Star Destroyer
-----
ff4fb461-8060-457a-9c16-000000000687
-----
ExtraIcon:BD:2-ifHaveForce
+++++

.....
Political Reliability Observer
-----
ff4fb461-8060-457a-9c16-000000000688
-----
onPlay:CommitTarget-Targeted-atUnit-isNotCommited$$UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
Control Room
-----
ff4fb461-8060-457a-9c16-000000000689
-----

+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000000690
-----
onResolveFate:CommitTarget-Targeted-atUnit-isNotCommited||UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
The Findsman's Intuition
-----
ff4fb461-8060-457a-9c16-000000000691
-----
whileInPlay:Force1Bonus-foreachCardCaptured-ifCapturingObjective
+++++

.....
Zuckuss
-----
ff4fb461-8060-457a-9c16-000000000692
-----
onStrike:CaptureTarget-DemiAutoTargeted-fromDeckOpponents-onTop3Cards-choose1-isReact
+++++

.....
4-LOM
-----
ff4fb461-8060-457a-9c16-000000000693
-----

+++++

.....
Containment Field
-----
ff4fb461-8060-457a-9c16-000000000694
-----

+++++

.....
Springing the Ambush
-----
ff4fb461-8060-457a-9c16-000000000695
-----
onPlay:CaptureTarget-Targeted-atUnit-isCommited
+++++

.....
Pay Out
-----
ff4fb461-8060-457a-9c16-000000000696
-----

+++++
R0:Remove1Focus-AutoTargeted-atObjective_and_Scum and Villainy-targetMine
.....
The Flight of the Crow
-----
ff4fb461-8060-457a-9c16-000000000697
-----
ConstantEffect:Edge1Bonus-AutoTargeted-atUnit_and_Jedi_and_Unique-targetMine-isParticipating-isDistributedEffect
+++++

....
Moldy Crow
-----
ff4fb461-8060-457a-9c16-000000000698
-----

+++++

....
Ruusan Colonist
-----
ff4fb461-8060-457a-9c16-000000000699
-----

+++++

....
Ruusan Colonist
-----
ff4fb461-8060-457a-9c16-000000000700
-----

+++++

....
Valley of the Jedi
-----
ff4fb461-8060-457a-9c16-000000000701
-----
whileInPlay:Remove1Focus-foreachForceStruggleLight-isReact
+++++

....
My Ally Is the Force
-----
ff4fb461-8060-457a-9c16-000000000702
-----
onPlay:DestroyMultiple-AutoTargeted-atUnit-isNotCommited
+++++

....
The Hoth Gambit
-----
ff4fb461-8060-457a-9c16-000000000703
-----
whileInPlay:Force1Bonus-perEveryHoth-AutoTargeted-atObjective_and_Hoth-hasntMarker{Damage}
+++++

....
General Carlist Rieekan
-----
ff4fb461-8060-457a-9c16-000000000704
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough||afterRefresh:Remove1Damage-DemiAutoTargeted-atObjective_and_Hoth-hasMarker{Damage}-choose1-isReact
+++++

....
Echo Base Technician
-----
ff4fb461-8060-457a-9c16-000000000705
-----

+++++

....
Tauntaun
-----
ff4fb461-8060-457a-9c16-000000000706
-----

+++++

....
Snowspeeder Counterattack
-----
ff4fb461-8060-457a-9c16-000000000707
-----
onPlay:Put1Damage-AutoTargeted-atObjective_and_Hoth-targetMine-isCost$$Put1Damage-perEveryHoth_and_Objective-DemiAutoTargeted-atUnit-targetOpponents-choose1
+++++

....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000708
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

....
Along the Gamor Run
-----
ff4fb461-8060-457a-9c16-000000000709
-----

+++++

....
Hyperspace Marauder
-----
ff4fb461-8060-457a-9c16-000000000710
-----
whileInPlay:Retrieve1Card-grabUnit-hasProperty{Cost}le1-toTable-foreachForceStruggleLight-isReact
+++++

....
Hired Hands
-----
ff4fb461-8060-457a-9c16-000000000711
-----
whileInPlay:SacrificeMyself-foreachForceStruggleDark-isReact-isForced
+++++

....
Hired Hands
-----
ff4fb461-8060-457a-9c16-000000000712
-----
whileInPlay:SacrificeMyself-foreachForceStruggleDark-isReact-isForced
+++++

....
Deneba Refueling Station
-----
ff4fb461-8060-457a-9c16-000000000713
-----
whileInPlay:Remove1Focus-foreachForceStruggleLight-isReact
+++++

....
Make Your Own Luck
-----
ff4fb461-8060-457a-9c16-000000000714
-----
onPlay:RequestInt-Msg{How many Force icons does target unit currently have?}&&CreateDummy||whileInPlay:Force1Bonus-perX-onlyforDummy||afterPhase:DestroyMyself-onlyforDummy-isSilent
+++++

....
The Plan of the Prophetess
-----
ff4fb461-8060-457a-9c16-000000000715
-----

+++++

....
Sariss
-----
ff4fb461-8060-457a-9c16-000000000716
-----
onCommit:CommitTarget-DemiAutoTargeted-atUnit-isNotCommited-targetOpponents-choose1-isReact
+++++

....
Servant of the Dark Side
-----
ff4fb461-8060-457a-9c16-000000000717
-----

+++++

....
Dark Temple
-----
ff4fb461-8060-457a-9c16-000000000718
-----
whileInPlay:Remove1Focus-foreachForceStruggleDark-isReact
+++++

....
Deadly Sight
-----
ff4fb461-8060-457a-9c16-000000000719
-----

+++++

....
Seeds of Decay
-----
ff4fb461-8060-457a-9c16-000000000720
-----
onResolveFate:Put1Focus-DemiAutoTargeted-atUnit-isCommited-hasntMarker{Focus}-choose1
+++++

....
The Slave Trade
-----
ff4fb461-8060-457a-9c16-000000000721
-----
whileInPlay:CaptureTarget-AutoTargeted-fromTopDeckOpponents-captureOnMyself-foreachForceStruggleDark-isReact||whileInPlay:RescueTarget-Targeted-isCapturedCurrentObjective-isRandom-foreachForceStruggleLight-isReact-isForced
+++++

....
Zygerrian Slaver
-----
ff4fb461-8060-457a-9c16-000000000722
-----

+++++

....
Galactic Scum
-----
ff4fb461-8060-457a-9c16-000000000723
-----
whileInPlay:Put1Damage-foreachForceStruggleLight-isReact-isForced
+++++

....
Galactic Scum
-----
ff4fb461-8060-457a-9c16-000000000724
-----
whileInPlay:Put1Damage-foreachForceStruggleLight-isReact-isForced
+++++

....
Slaver Holding Cells
-----
ff4fb461-8060-457a-9c16-000000000725
-----
whileInPlay:Remove1Focus-foreachForceStruggleDark-isReact
+++++

....
Relentless Pursuit
-----
ff4fb461-8060-457a-9c16-000000000726
-----
onPlay:SimplyAnnounce{look at opponent's deck and capture copy of revealed captured card}
+++++

....
May the Force Be With You
-----
ff4fb461-8060-457a-9c16-000000000727
-----

+++++
R0:Remove999Focus-Targeted-targetMine
.....
Yoda
-----
ff4fb461-8060-457a-9c16-000000000728
-----
onStrike:RequestInt-Msg{What is the value of the Death Star Dial?}$$Put1Weapon Mastery:UD-perX-AutoTargeted-atYoda-isSilent||afterConflict:Remove999Weapon Mastery:UD-AutoTargeted-hasMarker{Weapon Mastery:UD}-isSilent
+++++

.....
Dagobah Nudj
-----
ff4fb461-8060-457a-9c16-000000000729
-----
onPlay:Lose1Dial-isReact||onLeaving:Gain1Dial-isReact-isForced
+++++

.....
Dagobah Training Grounds
-----
ff4fb461-8060-457a-9c16-000000000730
-----

+++++

.....
Yoda, You Seek Yoda
-----
ff4fb461-8060-457a-9c16-000000000731
-----
onPlay:Retrieve1Card-grabYoda-toTable$$Gain1Dial$$ShuffleDeck
+++++

.....
Seeds of Decay
-----
ff4fb461-8060-457a-9c16-000000000732
-----
onResolveFate:Put1Focus-DemiAutoTargeted-atUnit-isCommited-hasntMarker{Focus}-choose1
+++++

.....
Behind Enemy Lines
-----
ff4fb461-8060-457a-9c16-000000000733
-----

+++++

.....
Winter
-----
ff4fb461-8060-457a-9c16-000000000734
-----
whileInPlay:Put1Destination:Command Deck-DemiAutoTargeted-atEnhancement-targetOpponents-choose1-foreachForceStruggleLight-isReact-isSilent
+++++

.....
Tactical Genius
-----
ff4fb461-8060-457a-9c16-000000000735
-----
onPlay:Remove1Focus-DemiAutoTargeted-atUnit-isCommited-targetMine-isReact
+++++

.....
Observation Point
-----
ff4fb461-8060-457a-9c16-000000000736
-----

+++++

.....
Hidden Outpost
-----
ff4fb461-8060-457a-9c16-000000000737
-----

+++++

.....
Infiltration
-----
ff4fb461-8060-457a-9c16-000000000738
-----
onPlay:BringToPlayTarget-Targeted-atCharacter-fromHand||whileInPlay:Put1Secret Guardian-foreachCardPlayed-onTriggerCard-typeCharacter-isSilent
+++++

.....
The Second Phase
-----
ff4fb461-8060-457a-9c16-000000000739
-----
whileInPlay:Reduce1CostPlay-affectsUnit_and_Sith-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeCapital Ship-onlyforDummy-isSilent
+++++
R0:SimplyAnnounce{damage it in order to reduce the cost of the next Sith unit they play this phase by 1}$$CreateDummy-nonUnique-isSilent-doNotDiscard$$Deal1Damage-isSilent-onlyOnce
.....
Dark Trooper Legion
-----
ff4fb461-8060-457a-9c16-000000000740
-----

+++++

.....
Dark Trooper Legion
-----
ff4fb461-8060-457a-9c16-000000000741
-----

+++++

.....
Force Shield
-----
ff4fb461-8060-457a-9c16-000000000742
-----
Placement:Objective_and_Sith||onHostObjectiveThwarted-Draw2Cards-isReact
+++++

.....
Facility Repair
-----
ff4fb461-8060-457a-9c16-000000000743
-----
onPlay:Remove1Damage-Targeted-atObjective_and_Sith-hasMarker{Damage}-isReact$$Put1Shield-Targeted-atObjective_and_Sith
+++++

.....
Consumed by the Dark Side
-----
ff4fb461-8060-457a-9c16-000000000744
-----
onPlay:Remove1Damage-AutoTargeted-atObjective-hasMarker{Damage}-targetMine-isReact
+++++

.....
Reinforcements
-----
ff4fb461-8060-457a-9c16-000000000745
-----
onPlay:Retrieve1Card-grabUnit_and_Imperial Navy-fromDiscard-isTopmost-toTable-isReact
+++++

.....
Reserve Troopers
-----
ff4fb461-8060-457a-9c16-000000000746
-----

+++++

.....
Reserve Troopers
-----
ff4fb461-8060-457a-9c16-000000000747
-----

+++++

.....
Security Checkpoint
-----
ff4fb461-8060-457a-9c16-000000000748
-----
whileInPlay:Edge1Bonus-perEveryUnit-AutoTargeted-atUnit-isCommited-targetMine-isParticipating-isDistributedEffect
+++++

.....
Award Ceremony
-----
ff4fb461-8060-457a-9c16-000000000749
-----
onPlay:BringtoPlayTarget-DemiAutoTargeted-atCharacter_and_Imperial Navy-fromHand-isReact
+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000000750
-----
onResolveFate:CommitTarget-Targeted-atUnit-isNotCommited||UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
The Scavengers
-----
ff4fb461-8060-457a-9c16-000000000751
-----
onPlay:DestroyMultiple-AutoTargeted-atUnit-isReact
+++++

.....
Wittin
-----
ff4fb461-8060-457a-9c16-000000000752
-----
whileInPlay:SimplyAnnounce{remove Wittin from the force}-foreachForceStruggleLight-isReact-isForced
+++++

.....
Jawa Scrap Dealers
-----
ff4fb461-8060-457a-9c16-000000000753
-----

+++++

.....
Jawa Scrap Dealers
-----
ff4fb461-8060-457a-9c16-000000000754
-----

+++++

.....
Watchful Eyes
-----
ff4fb461-8060-457a-9c16-000000000755
-----

+++++

.....
Seeds of Decay
-----
ff4fb461-8060-457a-9c16-000000000756
-----
onResolveFate:Put1Focus-DemiAutoTargeted-atUnit-isCommited-hasntMarker{Focus}-choose1
+++++

.....
Ties of Blood
-----
ff4fb461-8060-457a-9c16-000000000757
-----

+++++

.....
Leia Organa
-----
ff4fb461-8060-457a-9c16-000000000758
-----
afterConflict:Deal1Damage-AutoTargeted-atUnit-targetOpponents-isReady-duringOpponentTurn-isReact
+++++

.....
Ewok Companion
-----
ff4fb461-8060-457a-9c16-000000000759
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Native Support
-----
ff4fb461-8060-457a-9c16-000000000760
-----

+++++

.....
Leia's Command
-----
ff4fb461-8060-457a-9c16-000000000761
-----
onPlay:Deal1Damage-AutoTargeted-atObjective_or_Unit-isReady-targetOpponents-isReact
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000000762
-----
onResolveFate:Put1Shield-Targeted-atUnit_or_Objective
+++++

.....
Green Squadron Deployment
-----
ff4fb461-8060-457a-9c16-000000000763
-----

+++++

.....
Liberty
-----
ff4fb461-8060-457a-9c16-000000000764
-----

+++++

.....
Green Squadron A-Wing
-----
ff4fb461-8060-457a-9c16-000000000765
-----
onLeaving:Put1Destination:Command Deck-DemiAutoTargeted-atEvent-fromDiscard-isReact$$ShuffleDeck
+++++

.....
Rebel Fighter Bay
-----
ff4fb461-8060-457a-9c16-000000000766
-----

+++++

.....
Evasive Maneuvers
-----
ff4fb461-8060-457a-9c16-000000000767
-----
onPlay:ReturnTarget-Targeted-atVehicle-isReact
+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000000768
-----
onResolveFate:CommitTarget-Targeted-atUnit-isNotCommited||UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
A Wookiee's Journey
-----
ff4fb461-8060-457a-9c16-000000000769
-----

+++++

.....
Lowhhrick
-----
ff4fb461-8060-457a-9c16-000000000770
-----
whileInPlay:IncreaseBD:1-forMe-typeWookiee
+++++

.....
Loyal Wookiee
-----
ff4fb461-8060-457a-9c16-000000000771
-----

+++++

.....
Heart of a Wookiee
-----
ff4fb461-8060-457a-9c16-000000000772
-----
Placement:Wookiee_and_Unit
+++++

.....
Faithful Companion
-----
ff4fb461-8060-457a-9c16-000000000773
-----

+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000000774
-----
onResolveFate:CommitTarget-Targeted-atUnit-isNotCommited||UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
The Admiral's Assault
-----
ff4fb461-8060-457a-9c16-000000000775
-----
onPlay:Retrieve1Card-grabFate-fromDiscard-isTopmost
+++++

.....
Admiral Piett
-----
ff4fb461-8060-457a-9c16-000000000776
-----

+++++

.....
Hoth Reinforcements
-----
ff4fb461-8060-457a-9c16-000000000777
-----

+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000778
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000000779
-----
onResolveFate:Deal1Damage-Targeted-atObjective_and_Hoth-targetOpponents-noTargetingError||onResolveFate:Remove1Damage-Targeted-atObjective_and_Hoth-targetAllied-noTargetingError
+++++

.....
Seeds of Decay
-----
ff4fb461-8060-457a-9c16-000000000780
-----
onResolveFate:Put1Focus-DemiAutoTargeted-atUnit-isCommited-hasntMarker{Focus}-choose1
+++++

.....
The Droid's Task
-----
ff4fb461-8060-457a-9c16-000000000781
-----
afterRefresh:Lose1Reserves-duringMyTurn-isReact$$Put1Activation-isSilent$$Deal1Damage-AutoTargeted-atUnit-isCommited-choose1-targetOpponents||afterDraw:Remove1Activation-duringMyTurn-isCost-isSilent$$Gain1Reserves
+++++

.....
IG-88
-----
ff4fb461-8060-457a-9c16-000000000782
-----

+++++

.....
Reprogrammed DRK-1 Droid
-----
ff4fb461-8060-457a-9c16-000000000783
-----

+++++

.....
Reprogrammed DRK-1 Droid
-----
ff4fb461-8060-457a-9c16-000000000784
-----

+++++

.....
Sonic Detonation
-----
ff4fb461-8060-457a-9c16-000000000785
-----

+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000000786
-----
onResolveFate:CommitTarget-Targeted-atUnit-isNotCommited||UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
A Deep Commitment
-----
ff4fb461-8060-457a-9c16-000000000787
-----
+++++

.....
Ferus Olin
-----
ff4fb461-8060-457a-9c16-000000000788
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++
R0:Remove1Shield-isCost$$SimplyAnnounce{cancel the effects of the event card}$$Put1Effects Cancelled-DemiAutoTargeted-atEvent-isReady-choose1-isSilent
.....
ET-74 Communications Droid
-----
ff4fb461-8060-457a-9c16-000000000789
-----
+++++

.....
ET-74 Communications Droid
-----
ff4fb461-8060-457a-9c16-000000000790
-----
+++++

.....
Asteroid Base
-----
ff4fb461-8060-457a-9c16-000000000791
-----

+++++
R0:Remove1Shield-Targeted$$Put1Crossfire:UD-Targeted-atUnit||R0:Remove1Shield-Targeted$$Put1Crossfire:BD-Targeted-atUnit
.....
Force Barrier
-----
ff4fb461-8060-457a-9c16-000000000792
-----
onPlay:Put1Shield-AutoTargeted-atUnit_or_Objective-isMine-hasntMarker{Shield}
+++++

.....
Impersonating a Deity
-----
ff4fb461-8060-457a-9c16-000000000793
-----
onPlay:Retrieve1Card-grabUnit_and_Ewok-hasProperty{Cost}le3-toTable-isReact$$Put1Focus-isCost$$ShuffleDeck
+++++

.....
C-3PO
-----
ff4fb461-8060-457a-9c16-000000000794
-----
whileInPlay:Draw1Card-foreachEdgeWin-ifOrigEdgeWinner-isReact
+++++

.....
Ewok Lookout
-----
ff4fb461-8060-457a-9c16-000000000795
-----
+++++

.....
Ewok Lookout
-----
ff4fb461-8060-457a-9c16-000000000796
-----
+++++

.....
Rash Action
-----
ff4fb461-8060-457a-9c16-000000000797
-----
+++++

.....
Seeds of Decay
-----
ff4fb461-8060-457a-9c16-000000000798
-----
onResolveFate:Put1Focus-DemiAutoTargeted-atUnit-isCommited-hasntMarker{Focus}-choose1
+++++

.....
The Call of the Cult
-----
ff4fb461-8060-457a-9c16-000000000799
-----
+++++

.....
Cularin Cultist
-----
ff4fb461-8060-457a-9c16-000000000800
-----
+++++

.....
Believer Initiate
-----
ff4fb461-8060-457a-9c16-000000000801
-----
whileInPlay:SacrificeMyself-foreachForceStruggleLight-isReact-isForced
+++++

.....
Believer Initiate
-----
ff4fb461-8060-457a-9c16-000000000802
-----
whileInPlay:SacrificeMyself-foreachForceStruggleLight-isReact-isForced
+++++

.....
Hate
-----
ff4fb461-8060-457a-9c16-000000000803
-----
Placement:Character||onPlay:Put1Effects Cancelled-AutoTargeted-onHost
+++++

.....
Hate
-----
ff4fb461-8060-457a-9c16-000000000804
-----
Placement:Character||onPlay:Put1Effects Cancelled-AutoTargeted-onHost
+++++

.....
Superior Numbers
-----
ff4fb461-8060-457a-9c16-000000000805
-----
onPlay:Retrieve1Card-grabUnit_and_Fighter-hasProperty{Cost}le2-toTable$$ShuffleDeck
+++++

.....
Escort Carrier
-----
ff4fb461-8060-457a-9c16-000000000806
-----

+++++

.....
TIE Scout
-----
ff4fb461-8060-457a-9c16-000000000807
-----
onStrike:Remove1Shield-DemiAutoTargeted-sourceAny-hasMarker{Shield}-targetOpponents-choose1-isReact
+++++

.....
TIE Scout
-----
ff4fb461-8060-457a-9c16-000000000808
-----
onStrike:Remove1Shield-DemiAutoTargeted-sourceAny-hasMarker{Shield}-targetOpponents-choose1-isReact
+++++

.....
Precision Flying
-----
ff4fb461-8060-457a-9c16-000000000809
-----
Placement:Fighter_and_Unit||ConstantEffect:Edge2Bonus-onHost
+++++

.....
Precision Flying
-----
ff4fb461-8060-457a-9c16-000000000810
-----
Placement:Fighter_and_Unit||ConstantEffect:Edge2Bonus-onHost
+++++

.....
The Slimiest Scheme
-----
ff4fb461-8060-457a-9c16-000000000811
-----

+++++
R0:Put1Focus-isCost$$ReturnTarget-DemiAutoTargeted-atScum and Villainy_and_Unit-targetMine-choose1

.....
Salacious B. Crumb
-----
ff4fb461-8060-457a-9c16-000000000812
-----
onPlay:Remove1Focus-DemiAutoTargeted-atCharacter-targetMine-hasMarker{Focus}-choose1-isReact
+++++

.....
Palace Security
-----
ff4fb461-8060-457a-9c16-000000000813
-----
onPlay:Remove1Damage-DemiAutoTargeted-atObjective_and_Scum and Villainy-targetMine-choose1-isReact
+++++

.....
Palace Security
-----
ff4fb461-8060-457a-9c16-000000000814
-----
onPlay:Remove1Damage-DemiAutoTargeted-atObjective_and_Scum and Villainy-targetMine-choose1-isReact
+++++

.....
Prized Possession
-----
ff4fb461-8060-457a-9c16-000000000815
-----
+++++

.....
Chain Reaction
-----
ff4fb461-8060-457a-9c16-000000000816
-----
+++++

.....
A Hero's Trial
-----
ff4fb461-8060-457a-9c16-000000000817
-----

+++++

.....
Luke Skywalker
-----
ff4fb461-8060-457a-9c16-000000000818
-----
whileInPlay:Deal1Damage-DemiAutoTargeted-atUnit-targetOpponents-choose1-foreachCardPlayed-byMe-typeEnhancement-ifHostLuke Skywalker-isReact-onlyOnce
+++++
R0:DiscardCard-DemiAutoTargeted-atEnhancement-ifHostLuke Skywalker-choose1-isCost$$Remove1Focus-AutoTargeted-atLuke Skywalker

.....
Speeder Bike
-----
ff4fb461-8060-457a-9c16-000000000819
-----
ConstantEffect:Edge1Bonus||whileInPlay:DestroyMyself-foreachEdgeWin-ifOrigEdgeLoser-ifOrigParticipating-isReact-isForced
+++++

.....
Luke's Lightsaber
-----
ff4fb461-8060-457a-9c16-000000000820
-----
Placement:Force User_or_Force Sensitive||BonusIcons:UD:1, EE-UD:1
+++++

.....
I Am a Jedi
-----
ff4fb461-8060-457a-9c16-000000000821
-----
Placement:Force User
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000822
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
The Home of the Master
-----
ff4fb461-8060-457a-9c16-000000000823
-----

+++++

.....
Yoda
-----
ff4fb461-8060-457a-9c16-000000000824
-----
ExtraIcon:EE-T:1-perEveryObjective-AutoTargeted-atObjective_and_Jedi
+++++

.....
Bogwing
-----
ff4fb461-8060-457a-9c16-000000000825
-----
ExtraIcon:UD:1-perEveryObjective-AutoTargeted-atObjective_and_Jedi-div3
+++++

.....
Yoda's Hut
-----
ff4fb461-8060-457a-9c16-000000000826
-----
ConstantEffect:Force2Bonus-perEveryObjective-AutoTargeted-atObjective_and_Jedi-div3
+++++

.....
Lightsaber Deflection
-----
ff4fb461-8060-457a-9c16-000000000827
-----
onPlay:Transfer1Damage-Targeted-atUnit-sourceUnit_and_nonVehicle-targetMine-hasMarker{Damage}-destinationUnit
+++++

.....
The Jedi's Resolve
-----
ff4fb461-8060-457a-9c16-000000000828
-----

+++++

.....
Following Fate
-----
ff4fb461-8060-457a-9c16-000000000829
-----

+++++

.....
Obi-Wan Kenobi
-----
ff4fb461-8060-457a-9c16-000000000830
-----

+++++

.....
R2-D2
-----
ff4fb461-8060-457a-9c16-000000000831
-----

+++++

.....
Obi-Wan's Lightsaber
-----
ff4fb461-8060-457a-9c16-000000000832
-----
Placement:Force User||onHostParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Noble Sacrifice
-----
ff4fb461-8060-457a-9c16-000000000833
-----

+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000834
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Journey Through the Swamp
-----
ff4fb461-8060-457a-9c16-000000000835
-----
onPlay:Retrieve1Card-grabCreature-hasProperty{Cost}le3-toTable-isReact$$Put1Focus-isCost$$ShuffleDeck
+++++

.....
Jubba Bird
-----
ff4fb461-8060-457a-9c16-000000000836
-----

+++++

.....
Jubba Bird
-----
ff4fb461-8060-457a-9c16-000000000837
-----

+++++

.....
Knobby White Spider
-----
ff4fb461-8060-457a-9c16-000000000838
-----

+++++

.....
Life Creates It
-----
ff4fb461-8060-457a-9c16-000000000839
-----

+++++

.....
Size Matters Not
-----
ff4fb461-8060-457a-9c16-000000000840
-----

+++++

.....
Sacrifice on Endor
-----
ff4fb461-8060-457a-9c16-000000000841
-----

+++++

.....
Ewok Hunter
-----
ff4fb461-8060-457a-9c16-000000000842
-----
onPlay:Draw1Card-isReact||onLeaving:Draw1Card-isReact
+++++

.....
Ewok Hunter
-----
ff4fb461-8060-457a-9c16-000000000843
-----
onPlay:Draw1Card-isReact||onLeaving:Draw1Card-isReact
+++++

.....
Funeral Pyre
-----
ff4fb461-8060-457a-9c16-000000000844
-----

+++++

.....
Unexpected Help
-----
ff4fb461-8060-457a-9c16-000000000845
-----

+++++

.....
Retreat into the Forest
-----
ff4fb461-8060-457a-9c16-000000000846
-----

+++++

.....
Raiding Party
-----
ff4fb461-8060-457a-9c16-000000000847
-----

+++++

.....
Lieutenant Judder Page
-----
ff4fb461-8060-457a-9c16-000000000848
-----

+++++

.....
Page's Commandos
-----
ff4fb461-8060-457a-9c16-000000000849
-----

+++++

.....
Page's Commandos
-----
ff4fb461-8060-457a-9c16-000000000850
-----

+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000851
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000852
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Calling in Favors
-----
ff4fb461-8060-457a-9c16-000000000853
-----

+++++

.....
Talon Karrde
-----
ff4fb461-8060-457a-9c16-000000000854
-----

+++++

.....
Skipray Blastboat
-----
ff4fb461-8060-457a-9c16-000000000855
-----
onStrike:Put1Focus-isForced
+++++

.....
Skipray Blastboat
-----
ff4fb461-8060-457a-9c16-000000000856
-----
onStrike:Put1Focus-isForced
+++++

.....
Dirty Secrets
-----
ff4fb461-8060-457a-9c16-000000000857
-----

+++++

.....
Cunning Ploy
-----
ff4fb461-8060-457a-9c16-000000000858
-----

+++++

.....
"No Disintegrations"
-----
ff4fb461-8060-457a-9c16-000000000859
-----

+++++

.....
Boba Fett
-----
ff4fb461-8060-457a-9c16-000000000860
-----

+++++

.....
Freelance Hunter
-----
ff4fb461-8060-457a-9c16-000000000861
-----

+++++

.....
Flamethrower
-----
ff4fb461-8060-457a-9c16-000000000862
-----

+++++

.....
Prized Possession
-----
ff4fb461-8060-457a-9c16-000000000863
-----

+++++

.....
Entangled
-----
ff4fb461-8060-457a-9c16-000000000864
-----

+++++

.....
Masterful Manipulation
-----
ff4fb461-8060-457a-9c16-000000000865
-----

+++++

.....
Prince Xizor
-----
ff4fb461-8060-457a-9c16-000000000866
-----

+++++

.....
Black Sun Headhunter
-----
ff4fb461-8060-457a-9c16-000000000867
-----
afterDraw:SimplyAnnounce{Pay 1 Scum resource or destroy it}-duringMyTurn-isReact-isForced||onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Debt Collector
-----
ff4fb461-8060-457a-9c16-000000000868
-----

+++++

.....
Shadows of the Empire
-----
ff4fb461-8060-457a-9c16-000000000869
-----

+++++

.....
The Prince&#39;s Scheme
-----
ff4fb461-8060-457a-9c16-000000000870
-----

+++++

.....
All Out Brawl
-----
ff4fb461-8060-457a-9c16-000000000871
-----

+++++

.....
Zekka Thyne
-----
ff4fb461-8060-457a-9c16-000000000872
-----
onLeaving:SimplyAnnounce{Destroy each other unit in play}-isReact-isForced
+++++

.....
Debt Collector
-----
ff4fb461-8060-457a-9c16-000000000873
-----

+++++

.....
Armed to the Teeth
-----
ff4fb461-8060-457a-9c16-000000000874
-----

+++++

.....
Entangled
-----
ff4fb461-8060-457a-9c16-000000000875
-----

+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000876
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
The Best That Credits Can Buy
-----
ff4fb461-8060-457a-9c16-000000000877
-----

+++++

.....
Virago
-----
ff4fb461-8060-457a-9c16-000000000878
-----

+++++

.....
Black Sun Headhunter
-----
ff4fb461-8060-457a-9c16-000000000879
-----
afterDraw:SimplyAnnounce{Pay 1 Scum resource or destroy it}-duringMyTurn-isReact-isForced||onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Rise of the Black Sun
-----
ff4fb461-8060-457a-9c16-000000000880
-----

+++++

.....
Warning Shot
-----
ff4fb461-8060-457a-9c16-000000000881
-----
onPlay:Deal1Damage-Targeted-atVehicle
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000882
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
The Hunters
-----
ff4fb461-8060-457a-9c16-000000000883
-----

+++++

.....
Boushh
-----
ff4fb461-8060-457a-9c16-000000000884
-----

+++++

.....
Snoova
-----
ff4fb461-8060-457a-9c16-000000000885
-----

+++++

.....
A Better Offer
-----
ff4fb461-8060-457a-9c16-000000000886
-----

+++++

.....
Pay Out
-----
ff4fb461-8060-457a-9c16-000000000887
-----

+++++
R0:Remove1Focus-AutoTargeted-atObjective_and_Scum and Villainy-targetMine
.....
Show of Force
-----
ff4fb461-8060-457a-9c16-000000000888
-----

+++++

.....
The Investigation
-----
ff4fb461-8060-457a-9c16-000000000889
-----

+++++

.....
Ysanne Isard
-----
ff4fb461-8060-457a-9c16-000000000890
-----

+++++

.....
Officer of Imperial Intelligence
-----
ff4fb461-8060-457a-9c16-000000000891
-----

+++++

.....
Officer of Imperial Intelligence
-----
ff4fb461-8060-457a-9c16-000000000892
-----

+++++

.....
Confiscate
-----
ff4fb461-8060-457a-9c16-000000000893
-----

+++++

.....
Official Investigation
-----
ff4fb461-8060-457a-9c16-000000000894
-----

+++++

.....
Family Connections
-----
ff4fb461-8060-457a-9c16-000000000895
-----

+++++

.....
General Tagge
-----
ff4fb461-8060-457a-9c16-000000000896
-----

+++++

.....
Security Task Force
-----
ff4fb461-8060-457a-9c16-000000000897
-----

+++++
R0:Remove1Damage-DemiAutoTargeted-atTrooper-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
Security Task Force
-----
ff4fb461-8060-457a-9c16-000000000898
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atTrooper-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
Imperial Discipline
-----
ff4fb461-8060-457a-9c16-000000000899
-----
+++++

.....
Precision Fire
-----
ff4fb461-8060-457a-9c16-000000000900
-----
+++++

.....
Rogue Squadron Assault
-----
ff4fb461-8060-457a-9c16-000000000901
-----
whileInPlay:Draw1Card-foreachCardPlayed-typeFighter_or_Pilot-forMe-isReact-onlyOnce
+++++


.....
Derek "Hobbie" Klivian
-----
ff4fb461-8060-457a-9c16-000000000902
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1||onLeaving:ReturnMyself-isReact
+++++

.....
Rogue Squadron X-Wing
-----
ff4fb461-8060-457a-9c16-000000000903
-----
+++++
R0:DiscardCard-Targeted-atEnhancement_and_Pilot-isCost$$Remove999Focus$$Remove999Damage

.....
Rogue Squadron X-Wing
-----
ff4fb461-8060-457a-9c16-000000000904
-----
+++++
R0:DiscardCard-Targeted-atEnhancement_and_Pilot-isCost$$Remove999Focus$$Remove999Damage

.....
Pilot Ready Room
-----
ff4fb461-8060-457a-9c16-000000000905
-----
whileInPlay:Reduce1CostPlay-affectsPilot-onlyOnce-forMe
+++++

.....
Stay on Target
-----
ff4fb461-8060-457a-9c16-000000000906
-----
+++++

.....
Memories of Taanab
-----
ff4fb461-8060-457a-9c16-000000000907
-----
+++++

.....
Lando Calrissian
-----
ff4fb461-8060-457a-9c16-000000000908
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
System Patrol Craft
-----
ff4fb461-8060-457a-9c16-000000000909
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atObjective_and_Smugglers and Spies-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
System Patrol Craft
-----
ff4fb461-8060-457a-9c16-000000000910
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atObjective_and_Smugglers and Spies-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
Conner Net
-----
ff4fb461-8060-457a-9c16-000000000911
-----
+++++

.....
A Little Maneuver
-----
ff4fb461-8060-457a-9c16-000000000912
-----
+++++

.....
Black Squadron Formation
-----
ff4fb461-8060-457a-9c16-000000000913
-----
+++++
R0:Put1Focus-isCost$$Retrieve1Card-grabBlack Squadron-fromDiscard

.....
"Mauler" Mithel
-----
ff4fb461-8060-457a-9c16-000000000914
-----
onPlay:CustomScript||onPay:Reduce2CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce2
+++++

.....
Black Two
-----
ff4fb461-8060-457a-9c16-000000000915
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atVehicle-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
TIE Advanced
-----
ff4fb461-8060-457a-9c16-000000000916
-----
whileInPlay:Deal1Damage-foreachUnopposedEngagement-onTriggerCard-ifOrigAttacking-ifOrigParticipating-isReact
+++++

.....
Death Star Ready Room
-----
ff4fb461-8060-457a-9c16-000000000917
-----
whileInPlay:Reduce1CostPlay-affectsPilot-onlyOnce-forMe
+++++

.....
Stay on Target
-----
ff4fb461-8060-457a-9c16-000000000918
-----
+++++

.....
The Empire's Elite
-----
ff4fb461-8060-457a-9c16-000000000919
-----
+++++

.....
Baron Fel
-----
ff4fb461-8060-457a-9c16-000000000920
-----
onPlay:CustomScript||onPay:Reduce2CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce2
+++++

.....
181st TIE Interceptor
-----
ff4fb461-8060-457a-9c16-000000000921
-----
+++++

.....
181st TIE Interceptor
-----
ff4fb461-8060-457a-9c16-000000000922
-----
+++++

.....
Flight Academy
-----
ff4fb461-8060-457a-9c16-000000000923
-----
whileInPlay:Reduce1CostPlay-affectsPilot-onlyOnce-forMe
+++++

.....
Stay on Target
-----
ff4fb461-8060-457a-9c16-000000000924
-----
+++++

.....
The Grand Heist
-----
ff4fb461-8060-457a-9c16-000000000925
-----
+++++

.....
Niles Ferrier
-----
ff4fb461-8060-457a-9c16-000000000926
-----
onPlay:CustomScriptonPay:Increase1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxIncrease1
+++++

.....
Novice Starship Thief
-----
ff4fb461-8060-457a-9c16-000000000927
-----
onPlay:DestroyTarget-Targeted-atUnit_and_Vehicle-targetOpponents-hasProperty{Cost}le2
+++++

.....
Novice Starship Thief
-----
ff4fb461-8060-457a-9c16-000000000928
-----
onPlay:DestroyTarget-Targeted-atUnit_and_Vehicle-targetOpponents-hasProperty{Cost}le2
+++++

.....
Pirate Hideout
-----
ff4fb461-8060-457a-9c16-000000000929
-----
+++++

.....
Salvage Operation
-----
ff4fb461-8060-457a-9c16-000000000930
-----
+++++

.....
The Survivors
-----
ff4fb461-8060-457a-9c16-000000000931
-----
+++++
R0:Remove1Damage-Targeted-atUnit_and_Character_and_Jedi_Unique

.....
Qu Rahn
-----
ff4fb461-8060-457a-9c16-000000000932
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atCharacter-hasMarker{Damage}-choose1-isCost$$Put1Damage$$Deal1Damage-DemiAutoTargeted-atObjective-targetOpponents-choose1

.....
Sulon Sympathizer
-----
ff4fb461-8060-457a-9c16-000000000933
-----
+++++

.....
Shien Training
-----
ff4fb461-8060-457a-9c16-000000000934
-----
Placement:Force User
+++++
R0:Put1Focus-isCost$$SimplyAnnounce{transfers damage to target unit}-isReact

.....
Force Rejuvenation
-----
ff4fb461-8060-457a-9c16-000000000935
-----
onPlay:Remove999Focus$$Remove999Damage-Targeted-atCharacter-targetAllied
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000000936
-----
onResolveFate:Put1Shield-Targeted-atUnit_or_Objective
+++++

.....
Called to Arms
-----
ff4fb461-8060-457a-9c16-000000000937
-----
+++++

.....
Gray Squadron Gunner
-----
ff4fb461-8060-457a-9c16-000000000938
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Gray Squadron Y-Wing
-----
ff4fb461-8060-457a-9c16-000000000939
-----
+++++

.....
Advanced Proton Torpedoes
-----
ff4fb461-8060-457a-9c16-000000000940
-----
Placement:Fighter_and_Unit||BonusIcons:BD:1-perEveryUnit-AutoTargeted-atUnit-targetAllied-isParticipating
+++++

.....
Desperation
-----
ff4fb461-8060-457a-9c16-000000000941
-----

+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000942
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
The Daring Escape
-----
ff4fb461-8060-457a-9c16-000000000943
-----
+++++


.....
LE-B02D9
-----
ff4fb461-8060-457a-9c16-000000000944
-----
onPlay:CustomScript||onStrike:DisengageTarget-AutoTargeted-onHost-isReact
+++++

.....
Outrider
-----
ff4fb461-8060-457a-9c16-000000000945
-----
+++++


.....
Spacer Cantina
-----
ff4fb461-8060-457a-9c16-000000000946
-----
whileInPlay:Reduce1CostPlay-affectsPilot-onlyOnce-forMe
+++++

.....
Punch It
-----
ff4fb461-8060-457a-9c16-000000000947
-----
onPlay:SimplyAnnounce{choose a new target for the effect}
+++++

.....
Stay on Target
-----
ff4fb461-8060-457a-9c16-000000000948
-----
+++++

.....
The Emperor's Sword
-----
ff4fb461-8060-457a-9c16-000000000949
-----
+++++

.....
Maarek Stele
-----
ff4fb461-8060-457a-9c16-000000000950
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Delta One
-----
ff4fb461-8060-457a-9c16-000000000951
-----
onStrike:SimplyAnnounce{place 1 focus token on each participating unpiloted enemy Vehicle unit}-isReact
+++++

.....
Advanced Concussion Missiles
-----
ff4fb461-8060-457a-9c16-000000000952
-----
Placement:Fighter_and_Unit||BonusIcons:BD:1-perEveryUnit-AutoTargeted-atUnit-targetOpponents-isParticipating
+++++

.....
Hand of the Emperor
-----
ff4fb461-8060-457a-9c16-000000000953
-----
onPlay:Put1Focus-DemiAutoTargted-atUnit-targetOpponents-isParticipating-choose1||onPay:Reduce1CostPlay-ifDialle4
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000000954
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Guarding the Wing
-----
ff4fb461-8060-457a-9c16-000000000955
-----
+++++

.....
DS-61-3
-----
ff4fb461-8060-457a-9c16-000000000956
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1||DeployAllowance:Conflict
+++++

.....
Black Squadron Fighter
-----
ff4fb461-8060-457a-9c16-000000000957
-----
+++++

.....
Black Squadron Fighter
-----
ff4fb461-8060-457a-9c16-000000000958
-----
+++++

.....
Elite Pilot Training
-----
ff4fb461-8060-457a-9c16-000000000959
-----
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000000960
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Hidden from the Empire
-----
ff4fb461-8060-457a-9c16-000000000961
-----

+++++

.....
Vima-Da-Boda
-----
ff4fb461-8060-457a-9c16-000000000962
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Undercover Urchin
-----
ff4fb461-8060-457a-9c16-000000000963
-----

+++++

.....
Hidden in the Shadows
-----
ff4fb461-8060-457a-9c16-000000000964
-----
Placement:Character
+++++

.....
Hidden in the Shadows
-----
ff4fb461-8060-457a-9c16-000000000965
-----
Placement:Character
+++++

.....
Harassment
-----
ff4fb461-8060-457a-9c16-000000000966
-----
onPlay:SimplyAnnounce{increase the cost of the next unit they play this phase by 1}$$CreateDummy-isSilent-nonUnique-doNotDiscard||Increase1CostPlay-affectsUnit-byOpponent-onlyOnce-onlyforDummy||afterPhase:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Command and Control
-----
ff4fb461-8060-457a-9c16-000000000967
-----

+++++

.....
Independence
-----
ff4fb461-8060-457a-9c16-000000000968
-----
whileInPlay:Reduce1CostPlay-affectsCapital Ship-forMe||onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Corellian Corvette
-----
ff4fb461-8060-457a-9c16-000000000969
-----
onPlay:Draw1Card-isReact
+++++

.....
Corellian Corvette
-----
ff4fb461-8060-457a-9c16-000000000970
-----
onPlay:Draw1Card-isReact
+++++

.....
Resupply Depot
-----
ff4fb461-8060-457a-9c16-000000000971
-----

+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000000972
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
The Questioning
-----
ff4fb461-8060-457a-9c16-000000000973
-----

+++++

.....
Antinnis Tremayne
-----
ff4fb461-8060-457a-9c16-000000000974
-----

+++++

.....
Imperial Enforcers
-----
ff4fb461-8060-457a-9c16-000000000975
-----

+++++

.....
Imperial Enforcers
-----
ff4fb461-8060-457a-9c16-000000000976
-----

+++++

.....
Citadel Inquisitorious
-----
ff4fb461-8060-457a-9c16-000000000977
-----

+++++
R0:Put1Focus-isCost$$Discard1Card-ofAllOpponents-isRandom
.....
Put to the Question
-----
ff4fb461-8060-457a-9c16-000000000978
-----
onPlay:SimplyAnnounce{cancel the effects of the event card}$$Put1Effects Cancelled-Targeted-atEvent-isReady-isSilent
+++++

.....
Training Procedures
-----
ff4fb461-8060-457a-9c16-000000000979
-----

+++++

.....
Academy Pilot
-----
ff4fb461-8060-457a-9c16-000000000980
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Academy Pilot
-----
ff4fb461-8060-457a-9c16-000000000981
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
TIE Fighter Patrol
-----
ff4fb461-8060-457a-9c16-000000000982
-----

+++++

.....
TIE Fighter Patrol
-----
ff4fb461-8060-457a-9c16-000000000983
-----

+++++

.....
Koiogran Turn
-----
ff4fb461-8060-457a-9c16-000000000984
-----
onPlay:SimplyAnnounce{choose a new target for the effect}
+++++

.....
The Eater of Luck
-----
ff4fb461-8060-457a-9c16-000000000985
-----
whileInPlay:-foreachEdgeWin-ifOrigEdgeLoser-CaptureTarget-AutoTargeted-fromTopDeckOpponents-captureOnMyself-isReact
+++++

.....
Dannik Jerriko
-----
ff4fb461-8060-457a-9c16-000000000986
-----

+++++

.....
Advozse Mercenary
-----
ff4fb461-8060-457a-9c16-000000000987
-----

+++++

.....
Advozse Mercenary
-----
ff4fb461-8060-457a-9c16-000000000988
-----

+++++

.....
Calculated Wager
-----
ff4fb461-8060-457a-9c16-000000000989
-----

+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000000990
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
The Secret of Shantipole
-----
ff4fb461-8060-457a-9c16-000000000991
-----
+++++

.....
Keeyan Farlander
-----
ff4fb461-8060-457a-9c16-000000000992
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Blue Nine
-----
ff4fb461-8060-457a-9c16-000000000993
-----
+++++


.....
Temple Hangar
-----
ff4fb461-8060-457a-9c16-000000000994
-----
whileInPlay:Reduce1CostPlay-affectsPilot-onlyOnce-forMe
+++++

.....
Reassignment
-----
ff4fb461-8060-457a-9c16-000000000995
-----
+++++

.....
Stay on Target
-----
ff4fb461-8060-457a-9c16-000000000996
-----
+++++

.....
Running the Trench
-----
ff4fb461-8060-457a-9c16-000000000997
-----
+++++

.....
Luke Skywalker
-----
ff4fb461-8060-457a-9c16-000000000998
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Red Five
-----
ff4fb461-8060-457a-9c16-000000000999
-----
+++++

.....
R2-D2
-----
ff4fb461-8060-457a-9c16-000000001000
-----
+++++

.....
Use the Force, Luke
-----
ff4fb461-8060-457a-9c16-000000001001
-----
+++++

.....
I Have You Now
-----
ff4fb461-8060-457a-9c16-000000001002
-----
+++++

.....
The Smuggler's Gambit
-----
ff4fb461-8060-457a-9c16-000000001003
-----
+++++

.....
Platt Okeefe
-----
ff4fb461-8060-457a-9c16-000000001004
-----
+++++

.....
Information Broker
-----
ff4fb461-8060-457a-9c16-000000001005
-----
+++++

.....
Smuggler's Handbook
-----
ff4fb461-8060-457a-9c16-000000001006
-----
+++++

.....
Evading Authority
-----
ff4fb461-8060-457a-9c16-000000001007
-----
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000001008
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
Defending the Trench
-----
ff4fb461-8060-457a-9c16-000000001009
-----
+++++

.....
Darth Vader
-----
ff4fb461-8060-457a-9c16-000000001010
-----
onPlay:CustomScript||onPay:Reduce2CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce2
+++++

.....
Vader's TIE Advanced
-----
ff4fb461-8060-457a-9c16-000000001011
-----
+++++

.....
Black Squadron Fighter
-----
ff4fb461-8060-457a-9c16-000000001012
-----
+++++

.....
Closed Formation
-----
ff4fb461-8060-457a-9c16-000000001013
-----
+++++

.....
I Have You Now
-----
ff4fb461-8060-457a-9c16-000000001014
-----
+++++

.....
The Hunter's Flight
-----
ff4fb461-8060-457a-9c16-000000001015
-----
+++++

.....
Boba Fett
-----
ff4fb461-8060-457a-9c16-000000001016
-----
onPlay:CustomScript||onPay:Reduce2CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce2
+++++

.....
Slave 1
-----
ff4fb461-8060-457a-9c16-000000001017
-----
+++++

.....
Den of Thieves
-----
ff4fb461-8060-457a-9c16-000000001018
-----
whileInPlay:Reduce1CostPlay-affectsPilot-onlyOnce-forMe
+++++

.....
Bail Out
-----
ff4fb461-8060-457a-9c16-000000001019
-----
+++++

.....
Stay on Target
-----
ff4fb461-8060-457a-9c16-000000001020
-----
+++++

.....
A Hero's Beginning
-----
ff4fb461-8060-457a-9c16-000000001021
-----
+++++

.....
Luke's X-34 Landspeeder
-----
ff4fb461-8060-457a-9c16-000000001022
-----
+++++

.....
Owen Lars
-----
ff4fb461-8060-457a-9c16-000000001023
-----
whileInPlay:Reduce3CostPlay-affectsJedi-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeJedi-onlyforDummy-isSilent
+++++
R0:Put1Destination:Command Deck$$ShuffleDeck$$SimplyAnnounce{reduce the cost of the next Jedi card they play this phase by 3}$$CreateDummy-nonUnique-isSilent-doNotDiscard

.....
Moisture Vaporator
-----
ff4fb461-8060-457a-9c16-000000001024
-----
+++++

.....
Unfinished Business
-----
ff4fb461-8060-457a-9c16-000000001025
-----
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000001026
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
Breaking the Blockade
-----
ff4fb461-8060-457a-9c16-000000001027
-----
+++++

.....
Smuggling Freighter
-----
ff4fb461-8060-457a-9c16-000000001028
-----
+++++

.....
Smuggling Freighter
-----
ff4fb461-8060-457a-9c16-000000001029
-----
+++++

.....
Duros Smuggler
-----
ff4fb461-8060-457a-9c16-000000001030
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Duros Smuggler
-----
ff4fb461-8060-457a-9c16-000000001031
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Surprising Maneuver
-----
ff4fb461-8060-457a-9c16-000000001032
-----
+++++

.....
The Imperial Bureaucracy
-----
ff4fb461-8060-457a-9c16-000000001033
-----
+++++

.....
Sate Pestage
-----
ff4fb461-8060-457a-9c16-000000001034
-----
onPlay:Retrieve1Card-grabUnit_or_Event_or_Fate-fromDiscard-isReact||onLeaving:Retrieve1Card-grabUnit_or_Event_or_Fate-fromDiscard-isReact
+++++

.....
Advisor to the Emperor
-----
ff4fb461-8060-457a-9c16-000000001035
-----
+++++

.....
Quarren Bureaucrat
-----
ff4fb461-8060-457a-9c16-000000001036
-----
+++++

.....
Endless Bureaucracy
-----
ff4fb461-8060-457a-9c16-000000001037
-----
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000001038
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
The Last Grand Admiral
-----
ff4fb461-8060-457a-9c16-000000001039
-----
+++++

.....
Grand Admiral Thrawn
-----
ff4fb461-8060-457a-9c16-000000001040
-----
+++++
R0:Put1Focus-isCost$$Put1Focus-Targeted-atUnit-targetOpponents-onlyDuringEngagement

.....
Noghri Bodyguard
-----
ff4fb461-8060-457a-9c16-000000001041
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atOfficer-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
Noghri Bodyguard
-----
ff4fb461-8060-457a-9c16-000000001042
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atOfficer-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
Chain of Command
-----
ff4fb461-8060-457a-9c16-000000001043
-----
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000001044
-----
onResolveFate:SimplyAnnounce{allow a friendly player to place one nonfate card from their hand into their edge stack}
+++++

.....
Nar Shaddaa Drift
-----
ff4fb461-8060-457a-9c16-000000001045
-----
afterCardRefreshing:Remove1Focus-AutoTargeted-atVehicle-hasMarker{Focus}-choose1-duringMyTurn-targetAllied-isReact
+++++

.....
Race Circuit Champion
-----
ff4fb461-8060-457a-9c16-000000001046
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Racing Swoop
-----
ff4fb461-8060-457a-9c16-000000001047
-----
+++++

.....
Racing Swoop
-----
ff4fb461-8060-457a-9c16-000000001048
-----
+++++

.....
Black Market Exchange
-----
ff4fb461-8060-457a-9c16-000000001049
-----
+++++

.....
Cut Off
-----
ff4fb461-8060-457a-9c16-000000001050
-----
+++++

.....
The Forgotten Masters
-----
ff4fb461-8060-457a-9c16-000000001051
-----

+++++

.....
T'Ra Saa
-----
ff4fb461-8060-457a-9c16-000000001052
-----
+++++

.....
Lost Master
-----
ff4fb461-8060-457a-9c16-000000001053
-----
onPlay:CommitMyself
+++++

.....
Lost Master
-----
ff4fb461-8060-457a-9c16-000000001054
-----
onPlay:CommitMyself
+++++

.....
A Gift From the Past
-----
ff4fb461-8060-457a-9c16-000000001055
-----
onPlay:UncommitTarget-DemiAutoTargeted-atUnit-isCommited-targetMine-choose1&&CommitTarget-DemiAutoTargeted-atUnit-isNotCommited-targetMine-choose1
+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000001056
-----
onResolveFate:CommitTarget-Targeted-atUnit-isNotCommited||UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
Heroes of the Rebellion
-----
ff4fb461-8060-457a-9c16-000000001057
-----
+++++

.....
Tycho Celchu
-----
ff4fb461-8060-457a-9c16-000000001058
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Wes Janson
-----
ff4fb461-8060-457a-9c16-000000001059
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Rogue Six
-----
ff4fb461-8060-457a-9c16-000000001060
-----

+++++

.....
Rogue Nine
-----
ff4fb461-8060-457a-9c16-000000001061
-----

+++++

.....
Ready for Takeoff
-----
ff4fb461-8060-457a-9c16-000000001062
-----
+++++

.....
That Bucket o' Bolts
-----
ff4fb461-8060-457a-9c16-000000001063
-----
+++++

.....
Han Solo
-----
ff4fb461-8060-457a-9c16-000000001064
-----
onPlay:CustomScript||onPay:Reduce2CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce2
+++++

.....
Millennium Falcon
-----
ff4fb461-8060-457a-9c16-000000001065
-----
ConstantEffect:Edge1Bonus
+++++
R0:DisengageMyself-onlyOnce

.....
Well Paid
-----
ff4fb461-8060-457a-9c16-000000001066
-----
onPlay:SimplyAnnounce{reduce the cost and pilot cost of each Pilot and each Vehicle card they play this phase by 1.}$$CreateDummy-nonUnique-doNotDiscard-isSilent||whileInPlay:Reduce1CostPlay-affectsPilot_or_Vehicle-onlyforDummy||afterPhase:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Well Paid
-----
ff4fb461-8060-457a-9c16-000000001067
-----
onPlay:SimplyAnnounce{reduce the cost and pilot cost of each Pilot and each Vehicle card they play this phase by 1.}$$CreateDummy-nonUnique-doNotDiscard-isSilent||whileInPlay:Reduce1CostPlay-affectsPilot_or_Vehicle-onlyforDummy||afterPhase:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000001068
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
The Reawakening
-----
ff4fb461-8060-457a-9c16-000000001069
-----
whileInPlay:Discard1Card-DemiAutoTargeted-fromDeckOpponents-onTop2Cards-choose1-foreachForceStruggleDark-isReact
+++++

.....
Arden Lyn
-----
ff4fb461-8060-457a-9c16-000000001070
-----
+++++


.....
Dark Side Apprentice
-----
ff4fb461-8060-457a-9c16-000000001071
-----
+++++


.....
Return to Darkness
-----
ff4fb461-8060-457a-9c16-000000001072
-----
Placement:Force User_or_Force Sensitive
+++++


.....
Give in to Your Anger
-----
ff4fb461-8060-457a-9c16-000000001073
-----
+++++

.....
Give in to Your Anger
-----
ff4fb461-8060-457a-9c16-000000001074
-----
+++++

.....
Behind the Black Sun
-----
ff4fb461-8060-457a-9c16-000000001075
-----
+++++

.....
Guri
-----
ff4fb461-8060-457a-9c16-000000001076
-----
+++++

.....
Freelance Assassin
-----
ff4fb461-8060-457a-9c16-000000001077
-----
+++++

.....
Hidden Vibroknife
-----
ff4fb461-8060-457a-9c16-000000001078
-----
Placement:Character_or_Droid||BonusIcons:UD:1
+++++

.....
Threat Removal
-----
ff4fb461-8060-457a-9c16-000000001079
-----
onPlay:ReturnTarget-DemiAutoTargeted-atUnit-targetOpponents-isParticipating-choose1
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000001080
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
House Edge
-----
ff4fb461-8060-457a-9c16-000000001081
-----
+++++

.....
Lando Calrissian
-----
ff4fb461-8060-457a-9c16-000000001082
-----

+++++


.....
Herglic Sabacc Addict
-----
ff4fb461-8060-457a-9c16-000000001083
-----
onPlay:SimplyAnnounce{Name a card. Look at opponent's hand and discard all copies of that card.}
+++++

.....
Cloud City Casino
-----
ff4fb461-8060-457a-9c16-000000001084
-----

+++++

.....
Sabacc Shift
-----
ff4fb461-8060-457a-9c16-000000001085
-----

+++++

.....
The Gambler's Trick
-----
ff4fb461-8060-457a-9c16-000000001086
-----

+++++

.....
Debt of Honor
-----
ff4fb461-8060-457a-9c16-000000001087
-----
whileInPlay:Retrieve1Card-grabWookie-fromDiscard-isTopmost-foreachCardLeavingPlay-typeWookie-onlyOnce-isReact
+++++

.....
Chewbacca
-----
ff4fb461-8060-457a-9c16-000000001088
-----
+++++
R0:Put1Shield-DemiAutoTargeted-atUnit-choose2-targetAllied-onlyOnce

.....
Wookie Defender
-----
ff4fb461-8060-457a-9c16-000000001089
-----
ExtraIcon:UD:1-ifOrigHasMarker{Shield}
+++++

.....
Kashyyyk Resistance Hideout
-----
ff4fb461-8060-457a-9c16-000000001090
-----
+++++
R1:Put2Shield-DemiAutoTargeted-atUnit-choose1-targetAllied

.....
Wookie Rage
-----
ff4fb461-8060-457a-9c16-000000001091
-----
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000001092
-----
onResolveFate:Put1Shield-Targeted-atUnit_or_Objective
+++++

.....
Fortune and Fate
-----
ff4fb461-8060-457a-9c16-000000001093
-----

+++++

.....
Lady Luck
-----
ff4fb461-8060-457a-9c16-000000001094
-----
onStrike:SimplyAnnounce{Reveal the top 3 cards of your deck. Discard one of those cards, place one on the bottom of your deck, and place one into your hand}-isReact
+++++

.....
Cloud City Technician
-----
ff4fb461-8060-457a-9c16-000000001095
-----

+++++

.....
Cloud City Technician
-----
ff4fb461-8060-457a-9c16-000000001096
-----

+++++

.....
Central Computer
-----
ff4fb461-8060-457a-9c16-000000001097
-----

+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000001098
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Honor Among Thieves
-----
ff4fb461-8060-457a-9c16-000000001099
-----
whileInPlay:Remove1Focus-foreachCardPlayed-byOpponent-typeEvent-onlyOnce-isReact
+++++

.....
Mirax Terrik
-----
ff4fb461-8060-457a-9c16-000000001100
-----
whileInPlay:Reduce1CostPlay-affectsEvent-onlyOnce-forMe
+++++

.....
Fringer Captain
-----
ff4fb461-8060-457a-9c16-000000001101
-----

+++++

.....
Fringer Captain
-----
ff4fb461-8060-457a-9c16-000000001102
-----

+++++

.....
Special Discount
-----
ff4fb461-8060-457a-9c16-000000001103
-----

+++++

.....
One Last Trick
-----
ff4fb461-8060-457a-9c16-000000001104
-----
onPlay:Put1Focus-Targeted-atUnit
+++++

.....
Renegade Reinforcements
-----
ff4fb461-8060-457a-9c16-000000001105
-----
whileInPlay:IncreaseEE-T:1-foreachUnitStrike-onTriggerCard-typeRenegade Squadron-onlyOnce-isReact
+++++

.....
Corporal Dansra Beezer
-----
ff4fb461-8060-457a-9c16-000000001106
-----

+++++

.....
Renegade Squadron Operative
-----
ff4fb461-8060-457a-9c16-000000001107
-----

+++++

.....
Hidden Backup
-----
ff4fb461-8060-457a-9c16-000000001108
-----
+++++
R1:EngageTarget-Targeted-atUnit-targetMine-isNotParticipating-ifOrigDefending

.....
Directed Fire
-----
ff4fb461-8060-457a-9c16-000000001109
-----

+++++

.....
Last Minute Reinforcements
-----
ff4fb461-8060-457a-9c16-000000001110
-----

+++++

.....
Mysteries of the Rim
-----
ff4fb461-8060-457a-9c16-000000001111
-----
+++++
R0:Put1Focus-DemiAutoTargeted-atJedi_and_Unit-choose1-isCost$$Remove1Focus

.....
Outer Rim Mystic
-----
ff4fb461-8060-457a-9c16-000000001112
-----
+++++
R0:Remove1Focus-DemiAutoTargeted-atUnit-hasMarker{Focus}-choose1-isCost$$Put1Focus

.....
Outer Rim Mystic
-----
ff4fb461-8060-457a-9c16-000000001113
-----
+++++
R0:Remove1Focus-DemiAutoTargeted-atUnit-hasMarker{Focus}-choose1-isCost$$Put1Focus

.....
Niman Training
-----
ff4fb461-8060-457a-9c16-000000001114
-----
Placement:Force User_or_Force Sensitive
+++++

.....
Niman Training
-----
ff4fb461-8060-457a-9c16-000000001115
-----
Placement:Force User_or_Force Sensitive
+++++

.....
Force Illusion
-----
ff4fb461-8060-457a-9c16-000000001116
-----

+++++

.....
Planning the Rescue
-----
ff4fb461-8060-457a-9c16-000000001117
-----

+++++

.....
General Airen Cracken
-----
ff4fb461-8060-457a-9c16-000000001118
-----

+++++

.....
Alliance Infiltrator
-----
ff4fb461-8060-457a-9c16-000000001119
-----

+++++

.....
Superior Intelligence
-----
ff4fb461-8060-457a-9c16-000000001120
-----

+++++

.....
Undercover
-----
ff4fb461-8060-457a-9c16-000000001121
-----
onPlay:Retrieve2Card-fromDiscard-toDeck$$ShuffleDeck$$CaptureMyself
+++++

.....
Rescue Mission
-----
ff4fb461-8060-457a-9c16-000000001122
-----
onPlay:CustomScript
+++++

.....
The Tarkin Doctrine
-----
ff4fb461-8060-457a-9c16-000000001123
-----

+++++

.....
Grand Moff Tarkin
-----
ff4fb461-8060-457a-9c16-000000001124
-----

+++++

.....
Stormtrooper Assault Team
-----
ff4fb461-8060-457a-9c16-000000001125
-----
onStrike:RequestInt-Msg{How many Imperial Navy objectives do you control?}$$ExtraIcon:EE-UD:1-perX
+++++

.....
Rule by Fear
-----
ff4fb461-8060-457a-9c16-000000001126
-----
+++++
R0:SacrificeMyself$$ReturnTarget-DemiAutoTargeted-atUnit-targetOpponents-choose1

.....
Moment of Triumph
-----
ff4fb461-8060-457a-9c16-000000001127
-----
onPlay:DestroyMultiple-AutoTargeted-atUnit-hasProperty{Cost}le2
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000001128
-----
onResolveFate:CustomScript
+++++

.....
Might of the Empire
-----
ff4fb461-8060-457a-9c16-000000001129
-----

+++++

.....
Chimaera
-----
ff4fb461-8060-457a-9c16-000000001130
-----

+++++

.....
DP20 Corellian Gunship
-----
ff4fb461-8060-457a-9c16-000000001131
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough&&Put1Shield-AutoTargeted-atUnit_or_Objective-targetMine-choose1-isReact
+++++

.....
Fleet Staging Area
-----
ff4fb461-8060-457a-9c16-000000001132
-----

+++++

.....
Tractor Beam
-----
ff4fb461-8060-457a-9c16-000000001133
-----
onPlay:Transfer1Focus-Targeted-atVehicle-sourceVehicle-hasMarker{Focus}-destinationVehicle
+++++

.....
The Empire Strikes Back
-----
ff4fb461-8060-457a-9c16-000000001134
-----
onPlay:Gain1Dial
+++++

.....
Enforced Loyalty
-----
ff4fb461-8060-457a-9c16-000000001135
-----
atTurnEnd:Deal1Damage-AutoTargeted-atObjective-targetOpponents-duringOpponentTurn-ifOrigHasntMarker{Damage}-onlyOnce-isReact
+++++

.....
Colonel Yularen
-----
ff4fb461-8060-457a-9c16-000000001136
-----
onPlay:Remove2Damage-DemiAutoTargeted-atObjective-hasMarker{Damage}-targetMine-choose1-isCost-isReact$$Deal1Damage-DemiAutoTargeted-atObjective-targetOpponents-choose1
+++++

.....
Lieutenant Mithel
-----
ff4fb461-8060-457a-9c16-000000001137
-----

+++++

.....
MSE-6 "Mouse" Droid
-----
ff4fb461-8060-457a-9c16-000000001138
-----

+++++

.....
Control Room
-----
ff4fb461-8060-457a-9c16-000000001139
-----

+++++

.....
The Imperial Fist
-----
ff4fb461-8060-457a-9c16-000000001140
-----

+++++

.....
Imperial Entanglements
-----
ff4fb461-8060-457a-9c16-000000001141
-----

+++++

.....
Imperial Raider
-----
ff4fb461-8060-457a-9c16-000000001142
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
VT-49 Decimator
-----
ff4fb461-8060-457a-9c16-000000001143
-----

+++++

.....
VT-49 Decimator
-----
ff4fb461-8060-457a-9c16-000000001144
-----

+++++

.....
Customs Blockade
-----
ff4fb461-8060-457a-9c16-000000001145
-----

+++++

.....
Ion Cannon
-----
ff4fb461-8060-457a-9c16-000000001146
-----
Placement:Capital Ship_or_Transport||BonusIcons:T:1
+++++

.....
Phantoms of Imdaar
-----
ff4fb461-8060-457a-9c16-000000001147
-----

+++++

.....
TIE Phantom
-----
ff4fb461-8060-457a-9c16-000000001148
-----

+++++

.....
TIE Phantom
-----
ff4fb461-8060-457a-9c16-000000001149
-----

+++++

.....
Enhanced Laser Cannon
-----
ff4fb461-8060-457a-9c16-000000001150
-----
Placement:Fighter||BonusIcons:UD:1
+++++

.....
Fighters Coming In!
-----
ff4fb461-8060-457a-9c16-000000001151
-----

+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000001152
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Brothers of the Sith
-----
ff4fb461-8060-457a-9c16-000000001153
-----

+++++

.....
Gorc
-----
ff4fb461-8060-457a-9c16-000000001154
-----

+++++

.....
Pic
-----
ff4fb461-8060-457a-9c16-000000001155
-----

+++++

.....
Telepathic Connection
-----
ff4fb461-8060-457a-9c16-000000001156
-----

+++++

.....
Force Stasis
-----
ff4fb461-8060-457a-9c16-000000001157
-----
onPlay:Put1Force Stasis-Targeted-atCharacter_or_Creature
+++++

.....
Force Invisibility
-----
ff4fb461-8060-457a-9c16-000000001158
-----

+++++

.....
The Hutt's Menagerie
-----
ff4fb461-8060-457a-9c16-000000001159
-----

+++++

.....
Malakili
-----
ff4fb461-8060-457a-9c16-000000001160
-----

+++++

.....
Jabba's Rancor
-----
ff4fb461-8060-457a-9c16-000000001161
-----

+++++


.....
Bubo
-----
ff4fb461-8060-457a-9c16-000000001162
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atUnit_and_Scum and Villainy-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
Underground Entertainment
-----
ff4fb461-8060-457a-9c16-000000001163
-----

+++++

.....
Jabba's Summons
-----
ff4fb461-8060-457a-9c16-000000001164
-----
onPlay:Retrieve1Card-grabBounty Hunter_or_Mercenary-isReact$$ShuffleDeck
+++++

.....
Shield Generator Assault
-----
ff4fb461-8060-457a-9c16-000000001165
-----
atTurnStart:Remove1Damage-Targeted-atObjective_and_Endor-duringMyTurn-isReact-isCost$$Put1Damage-Targeted-atObjective_and_Endor
+++++

.....
Han Solo
-----
ff4fb461-8060-457a-9c16-000000001166
-----
onStrike:CustomScript-ifOrigAttacking-notHARDCOREenough
+++++

.....
SpecForce Pathfinder
-----
ff4fb461-8060-457a-9c16-000000001167
-----
+++++

.....
SpecForce Pathfinder
-----
ff4fb461-8060-457a-9c16-000000001168
-----
+++++

.....
Secret Objective
-----
ff4fb461-8060-457a-9c16-000000001169
-----
onResolveFate:CustomScript-ifOrigAttacking-notHARDCOREenough
+++++

.....
Ground Support
-----
ff4fb461-8060-457a-9c16-000000001170
-----

+++++

.....
Warriors of the Forest
-----
ff4fb461-8060-457a-9c16-000000001171
-----
whileInPlay:IncreaseEE-BD:1-forMe-typeEwok-isAttacking
+++++

.....
Wicket W. Warrick
-----
ff4fb461-8060-457a-9c16-000000001172
-----
onAttack:Put1Focus-DemiAutoTargeted-atUnit-hasProperty{Cost}le3-targetOpponents-choose1-isReact
+++++

.....
Ewok Warrior
-----
ff4fb461-8060-457a-9c16-000000001173
-----

+++++

.....
Part of the Tribe
-----
ff4fb461-8060-457a-9c16-000000001174
-----
Placement:Character_or_Droid||ConstantEffect:Trait{Ewok}1Bonus-onHost
+++++

.....
Secret Objective
-----
ff4fb461-8060-457a-9c16-000000001175
-----
onResolveFate:CustomScript-ifOrigAttacking-notHARDCOREenough
+++++

.....
Repel the Invaders
-----
ff4fb461-8060-457a-9c16-000000001176
-----

+++++

.....
The Emperor's Legion
-----
ff4fb461-8060-457a-9c16-000000001177
-----

+++++

.....
Lieutenant Renz
-----
ff4fb461-8060-457a-9c16-000000001178
-----

+++++

.....
Scout Trooper
-----
ff4fb461-8060-457a-9c16-000000001179
-----
DeployAllowance:Conflict
+++++

.....
Scout Trooper
-----
ff4fb461-8060-457a-9c16-000000001180
-----
DeployAllowance:Conflict
+++++

.....
Secret Objective
-----
ff4fb461-8060-457a-9c16-000000001181
-----
onResolveFate:CustomScript-ifOrigAttacking-notHARDCOREenough
+++++

.....
Prepared Ambush
-----
ff4fb461-8060-457a-9c16-000000001182
-----

+++++

.....
The Droid Revolution
-----
ff4fb461-8060-457a-9c16-000000001183
-----

+++++

.....
IG-88B
-----
ff4fb461-8060-457a-9c16-000000001184
-----
whileInPlay:IncreaseUD:1-forMe-typeDroid||onStrike:EngageTarget-Targeted-atUnit-targetOpponents-isNotParticipating-ifOrigAttacking-isReact
+++++

.....
Assassin Droid
-----
ff4fb461-8060-457a-9c16-000000001185
-----
+++++
R0:Remove1Focus

.....
K4 Security Droid
-----
ff4fb461-8060-457a-9c16-000000001186
-----

+++++

.....
Illegal Modifications
-----
ff4fb461-8060-457a-9c16-000000001187
-----
Placement:Droid_and_Unit||onHostMarkerAddFocus:Deal1Damage-AutoTargeted-onHost-isCost-isReact-onlyOnce$$Remove1Focus-AutoTargeted-onHost
+++++

.....
Prized Possession
-----
ff4fb461-8060-457a-9c16-000000001188
-----

+++++

.....
Mission Command
-----
ff4fb461-8060-457a-9c16-000000001189
-----

+++++

.....
Contract Hunter
-----
ff4fb461-8060-457a-9c16-000000001190
-----

+++++

.....
Contract Hunter
-----
ff4fb461-8060-457a-9c16-000000001191
-----

+++++

.....
Filthy Accusations
-----
ff4fb461-8060-457a-9c16-000000001192
-----
onPlay:Put1Focus-Targeted-atUnit-targetOpponents
+++++

.....
Secret Objective
-----
ff4fb461-8060-457a-9c16-000000001193
-----
onResolveFate:CustomScript-ifOrigAttacking-notHARDCOREenough
+++++

.....
Assassination Contract
-----
ff4fb461-8060-457a-9c16-000000001194
-----

+++++

.....
Out of Their Element
-----
ff4fb461-8060-457a-9c16-000000001195
-----

+++++

.....
Luke's Speeder Bike
-----
ff4fb461-8060-457a-9c16-000000001196
-----
ConstantEffect:Edge1Bonus||whileInPlay:DisengageMyself-foreachEdgeWin-ifOrigEdgeLoser-isReact
+++++

.....
Believer in the Old Ways
-----
ff4fb461-8060-457a-9c16-000000001197
-----
+++++

.....
Believer in the Old Ways
-----
ff4fb461-8060-457a-9c16-000000001198
-----
+++++

.....
Ambush Point
-----
ff4fb461-8060-457a-9c16-000000001199
-----
+++++

.....
Force Persuasion
-----
ff4fb461-8060-457a-9c16-000000001200
-----
onPlay:RequestInt-Msg{If the unit is out-of-faction, press 2, otherwise press 1}$$Put1Focus-perX-Targeted-atCharacter_or_Creature
+++++

.....
Secret Weapons
-----
ff4fb461-8060-457a-9c16-000000001201
-----

+++++

.....
Tydirium
-----
ff4fb461-8060-457a-9c16-000000001202
-----
ConstantEffect:Edge1Bonus-perEveryCard-AutoTargeted-isParticipating-targetOpponents||onLeaving:Lose1Dial-isReact
+++++

.....
Stolen Speeder Bike
-----
ff4fb461-8060-457a-9c16-000000001203
-----
onStrike:Put1Focus-AutoTargeted-atObjective-isParticipating-ifOrigAttacking-isStrikeAlternative-isReact-onlyOnce
+++++

.....
Stolen AT-ST
-----
ff4fb461-8060-457a-9c16-000000001204
-----
ConstantEffect:Protection-ifOrigHasntMarker{Focus}
+++++

.....
Hiding Among Enemies
-----
ff4fb461-8060-457a-9c16-000000001205
-----
onPlay:Put1Shield-Targeted-atUnit_and_Vehicle_and_Smugglers and Spies$$Discard1Card-ofAllOpponents-isRandom-isReact
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000001206
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Courage of the Tribe
-----
ff4fb461-8060-457a-9c16-000000001207
-----
afterRefresh:Remove1Focus-DemiAutoTargeted-atUnit_and_Ewok-targetMine-choose1-duringMyTurn-isReact
+++++

.....
Chief Chirpa
-----
ff4fb461-8060-457a-9c16-000000001208
-----
afterPhase:Put1Focus-DemiAutoTargeted-atUnit_and_Ewok-targetMine-choose1-isCost-isReact$$Draw1Card
+++++

.....
Ewok Horde
-----
ff4fb461-8060-457a-9c16-000000001209
-----
onPay:Reduce1CostPlay-perEveryCard-AutoTargeted-atUnit_and_Ewok-targetMine-maxReduce4
+++++

.....
Ewok Horde
-----
ff4fb461-8060-457a-9c16-000000001210
-----
onPay:Reduce1CostPlay-perEveryCard-AutoTargeted-atUnit_and_Ewok-targetMine-maxReduce4
+++++

.....
Bright Tree Village
-----
ff4fb461-8060-457a-9c16-000000001211
-----

+++++

.....
Battle of Endor
-----
ff4fb461-8060-457a-9c16-000000001212
-----
onResolveFate:RequestInt-Max3-Msg{How many Endor objectives and enhancements do you control? Max 3}$$CreateDummy-nonUnique-isSilent||whileInPlay:Edge1Bonus-perX-onlyforDummy||afterEngagement:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Merciless Plans
-----
ff4fb461-8060-457a-9c16-000000001213
-----
whileInPlay:SimplyAnnounce{Merciless Plans triggers to set the Balance of the Force to the Dark Side}-foreachCardPlayed-typeMission-isReact||whileInPlay:SimplyAnnounce{Merciless Plans triggers to set the Balance of the Force to the Dark Side}-foreachCardLeavingPlay-typeMission-isReact
+++++

.....
Boc
-----
ff4fb461-8060-457a-9c16-000000001214
-----
ExtraIcon:BD:2-ifOrigAttacking-hasObjectiveTrait-typeMission
+++++

.....
Expendable Scout
-----
ff4fb461-8060-457a-9c16-000000001215
-----
+++++
R0:SacrificeMyself$$SimplyAnnounce{Choose 1 player to discard 1 card from their hand and then draw 1 card from their command deck}

.....
Sith Lightsaber
-----
ff4fb461-8060-457a-9c16-000000001216
-----
Placement:Force User_or_Force Sensitive||BonusIcons:UD:1, EE-T:1
+++++

.....
Secret Objective
-----
ff4fb461-8060-457a-9c16-000000001217
-----
onResolveFate:CustomScript-ifOrigAttacking-notHARDCOREenough
+++++

.....
Dark Genocide
-----
ff4fb461-8060-457a-9c16-000000001218
-----
onPlay:CustomScript
+++++

.....
Sector Lockdown
-----
ff4fb461-8060-457a-9c16-000000001219
-----

+++++

.....
Captain Zed
-----
ff4fb461-8060-457a-9c16-000000001220
-----

+++++

.....
Stalker
-----
ff4fb461-8060-457a-9c16-000000001221
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Storm Commando
-----
ff4fb461-8060-457a-9c16-000000001222
-----
onPlay:Discard1Card-AutoTargeted-fromTopDeckOpponents-ofAllOpponents-isReact||onLeaving:Discard1Card-AutoTargeted-fromTopDeckOpponents-ofAllOpponents-isReact
+++++

.....
Sector Garrison
-----
ff4fb461-8060-457a-9c16-000000001223
-----
+++++
R0:Put1Focus-isCost$$Retrieve1Card-grabUnit-fromDiscard-toDeck$$ShuffleDeck

.....
Search and Detain
-----
ff4fb461-8060-457a-9c16-000000001224
-----

+++++

.....
The Spice Trade
-----
ff4fb461-8060-457a-9c16-000000001225
-----

+++++

.....
Moruth Doole
-----
ff4fb461-8060-457a-9c16-000000001226
-----
whileInPlay:Remove1Focus-foreachCardLeavingPlay-typeObjective-DemiAutoTargeted-atUnit-hasMarker{Focus}-targetMine-choose1-isReact$$Put1Focus-DemiAutoTargeted-atUnit-targetOpponents-choose1
+++++

.....
Energy Spider
-----
ff4fb461-8060-457a-9c16-000000001227
-----

+++++

.....
Energy Spider
-----
ff4fb461-8060-457a-9c16-000000001228
-----

+++++

.....
Spice Blitz
-----
ff4fb461-8060-457a-9c16-000000001229
-----

+++++

.....
Hallucination
-----
ff4fb461-8060-457a-9c16-000000001230
-----

+++++

.....
Matter Under Mind
-----
ff4fb461-8060-457a-9c16-000000001231
-----
+++++

.....
Brainiac
-----
ff4fb461-8060-457a-9c16-000000001232
-----
+++++

.....
Unhinged Astromech
-----
ff4fb461-8060-457a-9c16-000000001233
-----
+++++
R0:SacrificeMyself&&Deal1Damage-DemiAutoTargeted-atUnit-choose1||R0:SacrificeMyself&&Discard1Card-ofAllOpponents-isRandom-isReact||R0:SacrificeMyself&&Remove3Damage-DemiAutoTargeted-atUnit-choose1

.....
Unhinged Astromech
-----
ff4fb461-8060-457a-9c16-000000001234
-----
+++++
R0:SacrificeMyself&&Deal1Damage-DemiAutoTargeted-atUnit-choose1||R0:SacrificeMyself&&Discard1Card-ofAllOpponents-isRandom-isReact||R0:SacrificeMyself&&Remove3Damage-DemiAutoTargeted-atUnit-choose1

.....
Signal Scrambler
-----
ff4fb461-8060-457a-9c16-000000001235
-----
+++++

.....
Outwit
-----
ff4fb461-8060-457a-9c16-000000001236
-----
onPlay:SimplyAnnounce{Resolve fate cards from highest priority to lowest priority}$$Draw1Card
+++++

.....
Solidarity of Spirit
-----
ff4fb461-8060-457a-9c16-000000001237
-----
+++++

.....
Home One
-----
ff4fb461-8060-457a-9c16-000000001238
-----
onStrike:Deal3Damage-DemiAutoTargeted-atObjective-targetOpponents-choose1-ifOrighasEdge-isReact||onStrike:Deal2Damage-DemiAutoTargeted-atObjective-targetOpponents-choose1-isReact
+++++

.....
MC80 Liberty-type Cruiser
-----
ff4fb461-8060-457a-9c16-000000001239
-----
onPlay:SimplyAnnounce{reduce the cost of the next Vehicle they play this phase by 1}$$CreateDummy-isSilent-nonUnique-doNotDiscard||whileInPlay:Reduce1CostPlay-affectsVehicle-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeVehicle-onlyforDummy-isSilent
+++++

.....
MC80 Liberty-type Cruiser
-----
ff4fb461-8060-457a-9c16-000000001240
-----
onPlay:SimplyAnnounce{reduce the cost of the next Vehicle they play this phase by 1}$$CreateDummy-isSilent-nonUnique-doNotDiscard||whileInPlay:Reduce1CostPlay-affectsVehicle-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeVehicle-onlyforDummy-isSilent
+++++

.....
Rebel Fleet Command
-----
ff4fb461-8060-457a-9c16-000000001241
-----

+++++

.....
Battle of Endor
-----
ff4fb461-8060-457a-9c16-000000001242
-----
onResolveFate:RequestInt-Max3-Msg{How many Endor objectives and enhancements do you control? Max 3}$$CreateDummy-nonUnique-isSilent||whileInPlay:Edge1Bonus-perX-onlyforDummy||afterEngagement:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Sowers of Dissension
-----
ff4fb461-8060-457a-9c16-000000001243
-----
+++++

.....
Lobot
-----
ff4fb461-8060-457a-9c16-000000001244
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Duros Saboteur
-----
ff4fb461-8060-457a-9c16-000000001245
-----
+++++

.....
Duros Saboteur
-----
ff4fb461-8060-457a-9c16-000000001246
-----
+++++

.....
Paid Off
-----
ff4fb461-8060-457a-9c16-000000001247
-----
+++++

.....
Hiding Among Friends
-----
ff4fb461-8060-457a-9c16-000000001248
-----
onPlay:Put1Shield-DemiAutoTargeted-atCharacter_and_Smugglers and Spies-choose1$$Draw1Card
+++++

.....
Dark Counsel
-----
ff4fb461-8060-457a-9c16-000000001249
-----
whileInPlay:Put1Focus-foreachUnitStrike-onTriggerCard-typeUnit-hasMarker{Damage}-byOpposingOriginController-onlyOnce-isReact
+++++

.....
Janus Greejatus
-----
ff4fb461-8060-457a-9c16-000000001250
-----
+++++

.....
Imperial Functionary
-----
ff4fb461-8060-457a-9c16-000000001251
-----
+++++

.....
Sith Library
-----
ff4fb461-8060-457a-9c16-000000001252
-----
+++++

.....
Administrative Detainment
-----
ff4fb461-8060-457a-9c16-000000001253
-----
+++++

.....
Battle of Endor
-----
ff4fb461-8060-457a-9c16-000000001254
-----
onResolveFate:RequestInt-Max3-Msg{How many Endor objectives and enhancements do you control? Max 3}$$CreateDummy-nonUnique-isSilent||whileInPlay:Edge1Bonus-perX-onlyforDummy||afterEngagement:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Moon Blockade
-----
ff4fb461-8060-457a-9c16-000000001255
-----
+++++

.....
Executor
-----
ff4fb461-8060-457a-9c16-000000001256
-----
onPlay:Deal3Damage-DemiAutoTargeted-atObjective-targetOpponents-choose1-isReact
+++++

.....
Rear Admiral Chiraneau
-----
ff4fb461-8060-457a-9c16-000000001257
-----
+++++

.....
Imperial Engineer
-----
ff4fb461-8060-457a-9c16-000000001258
-----
+++++

.....
Jamming Protocol
-----
ff4fb461-8060-457a-9c16-000000001259
-----
onPlay:SimplyAnnounce{cancel the effects of the event card}$$Put1Effects Cancelled-DemiAutoTargeted-atEvent-isReady-choose1-isSilent
+++++

.....
Battle of Endor
-----
ff4fb461-8060-457a-9c16-000000001260
-----
onResolveFate:RequestInt-Max3-Msg{How many Endor objectives and enhancements do you control? Max 3}$$CreateDummy-nonUnique-isSilent||whileInPlay:Edge1Bonus-perX-onlyforDummy||afterEngagement:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Turning the Tide
-----
ff4fb461-8060-457a-9c16-000000001261
-----
whileInPlay:foreachCardPlayed-byMe-typeMission-Remove1Focus-onlyOnce-isReact||whileInPlay:foreachCardPlayed-byMe-typeEvent_and_Rebel Alliance-Remove1Focus-onlyOnce-isReact
+++++

.....
Admiral Ackbar
-----
ff4fb461-8060-457a-9c16-000000001262
-----

+++++

.....
Alliance B-Wing
-----
ff4fb461-8060-457a-9c16-000000001263
-----

+++++

.....
Alliance B-Wing
-----
ff4fb461-8060-457a-9c16-000000001264
-----

+++++

.....
Ackbar's Orders
-----
ff4fb461-8060-457a-9c16-000000001265
-----

+++++

.....
The Final Battle
-----
ff4fb461-8060-457a-9c16-000000001266
-----

+++++

.....
Feigning Captivity
-----
ff4fb461-8060-457a-9c16-000000001267
-----

+++++

.....
Tamtel Skreej
-----
ff4fb461-8060-457a-9c16-000000001268
-----

+++++

.....
Infiltration Specialist
-----
ff4fb461-8060-457a-9c16-000000001269
-----

+++++

.....
Infiltration Specialist
-----
ff4fb461-8060-457a-9c16-000000001270
-----

+++++

.....
Secret Objective
-----
ff4fb461-8060-457a-9c16-000000001271
-----
onResolveFate:CustomScript-ifOrigAttacking-notHARDCOREenough
+++++

.....
To Save a Friend
-----
ff4fb461-8060-457a-9c16-000000001272
-----

+++++

.....
The Tree Tribes
-----
ff4fb461-8060-457a-9c16-000000001273
-----

+++++

.....
Ewok Ambusher
-----
ff4fb461-8060-457a-9c16-000000001274
-----
DeployAllowance:Conflict
+++++

.....
Ewok Ambusher
-----
ff4fb461-8060-457a-9c16-000000001275
-----
DeployAllowance:Conflict
+++++

.....
Ewok Ambusher
-----
ff4fb461-8060-457a-9c16-000000001276
-----
DeployAllowance:Conflict
+++++

.....
Ewok Ambusher
-----
ff4fb461-8060-457a-9c16-000000001277
-----
DeployAllowance:Conflict
+++++

.....
Battle of Endor
-----
ff4fb461-8060-457a-9c16-000000001278
-----
onResolveFate:RequestInt-Max3-Msg{How many Endor objectives and enhancements do you control? Max 3}$$CreateDummy-nonUnique-isSilent||whileInPlay:Edge1Bonus-perX-onlyforDummy||afterEngagement:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Fearsome and Foul
-----
ff4fb461-8060-457a-9c16-000000001279
-----
onPlay:Retrieve1Card-grabCreature-isReact$$ShuffleDeck
+++++

.....
Sith Wyrm
-----
ff4fb461-8060-457a-9c16-000000001280
-----

+++++

.....
Sith Wyrm
-----
ff4fb461-8060-457a-9c16-000000001281
-----

+++++

.....
Sith Wyrm
-----
ff4fb461-8060-457a-9c16-000000001282
-----

+++++

.....
Dark Lair
-----
ff4fb461-8060-457a-9c16-000000001283
-----
whileInPlay:foreachCardPlayed-byMe-typeCreature_or_Sithspawn-Draw1Card-isReact
+++++

.....
Feeding Frenzy
-----
ff4fb461-8060-457a-9c16-000000001284
-----
onPlay:DestroyTarget-Targeted-atUnit
+++++

.....
Endor Entrapment
-----
ff4fb461-8060-457a-9c16-000000001285
-----
+++++
R0:SimplyAnnounce{discard an Imperial Navy card to cancel damage equal to the number of it's force icons}-onlyOnce

.....
Interdictor-class Heavy Cruiser
-----
ff4fb461-8060-457a-9c16-000000001286
-----
onAttack:EngageTarget-Targeted-atUnit-targetOpponents-hasntMarker{Focus}
+++++

.....
Gladiator-class Star Destroyer
-----
ff4fb461-8060-457a-9c16-000000001287
-----
+++++
R0:SimplyAnnounce{place one card not named Twist of Fate from their hand into their edge stack}

.....
Gladiator-class Star Destroyer
-----
ff4fb461-8060-457a-9c16-000000001288
-----
+++++
R0:SimplyAnnounce{place one card not named Twist of Fate from their hand into their edge stack}

.....
Control Room
-----
ff4fb461-8060-457a-9c16-000000001289
-----

+++++

.....
Battle of Endor
-----
ff4fb461-8060-457a-9c16-000000001290
-----
onResolveFate:RequestInt-Max3-Msg{How many Endor objectives and enhancements do you control? Max 3}$$CreateDummy-nonUnique-isSilent||whileInPlay:Edge1Bonus-perX-onlyforDummy||afterEngagement:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Schemes and Intrigues
-----
ff4fb461-8060-457a-9c16-000000001291
-----

+++++

.....
Ephant Mon
-----
ff4fb461-8060-457a-9c16-000000001292
-----

+++++

.....
Chevin Mercenary
-----
ff4fb461-8060-457a-9c16-000000001293
-----

+++++

.....
Head of Security
-----
ff4fb461-8060-457a-9c16-000000001294
-----
Placement:Scum and Villainy_and_Unit||BonusIcons:T:1
+++++

.....
Secret Objective
-----
ff4fb461-8060-457a-9c16-000000001295
-----
onResolveFate:CustomScript-ifOrigAttacking-notHARDCOREenough
+++++

.....
Capture the Assassin
-----
ff4fb461-8060-457a-9c16-000000001296
-----

+++++

.....
Lost in the Forest
-----
ff4fb461-8060-457a-9c16-000000001297
-----

+++++

.....
C-3PO
-----
ff4fb461-8060-457a-9c16-000000001298
-----

+++++

.....
Homeland Defender
-----
ff4fb461-8060-457a-9c16-000000001299
-----
afterDeployment:Remove1Focus-isReact
+++++

.....
Homeland Defender
-----
ff4fb461-8060-457a-9c16-000000001300
-----
afterDeployment:Remove1Focus-isReact
+++++

.....
Forest Awareness
-----
ff4fb461-8060-457a-9c16-000000001301
-----
Placement:Jedi_or_Ewok
+++++

.....
Battle of Endor
-----
ff4fb461-8060-457a-9c16-000000001302
-----
onResolveFate:RequestInt-Max3-Msg{How many Endor objectives and enhancements do you control? Max 3}$$CreateDummy-nonUnique-isSilent||whileInPlay:Edge1Bonus-perX-onlyforDummy||afterEngagement:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Strike Team Assemble
-----
ff4fb461-8060-457a-9c16-000000001303
-----

+++++

.....
Major Bren Derlin
-----
ff4fb461-8060-457a-9c16-000000001304
-----
whileInPlay:Put1TIE Attack Squadron:BD-foreachResolveFate-byMe-onlyOnce-ifOrigParticipating||afterEngagement:Remove999TIE Attack Squadron:UD-isSilent$$Remove999Activation-isSilent
+++++

.....
Strike Team Specialist
-----
ff4fb461-8060-457a-9c16-000000001305
-----

+++++

.....
Natural Cover
-----
ff4fb461-8060-457a-9c16-000000001306
-----
+++++
R0:Put1Focus-isCost$$Remove1Damage-Targeted-atCharacter_or_Objective-targetAllied

.....
Scouting Ahead
-----
ff4fb461-8060-457a-9c16-000000001307
-----

+++++

.....
Battle of Endor
-----
ff4fb461-8060-457a-9c16-000000001308
-----
onResolveFate:RequestInt-Max3-Msg{How many Endor objectives and enhancements do you control? Max 3}$$CreateDummy-nonUnique-isSilent||whileInPlay:Edge1Bonus-perX-onlyforDummy||afterEngagement:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Maw of Madness
-----
ff4fb461-8060-457a-9c16-000000001309
-----
onPlay:Discard1Card-ofAllOpponents-isRandom-ifHaventForce-isReact$$Discard1Card-ofAllOpponents-isRandom-ifHaveForce-isReact
+++++

.....
Maw
-----
ff4fb461-8060-457a-9c16-000000001310
-----
ConstantEffect:Edge1Bonus||onStrike:Discard1Card-ofAllOpponents-isRandom-isReact$$TakeoverTarget-AutoTargeted-atEnhancement-fromDiscardOpponents-onTop1Cards
+++++

.....
Fallen Jedi
-----
ff4fb461-8060-457a-9c16-000000001311
-----
whileInPlay:IncreaseUD:1-forMe-typeCharacter-isParticipating-ifOrigParticipating-ifOrigHasntMarker{Focus}
+++++

.....
Expendable Scout
-----
ff4fb461-8060-457a-9c16-000000001312
-----
+++++
R0:SacrificeMyself$$SimplyAnnounce{Choose 1 player to discard 1 card from their hand and then draw 1 card from their command deck}

.....
Juyo Training
-----
ff4fb461-8060-457a-9c16-000000001313
-----
Placement:Force User
+++++

.....
Force Pull
-----
ff4fb461-8060-457a-9c16-000000001314
-----
onPlay:SimplyAnnounce{Put an enhancement from an opponent's discard pile into play under your control, enhancing an eligible card or game element.} 
+++++

.....
Protect the Generator
-----
ff4fb461-8060-457a-9c16-000000001315
-----

+++++

.....
Colonel Dyer
-----
ff4fb461-8060-457a-9c16-000000001316
-----

+++++

.....
Endor AT-ST
-----
ff4fb461-8060-457a-9c16-000000001317
-----
+++++
R0:Remove1Focus

.....
Endor AT-ST
-----
ff4fb461-8060-457a-9c16-000000001318
-----
+++++
R0:Remove1Focus

.....
Endor Command Post
-----
ff4fb461-8060-457a-9c16-000000001319
-----
+++++
R0:Remove1Focus

.....
Promotion
-----
ff4fb461-8060-457a-9c16-000000001320
-----
Placement:Imperial Navy_and_Officer
+++++

.....
Hunter for Hire
-----
ff4fb461-8060-457a-9c16-000000001321
-----

+++++

.....
Bane Malar
-----
ff4fb461-8060-457a-9c16-000000001322
-----

+++++

.....
Lannik Lackey
-----
ff4fb461-8060-457a-9c16-000000001323
-----

+++++

.....
Lannik Lackey
-----
ff4fb461-8060-457a-9c16-000000001324
-----

+++++

.....
Abandoned Hideout
-----
ff4fb461-8060-457a-9c16-000000001325
-----
+++++
R1:UncommitTarget-Targeted-atUnit-isCommited$$CommitTarget-Targeted-atUnit-isNotCommited

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000001326
-----
onResolveFate:CommitTarget-Targeted-atUnit-isNotCommited||UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
Dark Lord of the Sith
-----
ff4fb461-8060-457a-9c16-000000001345
-----
+++++

.....
Darth Vader
-----
ff4fb461-8060-457a-9c16-000000001346
-----
+++++

.....
Sith Warrior
-----
ff4fb461-8060-457a-9c16-000000001347
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Vader's Meditation Chamber
-----
ff4fb461-8060-457a-9c16-000000001348
-----
onPay:Reduce1CostPlay-perEveryCard-AutoTargeted-atForce User_or_Force Sensitive-targetMine-maxReduce1
+++++

.....
Telekinetic Strike
-----
ff4fb461-8060-457a-9c16-000000001349
-----
onPlay:Put1Focus-DemiAutoTargeted-atUnit-targetMine&&Put1Focus-DemiAutoTargeted-atCharacter_or_Creature-targetOpponents-choose1-ifHaventForce&&Put2Focus-DemiAutoTargeted-atCharacter_or_Creature-targetOpponents-choose1-ifHaveForce
+++++

.....
Visage of the Dark Lord
-----
ff4fb461-8060-457a-9c16-000000001350
-----
onResolveFate:Put1Focus-perEverySith_and_Unique-isParticipating-max1-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Encounter at Stygeon Prime
-----
ff4fb461-8060-457a-9c16-000000001351
-----
+++++

.....
The Inquisitor
-----
ff4fb461-8060-457a-9c16-000000001352
-----
+++++
R0:Draw1Card-onlyOnce

.....
Stygeon Prison Guard
-----
ff4fb461-8060-457a-9c16-000000001353
-----
onStrike:SimplyAnnounce{force the Light Side to place 1 focus on a ready unit they control.}
+++++

.....
The Inquisitor's Lightsaber
-----
ff4fb461-8060-457a-9c16-000000001354
-----
Placement:Force User_or_Force Sensitive||BonusIcons:UD:1
+++++

.....
Hunted
-----
ff4fb461-8060-457a-9c16-000000001355
-----
Placement:Unit-targetOpponents||onHostMarkerAddDamage:Put1Focus-AutoTargeted-onHost-isReact
+++++

.....
Bones of a Fallen Master
-----
ff4fb461-8060-457a-9c16-000000001356
-----
Placement:Objective-targetMine
+++++

.....
Power of the Dark Side
-----
ff4fb461-8060-457a-9c16-000000001357
-----
+++++

.....
Emperor Palpatine
-----
ff4fb461-8060-457a-9c16-000000001358
-----
whileInPlay:Remove2Focus-DemiAutoTargeted-atForce User_or_Force Sensitive-targetMine-choose1-foreachForceStruggleDark-ifOrigCommited-isReact
+++++

.....
Royal Guard Champion
-----
ff4fb461-8060-457a-9c16-000000001359
-----
ConstantEffect:Edge1Bonus
+++++

.....
Sith Library
-----
ff4fb461-8060-457a-9c16-000000001360
-----
+++++

.....
Force Manipulation
-----
ff4fb461-8060-457a-9c16-000000001361
-----
onPlay:DestroyTarget-Targeted-atUnit-isCommited
+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000001362
-----
onResolveFate:CommitTarget-Targeted-atUnit-isNotCommited||UncommitTarget-Targeted-atUnit-isCommited
+++++

.....
Dark Defenders
-----
ff4fb461-8060-457a-9c16-000000001363
-----
+++++

.....
"Backstabber"
-----
ff4fb461-8060-457a-9c16-000000001364
-----
onPlay:Put1Focus-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1-onlyDuringEngagement-isReact||DeployAllowance:Conflict
+++++

.....
Black Squadron
-----
ff4fb461-8060-457a-9c16-000000001365
-----
onPay:Reduce1CostPlay-perEveryCard-AutoTargeted-atBlack Squadron-targetMine-maxReduce3
+++++

.....
Black Squadron Pilot
-----
ff4fb461-8060-457a-9c16-000000001366
-----
onPlay:CustomScript||BonusIcons:UD:1, BD:1
+++++

.....
Come With Me
-----
ff4fb461-8060-457a-9c16-000000001367
-----
onPlay:Retrieve1Card-grabBlack Squadron$$ShuffleDeck
+++++

.....
Seeds of Decay
-----
ff4fb461-8060-457a-9c16-000000001368
-----
onResolveFate:Put1Focus-DemiAutoTargeted-atUnit-isCommited-hasntMarker{Focus}-choose1
+++++

.....
Hunters of the Jedi
-----
ff4fb461-8060-457a-9c16-000000001369
-----
whileInPlay:BringToPlayTarget-DemiAutoTargeted-atUnit_and_Sithspawn-fromHand-choose1-foreachCardLeavingPlay-typeForce User_or_Force Sensitive-onlyOnce-isReact
+++++

.....
Terentatek
-----
ff4fb461-8060-457a-9c16-000000001370
-----
+++++

.....
Terentatek
-----
ff4fb461-8060-457a-9c16-000000001371
-----
+++++

.....
Tuk'ata
-----
ff4fb461-8060-457a-9c16-000000001372
-----
+++++

.....
Tuk'ata
-----
ff4fb461-8060-457a-9c16-000000001373
-----
+++++

.....
Valley of the Dark Lords
-----
ff4fb461-8060-457a-9c16-000000001374
-----
+++++

.....
Out of the Mists
-----
ff4fb461-8060-457a-9c16-000000001375
-----
+++++

.....
Zuckuss
-----
ff4fb461-8060-457a-9c16-000000001376
-----
+++++

.....
4-LOM
-----
ff4fb461-8060-457a-9c16-000000001377
-----
onStrike:CaptureTarget-Targeted-atUnit-targetOpponents-ifOrigAttacking-isReact
+++++

.....
Seedy Cantina
-----
ff4fb461-8060-457a-9c16-000000001378
-----
+++++

.....
Crisis of Identity
-----
ff4fb461-8060-457a-9c16-000000001379
-----
+++++

.....
A Quick Hunt
-----
ff4fb461-8060-457a-9c16-000000001380
-----
+++++

.....
Entrenched Defense
-----
ff4fb461-8060-457a-9c16-000000001381
-----
+++++
R0:CustomScript-isReact-onlyOnce

.....
Golan-II Defense Platform
-----
ff4fb461-8060-457a-9c16-000000001382
-----
+++++

.....
Golan-II Defense Platform
-----
ff4fb461-8060-457a-9c16-000000001383
-----
+++++

.....
Early Warning System
-----
ff4fb461-8060-457a-9c16-000000001384
-----
atTurnStart:Remove1Focus-DemiAutoTargeted-atVehicle-hasMarker{Focus}-targetMine-choose1-duringOpponentTurn-isReact
+++++

.....
Fleet Repairs
-----
ff4fb461-8060-457a-9c16-000000001385
-----
onPlay:Remove999Damage-Targeted-atVehicle
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000001386
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
Hope of Rebellion
-----
ff4fb461-8060-457a-9c16-000000001387
-----
whileInPlay:BringToPlayTarget-DemiAutoTargeted-atUnit-hasProperty{Cost}le2-fromHand-choose1-foreachCardLeavingPlay-typeLeader-onlyOnce-isReact
+++++

.....
Leia Organa
-----
ff4fb461-8060-457a-9c16-000000001388
-----
+++++

.....
Operations Planner
-----
ff4fb461-8060-457a-9c16-000000001389
-----
onPlay:Deal1Damage-Targeted-atObjective-targetOpponents-isReact
+++++

.....
Operations Planner
-----
ff4fb461-8060-457a-9c16-000000001390
-----
onPlay:Deal1Damage-Targeted-atObjective-targetOpponents-isReact
+++++

.....
Rousing Speech
-----
ff4fb461-8060-457a-9c16-000000001391
-----
onPlay:CreateDummy-nonUnique||whileInPlay:IncreaseUD:1-forMe-typeCharacter-isParticipating-onlyforDummy||afterEngagement:DestroyMyself-onlyforDummy-isSilent
+++++

.....
The Rebels' Hope
-----
ff4fb461-8060-457a-9c16-000000001392
-----
+++++

.....
Planning the Attack
-----
ff4fb461-8060-457a-9c16-000000001393
-----
onPlay:Gain1Reserves||onDamage:Lose1Reserves||onHeal:Gain1Reserves||onThwart:Lose1Reserves-ifOrigHasntMarker{Damage}
+++++

.....
General Jan Dodonna
-----
ff4fb461-8060-457a-9c16-000000001394
-----
+++++

.....
Rebel Tactician
-----
ff4fb461-8060-457a-9c16-000000001395
-----
ExtraIcon:UD:1-perEveryCard-AutoTargeted-atLeader-isParticipating-targetMine-max1||ExtraIcon:EE-BD:1-perEveryCard-AutoTargeted-atLeader-isParticipating-targetMine-max1
+++++

.....
Rebel Tactician
-----
ff4fb461-8060-457a-9c16-000000001396
-----
ExtraIcon:UD:1-perEveryCard-AutoTargeted-atLeader-isParticipating-targetMine-max1||ExtraIcon:EE-BD:1-perEveryCard-AutoTargeted-atLeader-isParticipating-targetMine-max1
+++++

.....
Massassi Temple War Room
-----
ff4fb461-8060-457a-9c16-000000001397
-----
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000001398
-----
onResolveFate:CustomScript
+++++

.....
Mission to Talay
-----
ff4fb461-8060-457a-9c16-000000001399
-----
+++++

.....
Mon Mothma
-----
ff4fb461-8060-457a-9c16-000000001400
-----
whileInPlay:Reduce1CostPlay-affectsUnit_and_Rebel Alliance-ifOrigCommited-onlyOnce
+++++

.....
Kyle Katarn
-----
ff4fb461-8060-457a-9c16-000000001401
-----
+++++

.....
Inspiring Presence
-----
ff4fb461-8060-457a-9c16-000000001402
-----
Placement:Unit_and_Leader
+++++

.....
Concussion Rifle
-----
ff4fb461-8060-457a-9c16-000000001403
-----
Placement:Character||onHostStrike:Put1Focus-isCost-isReact$$Put1Damage-DemiAutoTargeted-atUnit-hasntMarker{Focus}-targetOpponents-choose1
+++++

.....
Rebel for Hire
-----
ff4fb461-8060-457a-9c16-000000001404
-----
+++++

.....
The Alliance's Elite
-----
ff4fb461-8060-457a-9c16-000000001405
-----
afterRefresh:Remove1Focus-DemiAutoTargeted-atFighter_or_Speeder-hasMarker{Focus}-targetMine-choose1-isReact
+++++

.....
Rogue Squadron
-----
ff4fb461-8060-457a-9c16-000000001406
-----
+++++
R0:Draw1Card-onlyOnce

.....
Alliance X-Wing
-----
ff4fb461-8060-457a-9c16-000000001407
-----
+++++

.....
R3-A2
-----
ff4fb461-8060-457a-9c16-000000001408
-----
Placement:Fighter||onHostStrike:Put1Focus-isCost-isReact$$Put1Focus-DemiAutoTargeted-atUnit-targetOpponents-choose1
+++++

.....
Kill Marker
-----
ff4fb461-8060-457a-9c16-000000001409
-----
Placement:Fighter_or_Speeder||ConstantEffect:Edge1Bonus-ifOrigParticipatingHost
+++++

.....
Corellian Slip
-----
ff4fb461-8060-457a-9c16-000000001410
-----
onPlay:Put1Focus-Targeted-atVehicle
+++++

.....
Capital Cover
-----
ff4fb461-8060-457a-9c16-000000001411
-----
+++++

.....
Defiance
-----
ff4fb461-8060-457a-9c16-000000001412
-----
+++++

.....
MC40a Light Cruiser
-----
ff4fb461-8060-457a-9c16-000000001413
-----
+++++
R0:Remove1Shield-Targeted-atUnit_or_Objective_or_Mission-hasMarker{Shield}-onlyOnce-isCost$$Put1Shield

.....
MC30c Frigate
-----
ff4fb461-8060-457a-9c16-000000001414
-----
+++++

.....
Concentrated Firepower
-----
ff4fb461-8060-457a-9c16-000000001415
-----
onPlay:Remove1Shield-Targeted-atCapital Ship&&Put2Crossfire:UD-Targeted-atCapital Ship&&Put2Crossfire:BD-Targeted-atCapital Ship
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000001416
-----
onResolveFate:Put1Shield-Targeted-atUnit_or_Objective
+++++

.....
Spark of Rebellion
-----
ff4fb461-8060-457a-9c16-000000001417
-----
+++++
R0:Retrieve1Card-grabCharacter-hasProperty{Cost}le2-toTable-onTop1Cards-tellPlayer-isReact-onlyOnce||Retrieve1Card-grabUnit_and_Specter-toTable-onTop1Cards-tellPlayer-isReact-onlyOnce

.....
Kanan Jarrus
-----
ff4fb461-8060-457a-9c16-000000001418
-----
+++++

.....
Children of the Force
-----
ff4fb461-8060-457a-9c16-000000001419
-----
+++++
R0:SimplyAnnounce{looks at top card of their deck}-onlyOnce

.....
Children of the Force
-----
ff4fb461-8060-457a-9c16-000000001420
-----
+++++
R0:SimplyAnnounce{looks at top card of their deck}-onlyOnce

.....
Kanan's Concentration
-----
ff4fb461-8060-457a-9c16-000000001421
-----
onPlay:Remove1Focus-Targeted-atCharacter
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000001422
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
The Gardener's Secret
-----
ff4fb461-8060-457a-9c16-000000001423
-----
+++++

.....
Momaw Nadon
-----
ff4fb461-8060-457a-9c16-000000001424
-----
onPlay:Retrieve1Card-grabEnhancement-toTable-isReact&&ShuffleDeck
+++++

.....
Ithorian Junk Dealer
-----
ff4fb461-8060-457a-9c16-000000001425
-----
+++++

.....
Ithorian Junk Dealer
-----
ff4fb461-8060-457a-9c16-000000001426
-----
+++++

.....
Hidden Grove
-----
ff4fb461-8060-457a-9c16-000000001427
-----
+++++

.....
Hidden Grove
-----
ff4fb461-8060-457a-9c16-000000001428
-----
+++++

.....
A Hero's Duty
-----
ff4fb461-8060-457a-9c16-000000001429
-----
+++++

.....
Luke Skywalker
-----
ff4fb461-8060-457a-9c16-000000001430
-----
+++++

.....
I Will Not Fight You
-----
ff4fb461-8060-457a-9c16-000000001431
-----
+++++

.....
Search Your Feelings
-----
ff4fb461-8060-457a-9c16-000000001432
-----
+++++

.....
Secret Objective
-----
ff4fb461-8060-457a-9c16-000000001433
-----
onResolveFate:CustomScript-ifOrigAttacking-notHARDCOREenough
+++++

.....
Redeem the Fallen
-----
ff4fb461-8060-457a-9c16-000000001434
-----
+++++

.....
Engineering the Future
-----
ff4fb461-8060-457a-9c16-000000001435
-----
+++++

.....
General Walex Blissex
-----
ff4fb461-8060-457a-9c16-000000001436
-----
+++++

.....
Overworked Engineer
-----
ff4fb461-8060-457a-9c16-000000001437
-----
+++++

.....
A-A5 Heavy Speeder Truck
-----
ff4fb461-8060-457a-9c16-000000001438
-----
+++++

.....
Portable Shield Generator
-----
ff4fb461-8060-457a-9c16-000000001439
-----
+++++

.....
Engineering Brilliance
-----
ff4fb461-8060-457a-9c16-000000001440
-----
+++++

.....
Beyond the Rim
-----
ff4fb461-8060-457a-9c16-000000001441
-----
+++++

.....
Pulsar Skate
-----
ff4fb461-8060-457a-9c16-000000001442
-----
+++++

.....
Navigation Droid
-----
ff4fb461-8060-457a-9c16-000000001443
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atVehicle_and_Smugglers and Spies-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
Navigation Droid
-----
ff4fb461-8060-457a-9c16-000000001444
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atVehicle_and_Smugglers and Spies-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
Smuggler's Hideaway
-----
ff4fb461-8060-457a-9c16-000000001445
-----
+++++

.....
Last Ditch Maneuver
-----
ff4fb461-8060-457a-9c16-000000001446
-----
+++++

.....
The Emperor's Promise
-----
ff4fb461-8060-457a-9c16-000000001447
-----
+++++

.....
Emperor Palpatine
-----
ff4fb461-8060-457a-9c16-000000001448
-----
+++++

.....
Emperor's Royal Guard
-----
ff4fb461-8060-457a-9c16-000000001449
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atCharacter-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
ISB Officer
-----
ff4fb461-8060-457a-9c16-000000001450
-----
+++++

.....
Secret Objective
-----
ff4fb461-8060-457a-9c16-000000001451
-----
onResolveFate:CustomScript-ifOrigAttacking-notHARDCOREenough
+++++

.....
Lure of the Dark Side
-----
ff4fb461-8060-457a-9c16-000000001452
-----
+++++

.....
The Lady's Lesson
-----
ff4fb461-8060-457a-9c16-000000001453
-----
+++++

.....
Lady Valarian
-----
ff4fb461-8060-457a-9c16-000000001454
-----
+++++

.....
Whiphid Enforcer
-----
ff4fb461-8060-457a-9c16-000000001455
-----
+++++

.....
Whiphid Enforcer
-----
ff4fb461-8060-457a-9c16-000000001456
-----
+++++

.....
Unrefusable Offer
-----
ff4fb461-8060-457a-9c16-000000001457
-----
+++++

.....
Vicious Counterattack
-----
ff4fb461-8060-457a-9c16-000000001458
-----
+++++

.....
A New Beginning
-----
ff4fb461-8060-457a-9c16-000000001459
-----
+++++

.....
Ahsoka Tano
-----
ff4fb461-8060-457a-9c16-000000001460
-----
+++++

.....
Ahsoka's Informant
-----
ff4fb461-8060-457a-9c16-000000001461
-----
+++++

.....
Ahsoka's Lightsabers
-----
ff4fb461-8060-457a-9c16-000000001462
-----
Placement:Force User_or_Force Sensitive||BonusIcons:UD:1, EE-BD:1
+++++

.....
Ancient Rivals
-----
ff4fb461-8060-457a-9c16-000000001463
-----
+++++

.....
Ancient Rivals
-----
ff4fb461-8060-457a-9c16-000000001464
-----
+++++

.....
Explosives Artist
-----
ff4fb461-8060-457a-9c16-000000001465
-----
onPlay:Retrieve1Card-grabSpecter-onTop10Cards-isReact$$ShuffleDeck||onHostGenerate:Put1Ignores Affiliation Match-AutoTargeted-isUnpaid
+++++

.....
Sabine Wren
-----
ff4fb461-8060-457a-9c16-000000001466
-----
+++++

.....
Sabine's Armor
-----
ff4fb461-8060-457a-9c16-000000001467
-----
Placement:Character
+++++

.....
Custom Paint Job
-----
ff4fb461-8060-457a-9c16-000000001468
-----
+++++

.....
Improvised Explosive
-----
ff4fb461-8060-457a-9c16-000000001469
-----
Placement:Objective
+++++
R0:SacrificeMyself$$Deal1Damage-DemiAutoTargeted-atUnit-isAttacking-targetOpponents-isParticipating-choose2

.....
Well Equipped
-----
ff4fb461-8060-457a-9c16-000000001470
-----
onResolveFate:Remove1Focus-Targeted-atUnit_or_Objective
+++++

.....
No Match for a Good Blaster
-----
ff4fb461-8060-457a-9c16-000000001471
-----
whileInPlay:Deal1Damage-AutoTargeted-atObjective-isCurrentObjective-onlyDuringEngagement-foreachCardLeavingPlay-typeUnit-byOpposingOriginController-isReact
+++++

.....
Han Solo
-----
ff4fb461-8060-457a-9c16-000000001472
-----
whileInPlay:IncreaseUD:1-forMe-typeUnit_and_Smugglers and Spies_and_typenotHan Solo
+++++

.....
Chewbacca
-----
ff4fb461-8060-457a-9c16-000000001473
-----
+++++

.....
DL-44 Blaster Pistol
-----
ff4fb461-8060-457a-9c16-000000001474
-----
Placement:Character||BonusIcons:UD:1
+++++

.....
Don't Get Cocky
-----
ff4fb461-8060-457a-9c16-000000001475
-----
onPlay:Put2Cocky:BD-Targeted-atUnit-isParticipating
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000001476
-----
onResolveFate:Deal1Damage-DemiAutoTargeted-atUnit-isParticipating-targetOpponents-choose1
+++++

.....
There is No Conflict
-----
ff4fb461-8060-457a-9c16-000000001477
-----
+++++

.....
Darth Vader
-----
ff4fb461-8060-457a-9c16-000000001478
-----
whileInPlay:Deal1Damage-foreachResolveFate-byMe-DemiAutoTargeted-atUnit-targetOpponents-choose1-onlyOnce-isReact
+++++

.....
501st Commander
-----
ff4fb461-8060-457a-9c16-000000001479
-----
whileInPlay:DisengageMyself-foreachEdgeWin-ifOrigEdgeLoser-ifOrigParticipating-isReact$$DisengageTarget-DemiAutoTargeted-atUnit_and_Jedi_or_Unit_and_Neutral-targetOpponents-isParticipating-choose1
+++++

.....
Join Me
-----
ff4fb461-8060-457a-9c16-000000001480
-----
onPlay:TakeoverTarget-Targeted-atUnit_and_Character_and_nonUnique
+++++

.....
Ancient Rivals
-----
ff4fb461-8060-457a-9c16-000000001481
-----
+++++

.....
Ancient Rivals
-----
ff4fb461-8060-457a-9c16-000000001482
-----
+++++

.....
Heartless Tactics
-----
ff4fb461-8060-457a-9c16-000000001483
-----
+++++

.....
Dengar
-----
ff4fb461-8060-457a-9c16-000000001484
-----
+++++

.....
Security Operator
-----
ff4fb461-8060-457a-9c16-000000001485
-----
+++++

.....
Fortified Holding Cells
-----
ff4fb461-8060-457a-9c16-000000001486
-----
Placement:Objective_and_Scum and Villainy
+++++

.....
Captured
-----
ff4fb461-8060-457a-9c16-000000001487
-----
onPlay:CaptureTarget-Targeted-atUnit
+++++

.....
Preparation and Planning
-----
ff4fb461-8060-457a-9c16-000000001488
-----
onResolveFate:SimplyAnnounce{reduce the cost of the next event they play this turn by 2}$$CreateDummy-nonUnique-isSilent-doNotDiscard||whileInPlay:Reduce2CostPlay-affectsEvent-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeEvent-onlyforDummy-isSilent||atTurnEnd:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Resourceful Survivors
-----
ff4fb461-8060-457a-9c16-000000001489
-----
+++++
R0: SimplyAnnounce{play a [Rebel Alliance] event card from discard, then place out of play}

.....
General Vanden Willard
-----
ff4fb461-8060-457a-9c16-000000001490
-----
whileInPlay:Draw1Card-foreachCardPlayed-byMe-typeEvent-isReact-onlyOnce
+++++

.....
Alderaanian Survivor
-----
ff4fb461-8060-457a-9c16-000000001491
-----
onPlay:Retrieve1Card-grabEvent-toHand-onTop5Cards-tellPlayer-isReact$$ShuffleDeck
+++++

.....
Peaceful Resistance
-----
ff4fb461-8060-457a-9c16-000000001492
-----
onPlay:DestroyTarget-Targeted-atEnhancement
+++++

.....
A New Hope
-----
ff4fb461-8060-457a-9c16-000000001493
-----
+++++

.....
Preparation and Planning
-----
ff4fb461-8060-457a-9c16-000000001494
-----
onResolveFate:SimplyAnnounce{reduce the cost of the next event they play this turn by 2}$$CreateDummy-nonUnique-isSilent-doNotDiscard||whileInPlay:Reduce2CostPlay-affectsEvent-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeEvent-onlyforDummy-isSilent||atTurnEnd:DestroyMyself-onlyforDummy-isSilent
+++++

.....
The Last Warrior
-----
ff4fb461-8060-457a-9c16-000000001495
-----
onHostGenerate:Put1Ignores Affiliation Match-AutoTargeted-isUnpaid||whileInPlay:PreventDraw-forOpponent-ifOrigHasMore-typeUnit_and_Specter
+++++

.....
Zeb Orrelios
-----
ff4fb461-8060-457a-9c16-000000001496
-----
ConstantAbility:TargetStrike-ifOrigHasMore-typeEnhancement
+++++

.....
Freelance Slicer
-----
ff4fb461-8060-457a-9c16-000000001497
-----
+++++
R0:Retrieve1Card-grabEnhancement-toTable-onTop1Cards-tellPlayer-isReact-onlyOnce

.....
Bo-Rifle
-----
ff4fb461-8060-457a-9c16-000000001498
-----
Placement:Specter_or_Smugglers and Spies_and_Character||BonusIcons:UD:1, EE-UD:1
+++++

.....
Improvised Defenses
-----
ff4fb461-8060-457a-9c16-000000001499
-----
Placement:Objective-targetAllied||onHostLeaving:ReturnMyself-isReact
+++++

.....
Well Equipped
-----
ff4fb461-8060-457a-9c16-000000001500
-----
onResolveFate:Remove1Focus-Targeted-atUnit_or_Objective
+++++

.....
The Emperor's Cabal
-----
ff4fb461-8060-457a-9c16-000000001501
-----
whileInPlay:Retrieve1Card-grabEvent-fromDiscard-toDeck-foreachForceStruggleDark-isReact$$ShuffleDeck
+++++

.....
Sim Aloo
-----
ff4fb461-8060-457a-9c16-000000001502
-----
+++++

.....
Imperial Senate Guard
-----
ff4fb461-8060-457a-9c16-000000001503
-----
whileInPlay:Put1Shield-AutoTargeted-atUnit_or_Objective_and_Sith-targetMine-choose1-hasntMarker{Shield}-foreachCardPlayed-byMe-typeEvent-isReact-onlyOnce
+++++

.....
Executive Override
-----
ff4fb461-8060-457a-9c16-000000001504
-----
+++++

.....
Cruel Procedures
-----
ff4fb461-8060-457a-9c16-000000001505
-----
onPlay:Remove1Damage-DemiAutoTargeted-atUnit_and_Sith-hasMarker{Damage}-targetMine-isParticipating-choose1-isCost$$Put1Damage-DemiAutoTargeted-atUnit-targetOpponents-isParticipating-choose1
+++++

.....
Preparation and Planning
-----
ff4fb461-8060-457a-9c16-000000001506
-----
onResolveFate:SimplyAnnounce{reduce the cost of the next event they play this turn by 2}$$CreateDummy-nonUnique-isSilent-doNotDiscard||whileInPlay:Reduce2CostPlay-affectsEvent-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeEvent-onlyforDummy-isSilent||atTurnEnd:DestroyMyself-onlyforDummy-isSilent
+++++

.....
Pattern Analysis
-----
ff4fb461-8060-457a-9c16-000000001507
-----
+++++

.....
Agent Kallus
-----
ff4fb461-8060-457a-9c16-000000001508
-----
+++++

.....
Academy Engineer
-----
ff4fb461-8060-457a-9c16-000000001509
-----
onPlay:Retrieve1Card-grabEnhancement-toHand-onTop5Cards-tellPlayer-isReact$$ShuffleDeck
+++++

.....
Squad Leader
-----
ff4fb461-8060-457a-9c16-000000001510
-----
Placement:Trooper_or_Character_and_Imperial Navy
+++++

.....
T-7 Ion Disruptor
-----
ff4fb461-8060-457a-9c16-000000001511
-----
Placement:Trooper_or_Character_and_Imperial Navy||BonusIcons:UD:1, EE-BD:1
+++++

.....
Well Equipped
-----
ff4fb461-8060-457a-9c16-000000001512
-----
onResolveFate:Remove1Focus-Targeted-atUnit_or_Objective
+++++

.....
I Don't Like You, Either
-----
ff4fb461-8060-457a-9c16-000000001513
-----
+++++

.....
Dr. Evazan
-----
ff4fb461-8060-457a-9c16-000000001514
-----
+++++

.....
Ponda Baba
-----
ff4fb461-8060-457a-9c16-000000001515
-----
+++++

.....
Coerced
-----
ff4fb461-8060-457a-9c16-000000001516
-----
Placement:Character-targetOpponents||onHostLeaving:CaptureTarget-DemiAutoTargeted-fromDeckOpponents-choose1-isReact
+++++

.....
Prized Possession
-----
ff4fb461-8060-457a-9c16-000000001517
-----
+++++

.....
He Doesn't Like You
-----
ff4fb461-8060-457a-9c16-000000001518
-----
+++++

.....
Daughter of Taanab
-----
ff4fb461-8060-457a-9c16-000000001519
-----
whileInPlay:Draw1Card-foreachCardPlayed-byMe-typeEvent-ifOrigmarkers{Damage}le2-onlyOnce-isReact
+++++

.....
Sarenda
-----
ff4fb461-8060-457a-9c16-000000001520
-----
onLeaving:Retrieve1Card-grabEvent-toHand-tellPlayer-isReact$$ShuffleDeck
+++++

.....
Cathar Defender
-----
ff4fb461-8060-457a-9c16-000000001521
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough||ExtraIcon:UD:1-ifOrigDefending
+++++

.....
Gotal Outcast
-----
ff4fb461-8060-457a-9c16-000000001522
-----
ExtraIcon:BD:2-ifHaveForce
+++++

.....
Return of the Jedi
-----
ff4fb461-8060-457a-9c16-000000001523
-----
onPlay:CustomScript
+++++

.....
Preparation and Planning
-----
ff4fb461-8060-457a-9c16-000000001524
-----
onResolveFate:SimplyAnnounce{reduce the cost of the next event they play this turn by 2}$$CreateDummy-nonUnique-isSilent-doNotDiscard||whileInPlay:Reduce2CostPlay-affectsEvent-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeEvent-onlyforDummy-isSilent||atTurnEnd:DestroyMyself-onlyforDummy-isSilent
+++++

.....
A Legend Begins
-----
ff4fb461-8060-457a-9c16-000000001525
-----
+++++
R0:DisengageTarget-DemiAutoTargeted-atUnit-isParticipating-choose1

.....
Wedge Antilles
-----
ff4fb461-8060-457a-9c16-000000001526
-----
onPlay:CustomScript||BonusIcons:UD:1, BD:1-ifHostSpeeder_or_Fighter
+++++

.....
Red Two
-----
ff4fb461-8060-457a-9c16-000000001527
-----
whileInPlay:Transfer1Focus-Targeted-atEnhancement-sourceEnhancement-hasMarker{Focus}-destinationEnhancement-foreachCardPlayed-byMe-typeEnhancement_and_Pilot-ifHostRed Two-isReact-onlyOnce
+++++

.....
Pilot Ready Room
-----
ff4fb461-8060-457a-9c16-000000001528
-----
whileInPlay:Reduce1CostPlay-affectsPilot-onlyOnce-forMe
+++++

.....
Tactical Planning
-----
ff4fb461-8060-457a-9c16-000000001529
-----
+++++

.....
Tactical Planning
-----
ff4fb461-8060-457a-9c16-000000001530
-----
+++++

.....
Resistance and Rebellion
-----
ff4fb461-8060-457a-9c16-000000001531
-----
+++++

.....
Nien Numb
-----
ff4fb461-8060-457a-9c16-000000001532
-----
onPlay:CustomScript||BonusIcons:UD:1, EE-T:1-ifHostTransport
+++++

.....
Loyal Co-Pilot
-----
ff4fb461-8060-457a-9c16-000000001533
-----
onPlay:CustomScript||onHostParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough-ifHostTransport
+++++

.....
YT-2000 Freighter
-----
ff4fb461-8060-457a-9c16-000000001534
-----
+++++

.....
Spacer Cantina
-----
ff4fb461-8060-457a-9c16-000000001535
-----
whileInPlay:Reduce1CostPlay-affectsPilot-onlyOnce-forMe
+++++

.....
Stay on Target
-----
ff4fb461-8060-457a-9c16-000000001536
-----
+++++

.....
Inexorable Destruction
-----
ff4fb461-8060-457a-9c16-000000001537
-----
+++++

.....
Admiral Screed
-----
ff4fb461-8060-457a-9c16-000000001538
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1
+++++

.....
Demolisher
-----
ff4fb461-8060-457a-9c16-000000001539
-----
+++++

.....
Nebulon-B2 Frigate
-----
ff4fb461-8060-457a-9c16-000000001540
-----
+++++

.....
Tactical Planning
-----
ff4fb461-8060-457a-9c16-000000001541
-----
+++++

.....
Tactical Planning
-----
ff4fb461-8060-457a-9c16-000000001542
-----
+++++

.....
Hunter in the Night
-----
ff4fb461-8060-457a-9c16-000000001543
-----
+++++

.....
Djas Puhr
-----
ff4fb461-8060-457a-9c16-000000001544
-----
ConstantAbility:TargetStrike-ifOrigHasProperty{Night}ge2
+++++

.....
Defel Mercenary
-----
ff4fb461-8060-457a-9c16-000000001545
-----
ExtraIcon:UD:1-perEveryNight
+++++

.....
Master of the Night
-----
ff4fb461-8060-457a-9c16-000000001546
-----
Placement:Unit_or_Objective_or_Enhancement-targetMine
+++++
R0:SendToBottomMyself$$SimplyAnnounce{cancel the card effect}$$ShuffleDeck

.....
Blaster Pistol
-----
ff4fb461-8060-457a-9c16-000000001547
-----
Placement:Character_and_Unit||BonusIcons:UD:1
+++++

.....
Well Equipped
-----
ff4fb461-8060-457a-9c16-000000001548
-----
onResolveFate:Remove1Focus-Targeted-atUnit_or_Objective
+++++

.....
Hero of a Thousand Devices
-----
ff4fb461-8060-457a-9c16-000000001549
-----
+++++

.....
R2-D2
-----
ff4fb461-8060-457a-9c16-000000001550
-----

+++++

.....
C-3PO
-----
ff4fb461-8060-457a-9c16-000000001551
-----
onPlay:DestroyTarget-Targeted-atEnhancement-hasProperty{Cost}le2-choose1-isReact
+++++

.....
2-1B Surgical Droid
-----
ff4fb461-8060-457a-9c16-000000001552
-----
+++++
R0:Remove1Damage-Targeted-atUnit_and_typenotVehicle-choose1-onlyOnce

.....
Grappling Arm
-----
ff4fb461-8060-457a-9c16-000000001553
-----
+++++

.....
Well Equipped
-----
ff4fb461-8060-457a-9c16-000000001554
-----
onResolveFate:Remove1Focus-Targeted-atUnit_or_Objective
+++++

.....
Sacrifice of Heroes
-----
ff4fb461-8060-457a-9c16-000000001555
-----
whileInPlay:Draw1Card-foreachCardLeavingPlay-typeUnit-byFriendlyOriginController-isReact
+++++

.....
Jek Porkins
-----
ff4fb461-8060-457a-9c16-000000001556
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-noTargetingError-maxReduce1||onHostLeaving:BringToPlayTarget-Targeted-atUnit_and_Rebel Alliance-choose1-ifHostFighter-isReact
+++++

.....
Red Six
-----
ff4fb461-8060-457a-9c16-000000001557
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atVehicle-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
R5-D8
-----
ff4fb461-8060-457a-9c16-000000001558
-----
+++++

.....
I've Got a Problem Here
-----
ff4fb461-8060-457a-9c16-000000001559
-----
onPlay:
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000001560
-----
onResolveFate:Put1Shield-Targeted-atUnit_or_Objective
+++++

.....
Threat from the Depths
-----
ff4fb461-8060-457a-9c16-000000001561
-----
+++++

.....
Dragonsnake
-----
ff4fb461-8060-457a-9c16-000000001562
-----
+++++

.....
Dragonsnake
-----
ff4fb461-8060-457a-9c16-000000001563
-----
+++++

.....
Endless Hunger
-----
ff4fb461-8060-457a-9c16-000000001564
-----
+++++

.....
Bestial Fury
-----
ff4fb461-8060-457a-9c16-000000001565
-----
+++++

.....
Feeding Frenzy
-----
ff4fb461-8060-457a-9c16-000000001566
-----
+++++

.....
Imperial Vengeance
-----
ff4fb461-8060-457a-9c16-000000001567
-----
whileInPlay:Deal2Damage-DemiAutoTargeted-atUnit-targetOpponents-choose1-foreachObjectiveThwarted-byFriendlyOriginController-isReact
+++++

.....
Avenger
-----
ff4fb461-8060-457a-9c16-000000001568
-----
whileInPlay:Deal1Damage-DemiAutoTargeted-atUnit-targetOpponents-choose1-foreachCardLeavingPlay-typeUnit-byFriendlyOriginController-onlyDuringEngagement-isReact
+++++

.....
Alpha-class Star Wing
-----
ff4fb461-8060-457a-9c16-000000001569
-----
+++++

.....
We Have Them
-----
ff4fb461-8060-457a-9c16-000000001570
-----
+++++

.....
Apology Accepted
-----
ff4fb461-8060-457a-9c16-000000001571
-----
onPlay:SacrificeTarget-Targeted-atUnit_and_Imperial Navy_and_Officer$$Remove999Focus-Targeted-atUnit_and_Imperial Navy_and_Vehicle
+++++

.....
Preparation and Planning
-----
ff4fb461-8060-457a-9c16-000000001572
-----
onResolveFate:SimplyAnnounce{reduce the cost of the next event they play this turn by 2}$$CreateDummy-nonUnique-isSilent-doNotDiscard||whileInPlay:Reduce2CostPlay-affectsEvent-onlyforDummy||whileInPlay:DestroyMyself-foreachCardPlayed-typeEvent-onlyforDummy-isSilent||atTurnEnd:DestroyMyself-onlyforDummy-isSilent
+++++

.....
His High Exaltedness
-----
ff4fb461-8060-457a-9c16-000000001573
-----
whileInPlay:Retrieve1Card-grabEvent_and_Scum and Villainy-fromDiscard-foreachObjectiveThwarted-isReact
+++++

.....
Jabba the Hutt
-----
ff4fb461-8060-457a-9c16-000000001574
-----
whileInPlay:Reduce2CostPlay-affectsBounty Hunter_or_Event_and_Scum and Villainy-onlyOnce-forMe
+++++

.....
Twi'lek Sycophant
-----
ff4fb461-8060-457a-9c16-000000001575
-----
onPlay:Retrieve1Card-grabEvent-toHand-onTop5Cards-tellPlayer-isReact$$ShuffleDeck
+++++

.....
Freelance Hunter
-----
ff4fb461-8060-457a-9c16-000000001576
-----
+++++

.....
Death Mark
-----
ff4fb461-8060-457a-9c16-000000001577
-----
Placement:Character_or_Droid-targetOpponents
+++++

.....
Hutt's Hospitality
-----
ff4fb461-8060-457a-9c16-000000001578
-----
onPlay:DestroyTarget-Targeted-atCharacter_or_Droid-hasProperty{Cost}le2-choose1
+++++

.....
Stand Together
-----
ff4fb461-8060-457a-9c16-000000001579
-----
ConstantEffect:Force2Bonus-ifOrigHasProperty{Specter_and_Unit}ge2
+++++

.....
Ezra Bridger
-----
ff4fb461-8060-457a-9c16-000000001580
-----
onStrike:SimplyAnnounce{Opponent must choose to either place 1 focus token on one of his participating units or discard 2 cards at random from his hand.}
+++++

.....
Loth-cat
-----
ff4fb461-8060-457a-9c16-000000001581
-----
+++++

.....
Stolen Helmet
-----
ff4fb461-8060-457a-9c16-000000001582
-----
Placement:Character_or_Specter
+++++

.....
Improvised Demolition
-----
ff4fb461-8060-457a-9c16-000000001583
-----
+++++

.....
Specter's Concentration
-----
ff4fb461-8060-457a-9c16-000000001584
-----
+++++

.....
Haunting the Empire
-----
ff4fb461-8060-457a-9c16-000000001585
-----
+++++

.....
Hera Syndulla
-----
ff4fb461-8060-457a-9c16-000000001586
-----
ConstantEffect:IncreaseUD:1-forAlly-typeUnit_and_Specter_or_Neutral_and_Unit||afterRefresh:Remove1Focus-DemiAutoTargeted-atSpecter-hasMarker{Focus}-targetAllied-choose1-duringMyTurn-isReact-onlyOnce
+++++

.....
Ghost
-----
ff4fb461-8060-457a-9c16-000000001587
-----
+++++
R0:Remove1Damage-DemiAutoTargeted-atSpecter-hasMarker{Damage}-choose1-isCost$$Put1Damage

.....
Phantom
-----
ff4fb461-8060-457a-9c16-000000001588
-----
+++++

.....
Hidden Outpost
-----
ff4fb461-8060-457a-9c16-000000001589
-----
+++++

.....
Call to Action
-----
ff4fb461-8060-457a-9c16-000000001590
-----
+++++

.....
On the Run
-----
ff4fb461-8060-457a-9c16-000000001591
-----
+++++

.....
BoShek
-----
ff4fb461-8060-457a-9c16-000000001592
-----
+++++

.....
R4-E1
-----
ff4fb461-8060-457a-9c16-000000001593
-----
+++++

.....
Make Your Own Resources
-----
ff4fb461-8060-457a-9c16-000000001594
-----
+++++

.....
Tricks and Nonsense
-----
ff4fb461-8060-457a-9c16-000000001595
-----
+++++

.....
Tricks and Nonsense
-----
ff4fb461-8060-457a-9c16-000000001596
-----
+++++

.....
Lure of the Lost
-----
ff4fb461-8060-457a-9c16-000000001597
-----
afterCardRefreshing:Put1Focus-isCost-isReact$$Retrieve1Card-fromDiscard-toDeck$$ShuffleDeck
+++++

.....
Rav Naaran
-----
ff4fb461-8060-457a-9c16-000000001598
-----
+++++

.....
Berserk Hunter
-----
ff4fb461-8060-457a-9c16-000000001599
-----
afterStrike:SacrificeMyself-isReact-isForced
+++++

.....
Berserk Hunter
-----
ff4fb461-8060-457a-9c16-000000001600
-----
afterStrike:SacrificeMyself-isReact-isForced
+++++

.....
Naaran's Lightsaber
-----
ff4fb461-8060-457a-9c16-000000001601
-----
Placement:Force User_or_Force Sensitive||ConstantEffect:Edge1Bonus-ifOrigParticipatingHost
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000001602
-----
onResolveFate:CustomScript
+++++

.....
Cloud Cover
-----
ff4fb461-8060-457a-9c16-000000001603
-----
+++++

.....
Howlrunner
-----
ff4fb461-8060-457a-9c16-000000001604
-----
onPlay:CustomScript||ConstantEffect:IncreaseUD:1-forAlly-typeFighter-ifHostVehicle
+++++

.....
Night Beast
-----
ff4fb461-8060-457a-9c16-000000001605
-----
onPlay:CustomScript||onPay:Reduce1CostPlay-perEveryVehicle-Targeted-atVehicle-noTargetingError-maxReduce1||afterEngagement:Remove1Focus-AutoTargeted-onHost-ifHostFighter-ifOrigParticipatingHost-isReact
+++++

.....
Obsidian Leader
-----
ff4fb461-8060-457a-9c16-000000001606
-----
+++++

.....
Obsidian 2
-----
ff4fb461-8060-457a-9c16-000000001607
-----
+++++

.....
Stay on Target
-----
ff4fb461-8060-457a-9c16-000000001608
-----
+++++

.....
Running the Canyon
-----
ff4fb461-8060-457a-9c16-000000001639
-----
+++++

.....
Luke's T-16 Skyhopper
-----
ff4fb461-8060-457a-9c16-000000001640
-----
whileInPlay:Deal1Damage-foreachCardPlayed-byMe-typeEvent-DemiAutoTargeted-atObjective-choose1-targetOpponents-onlyOnce-isReact
+++++

.....
T-16 Skyhopper
-----
ff4fb461-8060-457a-9c16-000000001641
-----
+++++

.....
Memories of Home
-----
ff4fb461-8060-457a-9c16-000000001642
-----
onPlay:Put1Shield-DemiAutoTargeted-atUnit-choose1-targetAllied
+++++

.....
Bull's-eye!
-----
ff4fb461-8060-457a-9c16-000000001643
-----
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000001644
-----
onResolveFate:Deal1Damage-AutoTargeted-atObjective-isParticipating-ifOrigAttacking
+++++

.....
Tiny Robotic Sociopath
-----
ff4fb461-8060-457a-9c16-000000001645
-----
+++++

.....
Chopper
-----
ff4fb461-8060-457a-9c16-000000001646
-----
+++++

.....
Captured Courier Droid
-----
ff4fb461-8060-457a-9c16-000000001647
-----
onPlay:SimplyAnnounce{Opponent must choose and discard 1 card from hand}-isReact
+++++

.....
Electroshock Prod
-----
ff4fb461-8060-457a-9c16-000000001648
-----
Placement:Specter_or_Droid
+++++

.....
Makeshift Repairs
-----
ff4fb461-8060-457a-9c16-000000001649
-----
+++++

.....
Improvised Tactics
-----
ff4fb461-8060-457a-9c16-000000001650
-----
+++++

.....
The Emperor's Shadow
-----
ff4fb461-8060-457a-9c16-000000001651
-----
whileInPlay:Draw1Card-foreachCardPlayed-byMe-typeEnhancement-onlyOnce-isReact
+++++

.....
The Emperor's Shuttle
-----
ff4fb461-8060-457a-9c16-000000001652
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Shuttle Pilot
-----
ff4fb461-8060-457a-9c16-000000001653
-----
onPlay:CustomScript||ConstantEffect:Edge1Bonus-ifOrigParticipatingHost
+++++

.....
The Emperor's Favor
-----
ff4fb461-8060-457a-9c16-000000001654
-----
Placement:Sith_and_Unit||BonusIcons:UD:1
+++++

.....
Sensor Array
-----
ff4fb461-8060-457a-9c16-000000001655
-----
+++++

.....
Well Equipped
-----
ff4fb461-8060-457a-9c16-000000001656
-----
onResolveFate:Remove1Focus-Targeted-atUnit_or_Objective
+++++

.....
Technological Terror
-----
ff4fb461-8060-457a-9c16-000000001657
-----
+++++

.....
Death Star
-----
ff4fb461-8060-457a-9c16-000000001658
-----
onParticipation:Put1Shield-AutoTargeted-atUnit_or_Objective-isParticipating-targetMine-choose1-hasntMarker{Shield}-notHARDCOREenough
+++++

.....
Fleet Navigator
-----
ff4fb461-8060-457a-9c16-000000001659
-----
+++++

.....
Death Star Engineer
-----
ff4fb461-8060-457a-9c16-000000001660
-----
+++++
R0:SacrificeMyself$$Remove1Focus-DemiAutoTargeted-atSpace Station_or_Capital Ship

.....
Death Star Engineer
-----
ff4fb461-8060-457a-9c16-000000001661
-----
+++++
R0:SacrificeMyself$$Remove1Focus-DemiAutoTargeted-atSpace Station_or_Capital Ship

.....
Control Room
-----
ff4fb461-8060-457a-9c16-000000001662
-----
+++++

.....
Heart of Cold
-----
ff4fb461-8060-457a-9c16-000000001663
-----
+++++

.....
IG-88C
-----
ff4fb461-8060-457a-9c16-000000001664
-----
+++++

.....
FEX-model Combat Droid
-----
ff4fb461-8060-457a-9c16-000000001665
-----
+++++

.....
Ugnaught
-----
ff4fb461-8060-457a-9c16-000000001666
-----
whileInPlay:Remove1Damage-DemiAutoTargeted-atUnit_and_Vehicle_or_Unit_and_Droid-targetMine-choose1-hasMarker{Damage}-foreachCardCaptured-isReact
+++++

.....
Tricks and Nonsense
-----
ff4fb461-8060-457a-9c16-000000001667
-----
+++++

.....
Tricks and Nonsense
-----
ff4fb461-8060-457a-9c16-000000001668
-----
+++++

.....
Guardians of Justice
-----
ff4fb461-8060-457a-9c16-000000001669
-----
+++++

.....
No Questions Asked
-----
ff4fb461-8060-457a-9c16-000000001670
-----
+++++

.....
Fighters for Freedom
-----
ff4fb461-8060-457a-9c16-000000001671
-----
+++++

.....
Information Network
-----
ff4fb461-8060-457a-9c16-000000001672
-----
+++++

.....
Desperate Allies
-----
ff4fb461-8060-457a-9c16-000000001673
-----
+++++

.....
Mercenary Contacts
-----
ff4fb461-8060-457a-9c16-000000001674
-----
+++++

.....
Galactic Enforcers
-----
ff4fb461-8060-457a-9c16-000000001675
-----
+++++

.....
Expendable Allies
-----
ff4fb461-8060-457a-9c16-000000001676
-----
+++++

.....
Dark Masters
-----
ff4fb461-8060-457a-9c16-000000001677
-----
+++++

.....
Any Methods Necessary
-----
ff4fb461-8060-457a-9c16-000000001678
-----
+++++

.....
Promise of Power
-----
ff4fb461-8060-457a-9c16-000000001679
-----
+++++

.....
Imperial Contractors
-----
ff4fb461-8060-457a-9c16-000000001680
-----
+++++

.....
Pushing Back the Empire
-----
ff4fb461-8060-457a-9c16-000000001681
-----
+++++

.....
Captain Cassian Andor
-----
ff4fb461-8060-457a-9c16-000000001682
-----
+++++

.....
Rebel Saboteur
-----
ff4fb461-8060-457a-9c16-000000001683
-----
+++++

.....
Rebel Saboteur
-----
ff4fb461-8060-457a-9c16-000000001684
-----
+++++

.....
Teamwork
-----
ff4fb461-8060-457a-9c16-000000001685
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001686
-----
+++++

.....
Spirit of Rebellion
-----
ff4fb461-8060-457a-9c16-000000001687
-----
+++++

.....
Jyn Erso
-----
ff4fb461-8060-457a-9c16-000000001688
-----
+++++

.....
Crafty Smuggler
-----
ff4fb461-8060-457a-9c16-000000001689
-----
+++++

.....
Necessary Alliances
-----
ff4fb461-8060-457a-9c16-000000001690
-----
+++++

.....
Well-Laid Ambush
-----
ff4fb461-8060-457a-9c16-000000001691
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001692
-----
+++++

.....
Rogue Archaeology
-----
ff4fb461-8060-457a-9c16-000000001693
-----
+++++

.....
Doctor Aphra
-----
ff4fb461-8060-457a-9c16-000000001694
-----
+++++

.....
BX-series Droid Commando
-----
ff4fb461-8060-457a-9c16-000000001695
-----
+++++

.....
Secret Information
-----
ff4fb461-8060-457a-9c16-000000001696
-----
+++++

.....
Reconstruction
-----
ff4fb461-8060-457a-9c16-000000001697
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001698
-----
+++++

.....
Immeasurable Power
-----
ff4fb461-8060-457a-9c16-000000001699
-----
+++++

.....
Director Krennic
-----
ff4fb461-8060-457a-9c16-000000001700
-----
+++++

.....
Death Trooper
-----
ff4fb461-8060-457a-9c16-000000001701
-----
+++++

.....
Death Trooper
-----
ff4fb461-8060-457a-9c16-000000001702
-----
+++++

.....
Death Trooper
-----
ff4fb461-8060-457a-9c16-000000001703
-----
+++++

.....
Assembly Area
-----
ff4fb461-8060-457a-9c16-000000001704
-----
+++++

.....
Trust in the Force
-----
ff4fb461-8060-457a-9c16-000000001705
-----
+++++

.....
Chirrut Imwe
-----
ff4fb461-8060-457a-9c16-000000001706
-----
+++++

.....
Mirialan Mystic
-----
ff4fb461-8060-457a-9c16-000000001707
-----
+++++

.....
Handcrafted Light Bow
-----
ff4fb461-8060-457a-9c16-000000001708
-----
+++++

.....
Stunning Blow
-----
ff4fb461-8060-457a-9c16-000000001709
-----
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000001710
-----
+++++

.....
Badge of Honor
-----
ff4fb461-8060-457a-9c16-000000001711
-----
+++++

.....
Wookiee Chieftain
-----
ff4fb461-8060-457a-9c16-000000001712
-----
+++++

.....
Wookiee Champion
-----
ff4fb461-8060-457a-9c16-000000001713
-----
+++++

.....
Wookiee Warrior
-----
ff4fb461-8060-457a-9c16-000000001714
-----
+++++

.....
Dense Wroshyr Forest
-----
ff4fb461-8060-457a-9c16-000000001715
-----
+++++

.....
Battle Fury
-----
ff4fb461-8060-457a-9c16-000000001716
-----
+++++

.....
Vader's Army
-----
ff4fb461-8060-457a-9c16-000000001717
-----
+++++

.....
0-0-0
-----
ff4fb461-8060-457a-9c16-000000001718
-----
+++++

.....
BT-1
-----
ff4fb461-8060-457a-9c16-000000001719
-----
+++++

.....
Forgotten Droid Factory
-----
ff4fb461-8060-457a-9c16-000000001720
-----
+++++

.....
Overwrite Protocol
-----
ff4fb461-8060-457a-9c16-000000001721
-----
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000001722
-----
+++++

.....
Cell Block Detention
-----
ff4fb461-8060-457a-9c16-000000001723
-----
+++++

.....
Lieutenant Childsen
-----
ff4fb461-8060-457a-9c16-000000001724
-----
+++++

.....
Security Trooper
-----
ff4fb461-8060-457a-9c16-000000001725
-----
+++++

.....
Security Trooper
-----
ff4fb461-8060-457a-9c16-000000001726
-----
+++++

.....
Security Alarm
-----
ff4fb461-8060-457a-9c16-000000001727
-----
+++++

.....
Security Protocols
-----
ff4fb461-8060-457a-9c16-000000001728
-----
+++++

.....
Shadowed Surveillance
-----
ff4fb461-8060-457a-9c16-000000001729
-----
+++++

.....
Garindan
-----
ff4fb461-8060-457a-9c16-000000001730
-----
+++++

.....
Trandoshan Mercenary
-----
ff4fb461-8060-457a-9c16-000000001731
-----
+++++

.....
Prized Possession
-----
ff4fb461-8060-457a-9c16-000000001732
-----
+++++

.....
Hidden Vibroknife
-----
ff4fb461-8060-457a-9c16-000000001733
-----
+++++

.....
Seeds of Decay
-----
ff4fb461-8060-457a-9c16-000000001734
-----
+++++

.....
Desert Recruitment
-----
ff4fb461-8060-457a-9c16-000000001735
-----
+++++

.....
Dice Ibegon
-----
ff4fb461-8060-457a-9c16-000000001736
-----
+++++

.....
Twi'lek Con Artist
-----
ff4fb461-8060-457a-9c16-000000001737
-----
+++++

.....
Necessary Alliances
-----
ff4fb461-8060-457a-9c16-000000001738
-----
+++++

.....
Unseen Sabotage
-----
ff4fb461-8060-457a-9c16-000000001739
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001740
-----
+++++

.....
The Lost Commander
-----
ff4fb461-8060-457a-9c16-000000001741
-----
+++++

.....
Captain Rex
-----
ff4fb461-8060-457a-9c16-000000001742
-----
+++++

.....
Battlefield Engineers
-----
ff4fb461-8060-457a-9c16-000000001743
-----
+++++

.....
Republic Supply Cache
-----
ff4fb461-8060-457a-9c16-000000001744
-----
+++++

.....
Necessary Alliances
-----
ff4fb461-8060-457a-9c16-000000001745
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001746
-----
+++++

.....
Bait and Switch
-----
ff4fb461-8060-457a-9c16-000000001747
-----
+++++

.....
Lak Sivrak
-----
ff4fb461-8060-457a-9c16-000000001748
-----
+++++

.....
Wolfman Scout
-----
ff4fb461-8060-457a-9c16-000000001749
-----
+++++

.....
Wolfman Scout
-----
ff4fb461-8060-457a-9c16-000000001750
-----
+++++

.....
Clever Distraction
-----
ff4fb461-8060-457a-9c16-000000001751
-----
+++++

.....
Seeds of Decay
-----
ff4fb461-8060-457a-9c16-000000001752
-----
+++++

.....
Knives in the Night
-----
ff4fb461-8060-457a-9c16-000000001753
-----
+++++

.....
Nightsister Matron
-----
ff4fb461-8060-457a-9c16-000000001754
-----
+++++

.....
Nightsister Warrior
-----
ff4fb461-8060-457a-9c16-000000001755
-----
+++++

.....
Nightsister Warrior
-----
ff4fb461-8060-457a-9c16-000000001756
-----
+++++

.....
Nightfall
-----
ff4fb461-8060-457a-9c16-000000001757
-----
+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000001758
-----
+++++

.....
Automated Assassin
-----
ff4fb461-8060-457a-9c16-000000001759
-----
+++++

.....
IG-88D
-----
ff4fb461-8060-457a-9c16-000000001760
-----
+++++

.....
Rogue B1 Battle Droid
-----
ff4fb461-8060-457a-9c16-000000001761
-----
+++++

.....
Bounty Listing
-----
ff4fb461-8060-457a-9c16-000000001762
-----
+++++

.....
Droid Uprising
-----
ff4fb461-8060-457a-9c16-000000001763
-----
+++++

.....
Security Protocols
-----
ff4fb461-8060-457a-9c16-000000001764
-----
+++++

.....
Native Blessings
-----
ff4fb461-8060-457a-9c16-000000001765
-----
+++++

.....
Logray
-----
ff4fb461-8060-457a-9c16-000000001766
-----
+++++

.....
Ewok Ally
-----
ff4fb461-8060-457a-9c16-000000001767
-----
+++++

.....
Ewok Ally
-----
ff4fb461-8060-457a-9c16-000000001768
-----
+++++

.....
Feast of Honor
-----
ff4fb461-8060-457a-9c16-000000001769
-----
+++++

.....
Ultimate Sacrifice
-----
ff4fb461-8060-457a-9c16-000000001770
-----
+++++

.....
They'll Never Stop Us
-----
ff4fb461-8060-457a-9c16-000000001771
-----
+++++

.....
Biggs Darklighter
-----
ff4fb461-8060-457a-9c16-000000001772
-----
+++++

.....
Red 3
-----
ff4fb461-8060-457a-9c16-000000001773
-----
+++++

.....
Red Squadron X-Wing
-----
ff4fb461-8060-457a-9c16-000000001774
-----
+++++

.....
Coordinated Strike
-----
ff4fb461-8060-457a-9c16-000000001775
-----
+++++

.....
Seeds of Decay
-----
ff4fb461-8060-457a-9c16-000000001776
-----
+++++

.....
From the Abyss
-----
ff4fb461-8060-457a-9c16-000000001777
-----
+++++

.....
Myo
-----
ff4fb461-8060-457a-9c16-000000001778
-----
+++++

.....
Abyssin Scout
-----
ff4fb461-8060-457a-9c16-000000001779
-----
+++++

.....
Shadows in the Night
-----
ff4fb461-8060-457a-9c16-000000001780
-----
+++++

.....
Regeneration
-----
ff4fb461-8060-457a-9c16-000000001781
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001782
-----
+++++

.....
Capital Support
-----
ff4fb461-8060-457a-9c16-000000001783
-----
+++++

.....
Corruptor
-----
ff4fb461-8060-457a-9c16-000000001784
-----
+++++

.....
Gamma Squadron TIE Bomber
-----
ff4fb461-8060-457a-9c16-000000001785
-----
+++++

.....
Gamma Squadron TIE Bomber
-----
ff4fb461-8060-457a-9c16-000000001786
-----
+++++

.....
Overwhelming Firepower
-----
ff4fb461-8060-457a-9c16-000000001787
-----
+++++

.....
Bombing Run
-----
ff4fb461-8060-457a-9c16-000000001788
-----
+++++

.....
Unsavory Contracts
-----
ff4fb461-8060-457a-9c16-000000001789
-----
+++++

.....
Black Krrsantan
-----
ff4fb461-8060-457a-9c16-000000001790
-----
+++++

.....
Aqualish Arms Dealer
-----
ff4fb461-8060-457a-9c16-000000001791
-----
+++++

.....
Underworld Contact
-----
ff4fb461-8060-457a-9c16-000000001792
-----
+++++

.....
Alliance of Evil
-----
ff4fb461-8060-457a-9c16-000000001793
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001794
-----
+++++

.....
Danger in the Wastes
-----
ff4fb461-8060-457a-9c16-000000001795
-----
+++++

.....
Obi-Wan Kenobi
-----
ff4fb461-8060-457a-9c16-000000001796
-----
+++++

.....
Steadfast Settler
-----
ff4fb461-8060-457a-9c16-000000001797
-----
+++++

.....
Obi-Wan's Robes
-----
ff4fb461-8060-457a-9c16-000000001798
-----
+++++

.....
Krayt Dragon Howl
-----
ff4fb461-8060-457a-9c16-000000001799
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001800
-----
+++++

.....
Inhospitable Deployments
-----
ff4fb461-8060-457a-9c16-000000001801
-----
+++++

.....
Major Bren Derlin
-----
ff4fb461-8060-457a-9c16-000000001802
-----
+++++

.....
Echo Scout
-----
ff4fb461-8060-457a-9c16-000000001803
-----
+++++

.....
Wilderness Fighters
-----
ff4fb461-8060-457a-9c16-000000001804
-----
+++++

.....
Evacuation Plan
-----
ff4fb461-8060-457a-9c16-000000001805
-----
+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000001806
-----
+++++

.....
Across the Dune Sea
-----
ff4fb461-8060-457a-9c16-000000001807
-----
+++++

.....
Dune Sea Hero
-----
ff4fb461-8060-457a-9c16-000000001808
-----
+++++

.....
Jawa Warrior
-----
ff4fb461-8060-457a-9c16-000000001809
-----
+++++

.....
Jawa Warrior
-----
ff4fb461-8060-457a-9c16-000000001810
-----
+++++

.....
Jawa Blaster
-----
ff4fb461-8060-457a-9c16-000000001811
-----
+++++

.....
Diversion
-----
ff4fb461-8060-457a-9c16-000000001812
-----
+++++

.....
Blizzard Assault
-----
ff4fb461-8060-457a-9c16-000000001813
-----
+++++

.....
General Veers
-----
ff4fb461-8060-457a-9c16-000000001814
-----
+++++

.....
Blizzard 1
-----
ff4fb461-8060-457a-9c16-000000001815
-----
+++++

.....
Blizzard 2
-----
ff4fb461-8060-457a-9c16-000000001816
-----
+++++

.....
Decisive Victory
-----
ff4fb461-8060-457a-9c16-000000001817
-----
+++++

.....
Battle of Hoth
-----
ff4fb461-8060-457a-9c16-000000001818
-----
+++++

.....
Patrolling the Wastes
-----
ff4fb461-8060-457a-9c16-000000001819
-----
+++++

.....
Klaatu
-----
ff4fb461-8060-457a-9c16-000000001820
-----
+++++

.....
Barada
-----
ff4fb461-8060-457a-9c16-000000001821
-----
+++++

.....
Cargo Skiff
-----
ff4fb461-8060-457a-9c16-000000001822
-----
+++++

.....
Shield Generator Modification
-----
ff4fb461-8060-457a-9c16-000000001823
-----
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000001824
-----
+++++

.....
Twilight of the Apprentice
-----
ff4fb461-8060-457a-9c16-000000001825
-----
+++++

.....
Ezra Bridger
-----
ff4fb461-8060-457a-9c16-000000001826
-----
+++++

.....
"Old Master"
-----
ff4fb461-8060-457a-9c16-000000001827
-----
+++++

.....
Ezra's Lightsaber
-----
ff4fb461-8060-457a-9c16-000000001828
-----
+++++

.....
Use Your Power
-----
ff4fb461-8060-457a-9c16-000000001829
-----
+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000001830
-----
+++++

.....
The Broken Horn
-----
ff4fb461-8060-457a-9c16-000000001831
-----
+++++

.....
Cikatro Vizago
-----
ff4fb461-8060-457a-9c16-000000001832
-----
+++++

.....
IG-RM Bodyguard Droid
-----
ff4fb461-8060-457a-9c16-000000001833
-----
+++++

.....
IG-RM Bodyguard Droid
-----
ff4fb461-8060-457a-9c16-000000001834
-----
+++++

.....
Payback
-----
ff4fb461-8060-457a-9c16-000000001835
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001836
-----
+++++

.....
Order of Inquisitors
-----
ff4fb461-8060-457a-9c16-000000001837
-----
+++++

.....
The Seventh Sister
-----
ff4fb461-8060-457a-9c16-000000001838
-----
+++++

.....
The Fifth Brother
-----
ff4fb461-8060-457a-9c16-000000001839
-----
+++++

.....
The Eighth Brother
-----
ff4fb461-8060-457a-9c16-000000001840
-----
+++++

.....
Double-bladed Lightsaber
-----
ff4fb461-8060-457a-9c16-000000001841
-----
+++++

.....
Press For Answers
-----
ff4fb461-8060-457a-9c16-000000001842
-----
+++++

.....
Support of the Fleet
-----
ff4fb461-8060-457a-9c16-000000001843
-----
+++++

.....
Relentless
-----
ff4fb461-8060-457a-9c16-000000001844
-----
+++++

.....
TIE Escort
-----
ff4fb461-8060-457a-9c16-000000001845
-----
+++++

.....
TIE Escort
-----
ff4fb461-8060-457a-9c16-000000001846
-----
+++++

.....
Imperial Influence
-----
ff4fb461-8060-457a-9c16-000000001847
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001848
-----
+++++

.....
Double-Crossing Droid
-----
ff4fb461-8060-457a-9c16-000000001849
-----
+++++

.....
8t88
-----
ff4fb461-8060-457a-9c16-000000001850
-----
+++++

.....
Twi'lek Sycophant
-----
ff4fb461-8060-457a-9c16-000000001851
-----
+++++

.....
Secret Information
-----
ff4fb461-8060-457a-9c16-000000001852
-----
+++++

.....
Chain Reaction
-----
ff4fb461-8060-457a-9c16-000000001853
-----
+++++

.....
Allies of Necessity
-----
ff4fb461-8060-457a-9c16-000000001854
-----
+++++

.....
Legends Emerge
-----
ff4fb461-8060-457a-9c16-000000001855
-----
+++++

.....
Kyle Katarn
-----
ff4fb461-8060-457a-9c16-000000001856
-----
+++++

.....
Sulon Sympathizer
-----
ff4fb461-8060-457a-9c16-000000001857
-----
+++++

.....
The Way of the Jedi
-----
ff4fb461-8060-457a-9c16-000000001858
-----
+++++

.....
Qu Rahn&#39;s Lightsaber
-----
ff4fb461-8060-457a-9c16-000000001859
-----
+++++

.....
Temptation
-----
ff4fb461-8060-457a-9c16-000000001860
-----
+++++

.....
The Power of the Valley
-----
ff4fb461-8060-457a-9c16-000000001861
-----
+++++

.....
Trapped Spirit
-----
ff4fb461-8060-457a-9c16-000000001862
-----
+++++

.....
Trapped Spirit
-----
ff4fb461-8060-457a-9c16-000000001863
-----
+++++

.....
Nexus of Power
-----
ff4fb461-8060-457a-9c16-000000001864
-----
+++++

.....
Nexus of Power
-----
ff4fb461-8060-457a-9c16-000000001865
-----
+++++

.....
My Ally is the Force
-----
ff4fb461-8060-457a-9c16-000000001866
-----
+++++

.....
Venerating Lady Vader
-----
ff4fb461-8060-457a-9c16-000000001867
-----
+++++

.....
Khabarakh
-----
ff4fb461-8060-457a-9c16-000000001868
-----
+++++

.....
Noghri Commando
-----
ff4fb461-8060-457a-9c16-000000001869
-----
+++++

.....
Free From Slavery
-----
ff4fb461-8060-457a-9c16-000000001870
-----
+++++

.....
Uncertain Loyalties
-----
ff4fb461-8060-457a-9c16-000000001871
-----
+++++

.....
Subtle Sabotage
-----
ff4fb461-8060-457a-9c16-000000001872
-----
+++++

.....
Concealed Heritage
-----
ff4fb461-8060-457a-9c16-000000001873
-----
+++++

.....
Corran Horn
-----
ff4fb461-8060-457a-9c16-000000001874
-----
+++++

.....
Rogue Nine
-----
ff4fb461-8060-457a-9c16-000000001875
-----
+++++

.....
Corran&#39;s Lightsaber
-----
ff4fb461-8060-457a-9c16-000000001876
-----
+++++

.....
His Father&#39;s Message
-----
ff4fb461-8060-457a-9c16-000000001877
-----
+++++

.....
Jedi Reflexes
-----
ff4fb461-8060-457a-9c16-000000001878
-----
+++++

.....
The Future of the Jedi
-----
ff4fb461-8060-457a-9c16-000000001879
-----
+++++

.....
Promising Student
-----
ff4fb461-8060-457a-9c16-000000001880
-----
+++++

.....
Promising Student
-----
ff4fb461-8060-457a-9c16-000000001881
-----
+++++

.....
The Jedi Praxeum
-----
ff4fb461-8060-457a-9c16-000000001882
-----
+++++

.....
The New Order
-----
ff4fb461-8060-457a-9c16-000000001883
-----
+++++

.....
Twist of Fate
-----
ff4fb461-8060-457a-9c16-000000001884
-----
+++++

.....
Duty and Loyalty
-----
ff4fb461-8060-457a-9c16-000000001885
-----
+++++

.....
Corran Horn
-----
ff4fb461-8060-457a-9c16-000000001886
-----
+++++

.....
Rogue Five
-----
ff4fb461-8060-457a-9c16-000000001887
-----
+++++

.....
Scouting Vessel
-----
ff4fb461-8060-457a-9c16-000000001888
-----
+++++

.....
Whistler
-----
ff4fb461-8060-457a-9c16-000000001889
-----
+++++

.....
Torpedo Lock
-----
ff4fb461-8060-457a-9c16-000000001890
-----
+++++

.....
Covert Operation
-----
ff4fb461-8060-457a-9c16-000000001891
-----
+++++

.....
Jan Ors
-----
ff4fb461-8060-457a-9c16-000000001892
-----
+++++

.....
Rebel Guerrilla
-----
ff4fb461-8060-457a-9c16-000000001893
-----
+++++

.....
Staging Post
-----
ff4fb461-8060-457a-9c16-000000001894
-----
+++++

.....
Espionage
-----
ff4fb461-8060-457a-9c16-000000001895
-----
+++++

.....
Supporting Fire
-----
ff4fb461-8060-457a-9c16-000000001896
-----
+++++

.....
Stealing Secrets
-----
ff4fb461-8060-457a-9c16-000000001897
-----
+++++

.....
Borsk Fey&#39;lya
-----
ff4fb461-8060-457a-9c16-000000001898
-----
+++++

.....
Insightful Infiltrator
-----
ff4fb461-8060-457a-9c16-000000001899
-----
+++++

.....
Bothan Spy
-----
ff4fb461-8060-457a-9c16-000000001900
-----
+++++

.....
Political Clout
-----
ff4fb461-8060-457a-9c16-000000001901
-----
+++++

.....
Fatal Flaw
-----
ff4fb461-8060-457a-9c16-000000001902
-----
+++++

.....
The New Republic&#39;s Finest
-----
ff4fb461-8060-457a-9c16-000000001903
-----
+++++

.....
Wedge Antilles
-----
ff4fb461-8060-457a-9c16-000000001904
-----
+++++

.....
Rogue Leader
-----
ff4fb461-8060-457a-9c16-000000001905
-----
+++++

.....
Dedicated Bacta Supply
-----
ff4fb461-8060-457a-9c16-000000001906
-----
+++++

.....
Do The Impossible
-----
ff4fb461-8060-457a-9c16-000000001907
-----
+++++

.....
Stay on Target
-----
ff4fb461-8060-457a-9c16-000000001908
-----
+++++

.....
Games of Deception
-----
ff4fb461-8060-457a-9c16-000000001909
-----
+++++

.....
Wes Janson
-----
ff4fb461-8060-457a-9c16-000000001910
-----
+++++

.....
Pirated Interceptor
-----
ff4fb461-8060-457a-9c16-000000001911
-----
+++++

.....
Pirated Interceptor
-----
ff4fb461-8060-457a-9c16-000000001912
-----
+++++

.....
Lt&#46; Kettch
-----
ff4fb461-8060-457a-9c16-000000001913
-----
+++++

.....
&#34;Faulty&#34; Comms Board
-----
ff4fb461-8060-457a-9c16-000000001914
-----
+++++

.....
Veiled Rebellion
-----
ff4fb461-8060-457a-9c16-000000001915
-----
+++++

.....
General Garm Bel Iblis
-----
ff4fb461-8060-457a-9c16-000000001916
-----
+++++

.....
Naval Strategist
-----
ff4fb461-8060-457a-9c16-000000001917
-----
+++++

.....
Oppressed Citizen
-----
ff4fb461-8060-457a-9c16-000000001918
-----
+++++

.....
Local Support
-----
ff4fb461-8060-457a-9c16-000000001919
-----
+++++

.....
Reserve Forces
-----
ff4fb461-8060-457a-9c16-000000001920
-----
+++++

.....
Bargaining for Profit
-----
ff4fb461-8060-457a-9c16-000000001921
-----
+++++

.....
Booster Terrik
-----
ff4fb461-8060-457a-9c16-000000001922
-----
+++++

.....
Errant Venture
-----
ff4fb461-8060-457a-9c16-000000001923
-----
+++++

.....
Business Partner
-----
ff4fb461-8060-457a-9c16-000000001924
-----
+++++

.....
Cloud City Casino
-----
ff4fb461-8060-457a-9c16-000000001925
-----
+++++

.....
Expert Haggling
-----
ff4fb461-8060-457a-9c16-000000001926
-----
+++++

.....
Under the Radar
-----
ff4fb461-8060-457a-9c16-000000001927
-----
+++++

.....
Wild Karrde
-----
ff4fb461-8060-457a-9c16-000000001928
-----
+++++

.....
Cargo Hauler
-----
ff4fb461-8060-457a-9c16-000000001929
-----
+++++

.....
Personal Modifications
-----
ff4fb461-8060-457a-9c16-000000001930
-----
+++++

.....
Legitimate Business
-----
ff4fb461-8060-457a-9c16-000000001931
-----
+++++

.....
Flase Indentification
-----
ff4fb461-8060-457a-9c16-000000001932
-----
+++++

.....
Endless Boredom
-----
ff4fb461-8060-457a-9c16-000000001933
-----
+++++

.....
Zakarisz Ghent
-----
ff4fb461-8060-457a-9c16-000000001934
-----
+++++

.....
Freelance Operative
-----
ff4fb461-8060-457a-9c16-000000001935
-----
+++++

.....
Old Imperial Code
-----
ff4fb461-8060-457a-9c16-000000001936
-----
+++++

.....
Evading Authority
-----
ff4fb461-8060-457a-9c16-000000001937
-----
+++++

.....
Betrayal
-----
ff4fb461-8060-457a-9c16-000000001938
-----
+++++

.....
Wraiths From the Sky
-----
ff4fb461-8060-457a-9c16-000000001939
-----
+++++

.....
Kell Tainer
-----
ff4fb461-8060-457a-9c16-000000001940
-----
+++++

.....
Garik &#34;Face&#34; Loran
-----
ff4fb461-8060-457a-9c16-000000001941
-----
+++++

.....
Wraith Squadron X-Wing
-----
ff4fb461-8060-457a-9c16-000000001942
-----
+++++

.....
Hawkbat Base
-----
ff4fb461-8060-457a-9c16-000000001943
-----
+++++

.....
Impersonating the Crew
-----
ff4fb461-8060-457a-9c16-000000001944
-----
+++++

.....
The Hostile Jungle
-----
ff4fb461-8060-457a-9c16-000000001945
-----
+++++

.....
Drang
-----
ff4fb461-8060-457a-9c16-000000001946
-----
+++++

.....
Sturm
-----
ff4fb461-8060-457a-9c16-000000001947
-----
+++++

.....
Ysalamiri
-----
ff4fb461-8060-457a-9c16-000000001948
-----
+++++

.....
Ysalamiri
-----
ff4fb461-8060-457a-9c16-000000001949
-----
+++++

.....
Echoes of the Force
-----
ff4fb461-8060-457a-9c16-000000001950
-----
+++++

.....
Tomb of Darkness
-----
ff4fb461-8060-457a-9c16-000000001951
-----
+++++

.....
Dark Specter
-----
ff4fb461-8060-457a-9c16-000000001952
-----
+++++

.....
Dark Specter
-----
ff4fb461-8060-457a-9c16-000000001953
-----
+++++

.....
Nexus of Power
-----
ff4fb461-8060-457a-9c16-000000001954
-----
+++++

.....
Nexus of Power
-----
ff4fb461-8060-457a-9c16-000000001955
-----
+++++

.....
Well Equipped
-----
ff4fb461-8060-457a-9c16-000000001956
-----
+++++

.....
Reconditioning Techniques
-----
ff4fb461-8060-457a-9c16-000000001957
-----
+++++

.....
Ysanne Isard
-----
ff4fb461-8060-457a-9c16-000000001958
-----
+++++

.....
Lusankya Interrogator
-----
ff4fb461-8060-457a-9c16-000000001959
-----
+++++

.....
Solitary Confinement
-----
ff4fb461-8060-457a-9c16-000000001960
-----
+++++

.....
Official Inquiry
-----
ff4fb461-8060-457a-9c16-000000001961
-----
+++++

.....
Betrayal
-----
ff4fb461-8060-457a-9c16-000000001962
-----
+++++

.....
The Dark Youth
-----
ff4fb461-8060-457a-9c16-000000001963
-----
+++++

.....
Yun
-----
ff4fb461-8060-457a-9c16-000000001964
-----
+++++

.....
Sulon Garrison
-----
ff4fb461-8060-457a-9c16-000000001965
-----
+++++

.....
Sulon Garrison
-----
ff4fb461-8060-457a-9c16-000000001966
-----
+++++

.....
Yun&#39;s Lightsaber
-----
ff4fb461-8060-457a-9c16-000000001967
-----
+++++

.....
Force Blinding
-----
ff4fb461-8060-457a-9c16-000000001968
-----
+++++

.....
Engineered Suffering
-----
ff4fb461-8060-457a-9c16-000000001969
-----
+++++

.....
Evir Derricote
-----
ff4fb461-8060-457a-9c16-000000001970
-----
+++++

.....
Research Officer
-----
ff4fb461-8060-457a-9c16-000000001971
-----
+++++

.....
The Krytos Virus
-----
ff4fb461-8060-457a-9c16-000000001972
-----
+++++

.....
The Krytos Virus
-----
ff4fb461-8060-457a-9c16-000000001973
-----
+++++

.....
Uncontrolled Plague
-----
ff4fb461-8060-457a-9c16-000000001974
-----
+++++

.....
I Rule
-----
ff4fb461-8060-457a-9c16-000000001975
-----
+++++

.....
Joruus C&#39;baoth
-----
ff4fb461-8060-457a-9c16-000000001976
-----
+++++

.....
Oppressed Citizen
-----
ff4fb461-8060-457a-9c16-000000001977
-----
+++++

.....
Enslaved
-----
ff4fb461-8060-457a-9c16-000000001978
-----
+++++

.....
Force of Will
-----
ff4fb461-8060-457a-9c16-000000001979
-----
+++++

.....
Force Storm
-----
ff4fb461-8060-457a-9c16-000000001980
-----
+++++

.....
Pellaeon&#39;s Plan
-----
ff4fb461-8060-457a-9c16-000000001981
-----
+++++

.....
Captain Gilad Pellaeon
-----
ff4fb461-8060-457a-9c16-000000001982
-----
+++++

.....
TIE Defense Wing
-----
ff4fb461-8060-457a-9c16-000000001983
-----
+++++

.....
Engineering Deck
-----
ff4fb461-8060-457a-9c16-000000001984
-----
+++++

.....
Minor Setback
-----
ff4fb461-8060-457a-9c16-000000001985
-----
+++++

.....
Protection
-----
ff4fb461-8060-457a-9c16-000000001986
-----
+++++

.....
Advanced Designs
-----
ff4fb461-8060-457a-9c16-000000001987
-----
+++++

.....
Phase II Dark Trooper
-----
ff4fb461-8060-457a-9c16-000000001988
-----
+++++

.....
Phase II Dark Trooper
-----
ff4fb461-8060-457a-9c16-000000001989
-----
+++++

.....
Supply Station
-----
ff4fb461-8060-457a-9c16-000000001990
-----
+++++

.....
Successful Demonstration
-----
ff4fb461-8060-457a-9c16-000000001991
-----
+++++

.....
Suppression Tactics
-----
ff4fb461-8060-457a-9c16-000000001992
-----
+++++

.....
Experimental Weaponry
-----
ff4fb461-8060-457a-9c16-000000001993
-----
+++++

.....
Weapons Developer
-----
ff4fb461-8060-457a-9c16-000000001994
-----
+++++

.....
Weapons Developer
-----
ff4fb461-8060-457a-9c16-000000001995
-----
+++++

.....
Phase III Dark Trooper Armor
-----
ff4fb461-8060-457a-9c16-000000001996
-----
+++++

.....
Private Research Facility
-----
ff4fb461-8060-457a-9c16-000000001997
-----
+++++

.....
Deadly Weaponry
-----
ff4fb461-8060-457a-9c16-000000001998
-----
+++++

.....
Private Death Commandos
-----
ff4fb461-8060-457a-9c16-000000001999
-----
+++++

.....
Ruhk
-----
ff4fb461-8060-457a-9c16-000000002000
-----
+++++

.....
Noghri Commando
-----
ff4fb461-8060-457a-9c16-000000002001
-----
+++++

.....
Kidnapping Target
-----
ff4fb461-8060-457a-9c16-000000002002
-----
+++++

.....
Command Meditation Chamber
-----
ff4fb461-8060-457a-9c16-000000002003
-----
+++++

.....
Target of Opportunity
-----
ff4fb461-8060-457a-9c16-000000002004
-----
+++++

.....
The Grand Admiral&#39;s Strategy
-----
ff4fb461-8060-457a-9c16-000000002005
-----
+++++

.....
Ysalamiri
-----
ff4fb461-8060-457a-9c16-000000002006
-----
+++++

.....
Ysalamiri
-----
ff4fb461-8060-457a-9c16-000000002007
-----
+++++

.....
Ysalamiri
-----
ff4fb461-8060-457a-9c16-000000002008
-----
+++++

.....
Cultural Art Records
-----
ff4fb461-8060-457a-9c16-000000002009
-----
+++++

.....
The Emperor&#39;s Reserves
-----
ff4fb461-8060-457a-9c16-000000002010
-----
+++++

.....
Commanding the Remnant
-----
ff4fb461-8060-457a-9c16-000000002011
-----
+++++

.....
Warlord Zsinj
-----
ff4fb461-8060-457a-9c16-000000002012
-----
+++++

.....
SpecForce Raptor
-----
ff4fb461-8060-457a-9c16-000000002013
-----
+++++

.....
SpecForce Raptor
-----
ff4fb461-8060-457a-9c16-000000002014
-----
+++++

.....
Withering Fire
-----
ff4fb461-8060-457a-9c16-000000002015
-----
+++++

.....
Preparation and Planning
-----
ff4fb461-8060-457a-9c16-000000002016
-----
+++++

.....
The Ruthless Hunter
-----
ff4fb461-8060-457a-9c16-000000002017
-----
+++++

.....
Dengar
-----
ff4fb461-8060-457a-9c16-000000002018
-----
+++++

.....
Punishing One
-----
ff4fb461-8060-457a-9c16-000000002019
-----
+++++

.....
Scouting Vessel
-----
ff4fb461-8060-457a-9c16-000000002020
-----
+++++

.....
Astromech Gunner
-----
ff4fb461-8060-457a-9c16-000000002021
-----
+++++

.....
Explosive Charge
-----
ff4fb461-8060-457a-9c16-000000002022
-----
+++++

.....
Dangerous Criminals
-----
ff4fb461-8060-457a-9c16-000000002023
-----
+++++

.....
Bossk
-----
ff4fb461-8060-457a-9c16-000000002024
-----
+++++

.....
Hound&#39;s Tooth
-----
ff4fb461-8060-457a-9c16-000000002025
-----
+++++

.....
Prized Possession
-----
ff4fb461-8060-457a-9c16-000000002026
-----
+++++

.....
Picked Up
-----
ff4fb461-8060-457a-9c16-000000002027
-----
+++++

.....
Heat of Battle
-----
ff4fb461-8060-457a-9c16-000000002028
-----
+++++

.....
Double-Cross on Nar Shaddaa
-----
ff4fb461-8060-457a-9c16-000000002029
-----
+++++

.....
8t88
-----
ff4fb461-8060-457a-9c16-000000002030
-----
+++++

.....
Freelance Operative
-----
ff4fb461-8060-457a-9c16-000000002031
-----
+++++

.....
Stolen Data Disk
-----
ff4fb461-8060-457a-9c16-000000002032
-----
+++++

.....
Decrypting Station
-----
ff4fb461-8060-457a-9c16-000000002033
-----
+++++

.....
Intercepted Transmission
-----
ff4fb461-8060-457a-9c16-000000002034
-----
+++++

.....
Pursuing the Bounty
-----
ff4fb461-8060-457a-9c16-000000002035
-----
+++++

.....
IG-88
-----
ff4fb461-8060-457a-9c16-000000002036
-----
+++++

.....
IG-2000
-----
ff4fb461-8060-457a-9c16-000000002037
-----
+++++

.....
Inertial Dampeners
-----
ff4fb461-8060-457a-9c16-000000002038
-----
+++++

.....
Holowan Manufactory
-----
ff4fb461-8060-457a-9c16-000000002039
-----
+++++

.....
Segnor&#39;s Loop
-----
ff4fb461-8060-457a-9c16-000000002040
-----
+++++

.....
The Long Pursuit
-----
ff4fb461-8060-457a-9c16-000000002041
-----
+++++

.....
Zuckuss
-----
ff4fb461-8060-457a-9c16-000000002042
-----
+++++

.....
4-LOM
-----
ff4fb461-8060-457a-9c16-000000002043
-----
+++++

.....
Mist Hunter
-----
ff4fb461-8060-457a-9c16-000000002044
-----
+++++

.....
The Uncanny One
-----
ff4fb461-8060-457a-9c16-000000002045
-----
+++++

.....
Stay on Target
-----
ff4fb461-8060-457a-9c16-000000002046
-----
+++++

.....
ENDSCRIPTS
=====
'''
