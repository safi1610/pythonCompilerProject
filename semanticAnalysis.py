import token_1 as t
import semanticAnalyzer as san

tlLine = t.Queue()
localQueue = san.semanticTable()

def analyseSemantics(tokenQueue):
    sem = 0
    scope = []
    relop = ["<", ">", "<=", ">=", "<>", "=="]
    current = tokenQueue._front
    illegal = ""
    statement = ""
    while current is not None:
        match sem:
            case 0:
                if current.element == "def":
                    scope.append("func")
                    sem = 1
                if current.classification == "type":
                    if current.element == "int":
                        scope.append("integer")
                    else:
                        scope.append("double")
                    sem = 2
                if current.classification == "identifier":
                    if localQueue.search(current.element):
                        statement += current.element
                        scope.append(current.classification)
                        sem = 3
                    else:
                        print(current.element + "does not exist within this scope")

                current = current._next
            case 1:
                if current.classification == "type": 
                    if current.element == "int":
                        scope.append("integer")
                    else:
                        scope.append("double")
                    sem = 2
                current = current._next
            case 2:
                if current.classification == "identifier":
                    localQueue.insert(current.element, current.classification, scope)
                    scope.clear()
                    sem = 0
                current = current._next
            case 3:
                if current.element in relop:
                    statement += current.element
                    scope.append(current.classification)
                else:
                    localQueue.insert(statement, "bool", scope)
                    scope.clear()
                    statement = ""
                sem = 0
                current = current._next
                    

