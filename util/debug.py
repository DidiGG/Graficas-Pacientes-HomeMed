import pandas as pd

# URL del archivo CSV
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Graficas-Pacientes-HomeMed/main/data/lista_pacientes.csv"


df = pd.read_csv(archivo_csv, encoding="utf-8", nrows=100)
print(df.tail())  # Verifica la última fila cargada
