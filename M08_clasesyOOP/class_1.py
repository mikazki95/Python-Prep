class Gato:
    def __init__(self, nombre, edad,raza, sexo):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.sexo = sexo
    def presentar(self): #siempre las funciones empiezan con self, aun no se porque 
        return print("mi nombere es ",self.nombre," tengo ", self.edad, "raza",self.raza,"sexo",self.sexo)     
    #ss