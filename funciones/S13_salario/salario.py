# calcular salario de un obrero

# creamos una funcion, la funcion recibe dos parametros
def calcular_salario(horas, pago_hora):

# dentro de la funcion calculamos el salario, con return devolvemos el resultado
    return horas * pago_hora

# pedimos los datos al usuario    
horas = float(input("Ingrese las horas de trabajo semanal: "))
pago_hora = float(input("Ingrese el pago por cada hora de trabajo: "))

# llamamos a la funcion y se guarda el resultado en la variable
salario_semanal = calcular_salario(horas, pago_hora)

# mostramos el salario semanal, .2f que muestre con dos decimales
print(f"Su salario semanal es: {salario_semanal:.2f} dólares")