from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scraper import Musee, DB_URL

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Afficher quelques musées
musees = session.query(Musee).all()

for m in musees:
    print(f"{m.id} - {m.nom} ({m.ville}, {m.region})")
