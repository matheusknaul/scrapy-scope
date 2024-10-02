def __build__(lista_resultado):
    lista_resultado_new = []
    
    for i in range(len(lista_resultado)):
        print(len(lista_resultado))
        if i + 1 >= len(lista_resultado):
            resultado = [lista_resultado[i+1][0], [lista_resultado[i][1][0], 'teste']]
            lista_resultado_new.append(resultado)
            break
        resultado = [lista_resultado[i][0], [lista_resultado[i][1][0], lista_resultado[i+1][1][0]]]
        print(i)
        lista_resultado_new.append(resultado)
    
    return lista_resultado_new

def criar_texto(flag, comeco_intervalo, fim_intervalo, text):
    return [flag, text[comeco_intervalo:fim_intervalo]]