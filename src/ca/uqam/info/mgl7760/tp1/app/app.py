from flask import Flask
from ca.uqam.info.mgl7760.tp1.domain.livre import Livre
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/livres")
def get_livres():
    chaine = "<H1>Liste de Tous Les Livres</H1>"
    chaine = chaine + "<br><b>Titre (Année de parution)<tab>Auteurs</b></br>"
    livres = Livre.chercher_tous()
    for livre in livres:
        chaine = chaine + livre.titre + "(" + livre.annee + ")"

    return chaine
