import tkinter as tk
from tkinter import messagebox
from random import randrange

def create_board():
    return [
        ['','',''],
        ['','',''],
        ['','','']
    ]

board = create_board()
buttons = []
game_over = False

def draw_board():
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = board[row][col]
            if board[row][col] in ["X","O"]:
                buttons[row][col]["state"] = "disabled"

def check_winner():
    global game_over

    lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] in ["X","O"]:
            game_over = True
            return line[0]

    free = False
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                free = True

    if not free:
        game_over = True
        return "Empate"

    return None

def player_move(row, col):
    global game_over

    if game_over:
        return

    if board[row][col] == "":
        board[row][col] = "O"
        draw_board()

        winner = check_winner()
        if winner:
            show_result(winner)
            return

        computer_move()

def computer_move():
    global game_over

    if game_over:
        return

    free_positions = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                free_positions.append((row,col))

    if free_positions:
        choice = free_positions[randrange(len(free_positions))]
        board[choice[0]][choice[1]] = "X"
        draw_board()

    winner = check_winner()
    if winner:
        show_result(winner)

def show_result(winner):
    if winner == "X":
        messagebox.showinfo("Fim de jogo","Computador venceu")
    elif winner == "O":
        messagebox.showinfo("Fim de jogo","Você venceu")
    else:
        messagebox.showinfo("Fim de jogo","Empate")

root = tk.Tk()
root.title("Jogo da Velha")

for row in range(3):
    button_row = []
    for col in range(3):
        btn = tk.Button(
            root,
            text=board[row][col],
            width=10,
            height=4,
            command=lambda r=row,c=col: player_move(r,c)
        )
        btn.grid(row=row,column=col)
        button_row.append(btn)
    buttons.append(button_row)

board[1][1] = "X"
draw_board()

root.mainloop()