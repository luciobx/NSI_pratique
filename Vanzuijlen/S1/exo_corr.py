class Noeud:

    def __init__(self, valeur=None, gauche = None, droite = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
 
    def estFeuille(self):
        if not self.gauche and not self.droite:
            return True
        else:
            return False

# partie à modifier
            
def somme_maxi(arbre):
    if arbre.estFeuille():
        return arbre.valeur
    elif arbre.gauche == None:
        return arbre.valeur + somme_maxi(arbre.droite)
    elif arbre.droite == None:
        return arbre.valeur + somme_maxi(arbre.gauche)
    else:
        return arbre.valeur + max(somme_maxi(arbre.gauche),somme_maxi(arbre.droite))

    
onze = Noeud(11)
neuf = Noeud(9)
trente = Noeud(30)
quarante = Noeud(40,onze,None)
dixsept = Noeud(17,None,neuf)
huit = Noeud(8)
sept = Noeud(7,trente,quarante)
vingtetun = Noeud(21,dixsept,huit)
douze = Noeud(12,sept,vingtetun)

# test 
assert somme_maxi(douze) == 70
assert somme_maxi(trente) == 30
assert somme_maxi(sept) == 58
assert somme_maxi(vingtetun) == 47
