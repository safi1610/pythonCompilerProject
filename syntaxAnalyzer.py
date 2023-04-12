import token_1 as t


FIRST = {}
FIRST["program"] = {"def", "int", "double", "if", "while", "print", "return", "ID"}
FIRST["funcDecl"] = {"def", "EPSILON"}
FIRST["funcDef"] = {"def"}
FIRST["funcDefRight"] = {"def", "EPSILON"}
FIRST["params"] = {"int", "double", "EPSILON"}
FIRST["paramsRight"] = {",", "EPSILON"}
FIRST["funcName"] = {"ID"}
FIRST["declarations"] = {"int", "double", "EPSILON"}
FIRST["decl"] = {"int", "double"}
FIRST["declRight"] = {"int", "double", "EPSILON"}
FIRST["type"] = {"int", "double"}
FIRST["varlist"] = {"ID"}
FIRST["varlistRight"] = {",", "EPSILON"}
FIRST["statementSequence"] = {"if", "while", "print", "return", "ID", "EPSILON"}
FIRST["statement"] = {"if", "while", "print", "return", "ID", "EPSILON"}
FIRST["statementSequenceRight"] = {";", "EPSILON"}
FIRST["optionElse"] = {"else", "EPSILON"}
FIRST["expr"] = {"ID", "NUMBER", "("}
FIRST["term"] = {"ID", "NUMBER", "("}
FIRST["termRight"] = {"+", "-", "EPSILON"}
FIRST["varRight"] = {"[","EPSILON"}
FIRST["var"] = {"ID"}
FIRST["comp"] = {"<", ">", "==", "<=", ">=", "<>"}
FIRST["branchFactorParen"] = {"(", "not", "ID", "NUMBER", "EPSILON"}
FIRST["branchFactor"] = {"(", "not"}
FIRST["branchFactorRight"] = {"and", "EPSILON"}
FIRST["branchTerm"] = {"(", "not"}
FIRST["branchTermRight"] = {"or", "EPSILON"}
FIRST["branchExpression"] = {"(", "not"}
FIRST["expressionSequenceRight"] = {",", "EPSILON"}
FIRST["expressionSequence"] = {"(", "ID", "NUMBER"}
FIRST["factor"] = {"(", "ID", "NUMBER"}
FIRST["factorRight"] = {"*", "/", "%", "EPSILON"}
FIRST["factorParen"] = {"(","EPSILON"}

FOLLOW = {}
FOLLOW["program"] = {"$"}
FOLLOW["funcDecl"] = {"int", "double", "if", "while", "print", "return", "ID"}
FOLLOW["funcDef"] = {";"}
FOLLOW["funcDefRight"] = {";"}
FOLLOW["params"] = {")"}
FOLLOW["paramsRight"] = {")"}
FOLLOW["funcName"] = {"("}
FOLLOW["declarations"] = {"if","while","print","return","ID"}
FOLLOW["decl"] = {";"}
FOLLOW["declRight"] = {";"}
FOLLOW["type"] = {"ID"}
FOLLOW["varlist"] = {";", ",", ".", "(", ")", "]", "[", "then", "+", "-", "", "/", "%", "==", "<>", "<", ">"}
FOLLOW["varlistRight"] = {";", ",", ".", "(", ")", "]", "[", "then", "+", "-", "", "/", "%", "==", "<>", "<", ">"}
FOLLOW["statementSequence"] = {".", "fed", "fi", "od", "else"}
FOLLOW["statement"] = {".", ";", "fed", "fi", "od", "else"}
FOLLOW["statementSequenceRight"] = {".", ";", "fed", "fi", "od", "else"}
FOLLOW["optionElse"] = {"fi"}
FOLLOW["expr"] = {".", ";", "fed", "fi", "od", "else", ")", "=", ">", "<", "]",}
FOLLOW["term"] = {".", ";", "fed", "fi", "od", "else", ")", "=", ">", "<", "]", "+", "-", "", "/",}
FOLLOW["termRight"] = {".", ";", "fed", "fi", "od", "else", ")", "=", ">", "<", "]", "+", "-", "", "/"}
FOLLOW["varRight"] = {";", ",", ".", "(", ")", "]", "[", "then", "+", "-", "", "/", "%", "==", "<>", "<", ">"}
FOLLOW["var"] = {";", ",", ".", "(", ")", "]", "[", "then", "+", "-", "", "/", "%", "==", "<>", "<", ">"}
FOLLOW["comp"] = {""}
FOLLOW["branchFactorParen"] = {"then", "do", ")", "or", "and"}
FOLLOW["branchFactor"] = {"then", "do", ")", "or", "and"}
FOLLOW["branchFactorRight"] = {"then", "do", ")", "or", "and"}
FOLLOW["branchTerm"] = {"then", "do", ")", "or", "and"}
FOLLOW["branchTermRight"] = {"then", "do", ")", "or", "and"}
FOLLOW["branchExpression"] = {"then", "do", ")", "or"}
FOLLOW["expressionSequenceRight"] = {")"}
FOLLOW["expressionSequence"] = {")"}
FOLLOW["factor"] = {".", ";", "fed", "fi", "od", "else", ")", "=", ">", "<", "]", "+", "-", "", "/",}
FOLLOW["factorRight"] = {".", ";", "fed", "fi", "od", "else", ")", "=", ">", "<", "]", "+", "-", "", "/",}
FOLLOW["factorParen"] = {".",";","fed","fi","od","else",")","=",">","<","]","+","-","*","/"}

