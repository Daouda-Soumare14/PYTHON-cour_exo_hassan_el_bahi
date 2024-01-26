matrice = []
for i in range(5):
    liste = []
    for j in range(8):
        liste.append(i)
    matrice.append(liste)
print(matrice) # permet d'acceder a tous les elements de la liste
print()

print(matrice[:]) # permet d'acceder a tous les elements de la liste
print()
print(matrice[1]) # permet d'acceder a la ligne d'indice 1 de la liste
print()
print(matrice[-1]) # permet d'acceder a la dernière ligne de la liste
print()
print(matrice[2][0]) # permet d'acceder a la premiere colonne de la liste d'indice 2
print()
print(matrice[1][-2]) # permet d'acceder a la liste d'indice 1 a l'avant dernier colonne
print()
print(matrice[1][0::2]) # permet d'acceder a la liste d'indice 1 de 0 jusqu'a la fin avec un pat de 2
print()
print(matrice[2][::-1]) # permet d'acceder a la liste d'indice 2 du premier au dernier element de la liste a l'ordre inverse

