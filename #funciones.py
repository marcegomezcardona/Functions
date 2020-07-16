#funciones 
#agrupar codigo en comun que se va a estar llamando constantemente 
#definirla / llamara

def  n_robot (numero_robot):
    print (numero_robot)



def v_robot (porcent_bateria):
    print (porcent_bateria)
    

def p_robot (pola_robot):
    print (pola_robot)

def door_state (estado):
    if estado == True:
        print ("puerta abierta")
    if estado == False:
        print ("puerta cerrada")


def driver (nombre):
    print (nombre)




n_robot (7)
v_robot (12.3)
door_state (False)
driver ("Lorena")