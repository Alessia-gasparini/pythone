filename = input("Indica un nome file da leggere: ") #nome file = numeri.txt
daLeggere = open(filename, "r")
righe = daLeggere.readlines()


daScrivere = open("numeri.txt", "w")
numeri = list(range (1, 10))
file=daScrivere
daScrivere.close()

media= sum(numeri)
massimo = max(numeri)

daLeggere = open("numeri.txt", "r")
print(daLeggere.readline())
daLeggere.close()

print("valore max: ",massimo, "la media è: ",media )
daLeggere.close()