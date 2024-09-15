def saludar(nombre):
  print("Hola " + nombre + "! Espero que estes muy bien :)")


saludar("Manuel")


def mostrar_suma(sumando_1, sumando_2):
  suma = sumando_1 + sumando_2
  print("La suma es ", suma)


mostrar_suma(3, 13)


def sumar(sumando_1, sumando_2):
  resultado = sumando_1 + sumando_2
  return resultado


resultado_suma = sumar(5, 9)
print(resultado_suma)


# Podemos retornar mas de un resultado por funcion
def resultados(numero_1, numero_2):
  suma = numero_1 + numero_2
  resta = numero_1 - numero_2
  return suma, resta


# pero tenemos que preparar las variables para recibirlos
suma, resta = resultados(30, 18)
print("La suma es ", suma)
print("La resta es ", resta)
