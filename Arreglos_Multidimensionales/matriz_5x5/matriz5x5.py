matriz = [[0 for _ in range(5)] for _ in range(5)]

for fila in range(5):
    for columna in range(5):
        matriz = int(input("Ingrese 25 valores númericos:"), [fila][columna])
print(matriz)

for fila in range(5):
    for columna in range(5):
        print(matriz, end="")
