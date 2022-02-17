class Temps:
    """Initialise Temps (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, h, m, s):
        self.heures = h
        self.minutes = m
        self.secondes = s

    def ajouter_minutes(self, mins):
        """incrémente les minutes de la valeur mins passée en paramètre"""
        self.minutes = self.minutes + mins
        while ... :
            self.heures += 1
            self.minutes = self.minutes - 60


    def ajouter_secondes(self, secs):
        """incrémente les secondes de la valeur secondes passée en paramètre"""
        self.secondes = self.secondes + secs
        while ... :
            ...
            self.secondes = self.secondes - 60


    def __str__(self):
        """renvoie une chaine de caractères sous la forme hh : mm : ss"""
        return ...+" : "+...+" : "+...

    def en_secondes(self):
        """Convertie un temps en heures/minutes/secondes en secondes"""
        return ...

    def est_plus_petit (self, tps) :
        """Compare deux temps entre eux. Renvoie True si l'objet est plus petit que l'objet tps passé en paramètre"""
        return ...




#Test du code
...
...
t1.ajouterSecondes(20)

assert str(t1)== "2 : 0 : 5"
assert t1.est_plus_petit(t2) == True