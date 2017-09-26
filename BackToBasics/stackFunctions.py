from FBPrep.Stacks import Stack


def parChecker(symbolString):
    mystack = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({[":
            mystack.push(symbol)
        else:
            if mystack.isEmpty():
                balanced = False
            else:
                top = mystack.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if balanced and mystack.isEmpty():
        return True
    else:
        return False


def matches(opener, closer):
    opensymbols = "({["
    closesymbols = ")}]"
    return opensymbols.index(opener) == closesymbols.index(closer)


print parChecker('(()))')
print parChecker('((()))')
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))


# convert integer values into binary numbers - divide by two algorithm
def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


print(divideBy2(42), bin(42))


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


    # Assume the infix expression is a string of tokens delimited by spaces. The operator tokens are *, /, +, and -,
    # along with the left and right parentheses, ( and ). The operand tokens are the single-character identifiers A, B,
    # C, and so on. The following steps will produce a string of tokens in postfix order.
    #
    # Create an empty stack called opstack for keeping operators. Create an empty list for output.
    # Convert the input infix string to a list by using the string method split.
    # Scan the token list from left to right.
    # If the token is an operand, append it to the end of the output list.
    # If the token is a left parenthesis, push it on the opstack.
    # If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append
    # each operator to the end of the output list.
    # If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already
    # on the opstack that have higher or equal precedence and append them to the output list.
    # When the input expression has been completely processed, check the opstack. Any operators still on the stack can
    # be removed and appended to the end of the output list.


def infixerPost(equation):
    pemdasMap = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    operStack = Stack()
    output = []
    equation2 = equation.split()

    for symbol in equation2:
        if symbol.isalnum():
            output.append(symbol)
        elif symbol == "(":
            operStack.push(symbol)
        elif symbol == ")":
            top = operStack.pop()
            while top != '(':
                output.append(top)
                top = operStack.pop()
        else:
            while (not operStack.isEmpty()) and (pemdasMap[operStack.peek()] >= pemdasMap[symbol]):
                output.append(operStack.pop())
            operStack.push(symbol)
    while (not operStack.isEmpty()):
        output.append(operStack.pop())
    print " ".join(output)


infixerPost("A * B + 1 * D")
infixerPost("( A + B ) * ( C + D )")
infixerPost("( A + B ) * C")
infixerPost("A + B * C")
