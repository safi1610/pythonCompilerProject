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
    lineNum = 1
    curr = 0
    buffLen = len(token)

    while curr != buffLen:
        match state:
            case -1:
                while token[curr] not in delim:
                    symbol += token[curr]
                    curr += 1
                print(symbol +" is not a valid" + classification + " at line: " + lineNum)
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
                    if token[curr] == "\n":
                        lineNum += 1
                    curr += 1
                    symbol = ""
                
                if token[curr] in alphabet and token[curr].islower():
                    symbol += token[curr]
                    curr += 1 
                    state = 1

                if token[curr].isdigit():
                    symbol += token[curr]
                    curr += 1
                    state = 3
                
                    
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
            
            case 3:
                classification = "integer"
                if token[curr].isdigit():
                    symbol += token[curr]
                elif token[curr] == ".":
                    symbol += token[curr]
                    state = 4
                    curr += 1
                elif token[curr] in alphabet:
                    symbol += token[curr]
                    curr += 1
                    state = -1
                else:
                    tk = t.Token(symbol, classification)
                    symbol = ""
                    state = 0
                    print(tk.element, tk.classification)
            case 4:
                classification = "double"
                if token[curr].isdigit():
                    symbol += token[curr]
                    curr += 1
                elif token[curr] in alphabet:
                    symbol += token[curr]
                    curr += 1
                    state = -1
                else:
                    tk = t.Token(symbol, classification)
                    symbol = ""
                    state = 0
                    print(tk.element, tk.classification)

            

