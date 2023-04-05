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
    if token in FIRST["funcDef"]:
        funcDef(token)
    elif token in FOLLOW["funcDef"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        funcDeclRight(token)


def funcDeclRight(token):
    if token in FIRST["funcDef"]:
        funcDef(token)
    elif token in FOLLOW["funcDef"]:
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
        funcDeclRight(token)
    else:
        rmToken = None
    

def funcDef(token):
    if token == "def":
        rmToken = parserQueue.remove()
        token = parserQueue.peek()
    if token in FIRST["type"]:
        t_type(token)

def t_type(token):
    if token in FIRST["type"]:
        rmToken = parserQueue.remove
        token = parserQueue.peek()

    
        


