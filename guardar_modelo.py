import joblib
import pandas as pd

# Cargar el modelo entrenado
modelo = joblib.load("modelo_suicidios.pkl")

# Crear el DataFrame SOLO con la columna "year" porque es la única que el modelo reconoce
nuevos_datos = pd.DataFrame([[2023]], columns=["year"])

# Hacer la predicción
prediccion = modelo.predict(nuevos_datos)

# Mostrar el resultado
print(f"Predicción para {nuevos_datos.values}: {prediccion}")




