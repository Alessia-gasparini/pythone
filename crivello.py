def crivello(n):
    naturali = set(range(2, n+1))
    
    for j in range(2, int(n ** (1/2))):
        for i in [x * j for x in range(2, n//2 + 1)]:
            naturali.discard(i)
  
    print(naturali)
    print(len(naturali))
crivello(int(input("Scegli un numero: ")))
