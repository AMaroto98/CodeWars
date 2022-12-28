def to_jaden_case(string):

    listString = list(string.split(" "))

    myString= ""

    for i in listString:

        i = i.capitalize()
        myString += i + " "
        
    myString = myString[:-1]  
    return myString