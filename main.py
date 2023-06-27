print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line

Left_Or_Right = input('You find yourself at a cross road. Where do you want to go? Type "Left" or "Right"\n').lower()
if Left_Or_Right == "left":
  Swim_or_Wait = input('You go left. You\'ve come to a lake. It appears that there is a small island in the center of the lake. The island is but a 3 minute swim away. You\'re drawn to this island for some reason or another... What do you do? "Swim" or "Wait"?\n').lower()
  if Swim_or_Wait == "wait":
    Which_Door = input('You wait. After a time, a boat appears. This boat appears to take you to the island at the center of the lake. You board the boat looking for the captain, and the boat immediately takes off. There is no sign of life onboard. You arrive at the isalnd a short time later, only to discover a shack with three doors. Nothing more, nothing less. Every ounce of you screams to ignore the doors; however, you\'re compelled by some force to open one. Do you open the "Red," "Blue," or "Yellow" door?/n').lower()
    if Which_Door == "yellow":
      print("You win!")
    else:
      print("Before you can grab the handle, you black out. You awake to find yourself stranded on this island, no shack in sight, and no trace of a boat to be found. Game over!")
  else:
    print('You proceed to swim. A minute in to your swim you feel something brush your leg. You panic. Before you have time to process anything, you are swallowed whole. Game over!')
else:
  print('You go right. Out of nowhere, a hole opens up in the ground and are swallowed whole! Game over!')