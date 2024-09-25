import requests
from bs4 import BeautifulSoup
import csv

# URL de la page à scraper
url = 'https://sortiradouala.com/'

# Envoyer une requête GET pour récupérer le contenu HTML
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Ouvrir un fichier CSV pour enregistrer les données
with open('sortir_a_douala_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nom du lieu', 'Localisation', 'Image URL'])

    # Récupérer chaque section qui correspond à un lieu
    for place in soup.find_all('article', class_='listing-item'):
        # Récupérer le nom du lieu
        name = place.find('h2', class_='entry-title').text.strip()

        # Récupérer la localisation si disponible
        location_tag = place.find('div', class_='location')
        location = location_tag.text.strip() if location_tag else 'Localisation non disponible'

        # Récupérer l'URL de l'image
        image_tag = place.find('img')
        image_url = image_tag['src'] if image_tag else 'Image non disponible'

        # Écrire les données dans le fichier CSV
        writer.writerow([name, location, image_url])

        # Afficher les informations pour vérification
        print(f"Nom: {name}\nLocalisation: {location}\nImage: {image_url}\n")

print("Scraping terminé. Les données ont été enregistrées dans 'sortir_a_douala_data.csv'.")
