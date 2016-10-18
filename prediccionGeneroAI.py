#Este primer ejemplo determinara por las medidas que se le brinden
#El genero de la persona.
from sklearn import tree  #Con esto importamos "Decision tree"
#[Alto, peso, tamano de pie]
x = [[181,80,40], [177,70,43], [160,60,38], [154,54,37],
[166,65,40], [190,90,47], [175,64,39], [177,70,40], [159,55,37],
[171,75,42], [181,85,43]]
#Genero aplicado a cada array de x
y = ["male","female","female","female","male","male","male",
"female","male","female","male"]
#Llamamos metdo de clasficacion del objeto tree y lo guardamos en una variable
clf = tree.DecisionTreeClassifier()
#Llenamos el arbol con las variables previamente declaradas
clf = clf.fit(x,y)
#Ahora que tenemos el arbol de prediccion lleno, procedemos a ingresar datos
#Que querramos que sean predichos.
prediccion = clf.predict([[190,70,43]])
print(prediccion)
