#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:
#class Veiculo:
#   def __init__(self,color,tipo,cc):
#        self.color=color
#        self.tipo=tipo
#        self.cc=cc
        



# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:
class Veiculo_1:
    def __init__(self,color,tipo,cc):
        self.color=color
        self.tipo=tipo
        self.cc=cc
        self.velocidad=0
        self.direccion=0

    def acelerar (self,acelerar):
        self.velocidad += acelerar

    def frenar (self,desacelerar):
        self.velocidad -= desacelerar

    def doblar (self,direccion):
        self.direccion += direccion
    
    def estado (self):
        return print("la velocidad actual es: ", self.velocidad, "y su direccion es: ", self.direccion)
    
    def descripcion (self):
        return print("es un veiculo del tipo: ",self.tipo, " de color: ",self.color,"con motor de: ", self.cc)





# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:
gs310=Veiculo_1("negro","moto",310)
f150=Veiculo_1("negro","camioneta pickup",1100)
vracer=Veiculo_1("roja","moto",250)



# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:


gs310.acelerar(30)
f150.acelerar(10)
vracer.acelerar(20)

gs310.doblar(5)
f150.doblar(-5)
vracer.doblar(2)



# In[13]:

gs310.estado()
gs310.descripcion()

f150.estado()
f150.descripcion()

vracer.estado()
vracer.descripcion()

# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:



# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:





# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:




# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:




