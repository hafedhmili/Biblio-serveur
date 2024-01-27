from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: 
    from ca.uqam.info.mgl7760.tp1.domain.livre import Livre
    
class Editeur:

    # liste indexée d'auteurs
    EDITEURS = dict()

    def __init__(self,id : str, nom:str):
        self.id = id
        self.nom = nom
        self.livres = list()
        Editeur.EDITEURS[id] = self


    def ajouter_livre(self,livre: Livre):
        self.livres.append(livre)

        
    @classmethod
    def chercher_par_id(cls, an_id : str):
        return cls.EDITEURS[an_id]
    
    # returns the first element of the dictionary that has the 
    # name passed as argument
    @classmethod
    def chercher_par_nom(cls,un_nom: str):
        for editeur in cls.EDITEURS.values():
            if (editeur.nom == un_nom):
                return editeur

        

