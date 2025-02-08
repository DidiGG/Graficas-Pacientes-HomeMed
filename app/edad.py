import pandas as pd
import matplotlib.pyplot as plt

# URL del archivo CSV
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Graficas-Pacientes-HomeMed/main/data/lista_pacientes.csv"

# Cargar el dataset
df = pd.read_csv(archivo_csv)

# Verificar las columnas disponibles
print(df.columns)

# Reemplaza "edad" por el nombre exacto de la columna de edades en tu dataset
columna_edad = "Edad"  # Asegúrate de que coincide con el nombre de la columna

# Contar la cantidad de pacientes por edad
conteo_edades = df[columna_edad].value_counts().sort_index()

# Crear el gráfico
plt.figure(figsize=(15, 7))
plt.bar(conteo_edades.index, conteo_edades.values, color="skyblue")
plt.xlabel("Edad")
plt.ylabel("Cantidad de Pacientes")
plt.title("Distribución de Pacientes por Edad")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
