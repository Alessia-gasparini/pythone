#gennaio inizio posizione 0, febbraio inizio posizione 9, marzo inizio posizione 18..... etc
MESI = ("Gennaio  " +  #(1-1) * 9
"Febbraio " + # (2-1) * 9
"Marzo    " + # (3-1) * 9
"Aprile   " + # (4-1) * 9
"Maggio   " + # (5-1) * 9
"Giugno   " + # (6-1) * 9
"Luglio   " + # (7-1) * 9
"Agosto   " + # (8-1) * 9
"Settembre" + # (9-1) * 9
"Ottobre  " + # (10-1) * 9
"Novembre " + # (11-1) * 9
"Dicembre " ) # (12-1) * 9 
mese = int(input("indica mese: "))
p = (mese - 1) * 9
print(MESI[p:p+9])