# -*- coding: utf-8 -*-
#Auteur : Alexandre l'Heritier
print("----------------------------------------------------------------------")
print("Configuration initial")
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
import time
import RPi.GPIO as GPIO

mov = 0

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

motor1.start(1)
time.sleep(2)
motor2.start(1)
time.sleep(2)
motor3.start(1)
time.sleep(2)
motor4.start(1)

time.sleep(4)

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

def avance(a):
	print("Arrière")
	global mov
	mov = 1
def recule(a):
	print("Avant")
	global mov
	mov = 3
def droite(a):
	print("Droite !")
	global mov
	mov = 2
def gauche(a):
	print("Gauche !")
	global mov
	mov = 4
def tout(a):
	print("Entier")
	global mov
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
	global mov
	global moteur1
	global moteur2
	global moteur3
	global moteur4
	moteur1 += 1
	moteur2 += 1
	moteur3 += 1
	moteur4 += 1
	print(moteur1)
	if mov == 0:
		motor1.ChangeDutyCycle(pourcent(moteur1+1, "moteur1"))
		motor3.ChangeDutyCycle(pourcent(moteur3+1, "moteur3"))
		motor2.ChangeDutyCycle(pourcent(moteur2+1, "moteur2"))
		motor4.ChangeDutyCycle(pourcent(moteur4+1, "moteur4"))
	if mov == 1:
		motor1.ChangeDutyCycle(pourcent(moteur1+1, "moteur1"))
	if mov == 3:
		motor3.ChangeDutyCycle(pourcent(moteur3+1, "moteur3"))
	if mov == 2:
		motor2.ChangeDutyCycle(pourcent(moteur2+1, "moteur2"))
	if mov == 4:
		motor4.ChangeDutyCycle(pourcent(moteur4+1, "moteur4"))
def bas(a):
	global mov
	global moteur1
	global moteur2
	global moteur3
	global moteur4
	moteur1 -= 1
	moteur2 -= 1
	moteur3 -= 1
	moteur4 -= 1
	print(moteur1)
	if mov == 0:
		motor1.ChangeDutyCycle(pourcent(moteur1-1, "moteur1"))
		motor3.ChangeDutyCycle(pourcent(moteur3-1, "moteur3"))
		motor2.ChangeDutyCycle(pourcent(moteur2-1, "moteur2"))
		motor4.ChangeDutyCycle(pourcent(moteur4-1, "moteur4"))
	if mov == 1:
		motor1.ChangeDutyCycle(pourcent(moteur1-1, "moteur1"))
	if mov == 3:
		motor3.ChangeDutyCycle(pourcent(moteur3-1, "moteur3"))
	if mov == 2:
		motor2.ChangeDutyCycle(pourcent(moteur2-1, "moteur2"))
	if mov == 4:
		motor4.ChangeDutyCycle(pourcent(moteur4-1, "moteur4"))
fenetre = Tk()
fenetre.bind("<Up>", avance)
fenetre.bind("<Down>", recule)
fenetre.bind("<Right>", droite)
fenetre.bind("<Left>", gauche)
fenetre.bind("<t>", tout)
fenetre.bind("<s>", stop)
fenetre.bind("<a>", haut)
fenetre.bind("<q>", bas)
fenetre.mainloop()
print("moteur1 : ", moteur1)
print("moteur2 : ", moteur2)
print("moteur3 : ", moteur3)
print("moteur4 : ", moteur4)
moteur1.stop()
moteur2.stop()
moteur3.stop()
moteur4.stop()
input("Appuyer sur entrer pour quitter.")
