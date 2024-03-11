from flask import Flask
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from ca.uqam.info.mgl7760.tp1.domain.basebiblio import BaseBiblio
from ca.uqam.info.mgl7760.tp1.domain.livre import Livre
from ca.uqam.info.mgl7760.tp1.app.orm import init_system
from markupsafe import escape
import csv

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
file_name = './data/biblio.csv'


def load_data(engine, csvfile_path):
    from ca.uqam.info.mgl7760.tp1.domain.auteur import Auteur
    from ca.uqam.info.mgl7760.tp1.domain.livre import Livre
    from ca.uqam.info.mgl7760.tp1.domain.categorie import Categorie
    from ca.uqam.info.mgl7760.tp1.domain.editeur import Editeur

    with Session(engine) as load_session:
        # open csv file
        with open(csvfile_path,encoding='windows-1252',newline='') as biblio_data_file:
            biblio_data_reader = csv.reader(biblio_data_file, delimiter=',')

            dict_auteurs=dict()
            dict_editeurs=dict()
            dict_categories = dict()
            # skip first row, which consists of headers
            biblio_data_reader.__next__()
            # iterate over data rows
            for row in biblio_data_reader:
                # creer livre
                livre = Livre(titre=row[0],description=row[1],isbn=row[2],annee=row[3])
                load_session.add(livre)

                # get relatiosnhips

                # auteurs
                liste_auteurs = row[5]
                noms_auteurs = liste_auteurs.split(',')
                for nom_auteur in noms_auteurs:
                    if  (nom_auteur not in dict_auteurs):
                        auteur = Auteur(nom=nom_auteur)
                        dict_auteurs[nom_auteur] = auteur
                        load_session.add(auteur)
                    auteur = dict_auteurs[nom_auteur]
                    livre.ajoute_auteur(auteur)
                    
                # editeur
                nom_editeur = row[6]
                if (nom_editeur not in dict_editeurs):
                    editeur = Editeur(nom=nom_editeur)
                    dict_editeurs[nom_editeur] = editeur
                    load_session.add(editeur)
                editeur = dict_editeurs[nom_editeur]
                livre.editeur = editeur
                
                # categories
                liste_categories = row[7]
                noms_categories = liste_categories.split(',')
                for nom_categorie in noms_categories:
                    if (nom_categorie not in dict_categories):
                        categorie = Categorie(nom=nom_categorie)
                        dict_categories[nom_categorie] = categorie
                        load_session.add(categorie)
                    categorie = dict_categories.get(nom_categorie)                    
                    livre.ajouter_categorie(categorie)

        load_session.commit()



@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
@cross_origin()
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/livres")
@cross_origin()
def get_livres():
    print("Hey, I got called")
    chaine = "<H1>Liste de Tous Les Livres</H1>"
    chaine = chaine + "<br><b>Titre (Année de parution)<tab>Auteurs</b></br>"
    livres = Livre.chercher_tous()
    for livre in livres:
        chaine = chaine + livre.titre + "(" + livre.annee + ")"

    return chaine

# create an engine

engine = init_system()
load_data(engine,file_name)
print("hello world from Flask. Just created two users and saved them")
