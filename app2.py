import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya")
        self.current_player = "O"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                btn = tk.Button(self.root, text="", font=('Arial', 30), width=4, height=2,
                                command=lambda row=i, col=j: self.on_button_click(row, col))
                btn.grid(row=i, column=j, sticky="nsew")
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.show_winner()
            elif self.check_tie():
                self.show_tie()
            else:
                self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def show_winner(self):
        winner = "X" if self.current_player == "O" else "O"
        messagebox.showinfo("Resultado", f"Ganador: Jugador {winner}")
        self.reset_game()

    def show_tie(self):
        messagebox.showinfo("Resultado", "Empate")
        self.reset_game()

    def reset_game(self):
        self.current_player = "O"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
