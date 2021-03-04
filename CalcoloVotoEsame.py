#Calcola il risultato di un esame 
#Gli input sono due: il voto ottenuto nella prova scritta che dev'essere 
# compreso nell'intervallo [-8 e 8] e il voto della prova pratica in [0,24]

Scritto = input("Inserire voto scritto: ")          #Inserire il voto dello scritto
Scritto=int(Scritto)                                #poiché potrebbe essere str lo forzo ad intero
if (Scritto<-8 or Scritto>8):                       #condizione: il valore dello scritto dev'essere compreso tra -8 ed 8
    print("Il voto inserito non è corretto!")       #se l'utente inserisce un voto che non rientra nel range,
                                                    #messaggio di errore e si effettua nuovamente la richiesta
    Scritto=input("Inserire voto scritto: ")

#Analogo discorso per il voto pratico con range [0,24]
Pratica = input ("Inserire voto pratica: ")
Pratica=int(Pratica)
if (Pratica < 0 or Pratica>24):
    print("Il voto inserito non è corretto!")
    Pratica=input("Inserire voto pratica: ")


Ris = int(Scritto + Pratica)                        #Il risultato dell'esame è la somma tra scritto e pratica

                                                   
                                                    
                                                    
                                                    
if (Scritto<=0):                                    #voto dello scritto < 0 : bocciato, 
    print ("Bocciato")
elif (Scritto>0 and Ris<=18):                       #scritto positivo ma voto complessivo < 18: bocciato,
    print ("Bocciato")
elif (Ris>30):                                      #voto complessivo > 30 : LODE, 
    print ("Promosso con lode")
else:                                               #voto complessivo > 18 : promosso.
    print("Promosso")
print(Ris)                                          #stampa a video del risultato