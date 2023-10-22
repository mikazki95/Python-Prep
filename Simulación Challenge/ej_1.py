class Animal:
    # Tu código aquí
        def __init__(self, Especie, Color):
            if (type(Especie) == str) and (type(Color)== str):
                self.Especie = Especie
                self.Color = Color
                self.Edad=0
            else:
                print("para crear la clase solo se aceptan string de entrada")    

        def CumplirAnios(self):
            self.Edad+=1
            return self.Edad
