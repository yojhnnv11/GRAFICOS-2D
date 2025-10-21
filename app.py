import pandas as pd
import matplotlib.pyplot as plt

# Datos ficticios de municipios de Antioquia
data = {
    "Municipio": ["Medellín", "Envigado", "Bello", "Itagüí", "Rionegro", "La Ceja", "Santa Fe de Antioquia"],
    "Ventas_promedio": [150000, 80000, 60000, 70000, 50000, 30000, 25000],
    "Poblacion_aprox": [2500000, 250000, 500000, 280000, 160000, 60000, 25000]
}

# Crear un DataFrame con pandas
df = pd.DataFrame(data)

# Mostrar los datos
print(df)

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df["Municipio"], df["Ventas_promedio"], color="teal")

# Personalizar el gráfico
plt.title("Ventas promedio por municipio - Antioquia", fontsize=14)
plt.xlabel("Municipio", fontsize=12)
plt.ylabel("Ventas promedio (COP)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
