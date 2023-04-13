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

global token
parserQueue = t.Queue()
def parser(tokenQueue):
    global token

    global parserQueue
    parserQueue = tokenQueue

    token = parserQueue.peek()
    print(token)

    program(token)

def removeFromQueue(parserQueue):
    global token

    rmToken, rmClass = parserQueue.remove()

def newToken(parseQueue):
    token = parserQueue.peek()
    return token

def panicMode(token):
    print(f'{token} is an invalid syntax')
    removeFromQueue(parserQueue)

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
        removeFromQueue(parserQueue)
        token = newToken(parserQueue)
        funcDeclRight(token)


def funcDeclRight(token):
    funcDef(token)
    if token in FOLLOW["funcDef"]:
        removeFromQueue(parserQueue)
        token = newToken(parserQueue)
        funcDeclRight(token)
    else:
        rmToken = None
    

def funcDef(token):
    if token in FIRST["funcDef"]:
        removeFromQueue(parserQueue)
    else:
        panicMode(token)
    token = newToken(parserQueue)
    t_type(token)
    token = newToken(parserQueue)
    fname(token)
    token = newToken(parserQueue)
    if token in FOLLOW["funcName"]:
        removeFromQueue(parserQueue)
    else:
        panicMode(token)
    token = newToken(parserQueue)
    param(token)
    token = newToken(parserQueue)
    if token in FOLLOW["params"]:
        token = removeFromQueue(parserQueue)
    else:
        panicMode(token)

    token = newToken(parserQueue)
    declarations(token)

    token = newToken(parserQueue)
    statement(token)

def declarations(token):
    decl(token)
    if token in FOLLOW["decl"]:
        token = removeFromQueue(parserQueue)
    else:
        panicMode(token)
    token = newToken(parserQueue)

    declarationsRight(token)

def declarationsRight(token):
    if not token in FIRST["decl"]:
        rmToken = None
    else:
        decl(token)
        if token in FOLLOW["decl"]:
            token = removeFromQueue(parserQueue)
        else:
            panicMode(token)
    token = newToken(parserQueue)
    declarationsRight(token)

def decl(token):
    t_type(token)
    token = newToken(parserQueue)

    varList(token)
    token = newToken(parserQueue)


def varList(token):
    var(token)
    token = newToken(parserQueue)

    varListRight(token)

def varListRight(token):
    if token in FIRST["varlistRight"]:
        removeFromQueue(parserQueue)
    else:
        panicMode(token)
    token = newToken(parserQueue)

    varList(token)

def statementSeq(token):
    statement(token)

    token = newToken(parserQueue)

    statementSeqRight(token)

def statementSeqRight(token):
    if token in FIRST["statementSequenceRight"]:
        removeFromQueue(parserQueue)
    else:
        panicMode(token)
    token = newToken(parserQueue)
    statementSeq(token)

def statement(token):
    if token in FIRST["var"]:
        var(token)

        if token == "=":
            removeFromQueue(parserQueue)
        else:
            panicMode(token)
        token = newToken(parserQueue)

        expr(token)
    elif token == "if":
        removeFromQueue(parserQueue)

        token = newToken(parserQueue)
        bexp(token)
        token = newToken(parserQueue)

        if token == "then":
            removeFromQueue(parserQueue)
        else:
            panicMode(token)

        token = newToken(parserQueue)
        statementSeq(token)

        if token == "else":
            removeFromQueue(parserQueue)
            statementSeq(token)
        else:
            panicMode(token)
        token = newToken(parserQueue)

        if token == "fi":
            removeFromQueue(parserQueue)
        else:
            panicMode(token)
    elif token == "while":
        removeFromQueue(parserQueue)

        token = newToken(parserQueue)

        bexp(token)

        token = newToken(parserQueue)

        if token == "do":
            removeFromQueue(parserQueue)

            token = newToken(parserQueue)

            statementSeq(token)

            token = newToken(parserQueue)

            if token == "od":
                removeFromQueue(parserQueue)
            else:
                panicMode(token)
        else:
            panicMode(token)
    elif token == "print":
        removeFromQueue(parserQueue)

        token = newToken(parserQueue)

        expr(token)
    elif token == "return":
        removeFromQueue(parserQueue)

        token = newToken(parserQueue)

        expr(token)
    else:
        panicMode(token) 

        
        


def t_type(token):
    if token in FIRST["type"]:
       removeFromQueue(parserQueue)
    else:
        panicMode(token)

