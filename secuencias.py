tupla_vacia = ()
print("Lista vacia:", tupla_vacia)

lista_vacia = ()
print("Lista vacia", lista_vacia)

tupla_1_elemento = ("Pensamiento",)
print("Tupla 1 elemento:", tupla_1_elemento)

lista_1_elemento = ["Pensamiento"]
print("Lista 1 elemento:", lista_1_elemento)

tupla_varias_elemento = ("Pensamiento", 56, "a", [1, 2])
print("Tupla varios elemento:", tupla_varias_elemento)

lista_varias_elemento = ["Pensamiento", 87, 475.32443, ["Pensamiento", "Computacional"]]
print("Lista varios elemento:", lista_varias_elemento)

elemento_0_tupla = tupla_varias_elemento[0]
print(elemento_0_tupla)

elemento_3_lista = lista_varias_elemento[3]
print(elemento_3_lista)

fecha = (12, "Junio", 1970)
print(fecha)

dia, mes, anio = fecha
print(mes)

puntos = [
  (4, 6),
  (8, 2),
  (10, 5),
  (1, 1),
  (0, 7),
  (0, 0),
  (2, 3),
  (2, 2)
]

#Las listas tienen un monton de funciones que se pueden usar
# Append
# Agrega el elemento al final de la lista
puntos.append((50,50))
#Insert
# Insertamos el punto (80,80) en la posicion 4
puntos.insert(4, (80,80))
# Remove
# Removemos el punto (0,7)
puntos.remove( (0,7) )

for punto in puntos:
  x,y = punto
  print("x:", x, "- y:", y)

