# ecrire un programme qui calcule da somme d'un maximum de
# 8 nombres entres par l'utilisateur, si un nombre negatif
# est entre, la boucle ignore ce nombre

somme = 0
for i in range(1, 9):
    print(" saisir la valeur N ", i, " : ", end="")
    n = int(input())
    if(n < 0):
        continue
    somme += n
print(" la somme des nombre positif = {}".format(somme))

# autre façon de faire avec une fonction
def nombrePositif():
    s = 0
    for i in range(1, 9):
        print(" saisir la valeur M ", i, " : ", end="")
        m = int(input())
        if(m < 0):
            continue
        s += m
    print(" la somme des nombre positif = {}".format(s))

nombrePositif()    