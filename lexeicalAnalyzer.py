import string
import token_1 as t

keyWords = ["if", "fi", "while", "do", "od", "def", "fed", "print"]
types = ["int", "double"]

alphabet = string.ascii_lowercase + string.ascii_uppercase

# state = 0
def getNextToken(token):
    symbol = ""
    state = 0
    for element in token:
        if element == " " or element == r"\t" or element == r"\n":
            tk = t.Token(symbol, "token")
            state = 0
            symbol = ""

            print(tk.element, tk.classification)

            continue


        match state:
            case 0:
                if element in alphabet and element.islower():
                    symbol += element
                    state = 1
                # break
            case 1:

                if element in alphabet or element.isDigit():
                    symbol += element

                # break

            