def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_lst = phrase.split(" ")
    cap_phrase = ""
    for word in phrase_lst:
        cap_phrase += word.capitalize() + " "


    return cap_phrase

