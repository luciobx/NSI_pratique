class Noeud:

    def __init__(self, valeur=None, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite

    def estFeuille(self):
        return self.gauche is None and  self.droite is None

# partie à modifier
            
def poids_maxi_branche(arbre):
    if arbre.estFeuille():
        return arbre.valeur
    else:
        return arbre.valeur + max(poids_maxi_branche(arbre.gauche),poids_maxi_branche(arbre.droite))

# déclaration de l'arbre
trente = Noeud(30)
quarante = Noeud(40)
dixsept = Noeud(17)
huit = Noeud(8)
sept = Noeud(7,trente,quarante)
vingtetun = Noeud(21,dixsept,huit)
douze = Noeud(12,sept,vingtetun)

# test 
assert poids_maxi_branche(douze) == 70
assert poids_maxi_branche(trente) == 30
assert poids_maxi_branche(sept) == 58
assert poids_maxi_branche(vingtetun) == 47
