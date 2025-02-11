import pandas as pd
import matplotlib.pyplot as plt

# URL del archivo CSV
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Graficas-Pacientes-HomeMed/main/data/lista_pacientes.csv"

# Cargar el dataset
df = pd.read_csv(archivo_csv)
print(df.columns)

# Filtrar los pacientes con "VALORACIÓN COGNITIVA NORMAL" en la columna "resultado"
df_normal = df[df["resultado"] == "VALORACIÓN COGNITIVA NORMAL"]

# Contar la cantidad de pacientes por paquete
conteo_paquetes = df_normal["paquete"].value_counts().sort_index()

# Crear el gráfico
plt.figure(figsize=(15, 7))
bars = plt.bar(conteo_paquetes.index, conteo_paquetes.values, color="skyblue")

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=7)

plt.xlabel("Paquete")
plt.ylabel("Cantidad de Pacientes")
plt.title("Pacientes con VALORACIÓN COGNITIVA NORMAL por PAQUETE")
plt.xticks(rotation=0) 
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()