def fname(token):
    if token.isalnum() or token.isalpha():
        removeFromQueue(parserQueue)
    else:
        panicMode(token)
def param(token):
    if token in FIRST["type"]:
        t_type(token)
        token = newToken(parserQueue)
        var(token)
        token = newToken(parserQueue)
        paramRight(token)

def paramRight(token):
    if token in FIRST["paramsRight"]:
        removeFromQueue(parserQueue)
        
    else:
        rmToken = None
    token = newToken(parserQueue)
    param(token)

def var(token):
    if token.isalnum() or token.isalpha():
        removeFromQueue(parserQueue)
        token = newToken(parserQueue)
        varRight(token)
    else:
        panicMode(token)

def varRight(token):
    if token in FIRST["varRight"]:
        removeFromQueue(parserQueue)
        token = newToken(parserQueue)
        expr(token)
        
    else:
        rmToken = None

def expr(token):
    term(token)
    token = newToken(parserQueue)
    exprRight(token)

def exprRight(token):
    if token == "+" or token == "-":
        removeFromQueue(parserQueue)

        term(token)
        
    else:
        rmToken = None
    token = newToken(parserQueue)
    exprRight(token)

def term(token):
    factor(token)
    token = newToken(parserQueue)
    termRight(token)

def termRight(token):
    if token == "*" or token == "/" or token == "%":
        removeFromQueue(parserQueue)
        factor(token)
        
    else:
        rmToken = None
    token = newToken(parserQueue)
    termRight(token)

def factor(token):
    if token in FIRST["var"]:
        var(token)
        token = newToken(parserQueue)
    elif token.isnumeric():
        removeFromQueue(parserQueue)
        token = newToken(parserQueue)
    elif token in FIRST["factor"]:
        removeFromQueue(parserQueue)()
        token = newToken(parserQueue)
        expr(token)
        token = newToken(parserQueue)
        if token in FOLLOW["expr"]:
            removeFromQueue(parserQueue)
        else:
            panicMode(token)
        token = newToken(parserQueue)
        
    elif token.isalnum():
        fname(token)
        if token in FOLLOW["funcName"]:
            removeFromQueue(parserQueue)

            token = newToken(parserQueue)

            exprSeq(token)

            token = newToken(parserQueue)

            if token in FOLLOW["expressionSequence"]:
                removeFromQueue(parserQueue)
            else:
                panicMode(token)
            token = newToken(parserQueue)
        else:
            panicMode(token)
        token = newToken(parserQueue)
    else:
        panicMode(token)

def exprSeq(token):
    expr(token)
    token = newToken(parserQueue)
    exprSeqRight(token)

def exprSeqRight(token):
    if token in FIRST["expressionSequenceRight"]:
        removeFromQueue(parserQueue)
    else:
        rmToken = None
    token = newToken(parserQueue)

    exprSeq(token)


def bexp(token):
    bterm(token)
    token = newToken(parserQueue)
    bexpRight(token)


def bexpRight(token): 
    if token == "or":
        removeFromQueue(parserQueue)
        token = newToken(parserQueue)
        bterm(token)
       
    else:
        rmToken = None
    token = newToken(parserQueue)
    bexpRight(token)

def bterm(token):
    bfactor(token)
    token = newToken(parserQueue)
    btermRight(token)

def btermRight(token):
    if token == "and":
        removeFromQueue(parserQueue)
        token = newToken(parserQueue)
        bfactor(token)
        token = newToken(parserQueue)

        btermRight(token)
    else:
        rmToken = None

def bfactor(token):
    if token == "not":
        removeFromQueue(parserQueue)
        token = newToken(parserQueue)

        bfactor(token)
    elif token == "(":
        removeFromQueue(parserQueue)
        token = newToken(parserQueue)
        if token in FIRST ["branchExpression"]:
            bexp(token)
            token = newToken(parserQueue)
            if token in FOLLOW["branchExpression"]:
                removeFromQueue(parserQueue)
            else:
                panicMode(token)
            token = newToken(parserQueue)
        else:
            expr(token)
            token = newToken(parserQueue)
            comp(token)
            token = newToken(parserQueue)
            expr(token)
            token = newToken(parserQueue)
            if token in FOLLOW["expr"]:
                removeFromQueue(parserQueue)
            else:
                panicMode(token)
            token = newToken(parserQueue)

def comp(token):
    if token in FIRST['comp']:
        removeFromQueue(parserQueue)


    
        


