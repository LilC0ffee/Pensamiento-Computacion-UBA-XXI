def cortar_palabra(palabra):
  return palabra[:4]


palabras = ("mesa", "silla", "ventana", "puerta", "auto", "pileta", "plantas")
# map() recibe dos argumentos, la funcion y la lista
palabras_cortas = map(cortar_palabra, palabras)
# map() transforma la lista pero devuelve un mapa
print(palabras_cortas)
# Para que se vea la lista debemos convertir el mapa en una lista
print(list(palabras_cortas))


def sumar_uno(numero):
  return numero + 1


numeros = [3, 5, 7, 4, 2, 4]
nuevos_numeros = list(map(sumar_uno, numeros))
print(numeros)
print(nuevos_numeros)


# filter() recibe dos argumentos, la funcion y la lista
def es_palabra_corta(palabra):
  longitud = len(palabra)
  if (longitud < 5):
    return True
  else:
    return False


def es_palabra_larga(palabra):
  longitud = len(palabra)
  if (longitud < 5):
    return False
  else:
    return True


palabras_cortas = filter(es_palabra_corta, palabras)
palabras_largas = filter(es_palabra_larga, palabras)
print(list(palabras_cortas))
print(list(palabras_largas))
