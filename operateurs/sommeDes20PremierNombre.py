s = 0
for i in range(1, 21):
    s += i
print(" la somme des 20 premier entier positif {} ".format(s))

# autre facon de faire
n = int(input("saisir un nombre "))
somme = 0
for i in range(1, n+1):
    somme += i
print(" la somme des entier positif {} ".format(somme))