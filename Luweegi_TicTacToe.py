import tkinter  # graphical user interface library

# game setup
playerX = "X"
playerO = "O"
curr_player = playerX   #player X always starts
player1_score = 0
player2_score = 0
tie_score = 0  
board = [[0, 0, 0],     #board setup
         [0, 0, 0],
         [0, 0, 0]]


color_light_teal = "#029386"    # background color 2
color_teal = "#008080"          # background color
color_yg = "#9acd32"            # player 1 (X) color 
color_orange = "#f97306"        # player 2 (O) color
color_green = "#006400"         # victory color
color_red = "#a52a2a"           # tie color

turns = 0                       # variable to start the number of turns
game_over = False               # will trigger when a player wins or a game ties

def update_label():             # this function will update the label of player scores and player turns

    label["text"] = f"{curr_player}'s turn | Player 1 (X): {player1_score} - Player 2 (O): {player2_score} - Ties: {tie_score}"

def set_tile(row, column):      # this function handles an acton when a player clicks a tile on the board
    global curr_player

    if game_over:
        return

    if board[row][column]["text"] != "":    #if the tile is taken, return so that it does not replace the current clicked tile
       
        return

    # set the text for the current player 
    board[row][column]["text"] = curr_player  # marks the board

    # change the text color based on the current player
    if curr_player == playerO:
        board[row][column].config(foreground=color_orange)      # player O is orange
        curr_player = playerX
    else:
        board[row][column].config(foreground=color_yg)          # player X is yellow green
        curr_player = playerO

    update_label()      # updates the label

 
    check_winner()      #check if win or tie

def check_winner():                                                         #function for winning conditions
    global turns, game_over, player1_score, player2_score, tie_score        #global variables 
    turns += 1

    # check 3 rows horizontally
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_green)
            for column in range(3):
                board[row][column].config(foreground=color_green, background=color_light_teal)
            game_over = True
            if board[row][0]["text"] == playerX:
                player1_score += 1
            else:
                player2_score += 1
            return

    # check 3 columns vertically
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
                and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_green)
            for row in range(3):
                board[row][column].config(foreground=color_green, background=color_light_teal)
            game_over = True
            if board[0][column]["text"] == playerX:
                player1_score += 1
            else:
                player2_score += 1
            return

    # check tiles diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_green)
        for i in range(3):
            board[i][i].config(foreground=color_green, background=color_light_teal)
        game_over = True
        if board[0][0]["text"] == playerX:
            player1_score += 1
        else:
            player2_score += 1
        return

    # check tiles diagonally in reverse
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_green)
        board[0][2].config(foreground=color_green, background=color_light_teal)
        board[1][1].config(foreground=color_green, background=color_light_teal)
        board[2][0].config(foreground=color_green, background=color_light_teal)
        game_over = True
        if board[0][2]["text"] == playerX:
            player1_score += 1
        else:
            player2_score += 1
        return

    # tie condition if turns is equal to 9 without winnig, then it's a tie
    if turns == 9:
        game_over = True
        tie_score += 1      # increments to 1 when a tie occurs
        label.config(text="Tie!", foreground=color_red)
        return

def new_game():                             # function for new game or restarting a game
    global turns, game_over, curr_player

    turns = 0
    game_over = False
    curr_player = playerX

    label.config(foreground="white")
    
    update_label()

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_yg, background=color_teal)

def reset_game():                           # function for resetting a game
    """Resets the game board and all scores."""
    global player1_score, player2_score, tie_score
    # reset all scores to 0
    player1_score = 0
    player2_score = 0
    tie_score = 0
    # restart the game
    new_game()

# window setup
window = tkinter.Tk()               # call UI library
window.title("Tic Tac Toe")
window.resizable(False, False)      # fixed window size

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="", font=("Verdana", 20), background=color_teal, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

update_label()

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Verdana", 50, "bold"),
                                            background=color_teal, foreground=color_yg, width=5, height=2,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row + 1, column=column)

restart_button = tkinter.Button(frame, text="Restart", font=("Verdana", 20), background=color_teal,
                                foreground="white", command=new_game)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

reset_button = tkinter.Button(frame, text="Reset", font=("Verdana", 20), background=color_teal,
                              foreground="white", command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3, sticky="we")

frame.pack()

# center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
