from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from ca.uqam.info.mgl7760.tp1.domain.basebiblio import BaseBiblio


def init_system():
    # create an engine
    engine = create_engine("postgresql://postgres:goldfit@localhost:5432/mgl7760", echo=True)
    from ca.uqam.info.mgl7760.tp1.domain.auteur import Auteur
    from ca.uqam.info.mgl7760.tp1.domain.categorie import Categorie
    from ca.uqam.info.mgl7760.tp1.domain.editeur import Editeur
    from ca.uqam.info.mgl7760.tp1.domain.livre import Livre
   #engine = create_engine("postgresql://<username>:<password>@localhost:5432/<database>", echo=True)
    BaseBiblio.metadata.schema = "biblio"
    BaseBiblio.metadata.create_all(engine)
    print("Just emitted all the SQL")
    return engine

def load_data(engine):
    from ca.uqam.info.mgl7760.tp1.domain.auteur import Auteur
    with Session(engine) as load_session:
        auteur1 = Auteur(nom="David Thomas")
        auteur2 = Auteur(nom="Andrew Hunt")
        load_session.add(auteur1)
        load_session.add(auteur2)
        load_session.commit()

