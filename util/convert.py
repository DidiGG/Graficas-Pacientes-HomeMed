import pandas as pd
import os

# Cargar el archivo Excel
df = pd.read_excel(r"C:\Users\didie\Downloads\pacientes.xlsx", engine="openpyxl")  

#directorio destino
directorio_destino = r"C:\Users\didie\OneDrive\Documents\GitHub\Graficas-Pacientes-HomeMed\data"

# Definir la ruta completa del archivo final
ruta_destino = os.path.join(directorio_destino, "lista_pacientes.csv")

# Guardar como CSV
df.to_csv(ruta_destino, index=False, encoding="utf-8")  
