def to_camel_case(text):
    
    # Establecemos condición por la que si no hay texto devuelva nada.
    
    if len(text) == 0:
        
        return text
    
    # Ahora cambiabamos todas las _ por - para poder hacer split de manera más cómoda.
    
    text = text.replace("_","-")
    textSplitted = text.split("-")
    
    for i in range(len(textSplitted)):

        if i == 0:
            continue
        else:
            textSplitted[i] = textSplitted[i].capitalize()
            
        result = textSplitted[0] + ''.join(i.capitalize() for i in textSplitted[1:])
        
        return result


