from math import sqrt

def calcule_distance(donnee1, donnee2):
    d = sqrt((donnee1[1]-donnee2[1])**2 + (donnee1[2]-donnee2[2])**2)
    return d
   
def k_plus_proches(donnee, jeu_donnees, k):
    
    tab_distances = []
    for i in range(len(jeu_donnees)):
        tab_distances.append([calcule_distance(donnee, jeu_donnees[i]), i])
    tab_distances.sort()
    
    voisins = []
    for i in range(k):
        voisins.append(jeu_donnees[tab_distances[i][1]][0])
            
    return voisins
