from flask import Flask
from flask_cors import CORS, cross_origin
from ca.uqam.info.mgl7760.tp1.domain.livre import Livre
from ca.uqam.info.mgl7760.tp1.domain.basebiblio import BaseBiblio
from markupsafe import escape
from sqlalchemy import create_engine

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def init_system():
    # create an engine
    engine = create_engine("postgresql://localhost:5432", echo=True)
    print("Starting Flask server")
    BaseBiblio.metadata.create_all(engine)
    
init_system()
print("hello world from Flask")






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

