from icrawler.builtin import GoogleImageCrawler
import os

# Lista con las 50 plantas (puedes modificarla si quieres)
plantas = [
    "Albahaca planta", "Aloe vera planta", "Alocasia planta", "Anthurium planta",
    "Bambú planta", "Begonia planta", "Bonsái planta", "Cactus planta",
    "Calatea planta", "Cala planta", "Crotón planta", "Dracaena planta",
    "Ficus planta", "Geranio planta", "Hiedra planta", "Helecho planta",
    "Jazmín planta", "Lavanda planta", "Lirio planta", "Margarita planta",
    "Orquídea planta", "Palma planta", "Petunia planta", "Potos planta",
    "Sansevieria planta", "Violeta planta", "Yuca planta", "Zamioculca planta",
    "Anturio planta", "Azalea planta", "Begonia planta", "Cala planta",
    "Dalia planta", "Fucsia planta", "Gardenia planta", "Hortensia planta",
    "Jazmín planta", "Lirio planta", "Mimosa planta", "Nerium planta",
    "Orquídea planta", "Petunia planta", "Rosa planta", "Tulipán planta",
    "Violeta planta", "Yucca planta", "Zinnia planta", "Lavanda planta",
    "Geranio planta", "Helecho planta"
]

# Carpeta base donde están las carpetas de plantas
base_dir = "dataset"

for planta in plantas:
    carpeta_destino = os.path.join(base_dir, planta.lower().replace(" ", "_"))
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    google_crawler = GoogleImageCrawler(storage={"root_dir": carpeta_destino})
    print(f"Descargando imágenes para: {planta}")
    google_crawler.crawl(keyword=planta, max_num=30)  # Cambia max_num si quieres más imágenes
