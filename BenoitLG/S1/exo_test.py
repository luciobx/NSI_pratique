def decompose(nombre):
    tableau_chiffres = [0] * 10
    while nombre != 0:
        unite = nombre % 10
        tableau_chiffres[unite] = tableau_chiffres[unite] + 1
        nombre = nombre // 10
    return tableau_chiffres


def somme_chiffres(tableau_chiffres):
    resultat = 0
    for i in range(10):
        resultat = resultat + tableau_chiffres[i] * i
    return resultat

#Exercice 1
assert decompose(0) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert decompose(1234567890) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert decompose(111223) == [0, 3, 2, 1, 0, 0, 0, 0, 0, 0]

#Exercice 2
assert somme_chiffres([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert somme_chiffres([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
assert somme_chiffres(decompose(111223)) == 10
