parola=str(input("inserisci una parola \n"))

lunghezza=int(len(parola))
for i in range(0,lunghezza):
    if (parola[i]!=parola[-i-1]):
        print("non è palindroma")
        break
    
