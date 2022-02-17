def dicoAtome(molecule):
    dico = {"C":0,"H":0,"O":0,"N":0}
    for l in molecule :
        dico[l] += 1
    return dico

def factoriser(dicoMolecule):
    molecule = ""
    for cle, valeur in dicoMolecule.items():
        if valeur == 1 :
            molecule += cle
        elif valeur > 1:
            molecule += cle + str(valeur)
    return molecule