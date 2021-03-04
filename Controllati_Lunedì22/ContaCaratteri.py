#Funzione che conta il numero di caratteri in una stringa

def contaCaratteri ( ):                                     #definisco la funzione
    stringa = input("Inserisci una stringa: \n")            #chiedo in input una stringa
    
    numCaratteri = 0                                        #inizializzo il numero di caratteri a 0
                                                    
    for elem in stringa:                                    #ciclo sulla lunghezza della stringa
        if elem != " ":                                     #se l'elemento della stringa è diverso dal carattere vuoto
            numCaratteri += 1                               #aggiorno il numero di caratteri, incrementandolo
           

    return print("Il numero di caratteri è:",numCaratteri)  #stampa il numero di caratteri e ritorna questo valore alla funzione


contaCaratteri()
