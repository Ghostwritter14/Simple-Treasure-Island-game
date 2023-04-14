import PySimpleGUI as sg

def run_game():
    # Define the default GUI layout
    layout = [
        [sg.Image(filename='treasure_island.png')],
        [sg.Text('Welcome to Treasure Island game.')],
        [sg.Text('Your mission is to find the treasure.')],
        [sg.Text('You are at the crossroad. Which direction do you choose?')],
        [sg.Button('Left'), sg.Button('Right')],
    ]

    # Create the GUI window
    window = sg.Window('Treasure Island Game', layout)

    # Run the GUI event loop
    while True:
        event, values = window.read()

        # Exit the event loop if the user closes the window or clicks the "Cancel" button
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        # Handle the user's choice
        if event == 'Left':
            layout = [
                [sg.Image(filename='treasure_island.png')],
                [sg.Text('There is an island across the river.')],
                [sg.Text('You can either swim towards it or you can wait for the boat.')],
                [sg.Text('What do you choose: "swim" or "wait"?')],
                [sg.Button('Swim'), sg.Button('Wait')],
            ]
            window.close()
            window = sg.Window('Treasure Island Game', layout)

        elif event == 'Right':
            sg.popup('Game Over', 'You fell into a hole. Goodbye!')
            break

        elif event == 'Swim':
            sg.popup('Game Over', 'The sharks have attacked you and you are drowning. Goodbye!')
            break

        elif event == 'Wait':
            layout = [
                [sg.Image(filename='treasure_island.png')],
                [sg.Text('You arrived at the island unharmed and safe.')],
                [sg.Text('There is the castle ahead with 3 doors.')],
                [sg.Text('Which do you choose?')],
                [sg.Button('Red'), sg.Button('Blue'), sg.Button('Yellow')],
            ]
            window.close()
            window = sg.Window('Treasure Island Game', layout)

        elif event == 'Red':
            sg.popup('Game Over', 'It\'s a room full of fire. Goodbye!')
            break

        elif event == 'Blue':
            sg.popup('Game Over', 'You have entered the room which houses the monster of the island. Goodbye!')
            break

        elif event == 'Yellow':
            sg.popup('Congratulations!', 'You won the game.')
            break

    # Close the GUI window
    window.close()

    # Ask the user if they want to play again
    play_again = sg.popup_yes_no('Do you want to play again?')

    if play_again == 'Yes':
        run_game()


# Start the game
run_game()



