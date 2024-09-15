#if expresion:
#  accion_1
#  accion_2

hay_sol = False
hace_frio = True
if hay_sol and not hace_frio:
  print("Voy a usar gorra y no me pongo buzo")
elif hay_sol and hace_frio:
  print("Voy a usar gorra y me pongo buzo")
elif not hay_sol and not hace_frio:
  print("Salgo sin gorra y sin buzo")
else:
  print("Salgo sin gorra y me pongo buzo")

def division(dividendo, divisor):
  if divisor == 0:
    return "Error"
  else:
    resultado = dividendo / divisor
    return resultado

def division(dividendo, divisor):
  if divisor == 0:
    return "Error"
  return dividendo / divisor
