def racine_numerique(nombre):
    while nombre > 9:
        total = 0
        for c in str(nombre):
            total += int(c)
        nombre = total
    return nombre


assert racine_numerique(19) == 1  # La racine numérique de 19 est 1
assert racine_numerique(123) == 6  # La racine numérique de 123 est 6
assert racine_numerique(123456789) == 9  # La racine numérique de 123456789 est 9
