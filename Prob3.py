##################################################
# Name:
# Collaborators:
# Estimate of time spent (hr):
##################################################


def encrypt(message, key):
    """
    Function to take a given message and encrypt it using
    the given key and a letter-substitution cipher.

    Inputs:
        message (string): message to be encrypted
        key (string): 26-character string (upper or lower case)
    Outputs:
        (string): the encrypted message
    """
    pass # remove once you've added code











if __name__ == '__main__':
    KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"
    # KEY = "qwertyuiopasdfghjklzxcvbnm" # alternative key to test lower case key
    print(encrypt("Squeamish Ossifrage", KEY))
    print(encrypt("ABC - 123", KEY))
    print(encrypt("Isn't this great?", KEY))
