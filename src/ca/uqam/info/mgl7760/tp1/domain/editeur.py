from __future__ import annotations
from typing import TYPE_CHECKING
from typing import List
from ca.uqam.info.mgl7760.tp1.domain.basebiblio import BaseBiblio

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

if TYPE_CHECKING: 
    from ca.uqam.info.mgl7760.tp1.domain.livre import Livre
    
class Editeur(BaseBiblio):

    __tablename__="table_editeurs"
    __table_args__ = {"schema": "biblio"}
    nom: Mapped[str] = mapped_column(String(30),primary_key=True)
    livres: Mapped[List["Livre"]] = relationship(back_populates="editeur")


    def ajouter_livre(self,livre: Livre):
        self.livres.append(livre)

        
    @classmethod
    def chercher_par_id(cls, an_id : str):
        # write based on SQLAlchemy
        pass
    
    @classmethod
    def chercher_par_nom(cls,un_nom: str):
        # write based on SQLAlchemy
        pass

        

