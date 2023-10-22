def ordenarPalabras(palabras):
    # Escribe aqui tu codigo:
    print(palabras)
    test_0= False
    aux_1=[]
    aux_3=[]
    index_1=0
    for xi in palabras:
        if xi == '-':
            test_0=True
            aux_2="".join(aux_1)
            aux_3.append(aux_2)
            print(aux_2)
            aux_1=[]
        else:
            aux_1.append(xi)
    aux_2="".join(aux_1)
    aux_3.append(aux_2)
    print(aux_2)
    aux_1=[]
    if test_0 :
        resul_tx="-".join(sorted(aux_3))
        print(resul_tx)
    else:
        return None
x="hola-como-estas"

ordenarPalabras(x)