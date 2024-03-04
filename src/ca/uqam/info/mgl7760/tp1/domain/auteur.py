from __future__ import annotations

from ca.uqam.info.mgl7760.tp1.domain.basebiblio import BaseBiblio
from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING: 
    from ca.uqam.info.mgl7760.tp1.domain.livre import Livre

class Auteur(BaseBiblio):

    __tablename__ = "table_auteurs"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(30))
    livres: Mapped[List["Livre"]] = relationship(back_populates="auteurs")


    @classmethod
    def chercher_par_id(cls, an_id : str):
        pass
    
    # returns the first element of the dictionary that has the 
    # name passed as argument
    @classmethod
    def chercher_par_nom(cls,un_nom: str):
        pass
            

    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)

        

