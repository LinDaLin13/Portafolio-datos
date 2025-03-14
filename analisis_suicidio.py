import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos correctamente
df = pd.read_csv(r"C:\Users\Linda\Desktop\Portafolio_Linda\who_suicide_statistics.csv")

# Revisar nombres de las columnas
print(df.columns)

# Ver las primeras filas
print(df.head())

# Ajustar el código a los nombres correctos de columnas
plt.figure(figsize=(10,5))
sns.lineplot(x=df["year"], y=df["suicides_no"], marker="o", color="blue")
plt.title("Casos de suicidio por año")
plt.xlabel("Año")
plt.ylabel("Número de suicidios")
plt.grid()
plt.show()