#Funzione che restituisce il maggiore tra due numeri inseriti da tastiera

def piuGrande (numero1,numero2):
    if numero1>numero2:
        print("Il maggiore è:",numero1)
    else :
        print("Il maggiore è:",numero2)

a = input("Inserisci il primo valore: \n")
b = input("inserisci il secondo valore: \n")
piuGrande(a,b)

#La stessa funzione può evitare l'input da tastiera (più corretto)
def piuGrande (numero1,numero2):
    if numero1>numero2:
        print("Il maggiore è:",numero1)
    else :
        print("Il maggiore è:",numero2)


piuGrande(5,7)