from symtable import Symtable
from scanner import *
from programinternalform import PIF


if __name__ == "__main__":
    symtable = Symtable(17)
    pif = PIF()
    scanner = Scanner()
    fileName = "p1err.txt"
    exceptionMessage = ""
    with open(fileName, 'r') as file:
        lineCounter = 0
        for line in file:
            lineCounter += 1
            tokens = scanner.tokenize(line.strip())
            extra = ''
            for i in range(len(tokens)):
                if tokens[i] in scanner.operators + scanner.separators + scanner.reserved_words:
                    if tokens[i] == ' ':
                        continue
                    pif.add(tokens[i], (-1, -1))
                elif scanner.is_identifier(tokens[i]):
                    id = symtable.add(tokens[i])
                    pif.add("id", id)
                elif scanner.is_constant(tokens[i]):
                    const = symtable.add(tokens[i])
                    pif.add("const", const)
                else:
                    exceptionMessage += 'lexical error at token ' + tokens[i] + ', on line ' + str(lineCounter) + ".\n"

    with open('st.out', 'w') as writer:
        writer.write(str(symtable))

    with open('pif.out', 'w') as writer:
        writer.write(str(pif))

    if exceptionMessage == '':
        print("given program is lexically correct.")
    else:
        print(exceptionMessage)
