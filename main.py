from funciones import *


def solucion(f: int, c: int, laberinto: list[list[str]], matrizVis: list[list[int]], contador: int, mejor_solucion: SolucionOptima, salida, hPortales: bool):
    primera = contador > mejor_solucion.mejor_camino
    segunda = not hPortales and (calcular_distancia(
        (f, c), salida) + contador > mejor_solucion.mejor_camino)
    tercera = hPortales and (contador + distancia_portal((f,c),buscar_portales(laberinto),salida) > mejor_solucion.mejor_camino)

    if (primera or segunda or tercera) and mejor_solucion.mejor_camino != -1:
        return
    if laberinto[f][c] == "S":
        if contador < mejor_solucion.mejor_camino or mejor_solucion.mejor_camino == -1:
            mejor_solucion.mejor_camino = contador
            matrizCopia = [[x for x in matrizVis[i]] for i in range(len(matrizVis))] #nopep8
            mejor_solucion.matrizVisitados = matrizCopia
        return

    matrizVis[f][c] = 1

    if laberinto[f][c] not in ["#", ".", "E", "S"]:
        otroPortal = buscarPortalSalida(laberinto, (f, c), laberinto[f][c])
        if len(otroPortal) == 2 and matrizVis[otroPortal[0]][otroPortal[1]] != 1:
            letraPortal = laberinto[f][c]
            laberinto[f][c] = "."
            laberinto[otroPortal[0]][otroPortal[1]] = "."
            solucion(otroPortal[0], otroPortal[1], laberinto,
                     matrizVis, contador + 1, mejor_solucion, salida, hPortales)
            laberinto[f][c] = letraPortal
            laberinto[otroPortal[0]][otroPortal[1]] = letraPortal

    for i in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if esPosible(f + i[0], c + i[1], laberinto) and matrizVis[f + i[0]][c + i[1]] != 1:
            solucion(f + i[0], c + i[1], laberinto, matrizVis,
                     contador + 1, mejor_solucion, salida, hPortales)

    matrizVis[f][c] = 0


def main():
    laberinto = abrirLaberinto("laberinto.txt")
    entrada = encontrarCaracter(laberinto, 'E')
    salida = encontrarCaracter(laberinto, 'S')
    portales = len(buscar_portales(laberinto)) != 0
    matrizVisitados = [
        [0 for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]
    mejor_solucion = SolucionOptima()
    solucion(entrada[0], entrada[1], laberinto,
             matrizVisitados, 0, mejor_solucion, salida, portales)
    print("Mejor solución:", mejor_solucion.mejor_camino)
    exportarSolucion(laberinto, mejor_solucion.matrizVisitados,
                     mejor_solucion.mejor_camino)


if __name__ == "__main__":
    main()
