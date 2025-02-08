import pandas as pd
import matplotlib.pyplot as plt

# URL del archivo CSV
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Graficas-Pacientes-HomeMed/main/data/lista_pacientes.csv"

# Cargar el dataset y limpiar nombres de columnas
df = pd.read_csv(archivo_csv)
df.columns = df.columns.str.strip()  # Eliminar espacios en los nombres de las columnas

# Verificar el nombre exacto de la columna de edad
columna_edad = "edad"

if columna_edad not in df.columns:
    raise ValueError(f"La columna '{columna_edad}' no se encontró en el dataset.")

# Convertir la columna de edad a numérica
df[columna_edad] = pd.to_numeric(df[columna_edad], errors="coerce")

# Eliminar filas con edades nulas o fuera de rango
df = df.dropna(subset=[columna_edad])
df = df[df[columna_edad] >= 50]  # Filtrar edades menores a 50 años

# Definir los rangos de edad de 5 en 5 desde 50 hasta la edad máxima en los datos
bins = list(range(50, int(df[columna_edad].max()) + 6, 5))
labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins)-1)]

# Crear la nueva columna de rangos de edad
df["Rango de Edad"] = pd.cut(df[columna_edad], bins=bins, labels=labels, right=False)

# Contar la cantidad de pacientes en cada rango de edad
conteo_edades = df["Rango de Edad"].value_counts().sort_index()

# Crear el gráfico
plt.figure(figsize=(12, 6))
bars = plt.bar(conteo_edades.index, conteo_edades.values, color="skyblue", width=0.8)

# Añadir etiquetas exactas sobre cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=10, color="black")

# Configuración del gráfico
plt.xlabel("Rango de Edad")
plt.ylabel("Cantidad de Pacientes")
plt.title("Distribución de Pacientes por Rango de Edad (Desde 50 años)")
plt.xticks(rotation=45)  # Gira etiquetas para mejor legibilidad
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Mostrar la gráfica
plt.show()
