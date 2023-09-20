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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

crossroad = input('Are you at a crossroads, where would you like to go? Type "left" or "right"\n')
if crossroad.lower() == "right":
  print ("You fell into a hole. Game Over!")
elif crossroad.lower() == "left":
  lake = input('You come to a lake and there is an island in the middle. Type "wait" to wait for the boat or type "swim" to swim across.\n')
  if lake.lower() == "wait":
    print ("You were ambushed by bandits. Game Over!")
  elif lake.lower() == "swim":
    door = input("You swim to the island. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if door.lower() == "red":
      print ("You enter a room of tigers. Game Over!")
    elif door.lower() == "yellow":
      print ("You enter a room of fire. Game Over!")
    elif door.lower() == "blue":
      print ("You found the treasure. Good Job!")
else:
  print ("Game Over!")
