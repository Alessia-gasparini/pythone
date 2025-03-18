GIORNO = ("Lunedì   " +  #(1-1) * 9
"Martedì  " + # (2-1) * 9
"Mercoledì" + # (3-1) * 9
"Giovedì  " + # (4-1) * 9
"Venerdì  " + # (5-1) * 9
"Sabato   " + # (6-1) * 9
"Domenica " ) # (7-1) * 9
giorno = int(input("indica giorno: "))
p = (giorno - 1) * 9
print(GIORNO[p:p+9])