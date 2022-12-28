def descending_order(numbers):
   
    numbersList = list(map(int,str(numbers)))

    orderedNumbers = sorted(numbersList, reverse = True)

    result = ''.join(map(str, orderedNumbers))

    return int(result)


# Solución mucho más clara

def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)
