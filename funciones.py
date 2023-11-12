from typing import List, Tuple, Dict


def abrirLaberinto(fuente: str) -> list[list[str]]:
    """Esta función abre un archivo de texto y lo convierte en una matriz de caracteres Costo: O(n*m)"""
    with open(fuente, "r") as archivo:
        laberinto = []
        linea = archivo.readline().strip()
        while linea != "":
            laberinto.append(list(linea))
            linea = archivo.readline().strip()
    return laberinto


def encontrarCaracter(laberinto: list[list[str]], caracter: str) -> tuple:
    """Esta funcion busca un caracter en la matriz y regresa su posición. Costo: O(n*m)"""
    entrada = ()
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == caracter:
                entrada = (i, j)
    return entrada


def buscarPortalSalida(matriz, inicial: tuple, letra) -> tuple:
    """Esta funcion busca un portal en la matriz y regresa la posición del otro portal Costo: O(n*m)"""
    regreso = ()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == letra and (not (i == inicial[0] and j == inicial[1])):
                regreso = (i, j)
    return regreso


def esPosible(f, c, matriz) -> bool:
    """Esta funcion verifica si es posible moverse a una casilla. Costo: O(1)"""
    return 0 <= f < len(matriz) and 0 <= c < len(matriz[0]) and matriz[f][c] != "#"


def calcular_distancia(origen: tuple, salida: tuple) -> int:
    """Esta funcion calcula la distancia entre dos puntos segun la distancia de Manhattan. Costo: O(1)"""
    return (abs(origen[0] - salida[0]) + abs(origen[1] - salida[1]))


def exportarSolucion(laberinto, matriz, movimientos):
    if movimientos != -1:
        with open('laberintoSolucion.txt', 'w', encoding="utf-8") as archivo:
            for i in range(len(laberinto)):
                for j in range(len(laberinto[0])):
                    if matriz[i][j] == 1 and laberinto[i][j] == ".":
                        archivo.write("x")
                    else:
                        archivo.write(laberinto[i][j])
                archivo.write("\n")


def buscar_portales(laberinto: List[List[str]]) -> Dict[str, List[Tuple[int, int]]]:
    """Esta funcion busca todos los portales en el laberinto y los regresa en un diccionario. Costo: O(n*m)"""
    portales = {}
    for row, line in enumerate(laberinto):
        for col, char in enumerate(line):
            if char not in [".", "#", "E", "S"] and char in portales:
                portales[char].append((row, col))
            elif char not in [".", "#", "E", "S"]:
                portales[char] = [(row, col)]
    return portales




class SolucionOptima:
    def __init__(self) -> None:
        self.mejor_camino = -1
        self.matrizVisitados = []
