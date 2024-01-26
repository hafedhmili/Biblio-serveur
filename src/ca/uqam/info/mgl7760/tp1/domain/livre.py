from auteur import Auteur
from editeur import Editeur
from categorie import Categorie

class Livre:

    LIVRES_PAR_ID = dict()
    LIVRES_PAR_ISBN = dict()
    LIVRES_PAR_TITRE = dict()

    def __init__(self, id: str, titre: str, description:str, isbn: str, annee: int, nom_editeur: str):
        # id
        self.id = id
        Livre.LIVRES_PAR_ID[id] = self

        # titre
        self.titre = titre
        Livre.LIVRES_PAR_TITRE[titre] = self

        self.description = description

        # isbn
        self.isbn = isbn
        Livre.LIVRES_PAR_ISBN[isbn] = self
        self.annee = annee

        # editeur
        self.editeur = Editeur.chercher_par_nom(nom_editeur)
        self.editeur.ajouter_livre(self)

        self.auteurs = list()
        self.categories = list()

    def ajoute_auteur(self, nom_auteur: str):
        auteur = Auteur.chercher_par_nom(nom_auteur)
        self.auteurs.append(auteur)
        auteur.ajouter_livre(self)

    def ajouter_categorie(self, code_categorie: str):
        categorie =  Categorie.chercher_par_code(code_categorie)
        self.categories.append(categorie)
        categorie.ajouter_livre(self)


    def set_image_couverture(self,nom_fichier_image:str):
        self.fichier_image = nom_fichier_image


    @classmethod
    def charger_par_id(cls,id: str):
        return cls.LIVRES_PAR_ID[id]
    

    @classmethod
    def chercher_par_isbn(cls, isbn: str):
        return cls.LIVRES_PAR_ISBN[isbn]

    @classmethod
    def chercher_par_titre(cls,titre: str):
        return cls.LIVRES_PAR_TITRE[titre]
    
    @classmethod
    def chercher_par_auteur(cls,nom_auteur: str):
        return Auteur.chercher_par_nom(nom_auteur).livres
    
    @classmethod
    def chercher_par_editeur(cls, nom_editeur: str):
        return Editeur.chercher_par_nom(nom_editeur).livres
    
    @classmethod
    def chercher_par_categorie(cls, code_categorie: str):
        return Categorie.chercher_par_code(code_categorie).livres
    

    @classmethod
    def chercher_tous(cls):
        return cls.LIVRES_PAR_ID.values()