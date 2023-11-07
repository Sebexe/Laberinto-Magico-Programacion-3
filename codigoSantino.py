lista_1: list[int] = [1, 3, 5, 7, 9, 11]
lista_2: list[int] = [0, 2, 4, 6, 8, 10]

i : int = 0  #indice de la lista 1
j : int = 0  #indice de la lista 2

lista_3 = []

while (i < len(lista_1) or j < len(lista_2)):

  if i == len(lista_1): #Nos quedamos sin numeros en la lista 1
    lista_3.append(lista_2[j])
    j = j +  1
  elif j == len(lista_2): #Nos quedamos sin numeros en la lista 2
    lista_3.append(lista_1[i])
    i = i +  1
  
  elif lista_1[i] < lista_2[j]:  # Primer caso, el numero que esta en la lista 1 es menor
    lista_3.append(lista_1[i])
    i = i +1
  elif lista_2[j] < lista_1[i]:  # Segundo caso, el numero que esta en la lista 2 es menor
    lista_3.append(lista_2[j])
    j = j + 1
  
print(lista_3)


