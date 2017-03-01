# -*- coding: utf-8 -*-
#Auteur : Alexandreou
print("----------------------------------------------------------------------")
print("Reconfiguration v1.0")
print("----------------------------------------------------------------------")
print("")
#----------------------------------------------------
#         1 O x- ||          |                      |
#           |    \/          |                      |
#           |                |                      |
#         /+  \              |        Avance        |
#4       /     \             |          ||          |
#O--------      ---------O 2 |          ||          |
# y- ||  \     /       y+ || | Gauche ------ Droite |
#    \/   \   /           \/ |          ||          |
#           |                |          ||          |
#           |                |          \/          |
#           O x+ ||          |        Recule        |
#           3    \/          |                      |
#----------------------------------------------------
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

moteur1 = 0
moteur2 = 0
moteur3 = 0
moteur4 = 0

motor1 = GPIO.PWM(4, 50)
motor2 = GPIO.PWM(17, 50)
motor3 = GPIO.PWM(27, 50)
motor4 = GPIO.PWM(22, 50)
print("Veuillez patienter")
motor1.start(0)
time.sleep(2)
motor2.start(0)
time.sleep(2)
motor3.start(0)
time.sleep(2)
motor4.start(0)
time.sleep(2)

print("Préparation")
input("Brancher le moteur et appuyer sur entrer pour continuer")
motor1.start(0)
time.sleep(2)
motor2.start(0)
time.sleep(2)
motor3.start(0)
time.sleep(2)
motor4.start(0)
time.sleep(2)

print("Début")
motor1.start(7.5)
time.sleep(2)
motor2.start(7.5)
time.sleep(2)
motor3.start(7.5)
time.sleep(2)
motor4.start(7.5)
time.sleep(2)
motor1.start(1)
time.sleep(2)
motor2.start(1)
time.sleep(2)
motor3.start(1)
time.sleep(2)
motor4.start(1)
time.sleep(2)
motor1.start(0)
time.sleep(2)
motor2.start(0)
time.sleep(2)
motor3.start(0)
time.sleep(2)
motor4.start(0)
time.sleep(2)
motor1.start(1)
time.sleep(2)
motor2.start(1)
time.sleep(2)
motor3.start(1)
time.sleep(2)
motor4.start(1)
time.sleep(2)
motor1.start(0)
time.sleep(2)
motor2.start(0)
time.sleep(2)
motor3.start(0)
time.sleep(2)
motor4.start(0)
print("Fin")
