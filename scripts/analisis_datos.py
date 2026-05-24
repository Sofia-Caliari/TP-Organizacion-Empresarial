
# usamos pandas para manejar archivos CSV y datos
import pandas as pd

# usamos matplotlib para crear gráficos
import matplotlib.pyplot as plt

# leemos el archivo csv de ventas 2024
# df significa DataFrame (tabla de datos en Python)
df = pd.read_csv("datos/sales_sample_2024.csv")

# mostrar primeras filas del archivo
print("Primeras filas del dataset:")
print(df.head(9))

# calculamos el total de ventas
total_ventas = df["sales_amount"].sum()
print(f"\nTotal de ventas: ${total_ventas:,.2f}")

# calculamos el promedio de ventas
promedio_ventas = df["sales_amount"].mean()
print(f"Promedio de ventas: ${promedio_ventas:,.2f}")

# calculamos la venta máxima
venta_maxima = df["sales_amount"].max()
print(f"Venta máxima: ${venta_maxima:,.2f}")

# crear gráfico de distribución de ventas
plt.figure(figsize=(10, 6))

plt.hist(
    df["sales_amount"],
    bins=30,
    color='skyblue',
    edgecolor='black'
)

plt.title(f'Distribución de Ventas 2024 ({len(df)} registros)')
plt.xlabel('Monto ($)')
plt.ylabel('Cantidad de ventas')

plt.grid(axis='y', alpha=0.3)

# guardar el gráfico en la carpeta /resultados
plt.savefig("resultados/grafico_resultados.png")

# mostrar gráfico
plt.show()
