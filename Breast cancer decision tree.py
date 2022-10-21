#Importar librerias
import matplotlib.pyplot as plt
import graphviz
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
cancer_data = load_breast_cancer(return_X_y=True, as_frame=True)
#print(x.dtypes)
#print(cancer_data)
#df=pd.DataFrame(x,y.data,columns =[x,y.feature_names])
#df['target']=pd.Series(data=x,y.target,index=df.index)
#print(df)
#dataset = pd.read_csv(r"C:\Users\Jorge Salinas\PycharmProjects\progra\cancer.txt")
#dataset.info()
#display(dataset)
#dataset = dataset.drop(["id"], axis = 1)
#dataset = dataset.drop(["Unnamed: 32"], axis = 1)
#M = dataset[dataset.diagnosis == "M"]
#B = dataset[dataset.diagnosis == "B"]
#plt.title("Malignant vs Benign Tumor")
#plt.xlabel("Radius Mean")
#plt.ylabel("Texture Mean")
#plt.scatter(M.radius_mean, M.texture_mean, color = "red", label = "Malignant", alpha = 0.3)
#plt.scatter(B.radius_mean, B.texture_mean, color = "lime", label = "Benign", alpha = 0.3)
#plt.legend()
#plt.show()

#Revisar valores faltantes
#print(f'Hay {pd.concat([x,y], axis=1).isnull().sum().sum()} valores faltantes')
#print()
#print(f'Suma de tumores malignos: {y.value_counts()[0]}')
#print(f'Suma de tumores benignos: {y.value_counts()[1]}')
#ax = sns.countplot(y, label='Count')
#plt.show()

#Usar mapa de calor para observar la correlación entre valores
#plt.figure(figsize=(18,10))
#sns.heatmap(x.corr(), annot=True)
#plt.show()

#Deshacerse de los valores con una alta correlación
#drop_list = ['mean perimeter','mean radius','mean compactness','mean concave points','radius error','perimeter error','compactness error','concave points error','worst radius','worst perimeter','worst compactness','worst concave points','worst texture','worst area']
#x = x.drop(drop_list, axis=1)

#Dividir los datos en datos de entrenamiento y datos de prueba
cancer = load_breast_cancer()


#x_entrena, x_test, y_entrena, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
#print(f'La forma de los datos de entrenamiento es: {x_entrena.shape}')
#print(f'La forma de los datos de test es: {x_test.shape}')

#Crear una instancia para el algoritmo y conocer su porcentaje de acierto
#arbol = DecisionTreeClassifier(criterion = "gini")
#arbol.fit(x_test, y_test)
#arbol.fit(x_entrena, y_entrena)
#puntaje_test = arbol.score(x_test, y_test)
#puntaje_entrena = arbol.score(x_entrena, y_entrena)
#print("El porcentaje de acierto del modelo de entrenamiento es del {}%".format((round(puntaje_entrena*100, 2))))
#print("El porcentaje de acierto del modelo de prueba es del {}%".format((round(puntaje_test*100, 2))))

#Exportar el archivo para ver el árbol de decisiones
#export_graphviz(arbol, out_file="arbol.txt", class_names=["malignant", "benign"],feature_names=cancer.feature_names, impurity=False, filled=True)
#with open('arbol.txt', "w") as f:
#    f = export_graphviz(arbol, out_file=f)

#Convertir los datos a un dataframe
#df = pd.DataFrame(data=cancer['data'], columns = cancer['feature_names'])
#df.to_csv('cancer.txt', sep = ',', index = False)

#df=pd.DataFrame(cancer.data,columns =[cancer.feature_names])
#df['target']=pd.Series(data=cancer.target,index=df.index)
#x=pd.Series(df['target'].value_counts(ascending=True))
#x.index="malignant benign".split()
#X=df.iloc[0:,0:30]
#y=df['target']
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test=train_test_split(X,y,train_size=426,test_size=143,random_state=0)
#from sklearn.neighbors import KNeighborsClassifier
#model=KNeighborsClassifier(n_neighbors=1) #loading
#model.fit(X_train,y_train)  #training
#model.predict(X_test)
#model.score(X_test,y_test)



