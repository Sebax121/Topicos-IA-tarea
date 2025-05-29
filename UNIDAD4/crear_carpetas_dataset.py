import os

# Lista de nombres de plantas en español
plantas = [
    "sábila", "albahaca", "cactus", "menta", "lavanda", "manzanilla", "perejil", "orégano", "romero", "tomillo",
    "espinaca", "lechuga", "cilantro", "caléndula", "tulipán", "margarita", "girasol", "hibisco", "helecho", "bambú",
    "hiedra", "potus", "sansevieria", "lirio_de_paz", "árbol_del_caucho", "platanera", "tomatera", "pimiento_morrón",
    "chile", "jengibre", "cúrcuma", "col_rizada", "acelga", "rúcula", "aloe_jucunda", "eucalipto", "coleo",
    "begonia", "hortensia", "orquídea", "ciclamen", "geranio", "peonía", "petunia", "pensamiento", "azalea", "capuchina",
    "anturio", "crotón", "zamioculca"
]

# Crear carpeta raíz del dataset
carpeta_base = "dataset"
os.makedirs(carpeta_base, exist_ok=True)

# Crear subcarpetas
for planta in plantas:
    nombre_limpio = planta.replace(" ", "_").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n")
    ruta = os.path.join(carpeta_base, nombre_limpio.lower())
    os.makedirs(ruta, exist_ok=True)

print("✅ Carpetas creadas correctamente con nombres en español.")
