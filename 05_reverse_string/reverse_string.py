def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    reversed_phrase = ""
    for i in range(len(phrase)-1, -1, -1):
        reversed_phrase = reversed_phrase + phrase[i]

    return reversed_phrase

