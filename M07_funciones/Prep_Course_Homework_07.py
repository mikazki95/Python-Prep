#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:

def ver_prim(in_1):
    es_primo = True
    for i in range(2, in_1):
        if in_1 % i == 0:
            es_primo = False
            break
    return es_primo



# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
def primo_array(in_2):
    a=[]
    for x in in_2:
        if (ver_prim(int(x))==True):# en sentencias de v/f se puede obviar el verdadero
            a.append(x)
    return a

z=[1,2,3,4,5,6,7,8,9,10,11]
print(primo_array(z))

# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:

def moda(in_a):
    rep=[]
    visit=[False]
    if len(in_a)==0:
        return None
    for x in in_a:
        for y in in_a:
            print("x es:",x, "y es: ",y)
print("ejercicio 3 ")
z=[1,2,3,4,5,6,7,8,9,10,11]
print(moda(z))

# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:



# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:




# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:




