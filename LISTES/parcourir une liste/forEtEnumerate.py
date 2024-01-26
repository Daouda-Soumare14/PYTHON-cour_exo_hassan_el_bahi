# la fonction enumerate permet de parcourir une liste en accedant a la foi a l'index
# et a la valeur de chaque element
 # exemple 1
l = [11, 2, 4, 2, 13, 20, 17, 19]
for notes in l: # cette ligne veut dire pour chaque element de la liste stock dans la variable nom
    print(notes)
    
# exemple 3
n = [11, 2, 4, 2, 13, 20, 17, 19]
# la variable i permet de faire l'indiçage et notes permet de stocker les valeurs de la liste
for i, notes in enumerate(n): # enumerate permet aussi de parcourir les elements d'une liste
    print(" la note de l'etudiant", i+1, " = ", notes)
    
# exemple 3
n = [11, 2, 4, 2, 13, 20, 17, 19]
# la variable i permet de faire l'indiçage et notes permet de stocker les valeurs de la liste
for i, notes in enumerate(n, start=1): #  start permet de commencer le parcour a 1 il est par defaut a 0
    print(" la note de l'etudiant", i, " = ", notes)    
       