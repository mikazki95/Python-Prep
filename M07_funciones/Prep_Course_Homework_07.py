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

def con_temp (dato,data_in,data_out):
    error="error de tipo de dato, espesifique con: 'k' para kelvin, 'c' para celcius o 'f' para farenheit"
    if ((type(dato)==int)or(type(dato)==float)and(type(data_in)==str)and(type(data_out)==str)):
        match data_in:
            case 'k':
                if data_out=='f':
                    return (1.8*(dato-273)+32)
                elif data_out=='c':
                    return (dato-273.15)
                else:
                    return error
            case 'c':
                if data_out=='f':
                    return ((dato*9/5)+32)
                elif data_out=='k':
                    return (dato+273.15)
                else:
                    return error
            case 'f':
                if data_out=='c':
                    return ((dato-32)*5/9)
                elif data_out=='k':
                    return (273+(dato-32)/1.8)
                else:
                    return error
            case _:
                return error
    else:
        return error
print("ejercicio 4 ")
print(con_temp(147,'f','k'))
# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:
temp_in=[[25,'c'],[300,'k'],[87,'f']]
for x in temp_in:
    out_0='c'
    for y in range(0,2,1):
        if x[1]=='c':
            if y == 0:
                out_0='f'
            else:
                out_0='k'
        elif x[1]=='k':
            if y == 0:
                out_0='f'
            else:
                out_0='c'
        elif x[1]=='f':
            if y == 0:
                out_0='k'
            else:
                out_0='c'
        print("la convercion de °",x[1]," a °",out_0," es: ",con_temp(x[0],x[1],out_0)," °",out_0)



# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def fu_fac(data):
    out = 1
    error="esta funcion solo admite enteros positivos mayores a 0 "
    if (type(data)==int ) and (data > 0 ):
        for x in range(1,data+1,1):
            out=out*x
        return out
    else:
        return error
print(" ejercicio 6: ")
print(fu_fac(4))


