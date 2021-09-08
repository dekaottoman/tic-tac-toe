import tkinter as tk

#We create the root of our application
root = tk.Tk()
root.title('Tic Tac Toe')
root.maxsize(300,500)
root.minsize(300,500)

#Functions and variables from cmd version
turn = "X"
turn_count = 0
table = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#Function to reset the table
def reset_table():
    i = 0
    while i < 9:
        table[i] = "-"
        i += 1

#Function to insert plays into the table
def insert(turn, index):
    table[int(index)] = turn

#Function to check if there is a horizontal winner
def check_win_h():
    win = False

    #Row 1
    if(table[0] != "-"):
        if(table[0] == table[1]):
            if(table[0] == table[2]):
                win = True
    #Row 2
    if(table[3] != "-"):
        if(table[3] == table[4]):
            if(table[3] == table[5]):
                win = True
    #Row 3
    if(table[6] != "-"):
        if(table[6] == table[7]):
            if(table[6] == table[8]):
                win = True

    return win

#Function to check if there is a vertical winner
def check_win_v():
    win = False

    #Column 1
    if(table[0] != "-"):
        if(table[0] == table[3]):
            if(table[0] == table[6]):
                win = True

    #Column 2
    if(table[1] != "-"):
        if(table[1] == table[4]):
            if(table[1] == table[7]):
                win = True

    #Column 3
    if(table[2] != "-"):
        if(table[2] == table[5]):
            if(table[2] == table[8]):
                win = True

    return win

#Function to check if there is a diagonal winner
def check_win_d():
    win = False

    #Diagonal 1
    if(table[0] != "-"):
        if(table[0] == table[4]):
            if(table[0] == table[8]):
                win = True

    #Diagonal 2
    if(table[2] != "-"):
        if(table[2] == table[4]):
            if(table[2] == table[6]):
                win = True

    return win

#The function to bring together all the check win functions
def check_win():
    if check_win_h():
        return True
    elif check_win_v():
        return True
    elif check_win_d():
        return True
    else:
        return False
    

#Function to check draws
def check_draw(turn_count):
    if(turn_count < 9):
        return None
    else:
        win_label = tk.Label(button_frame, text= "Draw !!!")
        win_label.place(relwidth=0.3333,relheight=1, relx=0.6666, rely=0)
        
#We declare our 2 frames and our canvas
canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()

play_frame = tk.Frame(canvas, width=300, height=300)
play_frame.place(relwidth=1,relheight=0.75, relx=0, rely=0)

button_frame = tk.Frame(canvas, width=300, height=100)
button_frame.place(relwidth=1,relheight=0.25, relx=0, rely=0.75)

#Function that initiates and resets the game
def initiate_game():
    global turn
    global turn_count
    turn = "X"
    turn_count = 0
    reset_table()

    #Buttons for plays
    btn1 = tk.Button(play_frame, command=play1)
    btn1.place(relwidth=0.3333,relheight=0.3333, relx=0, rely=0)

    btn2 = tk.Button(play_frame, command=play2)
    btn2.place(relwidth=0.3333,relheight=0.3333, relx=0.3333, rely=0)

    btn3 = tk.Button(play_frame, command=play3)
    btn3.place(relwidth=0.3333,relheight=0.3333, relx=0.6666, rely=0)

    btn4 = tk.Button(play_frame, command=play4)
    btn4.place(relwidth=0.3333,relheight=0.3333, relx=0, rely=0.3333)

    btn5 = tk.Button(play_frame, command=play5)
    btn5.place(relwidth=0.3333,relheight=0.3333, relx=0.3333, rely=0.3333)

    btn6 = tk.Button(play_frame, command=play6)
    btn6.place(relwidth=0.3333,relheight=0.3333, relx=0.6666, rely=0.3333)

    btn7 = tk.Button(play_frame, command=play7)
    btn7.place(relwidth=0.3333,relheight=0.3333, relx=0, rely=0.6666)

    btn8 = tk.Button(play_frame, command=play8)
    btn8.place(relwidth=0.3333,relheight=0.3333, relx=0.3333, rely=0.6666)

    btn9 = tk.Button(play_frame, command=play9)
    btn9.place(relwidth=0.3333,relheight=0.3333, relx=0.6666, rely=0.6666)

    #We create a turn and a win label
    turn_label = tk.Label(button_frame, text="Turn of : " + turn)
    turn_label.place(relwidth=0.3333,relheight=1, relx=0, rely=0)

    win_label = tk.Label(button_frame, text="Waiting Winner")
    win_label.place(relwidth=0.3333,relheight=1, relx=0.6666, rely=0)

#Function to update turn label
def update_turn_label(t):
    turn_label = tk.Label(button_frame, text="Turn of : " + t)
    turn_label.place(relwidth=0.3333,relheight=1, relx=0, rely=0)

