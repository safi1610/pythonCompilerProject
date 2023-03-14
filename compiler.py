import lexeicalAnalyzer as lex
import re

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
    bufferSize = 24
    fileName = "Test1.cp"
    
    line = readFile(fileName, bufferSize)
    

    buff1 = nextRead(line)
    buff2 = nextRead(line)

    while True:
        print(buff1)

        # token = re.sub(r'[ \t\n]+', lambda match: "" if match.group(0) == '\t' else "" if match.group(0) == '\n' else " ", buff1)
        # print(token)
        # delBuff = buff1.split()
        # print(delBuff)
        lex.getNextToken(buff1)
        # for token in delBuff:
        #     lex.getNextToken(token)

        buff1, buff2 = buff2, buff1

        buff2 = nextRead(line)

        if buff1 == None:
            break


main()