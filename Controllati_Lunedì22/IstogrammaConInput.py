def istogramma():

    var = True #variabile booleana che non diventa mai false per non bloccare il while
    st = "" 
    while var:
        
        numero = int(input("Inserisci un valore:")) #numero di *
        if numero == 0: #comando per interrompere l'esecuzione e mandare in stampa l'istogramma
            break

        elif numero<0:
            print ("Inserisci un numero positivo")
            numero = input ("Inserisci un valore: ")
        
        for i in range (0,numero):
            
            st = st + "*" 
        st = st + "\n"

    print(st)

istogramma()


   