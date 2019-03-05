# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import getch
#from distancia import *

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

F_DIREITA = 16
F_ESQUERDA = 11
T_DIREITA = 18
T_ESQUERDA = 13
SENSOR_DIR = 40
SENSOR_ESQ = 38

def setup_motor():
    GPIO.setup(F_DIREITA, GPIO.OUT)
    GPIO.setup(F_ESQUERDA, GPIO.OUT)
    GPIO.setup(T_DIREITA, GPIO.OUT)
    GPIO.setup(T_ESQUERDA, GPIO.OUT)
    GPIO.output(F_DIREITA, GPIO.LOW)
    GPIO.output(F_ESQUERDA, GPIO.LOW)
    GPIO.output(T_DIREITA, GPIO.LOW)
    GPIO.output(T_ESQUERDA, GPIO.LOW)

def move_frente():
    GPIO.output(F_DIREITA, GPIO.HIGH)
    GPIO.output(F_ESQUERDA, GPIO.HIGH)
    GPIO.output(T_DIREITA, GPIO.LOW)
    GPIO.output(T_ESQUERDA, GPIO.LOW)
    '''time.sleep(0.4)
    GPIO.output(F_DIREITA, GPIO.LOW)
    GPIO.output(F_ESQUERDA, GPIO.LOW)'''

def move_tras():
    GPIO.output(T_DIREITA, GPIO.HIGH)
    GPIO.output(T_ESQUERDA, GPIO.HIGH)
    '''time.sleep(0.4)
    GPIO.output(T_DIREITA, GPIO.LOW)
    GPIO.output(T_ESQUERDA, GPIO.LOW)'''

def move_direita(estado):
    GPIO.output(F_ESQUERDA, GPIO.HIGH)
    GPIO.output(F_DIREITA, GPIO.LOW)
    while(GPIO.input(SENSOR_DIR) != estado):
          print("virando")
    GPIO.output(F_ESQUERDA, GPIO.LOW)
    move_frente()
    time.sleep(0.1)

def move_esquerda(estado):
    GPIO.output(F_DIREITA, GPIO.HIGH)
    GPIO.output(F_ESQUERDA, GPIO.LOW)
    while(GPIO.input(SENSOR_ESQ) != estado):
          print("virando")
    GPIO.output(F_DIREITA, GPIO.LOW)
    move_frente()
    time.sleep(0.1)

def move_parar():
    GPIO.output(T_DIREITA, GPIO.LOW)
    GPIO.output(T_ESQUERDA, GPIO.LOW)
    GPIO.output(F_DIREITA, GPIO.LOW)
    GPIO.output(F_ESQUERDA, GPIO.LOW)


'''def le_tecla():
    setup_sensor_som()
    while True:
        roda_medicao()
        if get_distancia() < 15:
            print("Colisao")
            move_parar()
        tecla_comando = getch.getch()
        if tecla_comando == 'w':
            move_frente()
        if tecla_comando == 'd':
            move_direita()
        if tecla_comando == 'a':
            move_esquerda()
       	if tecla_comando == 's':
            move_tras()
        if tecla_comando == 'q':
            move_parar()'''
 
#setup_motor()
#le_tecla()
