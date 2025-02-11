import pandas as pd
import matplotlib.pyplot as plt

# URL del archivo CSV
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Graficas-Pacientes-HomeMed/main/data/lista_pacientes.csv"

# Cargar el dataset
df = pd.read_csv(archivo_csv)
print(df.columns)

# Filtrar los pacientes con "DETERIORO COGNITIVO LEVE" en la columna "resultado"
df_leve = df[df["resultado"] == "DETERIORO COGNITIVO LEVE"]

# Verificar el nombre exacto de la columna de edad
columna_edad = "edad"

if columna_edad not in df_leve.columns:
    raise ValueError(f"La columna '{columna_edad}' no se encontró en el dataset.")

# Convertir la columna de edad a numérica
df_leve[columna_edad] = pd.to_numeric(df_leve[columna_edad], errors="coerce")

# Eliminar filas con edades nulas o fuera de rango
df_leve = df_leve.dropna(subset=[columna_edad])
df_leve = df_leve[df_leve[columna_edad] >= 50]  # Filtrar edades menores a 50 años

bins = list(range(50, int(df_leve[columna_edad].max()) + 6, 5))
labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins)-1)]

# Crear la nueva columna de rangos de edad
df_leve["Rango de Edad"] = pd.cut(df_leve[columna_edad], bins=bins, labels=labels, right=False)

# Contar la cantidad de pacientes en cada rango de edad
conteo_edades = df_leve["Rango de Edad"].value_counts().sort_index()

# Crear el gráfico
plt.figure(figsize=(12, 6))
bars = plt.bar(conteo_edades.index, conteo_edades.values, color="skyblue", width=0.8)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=10, color="black")

# Configuración del gráfico
plt.xlabel("Rango de Edad")
plt.ylabel("Cantidad de Pacientes")
plt.title("Pacientes con DETERIORO COGNITIVO LEVE por Edades")
plt.xticks(rotation=45)  # Gira etiquetas para mejor legibilidad
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()
