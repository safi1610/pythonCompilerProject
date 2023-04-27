import lexeicalAnalyzer as lex
import re
import token_1 as t
import syntaxAnalyzer as p
import semanticAnalysis as s
from copy import deepcopy

def readFile(fName, buffS):
    with open(fName, 'r') as fp:
        while True:
            data = fp.read(buffS)
            if not data:
                break

            yield data
            

def nextRead(line):
    try:
        return next(line)
    except StopIteration:
        return None

    



def main():
    bufferSize = 256
    fileName = "Test4.cp"
    
    tokenQueue = t.Queue()

    line = readFile(fileName, bufferSize)

    f = open("output.txt", "w")
    fError = open("Error.txt", "w")
    

    buff1 = nextRead(line)
    buff2 = nextRead(line)

    while True:
        print(buff1)

        # token = re.sub(r'[ \t\n]+', lambda match: "" if match.group(0) == '\t' else "" if match.group(0) == '\n' else " ", buff1)
        # print(token)
        # delBuff = buff1.split()
        # print(delBuff)
        tokenQueue = lex.getNextToken(buff1, f, fError)
        # for token in delBuff:
        #     lex.getNextToken(token)
        tokenQueue.insert("$", "END")

        parserQueue = t.Queue()
        parserQueue = deepcopy(tokenQueue)

        

        buff1, buff2 = buff2, buff1

        buff2 = nextRead(line)

        if buff1 == None:
            f.close()
            fError.close()

            p.parser(parserQueue)   
            # for tok in tokenQueue:
            #     print(tok)

            semanticQueue = deepcopy(tokenQueue)
            s.analyseSemantics(semanticQueue)


                
            break
            # tokenNode = tokenQueue.remove
            # parser(tokenNode)


            
            


main()