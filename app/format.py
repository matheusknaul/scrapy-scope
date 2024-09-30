def formatar_resultado(lista_intervalo):
    resultado_formatado = []

    current_class = None
    current_start = None
    current_end = None

    for entry in lista_intervalo:
        classification, start, end = entry

        if classification != current_class:
            if current_class is not None:
                resultado_formatado.append([current_class, current_start, current_end])
            current_class = classification
            current_start = start
            current_end = end
        else:
            current_end =  end
    
    if current_class is not None:
        resultado_formatado.append([current_class, current_start, current_end])
    
    return resultado_formatado