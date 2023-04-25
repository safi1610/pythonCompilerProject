import token_1 as t
import semanticAnalyzer as san
import stack as st

scopeStack = st.Stack()
tlLine = t.Queue()
funcQueue = san.semanticTable()
globalQueue = san.semanticTable()
ifQueue = san.semanticTable()
whileQueue = san.semanticTable()

ifScope = "if-scope"
whileScope = "while-scope"
funcScope = "func"
globalScope = "global"

def analyseSemantics(tokenQueue):
    sem = 0
    tagType = []
    relop = ["<", ">", "<=", ">=", "<>", "=="]
    operator = ["+", "-", "*", "%", "/"]
    current = tokenQueue._front
    illegal = ""
    statement = ""
    while current is not None:
        match sem:
            case 0:
                scopeStack.push(globalScope)
                if current.element == "def":
                    scope = "func"
                    scopeStack.push(funcScope)
                    tagType.append("func")

                    sem = 1
                if current.classification == "type":
                    scope = "global"
                    if current.element == "int":
                        tagType.append("integer")
                    else:
                        tagType.append("double")
                    sem = 2
                if current.classification == "identifier":
                    if funcQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)
                    elif globalQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)
                    elif ifQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)
                    elif whileQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)

                    else:
                        print(current.element + "does not exist within this scope")

                current = current._next
            case 1:
                if current.classification == "type": 
                    if current.element == "int":
                        tagType.append("integer")
                    else:
                        tagType.append("double")
                    sem = 2
                if current.classification == "identifier":
                    
                    if funcQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)
                    elif globalQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)
                    elif ifQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)
                    elif whileQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)

                    else:
                        print(current.element + "does not exist within any scope")

                if current.element == "if":
                    scope = "if-scope"
                    scopeStack.push(scope)
                    sem = 3
                if current.element == "return":
                    statement += current.element
                    returnFunc = funcQueue.searchByType("func")
                    if not returnFunc == None:
                        sem = 4
                if current.element == "fi":
                    scopeStack.pop()
                current = current._next
                

            case 2:
                if current.classification == "identifier":
                    if scopeStack.peek() == funcScope:
                        funcQueue.insert(current.element, current.classification, tagType)
                        print(funcQueue._rear.element, funcQueue._rear.classification, funcQueue._rear.t_type)
                        tagType.clear()
                    elif scopeStack.peek() == ifScope:
                        ifQueue.insert(current.element, current.classification, tagType)
                        print(ifQueue._rear.element, ifQueue._rear.classification, ifQueue._rear.t_type)
                        tagType.clear()
                    elif scopeStack.peek() == whileScope:
                        whileQueue.insert(current.element, current.classification, tagType)
                        print(whileQueue._rear.element, whileQueue._rear.classification, whileQueue._rear.t_type)
                        tagType.clear()
                    else:

                        globalQueue.insert(current.element, current.classification, tagType)
                        print(globalQueue._rear.element, globalQueue._rear.classification, globalQueue._rear.t_type)
                        tagType.clear()
                    sem = 1
                current = current._next
                    
            case 3:
                if current.classification == "identifier":
                    
                    if ifQueue.search(current.element):
                        statement += current.element
                        idType = ifQueue.getType(current.element)
                        if "integer" in idType:
                            tagType.append("integer")
                        else:
                            tagType.append("double")
                    elif funcQueue.search(current.element):
                        statement += current.element
                        idType = funcQueue.getType(current.element)
                        if "integer" in idType:
                            tagType.append("integer")
                        else:
                            tagType.append("double")
                    elif whileQueue.search(current.element):
                        statement += current.element
                        idType = whileQueue.getType(current.element)
                        if "integer" in idType:
                            tagType.append("integer")
                        else:
                            tagType.append("double")
                    elif globalQueue.search(current.element):
                        statement += current.element
                        idType = globalQueue.getType(current.element)
                        if "integer" in idType:
                            tagType.append("integer")
                        else:
                            tagType.append("double")

                    else:
                        print(current.element + " does not exist")
                elif "integer" and "double" in tagType:
                    print(statement + " does not have compatible type")
                    break
                elif current.element in relop:
                    statement += current.element
                    tagType.append(current.classification)
                elif current.element == "then":
                        ifQueue.insert(statement, "bool", tagType)
                        print(ifQueue._rear.element, ifQueue._rear.classification, ifQueue._rear.t_type)
                        tagType.clear()
                        statement = ""
                        sem = 1 
                current = current._next

            case 4:
                if current.classification == "identifier" or current.classification == "number" or current.classification == "double":
                    if ifQueue.search(current.element):
                        idType = ifQueue.getType(current.element)
                    elif funcQueue.search(current.element):
                        idType = funcQueue.getType(current.element)
                    elif whileQueue.search(current.element):
                        idType = whileQueue.getType(current.element)
                    elif globalQueue.search(current.element):
                        idType = globalQueue.getType(current.element)
                    else:
                        print(current.element + " does not exist")
                    
                    if ("integer" in idType and "integer" in returnFunc.t_type) or ("double" in idType and "double" in returnFunc.t_type):
                        if "integer" in idType:
                            tagType.append("integer")
                        else:
                            tagType.append("double")
                        if scopeStack.peek() == ifScope:
                                statement += current.element
                                ifQueue.insert(statement, "return", tagType)
                                print(ifQueue._rear.element, ifQueue._rear.classification, ifQueue._rear.t_type)

                        elif scopeStack.peek() == funcScope:
                                statement += current.element
                                funcQueue.insert(statement, "return", tagType)
                                print(funcQueue._rear.element, funcQueue._rear.classification, funcQueue._rear.t_type)
                        elif scopeStack.peek() == whileScope:
                                statement += current.element
                                whileQueue.insert(statement, "return", tagType)
                                print(whileQueue._rear.element, whileQueue._rear.classification, whileQueue._rear.t_type)
                    tagType.clear()
                    statement = ""
                    sem = 1
                current = current._next

