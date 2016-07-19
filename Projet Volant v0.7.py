# -*- coding: utf-8 -*-
#Auteur : Alexandreou
print("----------------------------------------------------------------------")
print("Projet Volant v0.7")
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
from tkinter import *
import threading
import time
import smbus
import RPi.GPIO as GPIO
import time

global bus
global mov
global moteur1
global moteur2
global moteur3
global moteur4

moteur1 = 0
moteur2 = 0
moteur3 = 0
moteur4 = 0

bus = smbus.SMBus(1)
mov = 0
bus.write_byte_data(0x68, 0x6B, 0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

motor1 = GPIO.PWM(4, 50)
motor2 = GPIO.PWM(17, 50)
motor3 = GPIO.PWM(27, 50)
motor4 = GPIO.PWM(22, 50)

motor1.start(1)
motor2.start(1)
motor3.start(1)
motor4.start(1)

time.sleep(3)

def pourcent(a, b):
	global moteur1
	global moteur2
	global moteur3
	global moteur4
	if a < 0:
		if b == "moteur1":
			moteur1 = 0
		if b == "moteur2":
			moteur2 = 0
		if b == "moteur3":
			moteur3 = 0
		if b == "moteur4":
			moteur4 = 0
		return 1
	if a > 180:
		if b == "moteur1":
			moteur1 = 180
		if b == "moteur2":
			moteur2 = 180
		if b == "moteur3":
			moteur3 = 180
		if b == "moteur4":
			moteur4 = 180
		return 9.5
	return 5 + a * 5 / 200

def a(a):
	global bus
	global mov
	global moteur1
	global moteur2
	global moteur3
	global moteur4
	ajustx = 7
	ajusty = 11
	listex = []
	listey = []
	while True:
		x = bus.read_byte_data(0x68, 0x3B)
		y = bus.read_byte_data(0x68, 0x3D)
		x += ajustx
		y += ajusty
		if x > 127:
			x -= 256
		if y > 127:
			y -= 256
		if len(liste) <= 4:
			listex.append(x)
			listey.append(y)
		else:
			xx = (listex[0]+listex[1]+listex[2]+listex[3])/4
			yy = (listey[0]+listey[1]+listey[2]+listey[3])/4
			listex.append(x)
			listey.append(y)
			del listex[0]
			del listey[0]
			x = xx
			y = yy
		if mov == 0 and x > 10:
			moteur3 += 2
			moteur1 -= 2
			motor1.ChangeDutyCycle(pourcent(moteur1, "moteur1"))
			motor3.ChangeDutyCycle(pourcent(moteur3, "moteur3"))
		if mov == 0 and x < -10:
			moteur3 -= 2
			moteur1 += 2
			motor1.ChangeDutyCycle(pourcent(moteur1, "moteur1"))
			motor3.ChangeDutyCycle(pourcent(moteur3, "moteur3"))
		if mov == 0 and y > 10:
			moteur2 += 2
			moteur4 -= 2
			motor2.ChangeDutyCycle(pourcent(moteur2, "moteur2"))
			motor4.ChangeDutyCycle(pourcent(moteur4, "moteur4"))
		if mov == 0 and y < -10:
			moteur2 -= 2
			moteur4 += 2
			motor2.ChangeDutyCycle(pourcent(moteur2, "moteur2"))
			motor4.ChangeDutyCycle(pourcent(moteur4, "moteur4"))
			time.sleep(0.1)
		

def b(a):
	global bus
	global mov
	global moteur1
	global moteur2
	global moteur3
	global moteur4
	def demarrage(a):
		print("C'est parti !")
		global moteur1
		global moteur2
		global moteur3
		global moteur4
		moteur1 = 50
		moteur2 = 50
		moteur3 = 50
		moteur4 = 50
		motor1.ChangeDutyCycle(pourcent(moteur1, "moteur1"))
		motor2.ChangeDutyCycle(pourcent(moteur2, "moteur2"))
		motor3.ChangeDutyCycle(pourcent(moteur3, "moteur3"))
		motor4.ChangeDutyCycle(pourcent(moteur4, "moteur4"))
	def avance(a):
		print("Avance !")
		global mov
		global moteur1
		mov = 1
		moteur1 -= 10
		motor1.ChangeDutyCycle(pourcent(moteur1, "moteur1"))
		moteur1 += 10
		mov = 0
	def recule(a):
		print("Recule !")
		global mov
		global moteur3
		mov = 3
		moteur3 -= 10
		motor3.ChangeDutyCycle(pourcent(moteur3, "moteur3"))
		moteur3 += 10
		mov = 0
	def droite(a):
		print("Tourne a droite !")
		global mov
		global moteur2
		mov = 2
		moteur2 -= 10
		motor2.ChangeDutyCycle(pourcent(moteur2, "moteur2"))
		moteur2 += 10
		mov = 0
	def gauche(a):
		print("Tourne a gauche !")
		global mov
		global moteur4
		mov = 4
		moteur4 -= 10
		motor4.ChangeDutyCycle(pourcent(moteur4, "moteur4"))
		moteur4 += 10
		mov = 0
	def stop(a):
		print("Stop")
		motor1.ChangeDutyCycle(0)
		motor3.ChangeDutyCycle(0)
		motor2.ChangeDutyCycle(0)
		motor4.ChangeDutyCycle(0)
		time.sleep(3)
		motor1.ChangeDutyCycle(1)
		motor3.ChangeDutyCycle(1)
		motor2.ChangeDutyCycle(1)
		motor4.ChangeDutyCycle(1)
		print("Go !")
		moteur1 = 0
		moteur2 = 0
		moteur3 = 0
		moteur4 = 0
	def haut(a):
		print("Monte !")
		global moteur1
		global moteur2
		global moteur3
		global moteur4
		moteur1 += 2
		moteur2 += 2
		moteur3 += 2
		moteur4 += 2
		motor1.ChangeDutyCycle(pourcent(moteur1, "moteur1"))
		motor2.ChangeDutyCycle(pourcent(moteur2, "moteur2"))
		motor3.ChangeDutyCycle(pourcent(moteur3, "moteur3"))
		motor4.ChangeDutyCycle(pourcent(moteur4, "moteur4"))
	def bas(a):
		print("Decend !")
		global moteur1
		global moteur2
		global moteur3
		global moteur4
		moteur1 -= 2
		moteur2 -= 2
		moteur3 -= 2
		moteur4 -= 2
		motor1.ChangeDutyCycle(pourcent(moteur1, "moteur1"))
		motor2.ChangeDutyCycle(pourcent(moteur2, "moteur2"))
		motor3.ChangeDutyCycle(pourcent(moteur3, "moteur3"))
		motor4.ChangeDutyCycle(pourcent(moteur4, "moteur4"))
	fenetre = Tk()
	fenetre.bind("<Return>", demarrage)
	fenetre.bind("<Up>", avance)
	fenetre.bind("<Down>", recule)
	fenetre.bind("<Right>", droite)
	fenetre.bind("<Left>", gauche)
	fenetre.bind("<a>", haut)
	fenetre.bind("<q>", bas)
	fenetre.bind("<s>", stop)
	fenetre.mainloop()

thread1 = threading.Thread(None, a, None, "a")
thread2 = threading.Thread(None, b, None, "a")

thread1.start()
thread2.start()
 
thread1.join()
thread2.join()

"""
Changelog :
v0.7 :
Algorithme pour l'accéléromètre.

v0.6 :
Ajustement avant test.

v0.5 :
Perfectionnement de la fonction pourcent.

v0.4 :
Commandes des moteurs complétées mais non testées ni ajustées.

v0.3 :
Gestion du gyroscope complétée mais pas testée.
Fonctions de directions complétées mais pas testées.

v0.2 :
Gestion du gyroscope (schématique).

v0.1 :
Interface de direction avec tkinter (schématique).
"""
