import os
import shutil

# Ruta de la carpeta del dataset
ruta_dataset = "dataset"

# Obtener todas las subcarpetas (es decir, las clases de plantas)
carpetas = sorted([carpeta for carpeta in os.listdir(ruta_dataset) if os.path.isdir(os.path.join(ruta_dataset, carpeta))])

# Mantener solo las primeras 50
carpetas_a_mantener = set(carpetas[:50])

# Eliminar el resto
for carpeta in carpetas:
    if carpeta not in carpetas_a_mantener:
        ruta_completa = os.path.join(ruta_dataset, carpeta)
        shutil.rmtree(ruta_completa)
        print(f"Carpeta eliminada: {carpeta}")

print("\n✅ Limpieza completa. Solo se mantienen las primeras 50 carpetas.")
