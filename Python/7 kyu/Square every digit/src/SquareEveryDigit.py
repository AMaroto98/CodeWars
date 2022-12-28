def square_digits(number):

    numberList = list(map(int, str(number)))
    
    squareList = []

    for element in numberList:

       squareList.append(element ** 2)
    
    result = ''.join(map(str,squareList))

    return int(result)
