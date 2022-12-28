def repeats(array):
    
    # Establecemos variable donde pondremos el resultado final
    result = 0
    
    # Creamos bucle for 
    for number in array:
        
        # count() cuenta el número de veces que hay en la array el valor number, si es 1 quiere decir que no está repetido
        # por lo tanto lo tiene que sumas a result
        if array.count(number) == 1:
            
             result += number
            
    return result
   