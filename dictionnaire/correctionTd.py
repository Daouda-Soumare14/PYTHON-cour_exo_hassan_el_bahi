# exo 1
#question 1

stock = {"pomme" : 2, "banane" : 6}
def ajouter(dico, fruit):
    stock = dico.copy()
    if fruit in stock.keys():
        stock[fruit] = stock[fruit] + 1
    else:
        stock[fruit] = 1
    return stock

a = ajouter(stock, "pomme")
print(a)

a = ajouter(stock, "poire")
print(a)

# autre methode
stock = {"pomme" : 2, "banane" : 6}
def ajouter1(dico, fruit):
    stock = dico.copy()
    stock[fruit] = stock.get(fruit, 0) + 1 # permet de verifier si la cles n'existe pas dans le dictionnaire il retourne 0 + 1 et il l'stock dans le dictionnaire stock, sinon si la clee existe il ajoute une valeur de plus et il stock dans de dictionnaire stock
    return stock

b = ajouter1(stock, "pomme")
print(b)

#question 2
def enlever1(dico, fruit):
    stock = dico.copy()
    q = stock.get(fruit) - 1
    if q > 0:
        stock[fruit] = q
    elif q == 0:
        del stock[fruit]
    else:
        print("Erreur : quantité insuffisante de {}".format(fruit))
        
        
c = enlever1(stock, "poire")
print(c)