import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import os

# Cargar modelo
modelo = load_model("modelo_plantas.h5")

# Cargar nombres de clases
clases = sorted(os.listdir("dataset"))

# Tamaño esperado de imagen por el modelo
img_size = (150, 150)

# Captura de video
cap = cv2.VideoCapture(0)

print("🎥 Presiona 'ESC' para salir")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocesamiento de la imagen
    img = cv2.resize(frame, img_size)
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    # Predicción
    pred = modelo.predict(img)
    clase_idx = np.argmax(pred)
    clase_nombre = clases[clase_idx]
    conf = np.max(pred) * 100

    # Mostrar resultado en el frame
    texto = f"{clase_nombre} ({conf:.2f}%)"
    cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Clasificador de Plantas - Proyecto IA", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
