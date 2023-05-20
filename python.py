list1=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
x=0
def table():
    global x
    global string
    string = ""
    for i in list1:
        x += 1
        string += f"|{i}"
        if x == 3:
            string += f"|\n"
            x = 0
    print(string)

turn = 1
def game():
    global turn
    while " " in list1:
        try:
            choice1 = int(input("Which square you wan to fill?"))
            choice = choice1-1
            if list1[choice] == " ":
                if turn % 2 == 1:
                    list1[choice] = 'X'

                elif turn % 2 == 0:
                    list1[choice] = 'O'
                turn += 1
                table()
            else:
                if list1[choice] != " ":
                    print('Square already Taken')

        except ValueError:
            print("You have to Type a number between 0 and 9")
        except IndexError:
            print("You have to Type a number between 0 and 9")


        for square in range(len(list1)):
            try:
                if list1[square] != " " and square in [0, 3, 5] and list1[square] == list1[square+1] == list1[square+2]:
                    print(f"player{list1[square]} won")
                    return
                elif list1[square] == list1[square+3] == list1[square+6] and list1[square] != " " :
                    print(f"player{list1[square]} won")
                    return
            except IndexError:
                pass
        if list1[4] != " " and list1[0] == list1[4] == list1[8] or list1[4] != " " and list1[2] == list1[4] == list1[6]:
            print(f"player{list1[4]} has won")
            return
    print("Draw")
game()







