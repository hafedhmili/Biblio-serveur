from ca.uqam.info.mgl7760.tp1.domain.auteur import Auteur
from ca.uqam.info.mgl7760.tp1.domain.editeur import Editeur
from ca.uqam.info.mgl7760.tp1.domain.categorie import Categorie

from typing import List
from ca.uqam.info.mgl7760.tp1.domain.basebiblio import BaseBiblio, table_auteur_livre, table_categorie_livre

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Livre(BaseBiblio):

    __tablename__ = "table_livres"
    __table_args__ = {"schema": "biblio"}
    id: Mapped[int] = mapped_column(primary_key=True)
    titre: Mapped[str] = mapped_column(String(80),nullable=False)
    description: Mapped[str] = mapped_column(String(80))
    isbn: Mapped[str] = mapped_column(String(18),nullable=False, unique=True)
    annee: Mapped[int] = mapped_column(nullable=False)

    auteurs: Mapped[List["Auteur"]] = relationship(back_populates="livres",secondary=table_auteur_livre)

    categories: Mapped[List["Categorie"]] = relationship(back_populates="livres", secondary=table_categorie_livre)

    editeur_id: Mapped[str] = mapped_column(String(30),ForeignKey("table_editeurs.nom"))
                                                
    editeur: Mapped["Editeur"] = relationship(back_populates="livres")

    
    def ajoute_auteur(self, auteur: Auteur):
        self.auteurs.append(auteur)
       
    def ajouter_categorie(self, categorie: Categorie):
        self.categories.append(categorie)

    def set_image_couverture(self,nom_fichier_image:str):
        self.fichier_image = nom_fichier_image


    @classmethod
    def chercher_par_id(cls,id: int):
        # define later with SQLAlchemy functionality
        pass
    

    @classmethod
    def chercher_par_isbn(cls, isbn: str):
        # define later with SQLAlchemy functionality
        pass

    @classmethod
    def chercher_par_titre(cls,titre: str):
        # define later with SQLAlchemy functionality
        pass
    
    @classmethod
    def chercher_par_auteur(cls,nom_auteur: str):
        # define later with SQLAlchemy functionality
        pass
    
    @classmethod
    def chercher_par_editeur(cls, nom_editeur: str):
        # define later with SQLAlchemy functionality
        pass
    
    @classmethod
    def chercher_par_categorie(cls, code_categorie: str):
        # define later with SQLAlchemy functionality
        pass
    

    @classmethod
    def chercher_tous(cls):
        # define later with SQLAlchemy functionality
        pass
