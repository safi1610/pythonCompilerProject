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
    curr = 0
    buffLen = token.len()

    while curr != buffLen:
        match state:
            case 0:
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