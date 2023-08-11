from pyfiglet import Figlet

def show():
    for row in game_board:
        for cell in row:
            print(cell, end= " ")
        print()   

def check1():
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print("Player1 Won!")
def check2():
    if game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("Player1 Won!")
def check3():
    if game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("Player1 Won!")
def check4():
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("Player1 Won!")

def check5():
    if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print("Player1 Won!")

def check6():
    if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print("Player1 Won!")

def check7():
    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("Player1 Won!")

def check8():
    if game_board[2][0] == "X" and game_board[1][1] == "X" and game_board[0][2] == "X":
        print("Player1 Won!")

def check9():
    if game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print("Player2 Won!")

def check10():
    if game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print("Player2 Won!")

def check11():
    if game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("Player2 Won!")

def check12():
    if game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print("Player2 Won!")

def check13():
    if game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        print("Player2 Won!")

def check14():
    if game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
        print("Player2 Won!")

def check15():
    if game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("Player2 Won!")

def check16():
   if game_board[2][0] == "O" and game_board[1][1] == "O" and game_board[0][2] == "O":
        print("Player2 Won!") 

def draw():
    if game_board[0][0] != "." and game_board[0][1] != "." and game_board[0][2] != "." and game_board[1][0] != "." and game_board[1][1] != "." and game_board[1][2] != "." and game_board[2][0] != "." and game_board[2][1] != "." and game_board[2][2] != ".":
        print("No One wins.")

f = Figlet(font='bubble' , width=10)
print(f.renderText('Welcome to Tic Tac Toe'))

game_board = [["." , "." , "."],
              ["." , "." , "."],
              ["." , "." , "."]]
#print(game_board)
show()

#player1
while True:
    print("player1")
    while True:
        row = int(input("enter row: "))
        col = int(input("enter col: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == ".":
                game_board[row][col] = "X"
                show()
                check1()
                check2()
                check3()
                check4()
                check5()
                check6()
                check7()
                check8()
                draw()
                break
            else:
                print("Choose another house!")
        else:
            print("Wrong number! give me 0 or 1 or 2.")
#player2
    print("player2")
    while True:
        row = int(input("enter row: "))
        col = int(input("enter col: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == ".":
                game_board[row][col] = "O"
                show()
                check9()
                check10()
                check11()
                check12()
                check13()
                check14()
                check15()
                check16()
                draw()
                break
            else:
                print("Choose another house!")
        else:
            print("Wrong number! give me 0 or 1 or 2.")
        