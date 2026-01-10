#Contexto global
p= 10
h= 20

nombre= "Estefanny"

def saludar (nombre): #Comienza un nuevo contexto
    x= 15
    print(x)

    def despedir (): #nuevo contexto que vive dentro de saludar 
        print ("Adios", x)


    