#Function to declare winner
def declare_winner(t):
    if(t == "X"):
        win_label = tk.Label(button_frame, text= t + " Wins !!!",  bg="#EA2027", fg="#FFFFFF")
    else:
        win_label = tk.Label(button_frame, text= t + " Wins !!!",  bg="#009432", fg="#FFFFFF")
    
    win_label.place(relwidth=0.3333,relheight=1, relx=0.6666, rely=0)

#Function to switch turns
def sw_turn():
    global turn
    if turn == "X":
        turn = "O"
        update_turn_label(turn)
    else:
        turn = "X"
        update_turn_label(turn)

#Function to check endgame
def check_end():
    global turn_count
    turn_count += 1
    if check_win():
        declare_winner(turn)
    else:
        check_draw(turn_count)

#Functions to play
def play1():
    if(turn == "X"):
        label = tk.Label(play_frame, text=turn, bg="#EA2027", fg="#FFFFFF")
    else:
        label = tk.Label(play_frame, text=turn, bg="#009432", fg="#FFFFFF")

    label.place(relwidth=0.3333,relheight=0.3333, relx=0, rely=0)
    insert(turn, 0)
    check_end()
    sw_turn()

def play2():
    if(turn == "X"):
        label = tk.Label(play_frame, text=turn, bg="#EA2027", fg="#FFFFFF")
    else:
        label = tk.Label(play_frame, text=turn, bg="#009432", fg="#FFFFFF")

    label.place(relwidth=0.3333,relheight=0.3333, relx=0.3333, rely=0)
    insert(turn, 1)
    check_end()
    sw_turn()

def play3():
    if(turn == "X"):
        label = tk.Label(play_frame, text=turn, bg="#EA2027", fg="#FFFFFF")
    else:
        label = tk.Label(play_frame, text=turn, bg="#009432", fg="#FFFFFF")

    label.place(relwidth=0.3333,relheight=0.3333, relx=0.6666, rely=0)
    insert(turn, 2)
    check_end()
    sw_turn()

def play4():
    if(turn == "X"):
        label = tk.Label(play_frame, text=turn, bg="#EA2027", fg="#FFFFFF")
    else:
        label = tk.Label(play_frame, text=turn, bg="#009432", fg="#FFFFFF")

    label.place(relwidth=0.3333,relheight=0.3333, relx=0, rely=0.3333)
    insert(turn, 3)
    check_end()
    sw_turn()

def play5():
    if(turn == "X"):
        label = tk.Label(play_frame, text=turn, bg="#EA2027", fg="#FFFFFF")
    else:
        label = tk.Label(play_frame, text=turn, bg="#009432", fg="#FFFFFF")

    label.place(relwidth=0.3333,relheight=0.3333, relx=0.3333, rely=0.3333)
    insert(turn, 4)
    check_end()
    sw_turn()

def play6():
    if(turn == "X"):
        label = tk.Label(play_frame, text=turn, bg="#EA2027", fg="#FFFFFF")
    else:
        label = tk.Label(play_frame, text=turn, bg="#009432", fg="#FFFFFF")

    label.place(relwidth=0.3333,relheight=0.3333, relx=0.6666, rely=0.3333)
    insert(turn, 5)
    check_end()
    sw_turn()

def play7():
    if(turn == "X"):
        label = tk.Label(play_frame, text=turn, bg="#EA2027", fg="#FFFFFF")
    else:
        label = tk.Label(play_frame, text=turn, bg="#009432", fg="#FFFFFF")

    label.place(relwidth=0.3333,relheight=0.3333, relx=0, rely=0.6666)
    insert(turn, 6)
    check_end()
    sw_turn()

def play8():
    if(turn == "X"):
        label = tk.Label(play_frame, text=turn, bg="#EA2027", fg="#FFFFFF")
    else:
        label = tk.Label(play_frame, text=turn, bg="#009432", fg="#FFFFFF")

    label.place(relwidth=0.3333,relheight=0.3333, relx=0.3333, rely=0.6666)
    insert(turn, 7)
    check_end()
    sw_turn()

def play9():
    if(turn == "X"):
        label = tk.Label(play_frame, text=turn, bg="#EA2027", fg="#FFFFFF")
    else:
        label = tk.Label(play_frame, text=turn, bg="#009432", fg="#FFFFFF")

    label.place(relwidth=0.3333,relheight=0.3333, relx=0.6666, rely=0.6666)
    insert(turn, 8)
    check_end()
    sw_turn()

#Button to initiate the game
initiate_btn = tk.Button(button_frame, text="Initiate Game", bg="#22a6b3", fg="#FFFFFF", command=initiate_game)
initiate_btn.place(relwidth=0.3333,relheight=1, relx=0.3333, rely=0)

#Label to satisfy my ego
dekaottoman_label = tk.Label(root, text="By dekaottoman", bg="#40739e", fg="#FFFFFF")
dekaottoman_label.place(relwidth=1,relheight=0.2, relx=0, rely=0.8)

root.mainloop()