class Noeud:
    def __init__(self,mot,gauche=None,droite=None):
        self.gauche = gauche
        self.droite = droite
        self.mot = mot

def inserer(ABR,mot):
    '''Insère un élément dans l'arbre binaire de recherche.'''
    if ABR is None :
        ABR = Noeud(mot)
    elif mot < ABR.mot :
        ABR.gauche = inserer(ABR.gauche,mot)
    elif  mot > ABR.mot :
        ABR.droite = inserer(ABR.droite,mot)
    return ABR

def afficher(ABR):
    '''Affiche les mots par ordre alphabétique.'''
    if ABR is not None :
        afficher(ABR.gauche)
        print(ABR.mot)
        afficher(ABR.droite)

arbre = None
arbre = inserer(arbre,"kiwi")
arbre = inserer(arbre,"pomme")
arbre = inserer(arbre,"abricot")
arbre = inserer(arbre,"mangue")
arbre = inserer(arbre,"poire")
afficher(arbre)
