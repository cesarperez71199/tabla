# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:49:17 2023

@author: Cesar Perez
"""

#Programa que crea una tabla de jugadores ingresando sus caracteristicas

nombre=[""]
renglon= [5]
columna=[10]
tabla=[]

for i in range(len(renglon)):
    for k in range(columna):
        nombre[0]=input("Dame el nombre: ")
        
    for j in range(columna):
        edad=input("Dame la edad: ")
        
        if edad <=18 :
            print("Menor")
            
        else:
            print("Dato guardado")
            
    
    for m in range(columna):
        altura= int(input("Dame la altura en cm: "))
        
        if altura <=180 :
            print("Muy bajo")
            
        else:
            print("Dato guardado")
            
     
    for n in range(columna):
        peso= float(input("Dame el peso: "))
        
        if peso <=50 :
            print("Bajo de peso")
            
        else:
            print("Dato guardado")
            
    
    for p in range(columna):
        print("Posicion: P=1, D=2, M=3, D=4")
        posicion=int(input("Dame la posicion con : "))
        
        if posicion !=2 :
            print("Posicion no disponible")
            
        else:
            print("Dato guardado")
            
            
            
                   
