import numpy as np
import tkinter as tk
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# ==== Paso 1: Generar el dataset con dígitos del 1 al 9 ====
def generar_dataset():
    X, y = [], []
    digitos = list(range(1, 10))
    for op in range(4):  # 0: suma, 1: resta, 2: multiplicación, 3: división
        for num1 in digitos:
            for num2 in digitos:
                if op == 0:
                    resultado = num1 + num2
                elif op == 1:
                    resultado = num1 - num2
                elif op == 2:
                    resultado = num1 * num2
                elif op == 3:
                    resultado = num1 / num2
                X.append([num1, num2, op])
                y.append(resultado)
    return np.array(X), np.array(y)

# ==== Paso 2: Preparar datos y entrenar la red ====
X, y = generar_dataset()
X_max = np.max(X, axis=0)
X = X / X_max
y_max = np.max(np.abs(y))
y = y / y_max

# Crear y entrenar el modelo
model = Sequential([
    Dense(32, input_dim=3, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='linear')
])
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(X, y, epochs=150, batch_size=8, verbose=0)

# ==== Paso 3: Función de predicción ====
def predecir(num1, num2, operacion):
    entrada = np.array([[num1, num2, operacion]]) / X_max
    pred = model.predict(entrada, verbose=0)
    return pred[0][0] * y_max

# ==== Paso 4: Interfaz gráfica ====
def calcular():
    try:
        n1 = int(entry1.get())
        n2 = int(entry2.get())
        op = operacion_var.get()

        if not (1 <= n1 <= 9 and 1 <= n2 <= 9):
            resultado_label.config(text="Números entre 1 y 9")
            return

        resultado = predecir(n1, n2, op)
        operaciones = ['suma', 'resta', 'multiplicación', 'división']
        resultado_label.config(text=f"Resultado ({operaciones[op]}): {resultado:.2f}")

    except ValueError:
        resultado_label.config(text="Entrada no válida")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora con red neuronal")
ventana.geometry("350x250")

# Widgets
tk.Label(ventana, text="Primer número (1-9):").pack()
entry1 = tk.Entry(ventana)
entry1.pack()

tk.Label(ventana, text="Segundo número (1-9):").pack()
entry2 = tk.Entry(ventana)
entry2.pack()

tk.Label(ventana, text="Operación:").pack()
operacion_var = tk.IntVar()
operacion_var.set(0)
tk.OptionMenu(ventana, operacion_var, 0, 1, 2, 3).pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Ejecutar ventana
ventana.mainloop()
