# No modifiques nada por fuera del cuerpo de la función.

def stringEspejo(texto):
    # Escribe tu codigo aqui:
    tx_esp=[]
    tx_in=[]
    if len(texto)<=3:
        return None
    for x in texto:
        tx_in.append(x)
    for y in range(len(tx_in),0,-1):
        tx_esp.append(tx_in[y-1])
    #print(tx_esp)
    res="".join(tx_esp)
    return res