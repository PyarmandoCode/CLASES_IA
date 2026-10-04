from sklearn.linear_model import LinearRegression

#Datos de entrenamiento
horas = [[1], [2], [3], [4], [5], [6]]
notas = [8, 10, 12, 14, 16, 18]

#Crear el Modelo
modelo = LinearRegression()

#Entrenar
modelo.fit(horas,notas)

#Hacer un prediccion
resultado = modelo.predict([[7]])

print("Horas estudiadas:7")
print("Nota Aproximada",resultado[0])