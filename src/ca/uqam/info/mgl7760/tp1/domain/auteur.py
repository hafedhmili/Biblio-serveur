class Auteur:

    # liste indexée d'auteurs
    AUTEURS = dict()

    def __init__(self,id : str, nom:str):
        self.id = id
        self.nom = nom
        Auteur.AUTEURS[id] = self


    @classmethod
    def chercher_par_id(cls, an_id : str) -> Auteur:
        return cls.AUTEURS[an_id]
    
    # returns the first element of the dictionary that has the 
    # name passed as argument
    @classmethod
    def chercher_par_nom(cls,un_nom: str) -> Auteur:
        for auteur in cls.AUTEURS.values():
            if (auteur.nom == un_nom):
                return auteur

        

