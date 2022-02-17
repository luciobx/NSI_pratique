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

