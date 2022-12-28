def comp(array1, array2):


    # Caso de que una de las arrays esté vacia nos devuelva un False.
    if array1 is None or array2 is None:
        return False

    # Compara el valor de a con el de b^2, si ambos números coinciden elimina el de la array 2.
    # La idea es vaciar una de las dos arrays.
    for i in array1:
        for squared in array2:
            if i*i == squared:
                array2.remove(squared)
            continue
        
    # Si la array2 se queda vacia quiere decir que nos tiene que devolver un True pues todos los números de a están en b.
    # En caso contrario y queda la array2 con algún valor quiere decir que es false.
    if not array2:
        return True
    else:
        return False


