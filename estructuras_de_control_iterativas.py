print("Antes del while")
paso = 1
while (paso <= 10):
  print(paso)
  paso = paso + 1

print("Despues del while")

conjunto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in conjunto:
  print(numero)
# El range nos permite generar un conjunto de numeros, pero no lo imprime
# El start es inclusivo mientro que el stop es exclusivo
# El start es por defecto 0 cero
range(1, 3)
for numero in range(1, 11):
  print(numero)
# El 3er argumento es el salto que da entre numeros
for numero in range(6, 11, 12):
  print(numero)
