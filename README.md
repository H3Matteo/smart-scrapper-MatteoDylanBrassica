🧠 SmartScraper – Projet de collecte et visualisation de données open data
🎯 Objectif du projet
Le projet SmartScraper a pour objectif de développer une application complète permettant de :

Collecter des données publiques via une source open data légale,

Les stocker dans une base relationnelle,

Les exposer via une API REST avec Flask,

Les afficher dynamiquement dans une interface web React,

Le tout conteneurisé avec Docker.

📊 Source de données utilisée
Nom : Musées de France – Base MUSEOFILE

URL : https://www.data.gouv.fr/fr/datasets/musees-de-france-base-museofile/

Fichier exploité : liste-des-musees-de-france.csv

Nombre d’entrées : ~1200 musées

Champs exploités (exemples) : Nom du musée, Département, Commune, Code INSEE, Coordonnées GPS, URL, etc.

📜 Licence et légalité
Licence : Licence Ouverte / Open Licence (Etalab)

Citation :

"Les données diffusées sur data.gouv.fr sont librement réutilisables dans les conditions fixées par la Licence Ouverte."

Justification de la légalité :
La base MUSEOFILE est diffusée sur la plateforme officielle data.gouv.fr, et publiée sous une licence ouverte permettant explicitement l’utilisation, la modification et la redistribution des données, y compris par des traitements automatisés comme le scraping ou l’import via API/CSV.
