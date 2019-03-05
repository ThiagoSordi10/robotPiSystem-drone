import RPi.GPIO as GPIO
import time
import threading
from controle import *
from distancia import *

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

SENSOR_DIR = 40
SENSOR_ESQ = 38

estado_ativo = GPIO.LOW
motores = 1

def setup_sensor():
    global estado_ativo
    GPIO.setup(SENSOR_DIR, GPIO.IN)
    GPIO.setup(SENSOR_ESQ, GPIO.IN)
    setup_motor()
    setup_sensor_som()
    if GPIO.input(SENSOR_ESQ) == GPIO.HIGH & GPIO.input(SENSOR_DIR) == GPIO.HIGH:
        estado_ativo = GPIO.HIGH
    else:
        estado_ativo = GPIO.LOW


def esquerdo():
    if GPIO.input(SENSOR_ESQ) == estado_ativo:
        print("CAMINHO")
        return True
    else:
        print("FORA CAMINHO")
        return False

def direito():
    if GPIO.input(SENSOR_DIR) == estado_ativo:
        print("Caminho")
        return True
    else:
        print("Fora caminho")
        return False
    
def controla_distancia():
    global motores
    motores = 0
    while True:
        if roda_medicao() < 30:
            print("Colisao")
            motores = 0
            move_parar()
        else:
            motores = 1

def prepara_estacionar():
    direita = False
    esquerda = False
    try:
        t1 = threading.Thread(target=controla_distancia,args=())
        t1.start()
        while True:
            if motores == 1:
                esquerda = esquerdo()
                direita = direito()

                if direita == True & esquerda == True:
                    print("FRENTE")
                    move_frente()
                elif direita == False & esquerda == False:
                    move_esquerda(estado_ativo)
                    estacionar()
                    return True
                elif direita == False:
                    print("DIREITA")
                    move_direita(estado_ativo)
                elif esquerda == False:
                    print("ESQUERDA")
                    move_esquerda(estado_ativo)
            else:
                print("Risco de choque")
            
    finally:
        GPIO.cleanup()

def estacionar():
    while True:
        if motores == 1:
            esquerda = esquerdo()
            direita = direito()

            if direita == True & esquerda == True:
                print("FRENTE")
                move_frente()
            elif(direita == False & esquerda == False):
                move_parar()
                return True
            elif direita == False:
                print("DIREITA")
                move_direita(estado_ativo)
            elif esquerda == False:
                print("ESQUERDA")
                move_esquerda(estado_ativo)
        else:
            print("Risco de choque")

#setup_sensor()
#find_line()
