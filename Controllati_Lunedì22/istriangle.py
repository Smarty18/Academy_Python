def isTriangle (a, b, c):                           #Definisco la funzione che richiede
                                                    #tre input pari alle lunghezze dei
                                                    #tre lati del triangolo
    
    if (a+b>=c) and (a+c>=b) and (b+c>=a):          #condizione affinché siano lati di un triangolo
        if (a+b==c) or (a+c==b) or (b+c==a):        #condizione affinché sia degenere
            print ("Degenere")
        else:                                       #se è triangolo, ma non degenere
            print("Sì")
    else:                                           #se non possono essere lati di un triangolo
        print("No!")

isTriangle(2,3,1)                                   #chiamata 