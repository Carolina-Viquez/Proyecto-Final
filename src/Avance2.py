import pandas
import matplotlib.pyplot as matplot
import plotly.express as px
import kagglehub
import os

# Diccionario para estandarizar columnas
nombres_validos = {
    # Nombre país
    'Country': 'Country or region',
    'Country name': 'Country or region',
    'Country or region': 'Country or region',
    # Score
    'Happiness Score': 'Score',
    'Happiness.Score': 'Score',
    'Ladder score': 'Score',
    'Score': 'Score',
    # Rank, PIB, etc. completos si los necesitas
    'Happiness.Rank': 'Overall rank',
    'Overall rank': 'Overall rank',
    'Economy (GDP per Capita)': 'GDP per capita',
    'Logged GDP per capita': 'GDP per capita',
    'GDP per capita': 'GDP per capita',
    'Health (Life Expectancy)': 'Healthy life expectancy',
    'Healthy life expectancy': 'Healthy life expectancy',
    'Trust (Government Corruption)': 'Perceptions of corruption',
    'Perceptions of corruption': 'Perceptions of corruption',
    'Freedom to make life choices': 'Freedom to make life choices',
    'Social support': 'Social support',
    'Generosity': 'Generosity'
}

class AnalisisFelicidad:
    def __init__(self, datos_por_año: dict):
        self.datos_por_año = datos_por_año

    def mostrar_info(self, año):
        datos = self.datos_por_año[año]
        print(f"\n---- INFORMÁCIÓn Básica del documento ({año}) ----")
        datos.info()
        print("----FIN DE INFORMACION BASICA----\n")
        print("\n--- MOSTRANDO FUNCION DESCRIBE ---")
        print(datos.describe(include='all'))
        print("----FIN DE FUNCION DESCRIBE----\n")
        print("\n--- MOSTRANDO FUNCION SHAPE ---")
        print(datos.shape)
        print("----FIN DE FUNCION SHAPE----\n")
        if datos.isnull().values.any():
            print("\nDatos nulos encontrados:\n", datos.isnull().sum())
        else:
            print("\nNo hay datos nulos.")
        print("\n--- MOSTRANDO LAS PRIMERAS 10 FILAS DE INFORMACION ---")
        pandas.set_option('display.max_columns', None)
        print(datos.head(10))
        print("----FIN DE LAS PRIMERAS 10 FILAS DE INFORMACION----\n")
        print("\n--- MOSTRANDO LOS TIPOS DE DATOS ---")
        print(datos.dtypes)
        print("----FIN DE LOS TIPOS DE DATOS----\n")
        print("---A CONTINUACION SE DESPLEGARAN 5 GRAFICOS CON INFORMACION DE ANALISIS DE DATOS---\n")

class VisualizacionFelicidad(AnalisisFelicidad):
    def grafico_barras_2019(self):
        datos = self.datos_por_año[2019]
        top10 = datos.sort_values(by='Score', ascending=False).head(10)
        matplot.figure(figsize=(12, 7))
        matplot.style.use('ggplot')
        matplot.bar(top10['Country or region'], top10['Score'], color='orchid')
        matplot.xlabel("País"); matplot.ylabel("Score"); matplot.title("Top 10 países más felices (2019)")
        matplot.xticks(rotation=45, ha='right')
        for bar in matplot.gca().patches:
            y = bar.get_height()
            matplot.text(bar.get_x() + bar.get_width()/2, y + 0.03, f"{y:.2f}", ha='center')
        for spine in ['top','right']:
            matplot.gca().spines[spine].set_visible(False)
        matplot.tight_layout()
        matplot.show()

    def grafico_lineas_tendencia_top_paises(self, top_n=5):
        top_paises = self.datos_por_año[2019].sort_values(by='Score', ascending=False).head(top_n)['Country or region']
        matplot.figure(figsize=(12, 7))

        for pais in top_paises:
            años, scores = [], []
            for año, df in self.datos_por_año.items():
                if 'Country or region' in df.columns and 'Score' in df.columns:
                    if pais in df['Country or region'].values:
                        años.append(int(año))  # Convertimos año a int para evitar el .0
                        scores.append(float(df[df['Country or region'] == pais]['Score'].values[0]))

            matplot.plot(años, scores, marker='o', label=pais)

        matplot.title(f"Tendencia (Top {top_n} países de 2015-2019)")
        matplot.xlabel("Año")
        matplot.ylabel("Score")
        matplot.xticks(ticks=sorted(self.datos_por_año.keys()))  # Asegura ticks limpios
        matplot.legend(title="País")
        matplot.grid(True)
        matplot.tight_layout()
        matplot.show()

    def grafico_dispersion(self, año):
        df = self.datos_por_año[año]
        matplot.figure(figsize=(8, 6))
        matplot.scatter(df['GDP per capita'], df['Score'], color='orchid')
        matplot.title(f"PIB vs Felicidad ({año})")
        matplot.xlabel("GDP per capita"); matplot.ylabel("Score")
        matplot.grid(True); matplot.tight_layout(); matplot.show()

    def histograma_distribucion(self, año):
        df = self.datos_por_año[año]
        matplot.figure(figsize=(8, 6))
        matplot.hist(df['Score'], bins=20, color='orchid', edgecolor='black')
        matplot.title(f"Distribución del Score ({año})")
        matplot.xlabel("Score"); matplot.ylabel("Frecuencia")
        matplot.grid(True); matplot.tight_layout(); matplot.show()

    def mapa_geografico(self, año):
        df = self.datos_por_año[año]
        fig = px.choropleth(df, locations='Country or region', locationmode='country names',
                            color='Score', color_continuous_scale="Viridis",
                            title=f"Mapa de Felicidad {año}")
        fig.show()

# Descargar el dataset 
path = kagglehub.dataset_download("unsdsn/world-happiness")
print("Dataset descargado en:", path)

datos_por_año = {}

for root, _, files in os.walk(path):
    for file in files:
        if file.endswith(".csv"):
            for año in range(2015, 2020):
                if file.startswith(str(año)):
                    full = os.path.join(root, file)
                    df = pandas.read_csv(full)
                    rename_map = {c: nombres_validos[c] for c in df.columns if c in nombres_validos}
                    df = df.rename(columns=rename_map)
                    df['Year'] = año
                    datos_por_año[año] = df
                    break


visualizador = VisualizacionFelicidad(datos_por_año)

visualizador.mostrar_info(2019)
visualizador.grafico_barras_2019()
visualizador.grafico_lineas_tendencia_top_paises(top_n=5)
visualizador.grafico_dispersion(2019)
visualizador.histograma_distribucion(2019)
visualizador.mapa_geografico(2019)
