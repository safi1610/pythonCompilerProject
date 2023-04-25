import string
import token_1 as t

keyWords = ["if", "fi", "while", "do", "od", "def", "fed", "print", "then", "return", "else"]
types = ["int", "double"]
operators = ["+", "-", "*", "/", "%"]

delim = [" ", "\n", "\t"]

tokenQueue = t.Queue()

alphabet = string.ascii_lowercase + string.ascii_uppercase

lineNum = 1

# f = open("output.txt", "a")

# state = 0
def getNextToken(token, f, fError):
    global lineNum
    classification = ""
    symbol = ""
    state = 0
    curr = 0
    buffLen = len(token) 

    while curr != buffLen:
        match state:
            case -1:
                while token[curr] not in delim:
                    symbol += token[curr]
                    curr += 1
                print(f"{symbol} is not a valid token at line: {lineNum}" )
                fError.write(f"{symbol} is not a valid token at line: {lineNum}\n" )

                symbol = ""
                curr += 1
                state = 0
            case 0:
                if token[curr] in operators:
                    classification = "operator"
                    symbol += token[curr]
                    curr += 1
                    state = 2
                elif token[curr] == ",":
                    classification = "comma"
                    symbol += token[curr]
                    curr += 1
                    state = 2
                elif token[curr] == ";":
                    classification = "semi-colon"
                    symbol += token[curr]
                    curr += 1
                    state = 2
                elif token[curr]  == "(":
                    classification = "opening parentheses"
                    symbol += token[curr]
                    curr += 1
                    state = 2
                elif token[curr] == ")":
                    classification = "closing parentheses"
                    symbol += token[curr]
                    curr += 1
                    state = 2
                elif token[curr] == ".":
                    classification = "END"
                    symbol = "$"
                    curr += 1
                    state = 2
                elif token[curr] in delim:
                    if token[curr] == "\n":
                        lineNum += 1
                    curr += 1
                    symbol = ""
                
                
                elif token[curr] in alphabet and token[curr].islower():
                    symbol += token[curr]
                    curr += 1 
                    state = 1

                elif token[curr].isdigit():
                    symbol += token[curr]
                    curr += 1
                    state = 3
                elif token[curr] == "<":
                    symbol += token[curr]
                    curr += 1
                    state = 5
                elif token[curr] == ">":
                    symbol += token[curr]
                    curr += 1
                    state = 5
                elif token[curr] == "=":
                    symbol += token[curr]
                    curr += 1
                    state = 5
                else:
                    state = -1
                    
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
                    # tk = t.Token(symbol, classification)
                    tokenQueue.insert(symbol, classification)
                    symbol = ""
                    state = 0
                    print(tokenQueue._rear.element, tokenQueue._rear.classification)
                    f.write(tokenQueue._rear.element+"|"+tokenQueue._rear.classification+"\n")

            case 2:
                # tk = t.Token(symbol, classification)
                tokenQueue.insert(symbol, classification)
                symbol = ""
                state = 0
                # curr += 1
                print(tokenQueue._rear.element, tokenQueue._rear.classification)
                f.write(tokenQueue._rear.element+"|"+tokenQueue._rear.classification+"\n")

            
            case 3:
                classification = "integer"
                if token[curr].isdigit():
                    symbol += token[curr]
                    curr += 1 
                elif token[curr] == "." or token[curr] == "e":
                    symbol += token[curr]
                    state = 4
                    curr += 1
                elif token[curr] in alphabet and token[curr] != "e":
                    symbol += token[curr]
                    curr += 1
                    state = -1
                else:
                    # tk = t.Token(symbol, classification)
                    tokenQueue.insert(symbol, classification)
                    symbol = ""
                    state = 0
                    print(tokenQueue._rear.element, tokenQueue._rear.classification)
                    f.write(tokenQueue._rear.element+"|"+tokenQueue._rear.classification+"\n")
            case 4:
                classification = "double"
                if token[curr].isdigit():
                    symbol += token[curr]
                    curr += 1
                elif token[curr] == "e":
                    symbol += token[curr]
                    curr += 1
                elif token[curr] in alphabet and token[curr] != "e":
                    symbol += token[curr]
                    curr += 1
                    state = -1
                else:
                    # tk = t.Token(symbol, classification)
                    tokenQueue.insert(symbol, classification)
                    symbol = ""
                    state = 0
                    print(tokenQueue._rear.element, tokenQueue._rear.classification)
                    f.write(tokenQueue._rear.element+"|"+tokenQueue._rear.classification+"\n")
            case 5:
                if token[curr] == "=":
                    symbol += token[curr]
                    curr += 1
                if token[curr] == ">":
                    symbol += token[curr]
                    curr += 1
                if token[curr] == "<":
                    symbol += token[curr]
                    curr += 1
                else:
                    if symbol == "<=":
                        classification = "LE"
                        state = 8
                    elif symbol == "<>":
                        classification = "NE"
                        state = 8
                    elif symbol == "<":
                        classification = "LT"
                        state = 8
                    elif symbol == ">=":
                        classification = "GE"
                        state = 8
                    elif symbol == ">":
                        classification = "GT"
                        state = 8
                    elif symbol == "==":
                        classification = "EQ"
                        state = 8
                    elif symbol == "=":
                        classification = "operator"
                        state = 2
                    else:
                         state = -1

            case 8:
                # tk = t.Token(symbol, classification)
                tokenQueue.insert(symbol, classification)
                symbol = ""
                state = 0
                print(tokenQueue._rear.element, tokenQueue._rear.classification)
                f.write(tokenQueue._rear.element+"|"+tokenQueue._rear.classification+"\n")
    return tokenQueue

                    


            

