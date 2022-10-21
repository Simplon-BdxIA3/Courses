# Objectifs :

### Ouvrir le fichier csv
### Initialiser un dict vide
### Récupérer la colonne/Identifier la colonne : "Film préféré"
### Stocker les données dans une list
### Pour chaque nom de film présent dans la list
    ### Créer l'URL de la page du film sur imdb
    ### Télécharger la page
    ### Identifier l'année du premier résultat
    ### Convertir le résultat en integer
    ### On stock le couple nom: année dans le dictionnaire

from bs4 import BeautifulSoup
import pandas as pd
import requests

akinator = pd.read_csv("akinatorIA3v3.csv")
films = akinator['Film préféré'].tolist()
movie_names = {}

for film in films:
    url = f'https://www.imdb.com/find?q={film}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    years = soup.find(class_="ipc-metadata-list-summary-item__li").text
    movie_names[film] = int(years)

print(movie_names)
