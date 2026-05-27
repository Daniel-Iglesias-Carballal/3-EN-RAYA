import os
import time

# =========================
# COLORES ANSI
# =========================
ROJO = "\033[91m"
AZUL = "\033[94m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# =========================
# TABLERO
# =========================
tablero = ["1", "2", "3",
           "4", "5", "6",
           "7", "8", "9"]

turno = "X"

# =========================
# LIMPIAR PANTALLA
# =========================
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# =========================
# ANIMACIÓN
# =========================
def animacion(texto, color):

    for letra in texto:
        print(color + letra + RESET, end="", flush=True)
        time.sleep(0.03)

    print()

# =========================
# COLOR POR JUGADOR
# =========================
def colorear(valor):

    if valor == "X":
        return ROJO + valor + RESET

    elif valor == "O":
        return AZUL + valor + RESET

    return CYAN + valor + RESET

# =========================
# MOSTRAR TABLERO
# =========================
def mostrar():

    limpiar()

    print(AMARILLO)
    print("╔═══╦═══╦═══╗")

    print(
        f"║ {colorear(tablero[0])} ║ "
        f"{colorear(tablero[1])} ║ "
        f"{colorear(tablero[2])} ║"
    )

    print("╠═══╬═══╬═══╣")

    print(
        f"║ {colorear(tablero[3])} ║ "
        f"{colorear(tablero[4])} ║ "
        f"{colorear(tablero[5])} ║"
    )

    print("╠═══╬═══╬═══╣")

    print(
        f"║ {colorear(tablero[6])} ║ "
        f"{colorear(tablero[7])} ║ "
        f"{colorear(tablero[8])} ║"
    )

    print("╚═══╩═══╩═══╝")
    print(RESET)

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
            return True

    return False

# =========================
# ANIMACIÓN INICIAL
# =========================
limpiar()

animacion("🎮 Cargando Tres en Raya...", VERDE)

time.sleep(1)

# =========================
# BUCLE PRINCIPAL
# =========================
while True:

    mostrar()

    color_turno = ROJO if turno == "X" else AZUL

    animacion(f"Turno de {turno}", color_turno)

    try:
        pos = int(input(CYAN + "Elige posición (1-9): " + RESET)) - 1

        if pos < 0 or pos > 8:
            animacion("❌ Posición inválida", ROJO)
            time.sleep(1)
            continue

        if tablero[pos] in ["X", "O"]:
            animacion("⚠ Casilla ocupada", AMARILLO)
            time.sleep(1)
            continue

        # ANIMACIÓN DE JUGADA
        animacion("Colocando ficha...", VERDE)

        time.sleep(0.5)

        tablero[pos] = turno

        # VICTORIA
        if victoria():

            mostrar()

            animacion(
                f"🏆 ¡Gana {turno}!",
                VERDE
            )

            break

        # EMPATE
        if all(x in ["X", "O"] for x in tablero):

            mostrar()

            animacion(
                "🤝 ¡Empate!",
                AMARILLO
            )

            break

        # CAMBIO DE TURNO
        turno = "O" if turno == "X" else "X"

    except ValueError:

        animacion(
            "❌ Introduce un número válido",
            ROJO
        )

        time.sleep(1)