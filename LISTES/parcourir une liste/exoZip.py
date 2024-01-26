# soit les trois listes suivantes:
prenoms = ["daouda", "rachid", "samba", "mamadou"]
noms = ["soumare", "eljay", "camara", "sylla"]
notes = [13, 20, 17, 19]
for prenom, nom, note in zip(prenoms, noms, notes):
    print(" la note de ", prenom, nom, " = ", note)