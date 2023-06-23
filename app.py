# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/Accueil")
def accueil():
    return render_template("Accueil.html")


@app.route("/Equipe1")
def equipe1():
    return render_template("Equipe1.html")


@app.route("/Planning")
def planning():
    return render_template("Planning.html")

@app.route('/Equipe2')
def equipe2():
    return redirect(url_for('Accueil'))

@app.route('/contacts')
def contacts():
    return redirect(url_for('Accueil'))
