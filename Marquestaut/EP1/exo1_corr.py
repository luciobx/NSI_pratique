# Votre code
def amplitude(valeurs):
    assert len(valeurs) > 0, "tableau vide"
    mini = valeurs[0]
    maxi = valeurs[0]  ## Ne pas initialiser à 0 !!
    for element in valeurs :          ## Parcours par élément car pas besoin de l'indice
        if element < mini :
            mini = element
        if element > maxi :
            maxi = element
    return maxi - mini

tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]

assert amplitude(tableau) == 11
assert amplitude([])