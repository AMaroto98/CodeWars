# def array_diff(a, b):
    
#     result = []
    
#     if len(a) == 0:
        
#         return result
    
#     for i in a:
#         for j in b:
#             if i == j:
#                 a.remove(i)

#     return a


def array_diff(a, b):
    
    output = []
    
    for item in a:
        if item in b:
            pass
        else:
            output.append(item)
            
    return output
