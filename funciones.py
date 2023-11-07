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
  for i, row in enumerate(matriz):
    if letra in row and (i, row.index(letra)) != inicial:
      return (i, row.index(letra))
  return ()


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
      distanciaTotal = (abs(origen[0] - j[0]) + abs(origen[1] - j[1])) + (abs(portales[i][0][0] - portales[i][1][0]) + abs(portales[i][0][1] - portales[i][1][1])) + (calcular_distancia(portales[i][0], salida) if calcular_distancia(portales[i][0], salida) < calcular_distancia(portales[i][1], salida) else calcular_distancia(portales[i][1], salida))
      if distanciaTotal < distancia_minima:
        distancia_minima = distanciaTotal
  return distancia_minima
