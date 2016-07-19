# -*- coding: utf-8 -*-
#Auteur : Alexandreou
print("----------------------------------------------------------------------")
print("Projet Volant v0.2")
print("----------------------------------------------------------------------")
print("")
from tkinter import *
import threading
import time

def a(a):
	ab = 0
	while True:
		print(ab, "reglage gyro")
		time.sleep(0)
		ab += 1

def b(a):
	def demarrage(a):
		print("C'est parti !")
	def avance(a):
		print("Avance !")
	def recule(a):
		print("Recule !")
	def droite(a):
		print("Tourne a droite !")
	def gauche(a):
		print("Tourne a gauche !")
	def haut(a):
		print("Monte !")
	def bas(a):
		print("Decend !")
	fenetre = Tk()
	fenetre.bind("<Return>", demarrage)
	fenetre.bind("<Up>", avance)
	fenetre.bind("<Down>", recule)
	fenetre.bind("<Right>", droite)
	fenetre.bind("<Left>", gauche)
	fenetre.bind("<a>", haut)
	fenetre.bind("<q>", bas)
	fenetre.mainloop()

thread1 = threading.Thread(None, a, None, "a")
thread2 = threading.Thread(None, b, None, "a")

thread1.start()
thread2.start()
 
thread1.join()
thread2.join()

"""
Changelog :
v0.2 :
Gestion du gyroscope (schématique)

v0.1 :
Interface de direction avec tkinter (schématique)
"""