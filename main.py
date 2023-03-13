print("*************TIC TAC TOE**************")
from tabulate import tabulate
import os

my_values = dict(
    value1="1",
    value2="2",
    value3="3",
    value4="4",
    value5="5",
    value6="6",
    value7="7",
    value8="8",
    value9="9"
)

def check():
    values_to_list = [my_values['value1'], my_values['value2'], my_values['value3'], my_values['value4'],
                      my_values['value5'], my_values['value6'], my_values['value7'], my_values['value8'],
                      my_values['value9']]
    if x_placement in values_to_list:
        return True
    if y_placement in values_to_list:
        return True
    else:
        return False


def table():
    my_table = tabulate([[my_values['value1'], my_values['value2'], my_values['value3']],
                         [my_values['value4'], my_values['value5'], my_values['value6']],
                         [my_values['value7'], my_values['value8'], my_values['value9']]], tablefmt="grid")
    # print(table)
    print(my_table)


table()

game_finished = False
x_winner = False

while game_finished == False:
    correct_valuex = False
    while correct_valuex == False:
        x_placement = input("Where would you like to place X? ")
        if check():
            for key, value in list(my_values.items()):
                if x_placement == value:
                    my_values[key] = "X"
                    correct_valuex = True
            table()
        else:
            print("That's an incorrect value. TRY AGAIN...")


    if my_values['value1'] == "X" and my_values['value2'] == "X" and my_values['value3'] == "X":
        print("X is the Winner")
        x_winner = True
        game_finished = True
    elif my_values['value4'] == "X" and my_values['value5'] == "X" and my_values['value6'] == "X":
        print("X is the Winner")
        x_winner = True
        game_finished = True
    elif my_values['value7'] == "X" and my_values['value8'] == "X" and my_values['value9'] == "X":
        print("X is the Winner")
        x_winner = True
        game_finished = True
    elif my_values['value1'] == "X" and my_values['value4'] == "X" and my_values['value7'] == "X":
        print("X is the Winner")
        x_winner = True
        game_finished = True
    elif my_values['value2'] == "X" and my_values['value5'] == "X" and my_values['value8'] == "X":
        print("X is the Winner")
        x_winner = True
        game_finished = True
    elif my_values['value3'] == "X" and my_values['value6'] == "X" and my_values['value9'] == "X":
        print("X is the Winner")
        x_winner = True
        game_finished = True
    elif my_values['value1'] == "X" and my_values['value5'] == "X" and my_values['value9'] == "X":
        print("X is the Winner")
        x_winner = True
        game_finished = True
    elif my_values['value3'] == "X" and my_values['value5'] == "X" and my_values['value7'] == "X":
        print("X is the Winner")
        x_winner = True
        game_finished = True
    elif my_values['value1'] == ("X" or "Y") and my_values['value2'] == ("X" or "Y") and my_values['value3'] == ("X" or "Y") and my_values['value4'] == ("X" or "Y") and my_values['value5'] == ("X" or "Y") and my_values['value6'] == ("X" or "Y") and my_values['value7'] == ("X" or "Y") and my_values['value8'] == ("X" or "Y") and my_values['value9'] == ("X" or "Y"):
        print("It's Draw")
        again = input("Do you want to play again? Yes or No? ").upper()
        if again == "YES":
            os.system("cls")
            print("*************TIC TAC TOE**************")
            table()
        else:
            game_finished = True

    elif x_winner == False:
        correct_valuey = False
        while correct_valuey == False:
            y_placement = input("Where would you like to place Y? ")
            if check():
                for key, value in list(my_values.items()):
                    if y_placement == value:
                        my_values[key] = "Y"
                        correct_valuey = True
                table()
            else:
                print("That's an incorrect value. TRY AGAIN...")

        if my_values['value1'] == "Y" and my_values['value2'] == "Y" and my_values['value3'] == "Y":
            print("Y is the Winner")
            game_finished = True
        elif my_values['value4'] == "Y" and my_values['value5'] == "Y" and my_values['value6'] == "Y":
            print("Y is the Winner")
            game_finished = True
        elif my_values['value7'] == "Y" and my_values['value8'] == "Y" and my_values['value9'] == "Y":
            print("Y is the Winner")
            game_finished = True
        elif my_values['value1'] == "Y" and my_values['value4'] == "Y" and my_values['value7'] == "Y":
            print("Y is the Winner")
            game_finished = True
        elif my_values['value2'] == "Y" and my_values['value5'] == "Y" and my_values['value8'] == "Y":
            print("Y is the Winner")
            game_finished = True
        elif my_values['value3'] == "Y" and my_values['value6'] == "Y" and my_values['value9'] == "Y":
            print("Y is the Winner")
            game_finished = True
        elif my_values['value1'] == "Y" and my_values['value5'] == "Y" and my_values['value9'] == "Y":
            print("Y is the Winner")
            game_finished = True
        elif my_values['value3'] == "Y" and my_values['value5'] == "Y" and my_values['value7'] == "Y":
            print("Y is the Winner")
            game_finished = True
