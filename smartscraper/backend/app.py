from flask import Flask, jsonify, request
from flask_cors import CORS
from db import SessionLocal, init_db
from models import Musee

app = Flask(__name__)
CORS(app)

# Initialisation de la base (au premier lancement)
init_db()

@app.route('/api/data', methods=['GET'])
def get_all_musees():
    session = SessionLocal()
    musees = session.query(Musee).all()
    result = [m.__dict__.copy() for m in musees]
    for r in result:
        r.pop('_sa_instance_state', None)
    session.close()
    return jsonify(result)

@app.route('/api/data/<ville>', methods=['GET'])
def get_musees_by_ville(ville):
    session = SessionLocal()
    musees = session.query(Musee).filter(Musee.ville.ilike(f"%{ville}%")).all()
    result = [m.__dict__.copy() for m in musees]
    for r in result:
        r.pop('_sa_instance_state', None)
    session.close()
    return jsonify(result)

@app.route('/api/data/nom/<nom>', methods=['GET'])
def get_musees_by_nom(nom):
    session = SessionLocal()
    # Recherche partielle insensible à la casse
    musees = session.query(Musee).filter(Musee.nom.ilike(f"%{nom}%")).all()
    result = [m.__dict__.copy() for m in musees]
    for r in result:
        r.pop('_sa_instance_state', None)
    session.close()
    return jsonify(result)


@app.route('/api/scrape', methods=['POST'])
def launch_scrape():
    from scraper import download_and_clean
    download_and_clean()
    return jsonify({"message": "Scraping et importation terminés."})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

