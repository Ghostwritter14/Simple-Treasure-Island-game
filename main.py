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
/______/______/______/______/______/______/______/______/______/______/________
''')
print("Welcome to Treasure Island game.")
print("Your mission is to find the treasure.")
choice1 = input("You are at the crossroad. which direction do you choose: ")

if choice1 == "left":
    print('There is an island across the river traveller. '
          'You can either swim towards it or you can wait for the boat. '
          'What do you choose: "swim" or "wait". ')
    choice2 = input('What do you choose traveller: "swim" or "wait":').lower()
    if choice2 == "wait":
        print('You arrived at the island unharmed and safe. '
              'There is the castle ahead with 3 doors. '
              'Which do you choose traveller: "Red", "Blue", "Yellow". \n')
        choice3 = input('What do you choose traveller: "Red", "Blue", "Yellow". \n').lower()
        if choice3 == "red":
            print("Its a room full of fire. Game Over.")
            print('''
                 (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
        if choice3 == "blue":
            print("You have entered the room which houses the monster of the island. '\n' Game Over")
            print('''
                               (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \     ( '        )(    )
      \   \    \.  _.__ ____( .  |
       \  /\   .(   .'  /\  '.  )
        \(  \.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
                        ''')
        if choice3 == "yellow":
            print("Congratulations Traveller '\n' You won the game.")
            print("""
             __________
        /\____;;___|
       | /         /
       `. ())oo() .
        |\(%()*^^()^|
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
            
            """)
    else:
        print("The sharks have attacked you and you are drowning. \n Game Over.")
        print('''
        ,|
     / ;
    /  |
   : ,'(
   |( `.|
   : \  `\       \.
    \ `.         | `.
     \  `-._     ;   |
      \     ``-.'.. _ `._
       `. `-.            ```-...__
        .'`.        --..        0  ``-..____
      ,'.-'`,_-._            ((((   ._``,_<               `-\,-'`-'      ~
_________,'       `' `/
                                                  ~~
        ~~                    ~             ~
        ''')
else:
    print("You fell into a hole. Game over.")



