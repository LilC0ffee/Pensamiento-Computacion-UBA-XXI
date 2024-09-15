def edad(persona):
  return persona[1]


personas = [
  ("Manola Bellido Mur", 34),
  ( "Segismundo Andreu Maldonado", 21),
  ("Anselma Arregui-Solano", 67),
  ("Candelas Perello Marquez", 23),
  ("Itziar Flores Viana", 87),
  ("Armida Peinado Jaen", 34),
  ("Cecilia del Vilaplana", 67),
  ("Mayte Amador Lamas", 99),
  ("Heliodoro Serra Cases", 28),
  ("Lope Orozco", 46)
]

resultado = ("Cecilia del Vilaplana", 67) in personas
print(resultado)

resultado = personas.index(("Cecilia del Vilaplana", 67))
print(resultado)

# Ordena la lista de forma ascendente
personas.sort()
print(personas)
# Ordena la lista de forma descendente. Ultimo a los mayores
personas.sort(reverse=True)
print(personas)

# Ordena la lista de forma ascendente por el nombre
personas.sort(key=edad)

# Ordena la lista de forma descendente por el nombre
personas.sort(key=edad, reverse=True)