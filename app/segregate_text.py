

def searchElement(text, listAnalys):
    """_summary_
    Args:
        text (str): text that will be analyzed.
        listAnalys (_type_): _description_
    Returns:
        _type_: _description_
    """
    index = []
   
    results = []
    for element in listAnalys:
        match = []
        start = 0
        while True:
            start = text.find(element, start)
            if start == -1:
                break
            match.append(element)
            match.append(start)
            start += len(element)
            index.append(match)
            print(index)
    
    indices = sorted(index, key=lambda x: x[1])

    i = 0
    while i < len(indices):
        if i == len(indices) - 1:
            results.append(text[indices[i][1]:])
        else:
            results.append(text[indices[i][1]:indices[i+1][1]])
        i += 1

    return results