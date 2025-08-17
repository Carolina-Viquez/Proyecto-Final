## DATASET: REPORTE MUNDIAL DE LA FELICIDAD (World Happiness Report).
Kaggle - World Happiness Report

# Descripción: Análisis exploratorio del Reporte Mundial de la Fecilidad. 

# Justificación: 

El presente proyecto tiene como objetivo aplicar técnicas fundamentales de análisis de datos utilizando Python, tomando como base el Reporte Mundial de la Felicidad. Desde una perspeciva académica y práctica, este proyecto permite desarrollar habilidades clave en la ciencia de datos, como la exploración de datos y visualización. 

# Ínteres en el caso de estudio:

Para el desarrollo de este proyecto, hemos seleccionado el dataset del **Reporte Mundial de la Felicidad** por su relevancia social, económica y política 
en el análisis del bienestar del ser humano. El cual proporcia datos comparativos sobre la felicidad persibida en más de 150 países. 
Combina indicadores interesantes con variables económicos, sociales y psicológicos, lo que permite exploración multidimensional de cómo diversos factores interactuan para influir en la percepción subjetiva del bienestar. Esta información es clave para el diseño de políticas centradas en el desarrollo humano sostenible. 
Este dataset ofrece la oportunidad de identificar patrones regionales, tendencias generacionales y correlacionales entre variables que enriquecen la comprensión de la felicidad como fenómeno social. En un conexto global marcado por desafíos económicos, sociales y ambientales, comprender los determinantes de la felicidad resulta esencial para promover sociedades más equicativas y resilientes. 

### Análisis del Dataset: exploración. 

# 🛠️ Herramientas Utilizadas:
- `pandas` para manipulación de datos.
- `matplotlib` y `plotly` para visualización.
- `os` y `kagglehub` para descarga y lectura de archivos.

## 📊 Visualizaciones Generadas:

### 1. `grafico_barras_2019()`
- Muestra los 10 países más felices en 2019 usando un gráfico de barras.
- Ordena los datos por `Score` y utiliza `matplotlib` para graficar.
- Añade etiquetas con el valor de felicidad encima de cada barra.
- Mejora la estética ocultando los bordes superiores y derechos.

### 2. `grafico_lineas_tendencia_top_paises(top_n=5)`
- Muestra la evolución del `Score` de los países más felices entre 2015 y 2019.
- Identifica los países más felices en 2019 y grafica su tendencia a lo largo de los años.

### 3. `grafico_dispersion(año)`
- Visualiza la relación entre el PIB per cápita (`GDP per capita`) y el `Score` de felicidad.
- Utiliza un gráfico de dispersión para observar correlaciones.

### 4. `histograma_distribucion(año)`
- Muestra cómo se distribuyen los valores de felicidad (`Score`) en un año específico.
- Utiliza un histograma con 20 bins para agrupar los países según su nivel de felicidad.

### 5. `mapa_geografico(año)`
- Muestra un mapa mundial con los niveles de felicidad por país.
- Utiliza `plotly.express` para crear un mapa coroplético con escala de colores continua.

---

## 📁 Carga y procesamiento de datos

Los datos se descargan desde Kaggle usando `kagglehub`, y se procesan de la siguiente manera:
- Se recorren los archivos `.csv` por año (2015 a 2019).
- Se renombra las columnas usando el diccionario `nombres_validos`.
- Se guarda cada DataFrame en el diccionario `datos_por_año`.

---

## 🧪 Ejecución del análisis

Se crea una instancia de la clase y se ejecutan los métodos para mostrar información y generar los gráficos:
- `mostrar_info(2019)`
- `grafico_barras_2019()`
- `grafico_lineas_tendencia_top_paises(top_n=5)`
- `grafico_dispersion(2019)`
- `histograma_distribucion(2019)`
- `mapa_geografico(2019)`

## Ejecusión de gráficos.

