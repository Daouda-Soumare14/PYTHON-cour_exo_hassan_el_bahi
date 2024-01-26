# premiere methode de creation d'une liste
# la methode la plus simple et la plus utiliser
liste = ["pomme", 3, 5, 4, 6, 7 + 6, True]
print(liste)

# deuxieme methode de creation d'une liste
# on utilise la fonction list()
l = list(("pomme", 3, 5, 4, 6, 7 + 6, True))
print(l)
lis = list(('daouda')) # cette methode permet aussi de creer une liste avec une seule valeur et qui sera afficher caractère par caractère
print(lis)

# la troisième methode de creation d'une liste
# liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = list(range(1, 11)) # permet d'afficher les valeurs de 1 a 10
print(list)