import pandas
import kagglehub 
import matplotlib.pyplot as matplot

#Descargar el dataset de la pagina
path = kagglehub.dataset_download("unsdsn/world-happiness")
print("Path to dataset files:", path)

#Importar el archivo
datos = pandas.read_csv(r"C:\Users\jvmur\.cache\kagglehub\datasets\unsdsn\world-happiness\versions\2\2019.csv")

#Mostrar la informacion basica del archivo
print("\n----INFORMACION BASICA DEL DOCUMENTO----")
datos.info()
print("----FIN DE INFORMACION BASICA----\n ")
print("----MOSTRANDO FUNCION DESCRIBE----")
print(datos.describe(include='all'))
print("----FIN DE FUNCION DESCRIBE----\n")
print("----MOSTRANDO FUNCION SHAPE----")
print(datos.shape)
print("----FIN DE FUNCION SHAPE----\n")

#Comprobacion de datos nulos
if datos.isnull().values.any() :
    print(datos.isnull)
else :
    print("No hay datos nulos")

#Mostrar las primeras 10 filas de informacion
print("----MOSTRANDO LAS PRIMERAS 10 FILAS DE INFORMACION----\n ")
pandas.set_option('display.max_columns', None) 
print (datos.head(10))
print("----FIN DE LAS PRIMERAS 10 FILAS DE INFORMACION----\n")

#Identificacion de tipos de datos por columna
print("----MOSTRANDO LOS TIPOS DE DATOS----\n")
print(datos.dtypes)
print("----FIN DE LOS TIPOS DE DATOS----\n")

#Mostrar una visualizacion general
print("A CONTINUACION SE MOSTRARA UN GRAFICO SOBRE EL TOP 10 DE PAISES MAS FELICES DEL MUNDO 2019")
top10 = datos.sort_values(by='Score', ascending=False).head(10)
matplot.figure(figsize=(10,6))
matplot.bar(top10['Country or region'], top10['Score'], color='mediumseagreen')
matplot.xlabel("Score")
matplot.ylabel("País")
matplot.title("Top 10 países más felices en 2019")
matplot.tight_layout()
matplot.show()