from exo_corr import *

# --- Exercice 1 ---
valeurs = [1, 2, 3]
attendu = [3, 2, 1]
echange(valeurs, 0, 2)
assert valeurs == attendu, f"Erreur avec {valeurs}"

valeurs = [1, 2, 3]
attendu = [1, 2, 3]
echange(valeurs, 1, 1)
assert valeurs == attendu, f"Erreur avec {valeurs}"

# --- Exercice 2 ---
# Tableau vide
valeurs = []
attendu = []
inverse_tableau(valeurs)
assert valeurs == attendu, f"Erreur avec {valeurs}"

# Tableau de taille 1
valeurs = ['a']
attendu = ['a']
inverse_tableau(valeurs)
assert valeurs == attendu, f"Erreur avec {valeurs}"

# Tableau de taille paire
valeurs = ['n','e','i','b']
attendu = ['b','i','e','n']
inverse_tableau(valeurs)
assert valeurs == attendu, f"Erreur avec {valeurs}"

# Tableau de taille impaire
valeurs  = ['t','u','l','a','s']
attendu  = ['s','a','l','u','t']
inverse_tableau(valeurs)
assert valeurs == attendu, f"Erreur avec {valeurs}"

# Fonction inverse_chaine
valeur   = "?idim ec enitnac al à elbmesne enuejéd nO !tulaS"
attendu  = "Salut! On déjeune ensemble à la cantine ce midi?"
resultat = inverse_chaine(valeur)
assert resultat == attendu, f"Erreur avec {valeur}"