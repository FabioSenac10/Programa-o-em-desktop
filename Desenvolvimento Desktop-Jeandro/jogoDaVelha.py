import tkinter as tk
from tkinter import messagebox
from random import randrange

def create_board():
    return [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]

board = create_board()
buttons = []
game_over = False

def draw_board():
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = board[row][col]

def check_winner():
    global game_over

    # Linhas
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "":
            game_over = True
            return board[row][0]

    # Colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            game_over = True
            return board[0][col]

    # Diagonal principal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        game_over = True
        return board[0][0]

    # Diagonal secundária
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        game_over = True
        return board[0][2]

    # Empate
    filled = True
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                filled = False

    if filled:
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

    # Primeira jogada no centro
    if board[1][1] == "":
        board[1][1] = "X"
        draw_board()
        return

    free_positions = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                free_positions.append((row, col))

    if free_positions:
        choice = free_positions[randrange(len(free_positions))]
        board[choice[0]][choice[1]] = "X"
        draw_board()

    winner = check_winner()
    if winner:
        show_result(winner)

def show_result(winner):
    if winner == "X":
        messagebox.showinfo("Fim de Jogo", "Computador venceu!")
    elif winner == "O":
        messagebox.showinfo("Fim de Jogo", "Você venceu!")
    else:
        messagebox.showinfo("Fim de Jogo", "Deu empate!")

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
            command=lambda r=row, c=col: player_move(r, c)
        )
        btn.grid(row=row, column=col)
        button_row.append(btn)
    buttons.append(button_row)

computer_move()

root.mainloop()