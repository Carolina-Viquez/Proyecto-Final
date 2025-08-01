# Entrega Inicial.
#DATASET REPORTE MUNDIAL DE LA FELICIDAD (World Happiness Report).

#Descripción: Análisis exploratorio del Reporte Mundial de la Fecilidad con enfoque en variables sociales, económicas y psicológicas.

#Justificación: el presente proyecto tiene como objetivo aplicar técnicas fundamentales de análisis de datos utilizando Python, tomando como base
el Reporte Mundial de la Felicidad. Desde una perspeciva académica y práctica, este proyecto permite desarrollar habilidades clave en la ciencia de 
datos, como la exploración de datos y visualización. 

##Ínteres en el caso de estudio.
Para el desarrollo de este proyecto, hemos seleccionado el dataset del **Reporte Mundial de la Felicidad** por su relevancia social, económica y política 
en el análisis del bienestar del ser humano. El cual proporcia datos comparativos sobre la felicidad persibida en más de 150 países. 

Este reporte combina indicadores interesantes económicos con variales sociales y psicológicos. Esta perspectiva multidimensional permite explorar como 
diversos factores interactuan para influir en la percepción subjetiva, lo cual es fundamental para el diseño de políticas  centradas en el desarrollo
humano sostenible. 

Este dataset ofrece la oportunidad de identificar patrones regionales, tendencias generacionales y correlacionaes entre variables que pueden enriquecer 
la comprensión de la felicidad como fenómeno social. En un conexto global marcado por desafíos económicos, sociales y ambientales, comprender los
determinantes de la felicidad resulta esencial para promover sociedades más equicativas y resilientes. 

#Análisis del Dataset. 

#Exploración:
##1.¿Qué variables tienen mayor correlación con el puntaje de felicidad?
**Objetivo:**
Identificar qué facores estan mas relacionados con el nivel de felicidad. 
**Análisis en python:**
-Matriz de correlacion (.coor())
-Mapa de calor con seaborn.heatmap()

##2. ¿Qué países tienen un nivel de felicidad más alto o más bajo de lo esperado según su PIB per capita?
**Objetivo:**
Evaluar si hay países que rompen la regla de que mas dinero = más felicidad.
**Analisis en python:**
-Modelo de regresíon lineal simple (scikit-learn)
-Visualizacion de residuos o dispersión (scatterplot)

##3.¿Cómo varía el puntaje de felicidad entre regiones del mundo?
**Objetivo:**
Comparar promedios de felicidad por regipon geográfica.
**Análisis en python:**
-Agrupación por región (groupby)
-Gráfico de barras comparativo (barplot)

# Hipótesis iniciales: 
1. **Hipotesis 1:** Los paises con mayor PIB per cápita tienen a tener un mayor puntaje de felicidad.
2. **Hipotesis 2:** El apoyo social y la libertad paa tomar decisiones personales tienen una correlación
mas fuerte con la felicidad que los factores económicos
3. **Hipotesis 3:**. Existen diferencias significativas en los niveles de felicidad entre regiones geográficas,
siendo Europa la región con los puntajes más altos.

#Visualizaciones planeadas.
1. **Matriz de correlación** entre todas las variables numericas para identificar relaciones significativas
2. **Gráfico debarras** del promedio de felicidad por región.
3. **Gráfico de dispersión con línea de regresión** entre PIB per capita y felicidad.
4. **Gráfica de residuos** para evaluar la precisión del mdelo de regresión.
5. **Gráfico de barras** de los países con mayor y menor felicidad respecto a lo predicho por el modelo.

#Metodología.
1. **Carga y limpieza de datos:** se utiliza ´pandas´para cargar el dataset y verificar valores nulos o inconsistencias.
2. **Análisis exploratorio:** se aplicarán estadísticas descriptivas y visualizaciones con ´matplotib´y ´seaborn´para entender la distribución de los datos.
3. **Correlación de variables:** se calculará la matriz de correlación para identificar qué factores están mas relacionados con la felicidad. 
4. **Agrupación por región:** se analizarán diferencias regionales mediante agrupaciones y promedios.
5. **Documentación:** todos los resultados se documentarán con gráficos para facilitar la interpretación. 



##Autores:
**Paula Alexandra Hernández Gutiérrez**
**Carolina Víquez**

**Referencia APA:**
Helliwell, J.F.,Layard, R, Sachs,J. D., De Neve, J.-E, Aknin, L. B, & Wang S. (Eds.).(2024).*Word Hapiness Report 2024*. Wellbeing Research Centre, University of Oxford. 
https://worldhappiness.report 

