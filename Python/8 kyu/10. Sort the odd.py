def sort_array(array):
    
    result = []

    if len(array) < 0:

        return result
    
    for number in array:
        
        if number % 2 != 0:
            
            for numerOdd in array:
                
                result = array.sort()
                                
                return result
                
            else:
                
                return array
            
    return result




if __name__ == "__main__":

    assert (sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4])
    assert (sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0])
    assert (sort_array([]) == [])