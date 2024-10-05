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
cors = CORS(app, resources={"*": {"origins": "*"}})
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
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def hello_world():
    response = Flask.jsonify({'messge':'Hello world'})
    response.headers.add
    return "<p>Hello, World!</p>"

@app.route("/<name>")
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/livres_html")
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_table_html_livres():
    print("Hey, I got called to return an HTML table")
    chaine = "<H1>Liste de Tous Les Livres</H1><br>"
    chaine = chaine + "<table><tr><th>Titre</th><th>Année de parution</th><th>Editeur</th><th>ISBN</th><br>"
    engine = get_engine()
    with Session(engine) as session:
        listes_livres = Livre.chercher_tous(session)
        for liste_livres in listes_livres:
            livre = liste_livres[0]
            print(livre.titre)
            chaine = chaine + "<tr><td>"+livre.titre + "</td><td>" + str(livre.annee)+ "</td><td>" + str(livre.editeur.nom)+"</td><td>" + str(livre.isbn) + "</td></tr>"
        session.close()
    chaine = chaine+ "</table>"
    #print(chaine)
    return chaine

@app.route("/livres")
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_liste_tous_livres():
    print("Hey, I got called to return a list of books")
    engine = get_engine()
    liste = []
    with Session(engine) as session:
        liste_livres = Livre.chercher_tous(session)
        for element_livre in liste_livres:
            livre = element_livre[0]
            liste_livre = [livre.titre,livre.annee,livre.editeur.nom,livre.isbn]
            liste.append(liste_livre)
        session.close()
    print(liste)
    return liste
# create an engine

def get_engine():
    return engine
#load_data(engine,file_name)

engine = init_system()
print("hello world from Flask. Just created two users and saved them")
