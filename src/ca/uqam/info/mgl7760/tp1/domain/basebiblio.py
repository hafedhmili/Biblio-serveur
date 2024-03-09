from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Table, Column, ForeignKey
class BaseBiblio(DeclarativeBase):
    pass

table_auteur_livre = Table(
    "auteur_livre",
    BaseBiblio.metadata,
    Column("auteur_id", String(30), ForeignKey("table_auteurs.nom")),
    Column("livre_id", Integer, ForeignKey("table_livres.id")),
)

table_categorie_livre = Table(
    "categorie_livre",
    BaseBiblio.metadata,
    Column("categorie_id",String(30), ForeignKey("table_categories.nom")),
    Column("livre_id", Integer, ForeignKey("table_livres.id")),
)
