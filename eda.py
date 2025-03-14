import pandas as pd

df = pd.read_csv(r"C:\Users\Linda\Desktop\Portafolio_Linda\who_suicide_statistics.csv")


# Información general del dataset
print("Información del dataset:")
print(df.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Valores nulos en cada columna
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Valores únicos en columnas clave
print("\nValores únicos en la columna 'country':")
print(df["country"].unique())

print("\nValores únicos en la columna 'sex':")
print(df["sex"].unique())

print("\nValores únicos en la columna 'age':")
print(df["age"].unique())

