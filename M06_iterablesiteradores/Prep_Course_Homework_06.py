#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
x=-15
a=[]
while (x < 0):
    a.append(x)
    x+=1
print(a)

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:

x=0
while(x<len(a)):
    if(a[x]%2==0):
        print(a[x])
    x+=1

# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:
print("ciclo for")
for x in a:
    if(a[x]%2==0):
        print(a[x])

# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
print("ejercicio 4: ")
# In[7]:
for x in a[0:3]:
    print(a[x])

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
print("ejercicio 5: ")
for x in enumerate(a):
    print(x)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
print("ejercicio 6: ")
b = [1,2,5,7,8,10,13,14,15,17,20]
x=1
while (x < b[len(b)-1]):
    if (x != b[x-1]):
        b.insert(x-1,x)
    x+=1
print(b)


# In[11]:


n = 1


# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
c=[0,1]
print("ejercicio 7: ")
for x in range (28):
    k=c[len(c)-1]+c[len(c)-2]
    c.append(k)
print(c)




# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

print("ejercicio 8: ")
print(sum(c))


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:
print("ejercicio 9: ")
x=0
while x <5:
    print(c[len(c)-1-x]/c[len(c)-2-x])
    x+=1




# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:
print("ejercicio 10: ")
cadena ='Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i, x in enumerate(cadena): #como la funcion enumerate devuelve 1 X 2 se consignan 
                                #dos indices y luego se decide que indice se va a evaluar
    if x == 'n':
        print(i)



# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:
print("ejercicio 11: ")
dir_1={ 'calss_1':[1,2,3],
       'class_2' : [4,5,6],
       'class_3' : [7,8,9]}
for x in dir_1:
    print(x)




# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:
print("ejercicio 12: ")
list_1=list(cadena)
int_1=iter(list_1)
for x in list_1:
    print(next(int_1))



# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip
print("ejercicio 13: ")
# In[48]:
f=[1,2,3,4,5,6]
g=[7,8,9,10,11,15]
h=tuple(zip(f,g))
print(type(h))
print(h)





# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
print("ejercicio 14: ")
# In[49]:
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
list_2=[]
for x in lis:
    if (x%7==0):
        list_2.append(x)
print(list_2)

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:
print("ejercicio 15: ")
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
z=0
for x in lis:
    if (type(x)==list):
        z=z+len(x)
    else:
        z+=1
print(z)



# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:
print("ejercicio 16: ")
for x in lis:
    if (type(x) != list):
        x=list(x)
    print(type(x))
print(lis)
