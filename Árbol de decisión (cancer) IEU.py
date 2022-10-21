# arbol de desicion
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split
import graphviz
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import numpy as np

breastcancer = load_breast_cancer()

X_entrena, X_test, y_entrena, y_test = train_test_split(breastcancer.data, breastcancer.target)
arbol = DecisionTreeClassifier()
arbol.fit(X_entrena, y_entrena)
arbol.score(X_test, y_test)  # dio 0.947368
arbol.score(X_entrena, y_entrena)  # dio 1, lo que no es bueno
export_graphviz(arbol, out_file='arbol.txt', class_names=breastcancer.target_names,
                feature_names=breastcancer.feature_names, impurity=False, filled=True)

with open('arbol.txt', "w") as f:
    f = export_graphviz(arbol, out_file=f)

# grafico de barras
caract = breastcancer.data.shape[1]
plt.barh(range(caract), arbol.feature_importances_)
plt.yticks(np.arange(caract), breastcancer.feature_names)
plt.xlabel('Importancia de las características')
plt.ylabel('Características')
plt.show()

# niveles de desicion del arbol
arbol = DecisionTreeClassifier(max_depth=3)
arbol.fit(X_entrena, y_entrena)
arbol.score(X_test, y_test)  # 0.921052
arbol.score(X_entrena, y_entrena)  # 0732142.9

n_classes = 3
plot_colors = 'bry'
plot_step = 0.02

for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3],
                                [1, 2], [1, 3], [2, 3]]):
    X = breastcancer.data[:, pair]
    y = breastcancer.target

    # entrena algoritmo
    clf = DecisionTreeClassifier(max_depth=3).fit(X, y)
    plt.subplot(2, 3, pairidx + 1)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)

    plt.xlabel(breastcancer.feature_names[pair[0]])
    plt.ylabel(breastcancer.feature_names[pair[1]])
    plt.axis('tight')

    # plot puntos de entrenamiento
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        plt.scatter(X[idx, 0], X[idx, 1], c=color, label=breastcancer.target_names[i],
                    cmap=plt.cm.Paired)
    plt.axis('tight')

plt.suptitle('Ejemplos de clasificador de cáncer')

plt.legend()
plt.show()
