import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ECHO_DIR = 29
TRIG_DIR = 31

ECHO_ESQ = 35
TRIG_ESQ = 37

distancia_cm_esquerda = 0
distancia_cm_direita = 0

def setup_sensor_som():
    GPIO.setup(ECHO_DIR, GPIO.IN)
    GPIO.setup(TRIG_DIR, GPIO.OUT)
    GPIO.setup(ECHO_ESQ, GPIO.IN)
    GPIO.setup(TRIG_ESQ, GPIO.OUT)

def roda_medicao():
    #while True:
    time.sleep(0.5)
    t1 = threading.Thread(target=pulso_esquerdo,args=())
    t1.start()
    t2 = threading.Thread(target=pulso_direito,args=())
    t2.start()
    while t1.isAlive() | t2.isAlive():
        print("Processando")
    return get_distancia()

def pulso_esquerdo():
    global distancia_cm_esquerda
    distancia_cm_esquerda = 0
    GPIO.output(TRIG_ESQ, GPIO.HIGH)
    time.sleep (0.000010)
    GPIO.output(TRIG_ESQ, GPIO.LOW)
        
    while GPIO.input(ECHO_ESQ) == 0:
        pulso_inicial_esquerda = time.time()
        
    while GPIO.input(ECHO_ESQ) == 1:
        pulso_final_esquerda = time.time()
        
    duracao_pulso_esquerda = pulso_final_esquerda - pulso_inicial_esquerda   
    distancia_cm_esquerda =  34300 * (duracao_pulso_esquerda/2)
    distancia_cm_esquerda = round(distancia_cm_esquerda, 0)

def pulso_direito():
    global distancia_cm_direita
    distnacia_cm_direita = 0
    GPIO.output(TRIG_DIR, GPIO.HIGH)
    time.sleep (0.000010)
    GPIO.output(TRIG_DIR, GPIO.LOW)
    while GPIO.input(ECHO_DIR) == 0:
        pulso_inicial_direita = time.time()
    while GPIO.input(ECHO_DIR) == 1:
        pulso_final_direita = time.time()

    duracao_pulso_direita = pulso_final_direita - pulso_inicial_direita
    distancia_cm_direita =  34300 * (duracao_pulso_direita/2)
    distancia_cm_direita = round(distancia_cm_direita, 0)

        
def get_distancia():
    print("Esquerda: "+str(distancia_cm_esquerda))
    print("Direita: "+str(distancia_cm_direita))
    if(distancia_cm_esquerda < distancia_cm_direita):
        return distancia_cm_esquerda
    else:
        return distancia_cm_direita

#setup_sensor()
#roda_medicao()
#get_distancia()
