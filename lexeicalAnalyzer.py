import string

keyWords = ["if", "fi", "while", "do", "od", "def", "fed", "print"]
types = ["int", "double"]

alphabet = string.ascii_lowercase + string.ascii_uppercase

state = 0
def getNextToken(token):
    for element in token:
        match state:
            case 0:
                if element in alphabet and element.islower():
                    state = 1
                break
            