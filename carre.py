#!/usr/bin/env python3

from dessin_tortue import *

up()     		# relever le crayon
goto(-150,50)	# reculer en haut a gauche

i=0
while i<9:
	down()
	carre(25,'red')
	up()
	forward(30)
	i=i+1
a=input()		# pour attendre
