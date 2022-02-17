def echange(tab, i1, i2):
   assert i1>=0 and i1<len(tab), "Erreur indice i1"
   assert i2>=0 and i2<len(tab), "Erreur indice i2"
   
   tmp = tab[i1]
   tab[i1] = tab[i2]
   tab[i2] = tmp 


def inverse_tableau(tab):
    i = 0
    while i<len(tab)//2:
        echange(tab, i, len(tab)-1-i)
        i = i + 1


def inverse_chaine(chaine):
    tab = list(chaine)
    inverse_tableau(tab)
    return "".join(tab)