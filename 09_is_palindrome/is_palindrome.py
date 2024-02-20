def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    new_str = phrase.replace(" ", "").lower()
    mid_idx = int(len(new_str)/2)

    for i in range(mid_idx):
        if new_str[i] != new_str[len(new_str)-1-i]:
            return False
    
    return True

