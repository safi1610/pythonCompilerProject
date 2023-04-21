import token_1 as t
import semanticAnalyzer as san

tlLine = t.Queue()
localQueue = san.semanticTable()
globalQueue = san.semanticTable()


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
                if current.element == "def":
                    scope = "local"
                    statement += current.element
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
                    if localQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)
                        sem = 3
                    elif globalQueue.search(current.element):
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
                    
                    if localQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)
                    elif globalQueue.search(current.element):
                        statement += current.element
                        tagType.append(current.classification)

                    else:
                        print(current.element + "does not exist within this scope")

                if current.element == "if":
                    sem = 3
                if current.element == "return":
                    
                current = current._next
                

            case 2:
                if current.classification == "identifier":
                    if scope == "local":
                        localQueue.insert(current.element, current.classification, tagType)
                        print(localQueue._rear.element, localQueue._rear.classification, localQueue._rear.t_type)
                        tagType.clear()
                    else:

                        globalQueue.insert(current.element, current.classification, tagType)
                        print(globalQueue._rear.element, globalQueue._rear.classification, globalQueue._rear.t_type)
                        tagType.clear()
                    sem = 1
                current = current._next
                    
            case 3:
                if current.classification == "identifier":
                    
                    if localQueue.search(current.element):
                        statement += current.element
                        idType = localQueue.getType(current.element)
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
                        print(current.element + " does not exist within this scope")
                elif "integer" and "double" in tagType:
                    print(statement + " does not have compatible type")
                    break
                elif current.element in relop:
                    statement += current.element
                    tagType.append(current.classification)
                elif current.element == "then":
                    if scope == "local":
                        localQueue.insert(statement, "bool", tagType)
                        print(localQueue._rear.element, localQueue._rear.classification, localQueue._rear.t_type)
                        tagType.clear()
                    else:

                        globalQueue.insert(statement, "bool", tagType)
                        print(globalQueue._rear.element, globalQueue._rear.classification, globalQueue._rear.t_type)
                        tagType.clear()
                    sem = 1 
                current = current._next
