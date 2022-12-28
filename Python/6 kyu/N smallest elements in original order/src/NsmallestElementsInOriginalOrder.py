# import heapq

def first_n_smallest(array, number):

#     smallestArray = heapq.nsmallest(number,array)
#     result = []

#     if number <= 0:

#         return result

#     for value in array:
#         for smallestValue in smallestArray:
#             if value != smallestValue:
#                 continue
#             else:
#                 result += [value]
#                 break
#         if len(result) == number:
#             break
#         continue
#     return result


# Solución buena

    result = []
    arraySort = sorted(array)
    arrayOrdenada = arraySort[:number]

    for element in array:
        if element in arrayOrdenada:
            result.append(element)
            arrayOrdenada.remove(element)
    return result

