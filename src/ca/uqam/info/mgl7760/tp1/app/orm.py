from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import csv
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

def load_data(engine, csvfile_path):
    from ca.uqam.info.mgl7760.tp1.domain.auteur import Auteur
    from ca.uqam.info.mgl7760.tp1.domain.livre import Livre
    from ca.uqam.info.mgl7760.tp1.domain.categorie import Categorie
    from ca.uqam.info.mgl7760.tp1.domain.editeur import Editeur

    with Session(engine) as load_session:
        # open csv file
        with open(csvfile_path,newline='') as biblio_data_file:
            biblio_data_reader = csv.reader(biblio_data_file, delimiter='\t')
            # skip first row, which consists of headers
            biblio_data_reader.__next__()
            # iterate over data rows
            for row in biblio_data_reader:
                # creer livre
                livre = Livre(titre=row[0],description=row[1],isbn=row[2],annee=row[3])
                load_session.add(livre)

                # get relatiosnhips
                liste_auteurs = row[5]
                editeur = row[6]
                liste_categories = row[7]

        load_session.commit()

