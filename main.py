def getUppercase(phrase):
    # Dictionary for the conversion
    DICT_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z', }
    # Alphabet to get the right key in the dictionary
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    convertedPhrase = ''

    # Cycling all the phrase
    for element in phrase:
        # If element is a letter of the alphabet, so I don't convert ad uppercase letter, a number ir a special character
        if element in alphabet:
            # Convert
            convertedPhrase = convertedPhrase + DICT_TO_UPPER[element]
        else:
            # Adding without convert
            convertedPhrase = convertedPhrase + element
    return convertedPhrase


assert getUppercase('Hello') == 'HELLO'
assert getUppercase('hello') == 'HELLO'
assert getUppercase('HELLO') == 'HELLO'
assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
assert getUppercase('12345') == '12345'
assert getUppercase('') == ''
