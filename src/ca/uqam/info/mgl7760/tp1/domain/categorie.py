from livre import Livre
class Categorie:

    # liste indexée d'auteurs
    CATEGORIES = dict()

    def __init__(self,id : str, code: str, nom:str):
        self.id = id
        self.code = code
        self.nom = nom
        self.livres = list()
        Categorie.CATEGORIES[id] = self


    @classmethod
    def chercher_par_id(cls, an_id : str):
        return cls.CATEGORIES[an_id]
    
    # returns the first element of the dictionary that has the 
    # name passed as argument
    @classmethod
    def chercher_par_code(cls,un_code: str):
        for cat in cls.CATEGORIES.values():
            if (cat.code == un_code):
                return cat
            
    
    @classmethod
    def chercher_tous(cls):
        return cls.CATEGORIES.values()


    def ajouter_livre(self,livre: Livre):
        self.livres.append(livre) 

