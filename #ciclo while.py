#ciclo while 

NM = int (input ("dime el numero magico muahaha: "))

print ("Ahora te toca adivinar el numero magico jeje")

NNM = int (input ("Escribe el numero no magico: "))

while NM != NNM:
    if NM > NNM:
       NNM = int (input ("fallaste, intenta con un numero mas grande: "))
       continue
    NNM = int (input ("fallaste, intenta con un numero mas pequeño: "))
print ("bien hecho")