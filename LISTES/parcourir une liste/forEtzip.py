#cette fonction permet de parcourir plusieurs listes en paralelle ou en meme temps
infos = ["daouda", "rachid", "samba", "mamadou"]
notes = [11, 13, 20, 17]
for info, note in zip(infos, notes):
    print(" la note de ", info,  " = ", note)