import random
import os
import numpy

#CREAR ARCHIVO
arch=open("numeros_prueba.txt","w") 
#NUMEROS ALEATORIOS EN EL ARCHIVO
for i in range(0,20):
    numero = str(random.randint(100, 1000))
    arch.write(numero+"\n") 

#CIERRE ARCHIVO
arch.close() 

lista = []
#APERTURA ARCHIVO PARA LECTURA
with open("numeros_prueba.txt","r") as archivo:
    for linea in archivo:
        #AGREGAR NUMEROS A LA LISTA
        lista.append(int(linea))
#LISTA DE IMPARES
lista_impar = []
#VERIFICACION DE NUMEROS IMPARES
for j in range(0,20):
    if (lista[j] % 2 == 1):
        #SE AGREGAN LOS IMPARES A LA LISTA
        lista_impar.append(lista[j])
#LARGO DE LA LISTA DE IMPARES
largo = numpy.size(lista_impar)
print("Largo: "+str(largo))
for k in range(0,largo):
    lista_impar[k]


        