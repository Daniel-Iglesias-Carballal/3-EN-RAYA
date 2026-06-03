import tkinter as tk
from tkinter import messagebox
import random

# ==========================================
# COLORES Y CONFIGURACIÓN
# ==========================================
COLOR_FONDO = "#1a1a1a"
COLOR_TABLERO = "#ffd60a"
COLOR_NUMEROS = "#ff66cc"
COLOR_X = "#ff3b30"
COLOR_O = "#3a86ff"
COLOR_TEXTO = "#ffffff"

# ==========================================
# VENTANA PRINCIPAL
# ==========================================
ventana = tk.Tk()
ventana.title("Tres en Raya Definitivo")
ventana.geometry("500x780")
ventana.config(bg=COLOR_FONDO)

# ==========================================
# VARIABLES DE CONTROL
# ==========================================
tablero = [" "] * 9  
turno = "X"
modo_juego = 1       # 1 = Vs Máquina, 2 = Vs Usuario 2
puntos_x = 0
puntos_o = 0
empates = 0
partidas_totales = 0
botones = []

# ==========================================
# COMPROBAR VICTORIA
# ==========================================
def comprobar_ganador(jugador):
    combinaciones = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontales
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticales
        (0, 4, 8), (2, 4, 6)              # Diagonales
    ]
    for a, b, c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c] == jugador:
            botones[a].config(bg="#00c853", fg="white")
            botones[b].config(bg="#00c853", fg="white")
            botones[c].config(bg="#00c853", fg="white")
            return True
    return False

# ==========================================
# ACTUALIZAR INTERFAZ Y MARCADORES
# ==========================================
def actualizar_marcador():
    marcador_x.config(text=f"X: {puntos_x}")
    marcador_o.config(text=f"O: {puntos_o}")
    texto_empates.config(text=f"Empates: {empates}")
    texto_totales.config(text=f"Partidas Totales: {partidas_totales}")

def cambiar_modo(modo):
    global modo_juego
    modo_juego = modo
    if modo == 1:
        btn_modo1.config(bg="#00c853", fg="white")
        btn_modo2.config(bg="#444444", fg="#aaaaaa")
    else:
        btn_modo2.config(bg="#00c853", fg="white")
        btn_modo1.config(bg="#444444", fg="#aaaaaa")
    reiniciar_marcadores()

# ==========================================
# FLUJO DE PARTIDAS (LOS DOS TIPOS DE REINICIO)
# ==========================================
def nueva_partida():
    """BOTÓN REINICIAR PARTIDA: Limpia el tablero manteniendo los marcadores."""
    global tablero, turno
    tablero = [" "] * 9
    turno = "X"
    texto_turno.config(text="Turno: X", fg=COLOR_X)
    
    for i in range(9):
        botones[i].config(
            text=" ",
            bg=COLOR_TABLERO,
            fg=COLOR_NUMEROS,
            state="normal"
        )

def reiniciar_marcadores():
    """BOTÓN REINICIAR MARCADOR: Resetea todas las estadísticas globales a 0."""
    global puntos_x, puntos_o, empates, partidas_totales
    puntos_x = 0
    puntos_o = 0
    empates = 0
    partidas_totales = 0
    actualizar_marcador()
    nueva_partida()

# ==========================================
# INTELIGENCIA ARTIFICIAL (IA)
# ==========================================
def ejecutar_movimiento_ia():
    global tablero
    
    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = "O"
            if comprobar_ganador("O"):
                hacer_movimiento_grafico(i, "O")
                return
            tablero[i] = " "

    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = "X"
            if comprobar_ganador("X"):
                tablero[i] = "O"
                hacer_movimiento_grafico(i, "O")
                return
            tablero[i] = " "

    if tablero[4] == " ":
        tablero[4] = "O"
        hacer_movimiento_grafico(4, "O")
        return

    esquinas = [0, 2, 6, 8]
    disponibles_esquinas = [i for i in esquinas if tablero[i] == " "]
    if disponibles_esquinas:
        elegido = random.choice(disponibles_esquinas)
        tablero[elegido] = "O"
        hacer_movimiento_grafico(elegido, "O")
        return

    laterales = [1, 3, 5, 7]
    disponibles_laterales = [i for i in laterales if tablero[i] == " "]
    if disponibles_laterales:
        elegido = random.choice(disponibles_laterales)
        tablero[elegido] = "O"
        hacer_movimiento_grafico(elegido, "O")
        return

def hacer_movimiento_grafico(pos, jugador):
    color = COLOR_X if jugador == "X" else COLOR_O
    botones[pos].config(text=jugador, fg="white", bg=color, state="disabled")

