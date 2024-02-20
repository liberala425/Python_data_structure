def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    cum_sum = 0
    for paren in parens:
        if paren == "(":
            cum_sum += 1
        elif paren == ")":
            cum_sum -= 1
        if cum_sum < 0:
            return False
    
    if cum_sum == 0:
        return True
    else:
        return False
    
