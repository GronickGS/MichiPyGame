import tkinter as tk
from tkinter import messagebox

class JuegoTresEnRaya:
    def __init__(self, root):
        self.root = root
        self.root.title("Michi")
        self.jugador_actual = "O"
        self.tablero = [['' for _ in range(3)] for _ in range(3)]
        self.botones = []
        self.crear_tablero()
        self.centrar_ventana()  # Centrar la ventana al inicializar el juego

    def crear_tablero(self):
        for i in range(3):
            fila_botones = []
            for j in range(3):
                btn = tk.Button(self.root, text="", font=('Arial', 30), width=4, height=2,
                                command=lambda fila=i, columna=j: self.on_click_boton(fila, columna))
                btn.grid(row=i, column=j, sticky="nsew")
                fila_botones.append(btn)
            self.botones.append(fila_botones)

    def centrar_ventana(self):
        ancho_ventana = self.root.winfo_reqwidth()
        alto_ventana = self.root.winfo_reqheight()
        pos_x = (self.root.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        pos_y = (self.root.winfo_screenheight() // 2) - (alto_ventana // 2)
        self.root.geometry(f"+{pos_x}+{pos_y}")

    def on_click_boton(self, fila, columna):
        if self.tablero[fila][columna] == "":
            self.botones[fila][columna].config(text=self.jugador_actual)
            self.tablero[fila][columna] = self.jugador_actual
            if self.verificar_ganador():
                self.mostrar_ganador()
            elif self.verificar_empate():
                self.mostrar_empate()
            else:
                self.jugador_actual = "X" if self.jugador_actual == "O" else "O"

    def verificar_ganador(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != "":
                return True
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != "":
                return True
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != "":
            return True
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != "":
            return True
        return False

    def verificar_empate(self):
        for fila in self.tablero:
            for celda in fila:
                if celda == "":
                    return False
        return True

    def mostrar_ganador(self):
        ganador = "X" if self.jugador_actual == "X" else "O"
        messagebox.showinfo("Resultado", f"Ganador: Jugador {ganador}")
        self.reiniciar_juego()

    def mostrar_empate(self):
        messagebox.showinfo("Resultado", "Empate")
        self.reiniciar_juego()

    def reiniciar_juego(self):
        self.jugador_actual = "O"
        self.tablero = [['' for _ in range(3)] for _ in range(3)]
        for fila in self.botones:
            for boton in fila:
                boton.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoTresEnRaya(root)
    root.mainloop()
