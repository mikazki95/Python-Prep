
def ciudadesPoblacion(ciudades):
    # Tu código aquí
    ciudades_B={}
    result_B=[]
    for x in ciudades:
        y= False
        z= False
        y=x.startswith("B", 0, 1)
        z=x.startswith("b", 0, 1)
        if (z== True) or (y == True):
            ciudades_B[x]=ciudades[x]
            result_B.append([x,ciudades[x]])
    promedio = 0 
    for index_cd_b in ciudades_B:
        #print(index_cd_b,': ',ciudades_B[index_cd_b])
        if type(ciudades_B[index_cd_b])== int:
            promedio+=ciudades_B[index_cd_b]
        else:
            promedio=0
            return print("el valor ingresado no es entero")
    if len(ciudades_B)>0:
        promedio=promedio/ len(ciudades_B)
        result_B.append(['promedio',promedio])
    else:
        ciudades_B={}
    #print("promedio: ", promedio/ len(ciudades_B))

    return result_B