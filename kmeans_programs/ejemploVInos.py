import numpy as np #calculos cientificos
import pandas as pd #Analisis de datos
import matplotlib.pyplot as plt #Creacion de graficos
import openpyxl #nos ayuda convertir los datos a excel
from sklearn.cluster import KMeans #para realizar el clustering de K-Means adquirimos la informacion de sklearn
from sklearn.decomposition import PCA #nos ayudara a utilizar la tecnica de analisis de componentes principales
#from sklearn import metrics 


vinos = pd.read_csv("csv/caracteristicas de vinos.csv", engine="python")  #Leemos el archivo csv y le decimos que lo compile en motor python
"""Las variables tienen que ser numericas para realizar el clustering"""
vinos.info() #Nos otorga la informacion de los datos csv
print(vinos.head()) #nos mostrara la informacion de las variables

vinos_variables = vinos.drop(["Vino"], axis=1) #quinamos la varible vino de el csv, parametro axis=1 indica que es una columna completa

vinos_variables.describe()

#Como algunos datos no tienen sus valores normalizados
#se procede a generar una conversion para que se encuentren desde el mismo rango

vinos_norm = (vinos_variables-vinos_variables.min())/(vinos_variables.max()-vinos_variables.min())
#vinos_norm
vinos_norm.describe()

#Como no sabemos la cantidad de cluster optimas a crear, realizamos el algoritmos de
#codo de jambu

#wcss es un indicador de que tan similares son los individuos dentro de los clusters
wcss = []  #creamos una lista para el code de jambu y ver la reaccion de clusters añadidos
#el codo de jambu sirve para ver el comportamiento de los datos unos con otros a traves de clusters
#mientras similares sean los datos mas distintos seran los cluster para un analisis visual
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, max_iter=300)#indicamos la cantidad de clusters a realizar y cuantas iteraciones para el kmeans
    kmeans.fit(vinos_norm) #Se aplica Kmeans a la base de datos
    wcss.append(kmeans.inertia_)#para obtener el valor de inercia el cual nos muestra el comportamiento optimo de los datos, se obtiene a partir de inertia_

plt.plot(range(1,11), wcss)# (x, y)
plt.title("codo de jambu")
plt.xlabel("numero de clusters")
plt.ylabel("WCSS") 
plt.show()

#para obtener el valor de clusters optimos a formar es a partir de la grafica.
#cuando los wcss dejen de bajar drasticamente es el punto optimo de cluster
#en la grafica se puede analizar que el punto donde deja de disminuir drasticamente es en 3, por ende los cluster optimos son 3

#Entrenamos el sistema con la cantidad de clusters optimos
clustering = KMeans(n_clusters=3, max_iter=300)
clustering.fit(vinos_norm)

vinos["KMeans_Clusters"] =  clustering.labels_ #los resultados del clustering se guardan en labels_ dentro del modelo
vinos.head()

#para darnos una idea de manera grafica de como quedaron formados los clusters y debido a que tenemos 13 caracteristicas y no es posible
#hacer un grafico que las represente a todas, se utiliza la tecnica de analisis de componentes pricipales
#Por sus siglas es PCA
#el cual reduce la cantidad de variables a analizar, en este caso a visualizar, creando una cantidad menor de nuevas variables
# que representen lo mejor posible a las variables originales


#teniendo en cuenta que el grafico sera en 2 dimensiones, le pedimos al PCA que sean 2 componentes
pca = PCA(n_components=2)
pca_vinos = pca.fit_transform(vinos_norm)
pca_vinos_df = pd.DataFrame(data=pca_vinos, columns=["componente_1", "componente_2"])
pca_nombres_vinos = pd.concat([pca_vinos_df, vinos[["KMeans_Clusters"]]], axis =1) #unimos una nueva columna con axis=1

pca_nombres_vinos

#graficamos los vinos por medio de los dos componentes principales coloreandolos segun el cluster que pertenecen

fig = plt.figure(figsize=(6,6)) #creamos una figura de tamaño 6x6

ax = fig.add_subplot(1,1,1) #con (1,1,1 ) indicamos que vamos a crear solo un grafico dentro de la figura

ax.set_xlabel("componente 1", fontsize=15)
ax.set_ylabel("componente 2", fontsize=15)
ax.set_title("Componentes principales", fontsize=20)

color_theme = np.array(["blue", "green", "orange"]) #indicamos los colores que deseamos 
ax.scatter(x=pca_nombres_vinos.componente_1, y=pca_nombres_vinos.componente_2,
            c=color_theme[pca_nombres_vinos.KMeans_Clusters], s=50)

plt.show()

vinos.to_csv("pruebaCategoriaVinos.csv")
#vinos.to_excel("pandasExcelPrueba.xlsx", "Sheet1")


