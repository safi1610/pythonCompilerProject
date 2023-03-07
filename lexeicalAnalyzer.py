import string

keyWords = ["if", "fi", "while", "do", "od", "def", "fed", "print"]
types = ["int", "double"]

alphabet = string.ascii_lowercase + string.ascii_uppercase

symbol = ""

state = 0
def getNextToken(token):
    for element in token:
        match state:
            case 0:
                if element in alphabet and element.islower():
                    symbol += element
                    state = 1
                break
            case 1:
                if element == "\s" or element == "\t" or element == "\n":
                    state = 0

                if element in alphabet or element.isDigit():
                    symbol += element

                break

            