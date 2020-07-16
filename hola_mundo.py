#hola mundo
a = 5 + 5
print (a)

#Variable e ingreso de datos

#nombre = input ("dame tu nombre:")

#print ("hola" + nombre )

#Operadores aritmeticos
 # lo mismo, como sumar, restar, dividir, los float  y todo eso 


#Condiciones 

#1
N1 = input ("numero1:")
N2 = input ("numero2:")
N3 = input ("numero3: ")

if N1 > N2 :
    if N1 > N3 :
        if N2 > N3 :
            print (float(N1) + "-" + str(N2) + "-"+ str(N3))
        else:
            print (str(N1) + "-" + str(N3) + "-" + str(N2))
    else:
        print (str(N3) + "-" + str(N1) + "-" + str(N2))
else:
    if N2 > N3 :
        if N1 > N3 :
            print (str(N3) + "-" + str(N2) + "-"+ str(N1))
        else:
            print (str(N2) + "-" + str(N1) + "-"+ str(N3))
print (str(N3) + "-" + str(N2) + "-"+ str(N1))
        

