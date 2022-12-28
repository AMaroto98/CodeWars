from collections import Counter

def duplicate_encode(word):
    
    # Primero pasamos todo a minúsculas pues el enunciado dice que debenmos ignorar las mayúsculas
    word = word.lower()
    
    # Introducimos todas las palabras en una lista para tenerlas por separado
    word = list(word)
    
    # Contamos las palabras para que nos diga si hay alguna letra repetida
    count = Counter(word)
    
    # Declaramos una variable vacia en la que posteriormente asignaremos el resultado
    result = ""
    
    # Bucle que va a pintar el resultado final
    
    for letter in word:
    
        if count[letter] == 1:

            result += "("
        else:
            result += ")"
            
    return result