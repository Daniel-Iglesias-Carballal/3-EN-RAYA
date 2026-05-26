
tablero = ["1", "2", "3",
           "4", "5", "6",
           "7", "8", "9"]

turno = "X"


def mostrar():
    print("\n╔═══╦═══╦═══╗")
    print(f"║ {tablero[0]} ║ {tablero[1]} ║ {tablero[2]} ║")
    print("╠═══╬═══╬═══╣")
    print(f"║ {tablero[3]} ║ {tablero[4]} ║ {tablero[5]} ║")
    print("╠═══╬═══╬═══╣")
    print(f"║ {tablero[6]} ║ {tablero[7]} ║ {tablero[8]} ║")
    print("╚═══╩═══╩═══╝\n")

while True:
        mostrar()


        pos = int(input("Elige posición (1-9): ")) - 1

        if tablero[pos] == "X" or tablero[pos] == "O":
            print("Casilla ocupada")
            continue
        tablero[pos] = turno

    # Comprobar victoria
        if (
                (tablero[0] == tablero[1] == tablero[2]) or
                (tablero[3] == tablero[4] == tablero[5]) or
                (tablero[6] == tablero[7] == tablero[8]) or
                (tablero[0] == tablero[3] == tablero[6]) or
                (tablero[1] == tablero[4] == tablero[7]) or
                (tablero[2] == tablero[5] == tablero[8]) or
                (tablero[0] == tablero[4] == tablero[8]) or
                (tablero[2] == tablero[4] == tablero[6])
        ):
                mostrar()
                print("¡Gana",turno,"!")
                break

        # Cambiar turno
        if turno == "X":
            turno = "O"
        else:
            turno = "X"
