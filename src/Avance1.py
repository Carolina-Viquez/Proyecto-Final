import pandas
import kagglehub
import matplotlib.pyplot as matplot
import os

# Descargar el dataset de Kaggle
path = kagglehub.dataset_download("unsdsn/world-happiness")
print("Path to dataset files:", path)

# Buscar automáticamente el archivo CSV en la carpeta descargada
csv_file = None
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith("9.csv"):
            csv_file = os.path.join(root, file)
            break
    if csv_file:
        break

if not csv_file:
    raise FileNotFoundError("No se encontró un archivo CSV en el dataset descargado.")

# Importar el archivo
datos = pandas.read_csv(csv_file)

# Mostrar la información básica del archivo
print("\n----INFORMACION BASICA DEL DOCUMENTO----")
datos.info()
print("----FIN DE INFORMACION BASICA----\n")

print("----MOSTRANDO FUNCION DESCRIBE----")
print(datos.describe(include='all'))
print("----FIN DE FUNCION DESCRIBE----\n")

print("----MOSTRANDO FUNCION SHAPE----")
print(datos.shape)
print("----FIN DE FUNCION SHAPE----\n")

# Comprobación de datos nulos
if datos.isnull().values.any():
    print("Hay datos nulos:")
    print(datos.isnull().sum())
else:
    print("No hay datos nulos")

# Mostrar las primeras 10 filas de información
print("----MOSTRANDO LAS PRIMERAS 10 FILAS DE INFORMACION----\n")
pandas.set_option('display.max_columns', None)
print(datos.head(10))
print("----FIN DE LAS PRIMERAS 10 FILAS DE INFORMACION----\n")

# Identificación de tipos de datos por columna
print("----MOSTRANDO LOS TIPOS DE DATOS----\n")
print(datos.dtypes)
print("----FIN DE LOS TIPOS DE DATOS----\n")

# Mostrar una visualización general del top 10
print("A CONTINUACION SE MOSTRARA UN GRAFICO SOBRE EL TOP 10 DE PAISES MAS FELICES DEL MUNDO 2019")

# Obtener el top 10 de países más felices
top10 = datos.sort_values(by='Score', ascending=False).head(10)

# Aplicar estilo
matplot.style.use('ggplot')

# Crear figura
matplot.figure(figsize=(12, 7))

matplot.grid(False)

# Gráfico de barras
bars = matplot.bar(top10['Country or region'], top10['Score'], color='orchid')

# Etiquetas y título
matplot.xlabel("País", fontsize=12)
matplot.ylabel("Puntaje de felicidad", fontsize=12)
matplot.title("Top 10 países más felices en 2019", fontsize=14, weight='bold')

# Rotación y alineación de etiquetas
matplot.xticks(rotation=45, ha='right')

# Mostrar valores encima de cada barra
for bar in bars:
    yval = bar.get_height()
    matplot.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f'{yval:.2f}', 
             ha='center', va='bottom', fontsize=10)

# Eliminar bordes innecesarios (spines)
for spine in ['top', 'right']:
    matplot.gca().spines[spine].set_visible(False)

# Ajustar diseño
matplot.tight_layout()

# Mostrar gráfico
matplot.show()