from math import sqrt

def calcule_distance(donnee1, donnee2):
    d = sqrt((...-...)**2 + (...-...)**2)
    return d
   
def k_plus_proches(donnee, jeu_donnees, k):
    
    tab_distances = []
    for i in range(len(jeu_donnees)):
        tab_distances.append([calcule_distance(donnee, ...), i])
    tab_distances.sort()
    
    voisins = []
    for i in range(...):
        voisins.append(jeu_donnees[tab_distances[i][1]][...])
            
    return voisins