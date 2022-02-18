def compte_points(p):
    if len(p) < 3:
        return 0
    else:
        couleur_papier1=p.pop(-1)
        couleur_papier2=p.pop(-1)
        couleur_papier3=p.pop(-1)
        if couleur_papier1 == couleur_papier2 and couleur_papier1 == couleur_papier3:
            if couleur_papier1 =='R':
                return -1 + compte_points(p)
            if couleur_papier1 == 'O':
                return 1 + compte_points(p)
            if couleur_papier1 == 'V':
                return 2 + compte_points(p)
        else:
            p.append(couleur_papier3)
            p.append(couleur_papier2)
            return compte_points(p)
            
            
assert compte_points(['V','V','R','R','R','O','V','V','V','O','O','O','V','V','V','R','R','R','R','R','O','V','V']) == 3
assert compte_points(['O','O','O','V','V','V','R','R','R']) == 2
assert compte_points(['V','V','O','O','R','R']) == 0
assert compte_points(['V','V','V','R','V','R','V','V','V']) == 4
assert compte_points([]) == 0
assert compte_points(['V','V']) == 0
assert compte_points(['V','R','R','R','V','R','R','R']) == -2
