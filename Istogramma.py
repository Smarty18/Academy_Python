def istogramma(numero):

    var = True                                          #variabile booleana che non diventa 
                                                        #mai false per evitare si blocchi il while
    st = "" 
    
    while var:
        if numero == 0: #comando per interrompere l'esecuzione e mandare in stampa l'istogramma
            break

        elif numero<0:
            print ("ERRORE: La funzione necessita di valore positivo")
        break  
    if numero > 0 :
        for i in range (0,numero):
            
            st = st + "*" 
        st = st + "\n"

    print(st)

istogramma(6)