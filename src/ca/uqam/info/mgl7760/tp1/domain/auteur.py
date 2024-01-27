from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: 
    from ca.uqam.info.mgl7760.tp1.domain.livre import Livre

class Auteur:

    # liste indexée d'auteurs
    AUTEURS = dict()

    def __init__(self,id : str, nom:str):
        self.id = id
        self.nom = nom
        self.livres = list()
        Auteur.AUTEURS[id] = self


    @classmethod
    def chercher_par_id(cls, an_id : str):
        return cls.AUTEURS[an_id]
    
    # returns the first element of the dictionary that has the 
    # name passed as argument
    @classmethod
    def chercher_par_nom(cls,un_nom: str):
        for auteur in cls.AUTEURS.values():
            if (auteur.nom == un_nom):
                return auteur
            

    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)

        

