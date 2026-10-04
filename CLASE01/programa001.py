"""
uso de variables y tipo de datos
primitivas
"""
nombre = "Jorge"  #str
edad = 28 #int
peso = 1.79 #float
estado = True #bool 

"""
Funciones principales
=========================
nombre = input("Cual es tu nombre?:")
apellido = input("Cual es tu apellido:?")
edad = input("Y Cual es tu edad")
print(f"Hola {nombre} {apellido} tiene {edad} años un gusto tenerte por aca")
"""

"""
Condicionales
"""

precio = 1200
cantidad = int(input("Ingrese la cantidad del producto:"))
subtotal = precio * cantidad
print(f"El Total a pagar es {round(subtotal,2)}")
#Y el total es mayor a 1000 tiene un descuento del 0.05
#>,<,>=,<=,<>,not,!= operadores de comparacion logicos
#AND y OR o
if subtotal>=200 and subtotal<=500 :
    descuento = subtotal * 0.05
elif subtotal>=501 and subtotal<=699:
    descuento = subtotal * 0.06
elif subtotal>700:
    descuento = subtotal * 0.07    
else:
    descuento = 0   
total =subtotal - descuento
print(f"El Total que se debe pagar es {round(total,2)}")     
