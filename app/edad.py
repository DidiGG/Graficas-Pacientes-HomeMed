import pandas as pd

# Ruta del archivo CSV con las edades
archivo_csv = "archivo.csv" 

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Verificar si la columna "edad" existe
if "Edad" in df.columns:
    # Asegurar que la columna sea numérica (por si viene como texto)
    df["edad"] = pd.to_numeric(df["edad"], errors="coerce")

    # Eliminar valores NaN (faltantes) en la columna edad
    df = df.dropna(subset=["edad"])

    # Generar estadísticas descriptivas
    estadisticas = df["edad"].describe()

    # Guardar los resultados en un nuevo CSV
    estadisticas.to_csv("estadisticas_edades.csv")

    print("Estadísticas descriptivas guardadas en 'estadisticas_edades.csv'")
    print(estadisticas)
else:
    print("Error: La columna 'edad' no existe en el archivo CSV.")
