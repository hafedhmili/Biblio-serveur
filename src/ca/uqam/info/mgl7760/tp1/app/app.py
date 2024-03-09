from flask import Flask
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from ca.uqam.info.mgl7760.tp1.domain.basebiblio import BaseBiblio
from ca.uqam.info.mgl7760.tp1.domain.livre import Livre
from ca.uqam.info.mgl7760.tp1.app.orm import init_system, load_data
from markupsafe import escape

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# create an engine

engine = init_system()
load_data(engine)
print("hello world from Flask. Just created two users and saved them")






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

