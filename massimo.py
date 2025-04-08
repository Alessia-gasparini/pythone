prova = []
userImput= input ("inserisci un numero: ")
while userImput != "q":
    prova.append(int(userImput))
    userImput= input ("inserisci un numero: ")
    temp = None # per fare un confronto (valore temporaneo)
    for v in prova:
        if temp == None :
            temp = v
        else:
            if temp < v:
                temp = v
    print("valore max: ", temp)