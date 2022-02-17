class Noeud:
    def __init__(self,mot,gauche = None,droite = None):
        self.gauche = gauche
        self.droite = droite
        self.mot = mot

def inserer(ABR,mot):
    '''Insère un élément dans l'arbre binaire de recherche.'''
    if ABR is None :
        ABR = ...
    elif mot < ABR.mot :
        ABR.gauche = ...
    elif  mot > ABR.mot :
        ABR.droite = ...
    return ABR



def afficher(ABR):
    '''Affiche les mots par ordre alphabétique.'''
    if ABR ... :
        afficher(...)
        print(...)
        afficher(...)

arbre = None
arbre = inserer(arbre,"kiwi")
arbre = inserer(arbre,"pomme")
arbre = inserer(arbre,"abricot")
arbre = inserer(arbre,"mangue")
arbre = inserer(arbre,"poire")
afficher(arbre)
