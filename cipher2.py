__author__ = 'danyalrehman'

def cipher(encrypted_message):
    """ the aim of this function is to take in a message
    that is encrypted, run it through the given dictionary
    and then decode the message so that the returned string
    is the decoded message.
    """

    dictionary_of_letters = {"a" : "i", "b" : "l", "c" : "o", "d" : "v", "e" : "e", "f" : "y", "g" : "u", " ": " ", \
                             "h" : "m", "i" : "r", "j" : "t", "k" : "h", "l" : "n", "m" : "f", "n": "a", "o": "d", \
                             "." : ".", "p" : "w", "q" : "s", ":" : ":", ")" : ")"}

    decrypted_message = ""

    for eachletter in encrypted_message:
        decrypted_message += str(dictionary_of_letters[eachletter])
    return decrypted_message

print cipher("a bcde fcg hcie jknl bame nlo a leeo fcg. a paqk a pnq pajk fcg. fcg nie hf bame :)")

def reversecipher(decrypted_message):
    """ the aim of this function is to take in a normal sentence
    and return the encrypted version of the word. It can be put
    into the first function to return the original decrypted message
    """

    encrypted_message = ""

    dictionary = {"a" : "q", "b" : "w", "c" : "e", "d" : "r", "e" : "t", "f" : "y", "g" : "u", \
                  "h" : "i", "i" : "o", "j" : "p", "k" : "a", "l" : "s", "m" : "d", "n" : "f", \
                  "o" : "g", "p" : "h", "q" : "j", "r" : "k", "s" : "l", "t" : "z", "u" : "x", \
                  "v" : "c", "w" : "v", "x" : "b", "y" : "n", "z": "m", " " : " "}

    keys = dictionary.keys()
    values = dictionary.values()

    keys.sort()

    new_keys = values
    new_values = keys

    compiler = zip(new_keys, new_values)

    new_dictionary = dict(compiler)

    for eachletter in decrypted_message:
        encrypted_message += str(new_dictionary[eachletter])
    return encrypted_message

print reversecipher("i love you")
    