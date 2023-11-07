import time,os

def imprimirMatriz(m):
    for i in m:
        print(i)


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


def distanciaPortal(origen, portales: dict,salida):
    distancia_minima = float("inf")
    for i in portales.keys():
        for j in portales[i]:
            distanciaTotal = calcular_distancia(
                origen, j) + min(calcular_distancia(portales[i][0],salida), calcular_distancia(portales[i][1],salida))
            if distanciaTotal < distancia_minima:
                distancia_minima = distanciaTotal
    return distancia_minima


def solucion(f: int, c: int, laberinto: list[list[str]], matrizVis: list[list[int]], contador: int, mejor_solucion: SolucionOptima, salida: tuple, portales: dict):
    distancia_acumulada = calcular_distancia((f, c), salida)
    posiblePortal = distanciaPortal((f, c), portales, salida)
    if distancia_acumulada - posiblePortal >= mejor_solucion.mejor_camino + 1 and mejor_solucion.mejor_camino != -1:
        return

    if laberinto[f][c] == "S":
        if contador < mejor_solucion.mejor_camino or mejor_solucion.mejor_camino == -1:
            mejor_solucion.mejor_camino = contador
        return

    matrizVis[f][c] = 1
    for i in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if laberinto[f][c] not in ["#", ".", "E", "S"]:
            otroPortal = buscarPortal(laberinto, (f, c), laberinto[f][c])
            temporalcar = laberinto[f][c]
            if matrizVis[otroPortal[0]][otroPortal[1]] != 1:
                laberinto[f][c] = "."
                laberinto[otroPortal[0]][otroPortal[1]] = "."
                solucion(otroPortal[0], otroPortal[1], laberinto,
                         matrizVis, contador + 1, mejor_solucion, salida,portales)
            laberinto[f][c] = temporalcar
            laberinto[otroPortal[0]][otroPortal[1]] = temporalcar
        elif esPosible(f + i[0], c + i[1], laberinto) and matrizVis[f + i[0]][c + i[1]] != 1:
            solucion(f + i[0], c + i[1], laberinto, matrizVis,
                     contador + 1, mejor_solucion, salida,portales)
    matrizVis[f][c] = 0


def main():
    laberinto = abrirLaberinto("laberinto.txt")
    entrada = encontrarCaracter(laberinto, 'E')
    salida = encontrarCaracter(laberinto, 'S')
    matrizVisitados = [
        [0 for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]
    mejor_solucion = SolucionOptima()
    solucion(entrada[0], entrada[1], laberinto,
             matrizVisitados, 0, mejor_solucion, salida,buscarPortales(laberinto))
    print("Mejor solución:", mejor_solucion.mejor_camino)




if __name__ == "__main__":
    main()
