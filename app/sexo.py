import pandas as pd
import matplotlib.pyplot as plt

# URL del archivo CSV
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Graficas-Pacientes-HomeMed/main/data/lista_pacientes.csv"

# Cargar el dataset
df = pd.read_csv(archivo_csv)
print(df.columns)
columna_sexo = "sexo"  

# Contar la cantidad de pacientes por sexo
conteo_sexos = df[columna_sexo].value_counts().sort_index()
conteo_sexos.index = conteo_sexos.index.map({"M": "Masculino", "F": "Femenino"})

# Crear un mapeo de colores para cada sexo
color_mapping = {"Masculino": "blue", "Femenino": "pink"}
colors = [color_mapping[sexo] for sexo in conteo_sexos.index]

# Crear el gráfico
plt.figure(figsize=(15, 7))
bars = plt.bar(conteo_sexos.index, conteo_sexos.values, color=colors)

# Añadir los valores exactos sobre cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval - 0.2, int(yval), ha='center', va='bottom', fontsize=8)

plt.xlabel("Sexo")
plt.ylabel("Cantidad de Pacientes")
plt.title("Distribución de Pacientes por Sexo")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()