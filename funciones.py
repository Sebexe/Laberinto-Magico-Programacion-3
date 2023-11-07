def abrirLaberinto(fuente):
    with open(fuente, "r") as archivo:
        laberinto = []
        linea = archivo.readline().strip()
        while linea != "":
            laberinto.append(list(linea))
            linea = archivo.readline().strip()
    return laberinto


class SolucionOptima:
    def __init__(self):
        self.mejor_camino = -1


def encontrarCaracter(laberinto, caracter):
    entrada = ()
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == caracter:
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
    return 0 <= f < len(matriz) and 0 <= c < len(matriz[0]) and matriz[f][c] != "#"


def calcular_distancia(origen: tuple, salida: tuple) -> float:
    return (abs(origen[0] - salida[0]) + abs(origen[1] - salida[1]))


def buscarPortales(laberinto):
    portales = dict()
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] not in [".", "#", "E", "S"] and laberinto[i][j] in portales.keys():
                portales[laberinto[i][j]].append((i, j))
            elif laberinto[i][j] not in [".", "#", "E", "S"]:
                portales[laberinto[i][j]] = [(i, j)]
    return portales


def distanciaPortal(origen, portales: dict, salida):
    distancia_minima = float("inf")
    for i in portales.keys():
        for j in portales[i]:
            distanciaTotal = calcular_distancia(
                origen, j) + calcular_distancia(portales[i][0], portales[i][1]) + min(calcular_distancia(portales[i][0], salida), calcular_distancia(portales[i][1], salida))
            if distanciaTotal < distancia_minima:
                distancia_minima = distanciaTotal
    return distancia_minima