### 1. Gráfico de Barras – Top 10 países más felices (2019)
Este gráfico muestra los 10 países con mayor puntuación de felicidad en el año 2019. Se utiliza `matplotlib` para representar la variable `Score` en función del país. El gráfico permite identificar rápidamente qué países lideran el ranking de felicidad.

**Objetivo**: Identificar los países líderes en felicidad en el último año del análisis.
**Comentario**: Los países nórdicos como Finlandia, Dinamarca y Noruega dominan el ranking, lo que sugiere una fuerte correlación entre políticas sociales y bienestar.

---

### 2. Gráfico de Líneas – Tendencia de felicidad (2015–2019)
Se representa la evolución del `Score` de los 5 países más felices en 2019 a lo largo de los años. Este gráfico permite observar si la felicidad se ha mantenido estable, ha aumentado o disminuido.

**Objetivo**: Analizar la consistencia en la felicidad de los países más destacados.
**Comentario**: La mayoría de los países del top 5 muestran una tendencia estable o ligeramente ascendente, lo que indica consistencia en sus políticas de bienestar.

---

### 3. Gráfico de Dispersión – PIB vs Felicidad (2019)
Este gráfico muestra la relación entre el PIB per cápita (`GDP per capita`) y el `Score` de felicidad. Se utiliza `matplotlib.scatter` para visualizar la correlación entre riqueza económica y bienestar.

**Objetivo**: Explorar la influencia del desarrollo económico en la percepción de felicidad.
**Comentario**: Existe una correlación positiva, aunque no perfecta, entre el PIB y la felicidad. Algunos países con alto PIB no necesariamente tienen altos niveles de felicidad.

---

### 4. Histograma – Distribución del Score (2019)
Se analiza la distribución de la puntuación de felicidad entre todos los países en 2019. El histograma permite identificar la concentración de países en rangos específicos de felicidad.

**Objetivo**: Comprender la dispersión y concentración de la felicidad entre países.
**Comentario**: La mayoría de los países se agrupan en puntuaciones medias, lo que sugiere que la felicidad global está lejos de los extremos.

---

### 5. Mapa Geográfico – Felicidad Mundial (2019)
Se utiliza `plotly.express` para generar un mapa coroplético que muestra la puntuación de felicidad por país. Este gráfico permite una visualización global del bienestar.

**Objetivo**: Visualizar geográficamente la distribución global de la felicidad.
**Comentario**: Se observan patrones regionales claros, con América Latina y África mostrando puntuaciones más bajas en comparación con Europa y Oceanía.


## 📌 Conclusiones

- Los países más felices tienden a tener altos niveles de PIB, apoyo social, esperanza de vida saludable y baja corrupción.
- La felicidad es una métrica multidimensional que no depende exclusivamente de la riqueza económica.
- Las políticas públicas enfocadas en salud, educación y equidad social tienen un impacto directo en el bienestar de la población.

## 💡 Insights Relevantes

- **Países nórdicos** lideran consistentemente los rankings de felicidad.
- **PIB alto ≠ felicidad garantizada**: países como EE.UU. tienen alto PIB pero no lideran el ranking.
- **Estabilidad en el tiempo**: los países más felices mantienen sus posiciones a lo largo de los años.
- **Visualización geográfica**: permite identificar regiones con desafíos estructurales en bienestar.



## Autores:
- **Paula Alexandra Hernández Gutiérrez**
- **Carolina Víquez Murillo**


**Referencia APA:**
Helliwell, J.F.,Layard, R, Sachs,J. D., De Neve, J.-E, Aknin, L. B, & Wang S. (Eds.).(2024).*Word Hapiness Report 2024*. Wellbeing Research Centre, University of Oxford. 
https://worldhappiness.report 

## Imagenes del codigo funcionando:

<p align="center">
  <img src=<img width="1397" height="848" alt="image" src="https://github.com/user-attachments/assets/48a6bca1-4ba1-4205-aa85-a1825eff98ec" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/314e85c4-2b89-476c-a698-4ad38e31bc30" alt="image" width="500"/>
</p>