# ==========================================
# LÓGICA GENERAL DE JUEGO
# ==========================================
def jugar(pos):
    global turno, puntos_x, puntos_o, empates, partidas_totales
    
    if tablero[pos] == " ":
        tablero[pos] = turno
        hacer_movimiento_grafico(pos, turno)
        
        if comprobar_ganador(turno):
            partidas_totales += 1
            if turno == "X":
                puntos_x += 1
            else:
                puntos_o += 1
            actualizar_marcador()
            messagebox.showinfo("Fin del juego", f"¡Gana el jugador {turno}!")
            nueva_partida()
            return

        if " " not in tablero:
            empates += 1
            partidas_totales += 1
            actualizar_marcador()
            messagebox.showinfo("Fin del juego", "¡Es un empate!")
            nueva_partida()
            return

        if modo_juego == 2:  
            turno = "O" if turno == "X" else "X"
            color_turno = COLOR_X if turno == "X" else COLOR_O
            texto_turno.config(text=f"Turno: {turno}", fg=color_turno)
            
        elif modo_juego == 1:  
            for b in botones: 
                b.config(state="disabled")
            
            texto_turno.config(text="Turno: Máquina (O)", fg=COLOR_O)
            ventana.update()
            ventana.after(300, procesar_turno_ia)

def procesar_turno_ia():
    global turno, puntos_o, empates, partidas_totales
    
    ejecutar_movimiento_ia()
    
    for i in range(9):
        if tablero[i] == " ":
            botones[i].config(state="normal")
            
    if comprobar_ganador("O"):
        partidas_totales += 1
        puntos_o += 1
        actualizar_marcador()
        messagebox.showinfo("Fin del juego", "¡La máquina ha ganado! 🤖")
        nueva_partida()
        return
        
    if " " not in tablero:
        empates += 1
        partidas_totales += 1
        actualizar_marcador()
        messagebox.showinfo("Fin del juego", "¡Es un empate!")
        nueva_partida()
        return
        
    turno = "X"
    texto_turno.config(text="Turno: X", fg=COLOR_X)

# ==========================================
# CONSTRUCCIÓN DE LA INTERFAZ GRÁFICA (GUI)
# ==========================================
frame_menu = tk.Frame(ventana, bg=COLOR_FONDO)
frame_menu.pack(pady=15)

btn_modo1 = tk.Button(frame_menu, text="Vs Máquina", font=("Arial", 11, "bold"), bg="#00c853", fg="white", width=12, command=lambda: cambiar_modo(1))
btn_modo1.grid(row=0, column=0, padx=10)

btn_modo2 = tk.Button(frame_menu, text="Vs Humano", font=("Arial", 11, "bold"), bg="#444444", fg="#aaaaaa", width=12, command=lambda: cambiar_modo(2))
btn_modo2.grid(row=0, column=1, padx=10)

titulo = tk.Label(ventana, text="TRES EN RAYA", font=("Arial", 24, "bold"), bg=COLOR_FONDO, fg=COLOR_TABLERO)
titulo.pack(pady=5)

texto_totales = tk.Label(ventana, text="Partidas Totales: 0", font=("Arial", 13), bg=COLOR_FONDO, fg="white")
texto_totales.pack()

frame_marcadores = tk.Frame(ventana, bg=COLOR_FONDO)
frame_marcadores.pack(pady=5)

marcador_x = tk.Label(frame_marcadores, text="X: 0", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_X)
marcador_x.grid(row=0, column=0, padx=25)

marcador_o = tk.Label(frame_marcadores, text="O: 0", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_O)
marcador_o.grid(row=0, column=1, padx=25)

texto_empates = tk.Label(ventana, text="Empates: 0", font=("Arial", 13), bg=COLOR_FONDO, fg="#cccccc")
texto_empates.pack()

texto_turno = tk.Label(ventana, text="Turno: X", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_X)
texto_turno.pack(pady=10)

frame_tablero = tk.Frame(ventana, bg=COLOR_FONDO)
frame_tablero.pack(pady=10)

for i in range(9):
    boton = tk.Button(
        frame_tablero,
        text=" ",
        font=("Arial", 22, "bold"),
        width=5,
        height=2,
        bg=COLOR_TABLERO,
        fg=COLOR_NUMEROS,
        activebackground="#ffe566",
        relief="solid",
        bd=3,
        command=lambda idx=i: jugar(idx)
    )
    boton.grid(row=i // 3, column=i % 3, padx=6, pady=6)
    botones.append(boton)

# Panel inferior con ambos botones de reinicio separados
frame_botones_abajo = tk.Frame(ventana, bg=COLOR_FONDO)
frame_botones_abajo.pack(pady=15)

boton_nueva_partida = tk.Button(
    frame_botones_abajo,
    text="Reiniciar Partida",
    font=("Arial", 11, "bold"),
    bg="#007aff",
    fg="white",
    padx=12,
    pady=6,
    command=nueva_partida
)
boton_nueva_partida.grid(row=0, column=0, padx=8)

boton_reiniciar_todo = tk.Button(
    frame_botones_abajo,
    text="Reiniciar Marcador",
    font=("Arial", 11, "bold"),
    bg="#ff9500",
    fg="white",
    padx=12,
    pady=6,
    command=reiniciar_marcadores
)
boton_reiniciar_todo.grid(row=0, column=1, padx=8)

ventana.mainloop()
