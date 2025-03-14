import matplotlib.pyplot as plt
import seaborn as sns

# Eliminar filas con valores nulos
df_cleaned = df.dropna()

# Verificar que no haya valores nulos
print("\nValores nulos después de limpieza:")
print(df_cleaned.isnull().sum())

# Eliminar duplicados si los hay
df_cleaned = df_cleaned.drop_duplicates()

# Convertir columna 'year' a tipo entero (por si no lo es)
df_cleaned["year"] = df_cleaned["year"].astype(int)

# Verificar cambios
print("\nInformación después de limpieza:")
print(df_cleaned.info())

# Guardar el dataset limpio
df_cleaned.to_csv(r"C:\Users\Linda\Desktop\Portafolio_Linda\who_suicide_statistics_cleaned.csv", index=False)


# Configuración de estilo
sns.set_style("darkgrid")

# Distribución de casos de suicidio por año
plt.figure(figsize=(10, 5))
sns.lineplot(x=df_cleaned["year"], y=df_cleaned["suicides_no"], marker="o", color="blue")
plt.title("Casos de suicidio por año")
plt.xlabel("Año")
plt.ylabel("Número de suicidios")
plt.grid()
plt.show()

# Casos de suicidio por género
plt.figure(figsize=(8, 5))
sns.barplot(x=df_cleaned["sex"], y=df_cleaned["suicides_no"], palette="coolwarm")
plt.title("Casos de suicidio por género")
plt.xlabel("Género")
plt.ylabel("Número de suicidios")
plt.show()

# Casos de suicidio por grupo de edad
plt.figure(figsize=(10, 5))
sns.barplot(x=df_cleaned["age"], y=df_cleaned["suicides_no"], palette="viridis", order=sorted(df_cleaned["age"].unique()))
plt.title("Casos de suicidio por grupo de edad")
plt.xlabel("Grupo de edad")
plt.ylabel("Número de suicidios")
plt.xticks(rotation=45)
plt.show()
