import string
import token_1 as t

keyWords = ["if", "fi", "while", "do", "od", "def", "fed", "print", "then"]
types = ["int", "double"]
operators = ["+", "-", "*", "/", "%", "="]


alphabet = string.ascii_lowercase + string.ascii_uppercase

# state = 0
def getNextToken(token):
    classification = ""
    symbol = ""
    state = 0
    delTok = ""
    for element in token:

        match state:
            
            case 0:
                if delTok == " ":
                    delTok = ""

                if delTok == ",":
                    symbol += delTok
                    classification = "comma"
                    tk = t.Token(symbol, classification)
                    print(tk.element, tk.classification)

                if delTok == ";":
                    symbol += delTok
                    classification = "semi-colon"
                    tk = t.Token(symbol, classification)
                    print(tk.element, tk.classification)

                if delTok == "(":
                    symbol += delTok
                    classification = "opening parentheses"
                    tk = t.Token(symbol, classification)
                    print(tk.element, tk.classification)

                if delTok == ")":
                    symbol += delTok
                    classification = "closing parentheses"
                    tk = t.Token(symbol, classification)
                    print(tk.element, tk.classification)

                if delTok in operators:
                    symbol += delTok
                    classification = "operator"
                    tk = t.Token(symbol, classification)
                    print(tk.element, tk.classification)
                
                symbol = ""
                delTok = ""

                if element in alphabet and element.islower():
                    symbol += element
                    state = 1

                # break
            case 1:

                if element in alphabet or element.isdigit():
                    symbol += element
                else:
                    if symbol in keyWords:
                        classification = "keyword"
                    elif symbol in types:
                        classification = "type"
                    else:
                        classification = "identifier"
                    tk = t.Token(symbol, classification)
                    symbol = ""
                    delTok += element
                    print(tk.element, tk.classification)
                    state = 0

                # break

            