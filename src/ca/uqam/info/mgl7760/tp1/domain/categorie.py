from __future__ import annotations
from typing import TYPE_CHECKING
from typing import List
from ca.uqam.info.mgl7760.tp1.domain.basebiblio import BaseBiblio, table_categorie_livre

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

if TYPE_CHECKING: 
    from ca.uqam.info.mgl7760.tp1.domain.livre import Livre
    
class Categorie(BaseBiblio):

    __tablename__="table_categories"
    __table_args__ = {"schema": "biblio"}

    nom: Mapped[str] = mapped_column(String(30),primary_key=True)
    livres: Mapped[List["Livre"]] = relationship(back_populates="categories",secondary=table_categorie_livre)


    @classmethod
    def chercher_par_id(cls, an_id : str):
        # write based on SQLAlchemy
        pass            
    
    @classmethod
    def chercher_tous(cls):
        # write based on SQLAlchemy
        pass


    def ajouter_livre(self,livre: Livre):
        self.livres.append(livre) 

