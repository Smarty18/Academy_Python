#Scrivere un programma che chieda all'utente di inserire una sequenza di interi 
#(chiedendo prima quanti numeri inserirà)
#e poi al termine dell'inserimento dell'intera sequenza mostrare il numero di positivi pari 
#e dispari

quantiNumeri = input("Quanti numeri inserirai? \n")         #chiede all'utente quanti numeri 
                                                            #da analizzare inserirà

pari = 0                                                    #inizializza una variabile contatore 
                                                            #dei valori pari
dispari = 0                                                 #inizializza una variabile contatore 
                                                            #dei valori dispari

for i in range (int(quantiNumeri)):                         #stabilisce il numero di iterazioni da 
                                                            #fare sulla base di quanti numeri ha inserito l'utente
    daControllare = input("inserisci numero: ")             #inserisce il numero da analizzare 
    daControllare=int(daControllare)                        #casting sulla variabile per essere certi 
                                                            #che il valore da controllare sia intero

    if(daControllare%2 == 0 and daControllare>0):           #condizione che vuole la parità e positività
        i+1                                                 #incremento del ciclo
        pari+=1                                             #incremento del contatore pari

    else:
        print("Il numero non è pari")
        dispari+=1                                          #incremento del contatore dispari

print("Il numero di valori positivi e pari è:",pari,"e il numero di dispari è:",dispari)

#a video mostro il numero di valori pari e il numero di valori dispari 
#ricordo che Python con la virgola post virgolette inserisce automaticamente lo spazio

