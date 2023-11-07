def abrirLaberinto(fuente):
    with open(fuente, "r") as archivo:
        laberinto = []
        linea = archivo.readline().strip()
        while linea != "":
            laberinto.append(list(linea))
            linea = archivo.readline().strip()
    return laberinto


laberinto = abrirLaberinto("laberinto.txt")

matrizVisitados = [[0 for _ in range(len(laberinto[0]))]
                   for _ in range(len(laberinto))]


def encontrarEntrada(laberinto):
    entrada = ()
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == "E":
                entrada = (i, j)
    return entrada


def buscarPortal(matriz, inicial: tuple, letra):
    regreso = ()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == letra and (not (i == inicial[0] and j == inicial[1])):
                regreso = (i, j)
    return regreso


def esPosible(f, c, matriz):
    posible = True
    # Nos vamos hacia arriba
    if (f == -1):
        posible = False
    elif (c == -1):  # Nos vamos hacia la izquierda
        posible = False
    elif (f >= len(matriz)):  # Nos vamos hacia la derecha
        posible = False
    elif (c >= len(matriz[0])):  # Nos vamos hacia abajo
        posible = False
    elif (matriz[f][c] == "#"):  # Nos vamos hacia una pared
        posible = False
    return posible


(-1, 0),


soluciones = []


def solucion(f: int, c: int, laberinto: list[list[str]], matrizVis: list[list[int]], contador: int = 0):
    if laberinto[f][c] == "S":  # Si estamos en la salida guardamos el contador
        soluciones.append(contador)
        return
    matrizVis[f][c] = 1  # Marcamos esta celda como visitada
    for i in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if laberinto[f][c] not in ["#", ".", "E", "S"]:
            otroPortal = buscarPortal(laberinto, (f, c), laberinto[f][c])
            temporalcar = laberinto[f][c]
            if matrizVis[otroPortal[0]][otroPortal[1]] != 1:
                laberinto[f][c] = "."
                laberinto[otroPortal[0]][otroPortal[1]] = "."
                solucion(otroPortal[0], otroPortal[1], laberinto,
                         matrizVis, contador + 1)
            laberinto[f][c] = temporalcar
            laberinto[otroPortal[0]][otroPortal[1]] = temporalcar
        elif esPosible(f + i[0], c + i[1], laberinto) and matrizVis[f + i[0]][c + i[1]] != 1:
            solucion(f + i[0], c + i[1], laberinto, matrizVis,
                     contador + 1)


entrada = encontrarEntrada(laberinto)

solucion(entrada[0], entrada[1], laberinto, matrizVisitados)

print(soluciones)
