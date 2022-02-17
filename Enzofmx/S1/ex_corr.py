def liste_des_diviseurs(nb):
    tab_diviseur = []
    for i in range(1,nb):
        if nb%i == 0 :
            tab_diviseur.append(i)
    return tab_diviseur


def est_parfait(nb):
    tab_diviseur = liste_des_diviseurs(nb)
    s = 0
    for i in tab_diviseur :
        s = s + i
    return s == nb
