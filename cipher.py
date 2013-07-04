__author__ = 'danyalrehman'

def create_cipher_table(filename):
    """this function returns a dictionary where the keys
    are the encoded letters and the values are the decoded letters.

    """
    input_file = open(filename, "r")
    
    dictionary = {}
    for elements in input_file:
        L = elements.split(":")
        encodedside = L[0]
        decodedside = L[1]

        # add the new value to the dictionary whereby the a space
        # is given the same value in the dictionary.
        dictionary[" "] = " "
        liststrip = decodedside.strip()

        dictionary[encodedside] = liststrip

    return dictionary

def decode_cipher(filename, encrypted_message):
    """this function takes in two parameters whereby one is a string

       and the other is a dictionary. The string is the message
       to be decrypted and the dictionary is the one that is
       called up from the create_cipher_table function.
    """

    dictionary = create_cipher_table(filename)
    stringletter = ""

    decrypted_message = ""
    # for loop results in taking each letter from the encrypted message
    # and then putting it into the dictionary and returning a decrypted
    # message.
    for each_letter in encrypted_message:

        stringletter += dictionary[each_letter]
        decrypted_message = decrypted_message + stringletter

    return decrypted_message

print decode_cipher("something.txt", "holy")