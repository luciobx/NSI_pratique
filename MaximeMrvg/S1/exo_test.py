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


# Question 1

eau = "HOH"
dioxygene = "HH"
methane = "HHCHH"
saccharose = "CCCOOOOHHHHCHHOCHHHOOHHHHCCHCCCCCOOOHHHHOHHHH"
dicEau = {"C":0,"H":2,"O":1,"N":0}
diCoxygene = {"C":1,"H":2,"O":0,"N":2} #On fait exprès une erreur ici

assert dicEau == dicoAtome(eau)
assert diCoxygene == dicoAtome(dioxygene) #Ne passe logiquement pas
assert dicoAtome(saccharose) == {"C":12,"H":22,"O":11,"N":0}


# Question 2

assert factoriser(dicEau) == "H2O"
assert factoriser(dicoAtome(saccharose)) == "C12H22O11"
assert factoriser(diCoxygene) == "H2" #Ne doit pas passer