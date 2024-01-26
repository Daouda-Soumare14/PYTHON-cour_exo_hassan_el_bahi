# en utilisant les modules standards de python, ecrire les programmes suivants:
# - un programme qui calcuke le factoriel d'un module
# - un programme qui affiche un nombre impair aleatoire entre 1 et 101
# - un programme qui determine le mode et l'ecart type d'une serie statistique
# - un programme qui affiche la date d'aujourd'hui
# - un programme qui ouvre le site google.com
# - un programme qui convertit les bitcoins en euro

#question1
import math
print(math.factorial(12))

#question2
import random
print(random.randrange(1, 102, 2))

#question3
import statistics
mode = statistics.mode([1, 2, 3, 4, 4]) # mode veut dire la valeur la plus representé dans la serie
ecart_type = statistics.stdev([1, 2, 3, 4, 4]) # stdev = ecart-type
print(" le mode = {}".format(mode))
print(" l'ecart-type = {}".format(ecart_type))

#question4
from datetime import date
date = date.today()
print(" la date d'aujourd'hui : {}".format(date))

#question5
import webbrowser
webbrowser.open('http://google.com')

#question6




