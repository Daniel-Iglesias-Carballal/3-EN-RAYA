import tkinter as tk
from tkinter import messagebox

# =========================
# COLORES
# =========================
COLOR_FONDO = "#1a1a1a"
COLOR_TABLERO = "#ffd60a"
COLOR_NUMEROS = "#ff66cc"
COLOR_X = "#ff3b30"
COLOR_O = "#3a86ff"
COLOR_TEXTO = "#ffffff"

# =========================
# VENTANA
# =========================
ventana = tk.Tk()
ventana.title("Tres en Raya")
ventana.attributes("-fullscreen", True)
ventana.config(bg=COLOR_FONDO)

def salir_pantalla(event=None):
    ventana.attributes("-fullscreen", False)

ventana.bind("<Escape>", salir_pantalla)

# =========================
# VARIABLES
# =========================
tablero = ["1","2","3",
           "4","5","6",
           "7","8","9"]

turno = "X"

puntos_x = 0
puntos_o = 0
empates = 0
partidas_totales = 0

botones = []

# =========================
# COMPROBAR VICTORIA
# =========================
def victoria():

    combinaciones = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a, b, c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c]:
            botones[a].config(bg="#00c853")
            botones[b].config(bg="#00c853")
            botones[c].config(bg="#00c853")
            return True

    return False

# =========================
# ACTUALIZAR MARCADORES
# =========================
def actualizar_marcador():

    marcador_x.config(text=f"X: {puntos_x}")
    marcador_o.config(text=f"O: {puntos_o}")
    texto_empates.config(text=f"Empates: {empates}")
    texto_totales.config(text=f"Partidas Totales: {partidas_totales}")

# =========================
# NUEVA PARTIDA
# (mantiene los marcadores)
# =========================
def nueva_partida():

    global tablero, turno

    tablero = ["1","2","3",
               "4","5","6",
               "7","8","9"]

    turno = "X"

    texto_turno.config(
        text="Turno: X",
        fg=COLOR_X
    )

    for i in range(9):
        botones[i].config(
            text=str(i + 1),
            bg=COLOR_TABLERO,
            fg=COLOR_NUMEROS
        )

# =========================
# REINICIAR MARCADORES
# =========================
def reiniciar_marcadores():

    global puntos_x, puntos_o, empates, partidas_totales

    puntos_x = 0
    puntos_o = 0
    empates = 0
    partidas_totales = 0

    actualizar_marcador()
    nueva_partida()

# =========================
# JUGAR
# =========================
def jugar(pos):

    global turno, puntos_x, puntos_o, empates, partidas_totales

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

            partidas_totales += 1

            if turno == "X":
                puntos_x += 1
            else:
                puntos_o += 1

            actualizar_marcador()

            messagebox.showinfo(
                "Fin del juego",
                f"¡Gana {turno}!"
            )

            nueva_partida()
            return

        # EMPATE
        if all(x in ["X", "O"] for x in tablero):

            empates += 1
            partidas_totales += 1

            actualizar_marcador()

            messagebox.showinfo(
                "Empate",
                "¡Empate!"
            )

            nueva_partida()
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
# PARTIDAS TOTALES
# =========================
texto_totales = tk.Label(
    ventana,
    text="Partidas Totales: 0",
    font=("Arial", 18, "bold"),
    bg=COLOR_FONDO,
    fg="white"
)
texto_totales.pack(pady=5)

# =========================
# MARCADORES
# =========================
frame_marcadores = tk.Frame(
    ventana,
    bg=COLOR_FONDO
)
frame_marcadores.pack(pady=10)

marcador_x = tk.Label(
    frame_marcadores,
    text="X: 0",
    font=("Arial", 22, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_X
)
marcador_x.grid(row=0, column=0, padx=50)

marcador_o = tk.Label(
    frame_marcadores,
    text="O: 0",
    font=("Arial", 22, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_O
)
marcador_o.grid(row=0, column=1, padx=50)

# =========================
# EMPATES
# =========================
texto_empates = tk.Label(
    ventana,
    text="Empates: 0",
    font=("Arial", 16, "bold"),
    bg=COLOR_FONDO,
    fg="#cccccc"
)
texto_empates.pack(pady=5)

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
boton_reiniciar = tk.Button(
    ventana,
    text="Reiniciar Marcadores",
    font=("Arial", 18, "bold"),
    bg="#ff9500",
    fg="white",
    padx=20,
    pady=10,
    command=reiniciar_marcadores
)

boton_reiniciar.pack(pady=20)

# =========================
# EJECUTAR
# =========================
ventana.mainloop()