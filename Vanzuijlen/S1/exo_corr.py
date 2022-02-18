class Noeud:

    def __init__(self, valeur=None, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
 
    def estFeuille(self):
        return self.gauche is None and  self.droite is None

# partie à modifier

def poids_maxi_branche(arbre):
    if arbre == None:
        return 0
    else :
        return arbre.valeur + max(poids_maxi_branche(arbre.gauche),poids_maxi_branche(arbre.droite))


def poids_maxi_branche2(arbre):
    if arbre.estFeuille():
        return arbre.valeur
    elif arbre.gauche == None:
        return arbre.valeur + poids_maxi_branche(arbre.droite)
    elif arbre.droite == None:
        return arbre.valeur + poids_maxi_branche(arbre.gauche)
    else:
        return arbre.valeur + max(poids_maxi_branche(arbre.gauche),poids_maxi_branche(arbre.droite))

# déclaration de l'arbre
onze = Noeud(11)
neuf = Noeud(9)
trente = Noeud(30)
quarante = Noeud(40,onze,None)
dixsept = Noeud(17,None,neuf)
huit = Noeud(8)
sept = Noeud(7,trente,quarante)
vingtetun = Noeud(21,dixsept,huit)
douze = Noeud(12,sept,vingtetun)

# test première fonction
assert poids_maxi_branche(douze) == 70
assert poids_maxi_branche(trente) == 30
assert poids_maxi_branche(sept) == 58
assert poids_maxi_branche(vingtetun) == 47

# test seconde fonction
assert poids_maxi_branche2(douze) == 70
assert poids_maxi_branche2(trente) == 30
assert poids_maxi_branche2(sept) == 58
assert poids_maxi_branche2(vingtetun) == 47
