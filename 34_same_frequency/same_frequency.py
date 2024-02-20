def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    new_num1 = str(num1)
    new_num2 = str(num2)

    if len(new_num1) != len(new_num2):
        return False
    
    for char in new_num1:
        if new_num1.count(char) != new_num2.count(char):
            return False
    
    return True

