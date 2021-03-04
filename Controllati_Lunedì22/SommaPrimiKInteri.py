# Programma che riceve in ingresso un numero positivo N e 
# determina il massimo K tale che òa somma dei primi K interi sia
# minore o unguale a N 
# Es. N=20 --> K=5, perchè 1+2+3+4+5=15


N=int(input("Inserisci un numero N positivo: ")) #l'utente inserisce il numero N 
K=0                                              #inizializzo la variabile K (numero dei primi interi la cui somma < N)
numero = 1                                       # numero è il successivo che aggiungo al primo numero (nl mio caso il primo numero è somma = 0)
somma = int(0)                                   # inizializzo la somma

while somma < N :                                #entro nel while finché la somma è minore del valore N
    
    somma = somma + numero                       #aggiungo alla somma il successivo (se somma è 0, successivo è 1) 
    print ("La somma è : ",somma)
    numero = numero + 1                          # incremento il successivo 
    print (numero)                              
    if somma < N:                                #voglio che K si incrementi SOLO SE la somma in out è <N
        K = K + 1
        print("Il k è : ",K)
     
print(K)
