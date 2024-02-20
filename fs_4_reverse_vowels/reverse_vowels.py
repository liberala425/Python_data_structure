def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    #vowels_pos = []
    vowels = []
    s_lst = list(s)
    for i in range(len(s_lst)):
        if s_lst[i].lower() in 'aeiou':
            #vowels_pos.append(i)
            vowels.append(s_lst[i])

    vowels.reverse()
    idx = 0
    for i in range(len(s_lst)):
        if s_lst[i].lower() in 'aeiou':
            s_lst[i] = vowels[idx]
            idx += 1
    
    return "".join(s_lst)

