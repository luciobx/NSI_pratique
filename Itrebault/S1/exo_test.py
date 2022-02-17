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


donnees_animaux = [['chat', 23, 3.5], 
                   ['elephant', 660, 5225],
                   ['chat', 28, 4.2], 
                   ['singe', 60, 22],
                   ['elephant', 550, 4100],
                   ['poisson rouge', 10, 0.1]
                   ]

assert round(calcule_distance(['chat', 23, 3.5], ['elephant', 660, 5225])) == 5260 
assert k_plus_proches(['mystère', 25, 4], donnees_animaux, 3) == ['chat', 'chat', 'poisson rouge']
assert k_plus_proches(['mystère', 500, 3800], donnees_animaux, 2) == ['elephant', 'elephant']
