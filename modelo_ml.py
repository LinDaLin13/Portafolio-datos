import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Cargar el dataset limpio
df_ml = pd.read_csv(r"C:\Users\Linda\Desktop\Portafolio_Linda\who_suicide_statistics_cleaned.csv")

# Seleccionar las variables para el modelo
X = df_ml[["year"]]  # Variable independiente (Año)
y = df_ml["suicides_no"]  # Variable dependiente (Número de suicidios)

# Dividir en datos de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X_train, y_train)

# Hacer predicciones
y_pred = modelo.predict(X_test)

# Evaluar el modelo
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nEvaluación del Modelo:")
print(f"MAE (Error Absoluto Medio): {mae:.2f}")
print(f"MSE (Error Cuadrático Medio): {mse:.2f}")
print(f"R² (Coeficiente de Determinación): {r2:.2f}")

# Visualizar la regresión
plt.figure(figsize=(10, 5))
sns.scatterplot(x=X_test["year"], y=y_test, color="blue", label="Datos reales")
sns.lineplot(x=X_test["year"], y=y_pred, color="red", label="Predicción")
plt.title("Regresión Lineal: Predicción de Suicidios por Año")
plt.xlabel("Año")
plt.ylabel("Número de Suicidios")
plt.legend()
plt.grid()
plt.show()
