"""
Prediccion de nota segun el estudio

"""
#Datos de ejemplo
horas = int(input("Cuantas horas vas a estudiar:?"))

#Regla creada por nosotros
nota = horas * 2 + 5

#Limitar la nota maxima 20
if nota >20:
    nota = 20

print(f"Horas estudiante {horas}")   
print(f"Nota Aproximada {nota}") 
