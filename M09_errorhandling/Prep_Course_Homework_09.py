#!/usr/bin/env python
# coding: utf-8

# ## Manejo de errores

# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

# In[1]:



def moda(in_a):
    count_max=0
    visit=[]
    maxim=0
    result=[0,0]
    if type(in_a)==list:
        if len(in_a)==0:
            return None
        else:
            for x in in_a:
                if (type(x)==int) or (type(x)==float):
                    visit.append(False)
                else:
                    print("la lista solo debe contener numeros")
            index_a=0
            while index_a<len(in_a):
                x=in_a[index_a]
                a=in_a.count(x)
                index_a+=1
                if a > count_max:
                    count_max=a
                    maxim=x
                    result[0]=maxim
                    result[1]=count_max
            return result
    else :
        print("se espera una lista de numeros")
print("ejercicio 3 ")
z=[2,21,13,44,5,6,7,8,9,10,11,21,21]
print(moda(z))

# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

# In[5]:


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


# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# 
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

# In[9]:
import unittest 




# 4) Probar una creación incorrecta y visualizar la salida del "raise"

# In[13]:




# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

# In[14]:




# 7) Agregar casos de pruebas para el método conversion_grados()

# In[17]:




# 8) Agregar casos de pruebas para el método factorial()

# In[20]:




