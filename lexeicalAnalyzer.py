import string
import token_1 as t

keyWords = ["if", "fi", "while", "do", "od", "def", "fed", "print", "then"]
types = ["int", "double"]
operators = ["+", "-", "*", "/", "%", "="]

delim = [" ", "\n", "\t"]


alphabet = string.ascii_lowercase + string.ascii_uppercase

# state = 0
def getNextToken(token):
    classification = ""
    symbol = ""
    state = 0
    delTok = ""
    curr = 0
    buffLen = len(token)

    while curr != buffLen:
        match state:
            case 0:
                if token[curr] in operators:
                    classification = "operator"
                    state = 2
                if token[curr] == ",":
                    classification = "comma"
                    state = 2
                if token[curr] == ";":
                    classification = "semi-colon"
                    state = 2
                if token[curr]  == "(":
                    classification == "opening parentheses"
                    state = 2
                if token[curr] == ")":
                    classification = "closing parentheses"
                    state = 2
                if token[curr] in delim:
                    curr += 1
                    symbol = ""
                
                if token[curr] in alphabet and token[curr].islower():
                    symbol += token[curr]
                    curr += 1 
                    state = 1
            case 1:
                if token[curr] in alphabet or token[curr].isdigit():
                    symbol += token[curr]
                    curr += 1
                else:
                    if symbol in keyWords:
                        classification = "keyword"
                    elif symbol in types:
                        classification = "type"
                    else:
                        classification = "identifier"
                    tk = t.Token(symbol, classification)
                    symbol = ""
                    state = 0
                    print(tk.element, tk.classification)

            case 2:
                symbol += token[curr]
                tk = t.Token(symbol, classification)
                symbol = ""
                state = 0
                curr += 1
                print(tk.element, tk.classification)
