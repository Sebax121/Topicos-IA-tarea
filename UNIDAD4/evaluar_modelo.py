import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score

img_size = (150, 150)

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
val_generator = datagen.flow_from_directory(
    "dataset",
    target_size=img_size,
    batch_size=32,
    class_mode='categorical',
    subset='validation',
    shuffle=False
)

model = tf.keras.models.load_model("modelo_plantas.h5")

y_pred = model.predict(val_generator)
y_pred_classes = y_pred.argmax(axis=1)
y_true = val_generator.classes

print("Accuracy:", accuracy_score(y_true, y_pred_classes))
print("Precision:", precision_score(y_true, y_pred_classes, average='macro'))
print("Recall:", recall_score(y_true, y_pred_classes, average='macro'))
print("\nMatriz de confusión:")
print(confusion_matrix(y_true, y_pred_classes))