parserQueue = t.Queue()
def parser(tokenQueue):
    global parserQueue
    parserQueue = tokenQueue

    token = parserQueue.peek()
    print(token)

    program(token)

def panicMode(token):
    print(f'{token} is an invalid syntax')
    rmToken = parserQueue.remove()
    token = parserQueue.peek()

def program(token):
    if token in FIRST["funcDecl"]:
        funcDecl(token)
    if token in FOLLOW["funcDecl"] and FIRST["declarations"]:
        declarations(token)
    if (token in FOLLOW["funcDecl"] and FIRST["statementSequence"]) or (token in FOLLOW["declarations"] and FIRST["statementSequence"]):
        statementSeq(token)
    if token in FOLLOW["program"]:
        rmToken = parserQueue.remove()

def funcDecl(token):
    funcDef(token)
    if token in FOLLOW["funcDef"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        funcDeclRight(token)


def funcDeclRight(token):
    funcDef(token)
    if token in FOLLOW["funcDef"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        funcDeclRight(token)
    else:
        rmToken = None
    

def funcDef(token):
    if token in FIRST["funcDef"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
    else:
        panicMode(token)
    t_type(token)
    fname(token)
    if token in FOLLOW["funcName"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
    else:
        panicMode(token)
    param(token)

    if token in FOLLOW["params"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
    else:
        panicMode(token)
    declarations(token)
    statements(token)

def declarations(token):
    decl(token)
    if token in FOLLOW["decl"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
    else:
        panicMode(token)

    declarationsRight(token)

def declarationsRight(token):
    if not token in FIRST["decl"]:
        rmToken = None
    else:
        decl(token)
        if token in FOLLOW["decl"]:
            rmToken = parserQueue.remove()
            token = parserQueue.peek()
            declarationsRight(token)
        else:
            panicMode(token)

def decl(token):
    t_type(token)
    varList(token)

def varList(token):
    var(token)
    varListRight(token)

def varListRight(token):
    if token in FIRST["varlistRight"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
    else:
        panicMode(token)
    varList(token)

def statmentSeq(token):
    statement(token)
    statmentSeqRight(token)

def statementSeqRight(token):
    if token in FIRST["statementSequenceRight"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
    else:
        panicMode(token)
    statmentSeq(token)

def statement(token):
    if token == "if":
        rmToken = parserQueue.remove()
        token = parserQueue.peek()

        bexp(token)

        if token == "then":
            rmToken = parserQueue.remove()
            token = parserQueue.peek()
        


def t_type(token):
    if token in FIRST["type"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
    else:
        panicMode(token)

def fname(token):
    if token.isalnum() or token.isalpha():
        rmToken = parserQueue.remove()
        token = parserQueue.peek
    else:
        panicMode(token)
def param(token):
    t_type(token)
    var(token)
    paramRight(token)

def paramRight(token):
    if token in FIRST["paramsRight"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        param(token)
    else:
        rmToken = None

def var(token):
    if token.isalnum() or token.isalpha():
        rmToken = parserQueue.remove()
        token = parserQueue.peek
    varRight(token)

def varRight(token):
    if token in FIRST["varRight"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        expr(token)
    else:
        rmToken = None

def expr(token):
    term(token)
    exprRight(token)

def exprRight(token):
    if token == "+" or token == "-":
        rmToken = parserQueue.remove()
        token = parserQueue.peek()

        term(token)
        exprRight(token)
    else:
        rmToken = None

def term(token):
    factor(token)
    termRight(token)

def termRight(token):
    if token == "*" or token == "/" or token == "%":
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        factor(token)
        termRight(token)
    else:
        rmToken = None

def factor(token):
    if token in FIRST["var"]:
        var(token)
    elif token.isnumeric():
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
    elif token in FIRST["factor"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        expr(token)
        if token in FOLLOW["expr"]:
            rmToken = parserQueue.remove()
            token = parserQueue.peeK()
        else:
            panicMode(token)
        
    elif token.isalnum():
        fname(token)
        if token in FOLLOW["funcName"]:
            rmToken = parserQueue.remove()
            token = parserQueue.peek()

            exprSeq(token)

            if token in FOLLOW["expressionSequence"]:
                rmToken = parserQueue.remove()
                token = parserQueue.peek()
            else:
                panicMode(token)
        else:
            panicMode(token)
    else:
        panicMode(token)

def exprSeq(token):
    expr(token)
    exprSeqRight(token)

def exprSeqRight(token):
    if token in FIRST["expressionSequenceRight"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()

        exprSeq(token)
    else:
        rmToken = None

def bexp(token):
    bterm(token)
    bexpRight(token)


def bexpRight(token): 
    if token == "or":
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        bterm(token)
        bexpRight(token)
    else:
        rmToken = None

def bterm(token):
    bfactor(token)
    btermRight(token)

def btermRight(token):
    if token == "and":
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        bfactor(token)
        btermRight(token)
    else:
        rmToken = None

def bfactor(token):
    if token == "not":
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        bfactor(token)
    elif token == "(":
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        if token in FIRST ["branchExpression"]:
            bexp(token)
            if token in FOLLOW["branchExpression"]:
                rmToken = parserQueue.remove()
                token = parserQueue.peek()
            else:
                panicMode(token)
        else:
            expr(token)
            comp(token)
            expr(token)
            if token in FOLLOW["expr"]:
                rmToken = parserQueue.remove()
                token = parserQueue.peek()
            else:
                panicMode(token)

def comp(token):
    if token in FIRST['comp']:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()


    
        


