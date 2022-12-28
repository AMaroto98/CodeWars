def solution(number):
      
    divs = []
    
    for i in range(1, number):
        if (i % 3 == 0) and (i % 5 == 0):
            divs.append(i)
        elif (i % 3 == 0) or (i % 5 == 0):
            divs.append(i)
    
    return sum(divs)