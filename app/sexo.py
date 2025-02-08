import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# URL del archivo CSV
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Graficas-Pacientes-HomeMed/main/data/lista_pacientes.csv"

# Cargar el dataset y limpiar nombres de columnas
df = pd.read_csv(archivo_csv)
df.columns = df.columns.str.strip()  # Elimina espacios en los nombres

# Verificar nombres de columnas
columna_edad = "Edad"
columna_sexo = "Sexo"

if columna_edad not in df.columns or columna_sexo not in df.columns:
    raise ValueError("No se encontraron las columnas necesarias en el dataset.")

# Convertir la columna de edad a numérica
df[columna_edad] = pd.to_numeric(df[columna_edad], errors="coerce")

# Eliminar filas con edades nulas o fuera de rango
df = df.dropna(subset=[columna_edad])
df = df[df[columna_edad] >= 0]  # Filtra edades negativas si las hay

# Definir los rangos de edad de 5 en 5
bins = list(range(0, int(df[columna_edad].max()) + 6, 5))
labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins)-1)]

# Crear la nueva columna de rangos de edad
df["Rango de Edad"] = pd.cut(df[columna_edad], bins=bins, labels=labels, right=False)

# Contar pacientes por sexo dentro de cada rango de edad
conteo_por_edad_sexo = df.groupby(["Rango de Edad", columna_sexo]).size().unstack(fill_value=0)

# Crear el gráfico
conteo_por_edad_sexo.plot(kind="bar", figsize=(15, 7), color=["lightblue", "lightcoral"], width=0.8)

# Configuración del gráfico
plt.xlabel("Rango de Edad")
plt.ylabel("Cantidad de Pacientes")
plt.title("Distribución de Pacientes por Sexo en Rangos de Edad")
plt.xticks(rotation=45)
plt.legend(title="Sexo")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Mostrar la gráfica
plt.show()
