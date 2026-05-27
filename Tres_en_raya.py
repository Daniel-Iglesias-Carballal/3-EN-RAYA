import tkinter as tk
from tkinter import messagebox

# =========================
# COLORES
# =========================
COLOR_FONDO = "#1a1a1a"
COLOR_TABLERO = "#ffd60a"   # amarillo
COLOR_NUMEROS = "#ff66cc"   # rosa
COLOR_X = "#ff3b30"         # rojo
COLOR_O = "#3a86ff"         # azul
COLOR_TEXTO = "#ffffff"

# =========================
# VENTANA
# =========================
ventana = tk.Tk()
ventana.title("Tres en Raya")
ventana.geometry("500x600")
ventana.config(bg=COLOR_FONDO)
ventana.resizable(False, False)

# =========================
# VARIABLES
# =========================
tablero = ["1", "2", "3",
           "4", "5", "6",
           "7", "8", "9"]

turno = "X"

botones = []

# =========================
# COMPROBAR VICTORIA
# =========================
def victoria():

    combinaciones = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]

    for a, b, c in combinaciones:

        if tablero[a] == tablero[b] == tablero[c]:

            botones[a].config(bg="#00c853")
            botones[b].config(bg="#00c853")
            botones[c].config(bg="#00c853")

            return True

    return False

# =========================
# REINICIAR
# =========================
def reiniciar():

    global tablero, turno

    tablero = ["1", "2", "3",
               "4", "5", "6",
               "7", "8", "9"]

    turno = "X"

    for i in range(9):

        botones[i].config(
            text=str(i + 1),
            bg=COLOR_TABLERO,
            fg=COLOR_NUMEROS,
            state="normal"
        )

    texto_turno.config(
        text="Turno: X",
        fg=COLOR_X
    )

# =========================
# JUGAR
# =========================
def jugar(pos):

    global turno

    if tablero[pos] not in ["X", "O"]:

        tablero[pos] = turno

        color = COLOR_X if turno == "X" else COLOR_O

        botones[pos].config(
            text=turno,
            fg="white",
            bg=color
        )

        # GANADOR
        if victoria():

            messagebox.showinfo(
                "Fin del juego",
                f"¡Gana {turno}!"
            )

            reiniciar()
            return

        # EMPATE
        if all(x in ["X", "O"] for x in tablero):

            messagebox.showinfo(
                "Empate",
                "¡Empate!"
            )

            reiniciar()
            return

        # CAMBIO DE TURNO
        turno = "O" if turno == "X" else "X"

        texto_turno.config(
            text=f"Turno: {turno}",
            fg=COLOR_X if turno == "X" else COLOR_O
        )

# =========================
# TÍTULO
# =========================
titulo = tk.Label(
    ventana,
    text="TRES EN RAYA",
    font=("Arial", 28, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TABLERO
)

titulo.pack(pady=20)

# =========================
# TURNO
# =========================
texto_turno = tk.Label(
    ventana,
    text="Turno: X",
    font=("Arial", 20, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_X
)

texto_turno.pack(pady=10)

# =========================
# TABLERO
# =========================
frame = tk.Frame(
    ventana,
    bg=COLOR_FONDO
)

frame.pack(pady=20)

for i in range(9):

    boton = tk.Button(
        frame,
        text=str(i + 1),
        font=("Arial", 28, "bold"),
        width=5,
        height=2,
        bg=COLOR_TABLERO,
        fg=COLOR_NUMEROS,
        activebackground="#ffe566",
        relief="solid",
        bd=4,
        command=lambda i=i: jugar(i)
    )

    boton.grid(
        row=i // 3,
        column=i % 3,
        padx=8,
        pady=8
    )

    botones.append(boton)

# =========================
# BOTÓN REINICIAR
# =========================
btn_reiniciar = tk.Button(
    ventana,
    text="REINICIAR",
    font=("Arial", 16, "bold"),
    bg="#ff66cc",
    fg="white",
    padx=15,
    pady=8,
    command=reiniciar
)

btn_reiniciar.pack(pady=20)

# =========================
# EJECUTAR
# =========================
ventana.mainloop()