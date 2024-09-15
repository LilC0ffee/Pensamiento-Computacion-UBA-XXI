# Enteros
x = 10
y = 15
# - Sumar
suma = x + y
print(type(suma))
# - Restar
resta = x - y
print(type(resta))
# - Multiplicar
multiplicacion = x * y
print(type(multiplicacion))
# - Dividir
division = x / y
print(type(division))

nombre = "Pensamiento"
apellido = "Computacional"

# Conocer el largo de un string
largo_nombre = len(nombre)
print(largo_nombre)

# Concatenar 2 strings
nombre_materia = nombre + " " + apellido
print(nombre_materia)

# Cortar un string
desde_donde = 5
hasta_donde = 9
cada_cuantas = 1
nombre_corto = nombre[desde_donde:hasta_donde:cada_cuantas]
nombre_corto_2 = nombre[5:12:2]
print(nombre_corto)
print(nombre_corto_2)
