print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
#.lower after () makes variable save as lowercase
direction=input("You are at a cross road which way would you like to go? "
                "\n Type 'l' for left or 'r' for right:").lower()
if direction=="r":
    print("You fell in a hole! GAME OVER!")
elif direction=="l":
    swim_or_wait=input('You are at a stream. Do you swim or wait?'
                       '\n Type "s" for swim and "w" for wait.')
    if swim_or_wait=="s" or swim_or_wait=="S":
        print("You have drowned! GAME OVER!")

    elif swim_or_wait=="w" or swim_or_wait=="W":
        door =input("You have arrived at the castle. Which door do you choose?"
                    "\n Type 'r' for red, 'y' for yellow, or 'b' for blue.")
        if door == "y" or door =="Y":
            print("Congratulations you found the Treasure!!!")
        else:
            print("The dragon attacks you! Game Over!")
    else:
        print("You have not made a valid selection. Pick swim or wait!")
else:
    print("You have not made a valid selection. It's left or right only!")
