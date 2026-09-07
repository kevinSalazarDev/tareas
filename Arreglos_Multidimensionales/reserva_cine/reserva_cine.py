asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

#antes de reservar necesitamos saber que asientos están disponibles
print("Asientos disponibles: ")

for fila in range(3):
    for columna in range(4):
        print(asientos[fila][columna], end=" ")
    print()

#no tiene lógica pedir un numero del 0 al 2, ya que el usuario del cine se confundirá
fila_reserva = int(input("Ingrese la fila (1 a 3): "))

#lo mismo con la columna del cine, el usuario puede que no sepa del lenguaje de las computadoras que usan 0 y 1 
columna_reserva = int(input("Ingrese la columna (1 a 4): ")) 

fila = fila_reserva - 1
columna = columna_reserva - 1

asientos[fila][columna] = 1
print("\nEstado de la sala: ")


for fila in range(3):
    for columna in range (4):
        print(asientos[fila][columna], end=" ")
    print()

print("\nEl asiento de la fila", fila_reserva, "y columna", columna_reserva, "ha sido reservado")