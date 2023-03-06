import lexeicalAnalyzer as lex

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
    bufferSize = 16
    fileName = "Test1.cp"
    
    line = readFile(fileName, bufferSize)

    buff1 = nextRead(line)
    buff2 = nextRead(line)

    while True:
        print(buff1)

        lex.getNextToken(buff1)

        buff1, buff2 = buff2, buff1

        buff2 = nextRead(line)

        if buff1 == None:
            break


main()