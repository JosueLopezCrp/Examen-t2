import random
def generar_lista(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(10, 9999)) 
    return lista
def min_max_multiplos3(lista, ini, fin):
    if ini == fin:
        if lista[ini] % 3 == 0:
            return lista[ini], lista[ini]
        else:
            return None, None
    medio = (ini + fin) // 2
    min1, max1 = min_max_multiplos3(lista, ini, medio)
    min2, max2 = min_max_multiplos3(lista, medio + 1, fin)
    min_final = None
    max_final = None
    if min1 is not None:
        min_final = min1
        max_final = max1
    if min2 is not None:
        if min_final is None:
            min_final = min2
            max_final = max2
        else:
            if min2 < min_final:
                min_final = min2
            if max2 > max_final:
                max_final = max2
    return min_final, max_final
def main():
    while True:
        n = int(input("Tamaño del arreglo: "))
        if 2 <= n <= 4:
            break
        else:
            print("Error: solo se permite 2, 3 o 4")
    lista = generar_lista(n)
    print("Lista:", lista)
    minimo, maximo = min_max_multiplos3(lista, 0, len(lista) - 1)
    if minimo is None:
        print("No hay múltiplos de 3")
    else:
        promedio = (minimo + maximo) / 2
        print("Min:", minimo)
        print("Max:", maximo)
        print("Promedio:", promedio)
main()