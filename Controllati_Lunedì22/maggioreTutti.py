#In commento quello che risale dall'aula
#n = input ("Inserisci il numero di valori da confrontare: ")
#if n==0:
 #   break
#else:
 #   maggiore = 0
  #  for i in range (int(n)):
   #     valore[i] = int(input("Inserisci valore"))

    #    for i in range (int(n))
     #       if valore[i] > maggiore:
      #          maggiore = valore[i]
       #         i = i+1


#Inizia il programma pensato da me
N = int(input("Quanti valori vuoi confrontare? \n")) #chiedo quanti valori bisogna confrontare 

if N==0: #se non ci sono valori da confrontare saluto l'utente
    print("Alla prossima!")
else: #se il numero N è diverso da zero inizializzo una variabile i contatore e impongo il massimo ipoteticamente a 0
    i=0
    max=0
    while i<N: #ciclo fino a che la i è minore di N
        valore=input("Inserisci valore: \n") #chiedo in input il valore da confrontare e lo forzo ad intero
        valore=int(valore)
        if (valore>max): #confronto il valore appena inserito con il massimo 
            max = valore #se il valore è maggiore del massimo, assegno al massimo questo nuovo valore
            i+=1
        else: #se il valore non è maggiore del massimo, passo all'iterazione successiva
            i+=1
    print("il valore massimo è: ", max) #alla fine del ciclo stampo il valore massimo