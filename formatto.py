lista = list(range (1, 10)) 
lista2 = [1 / x for x in lista]
for x in lista2: 
  print(f"valore: {x: 10.8f}")
