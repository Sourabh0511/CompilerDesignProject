import pickle
import sys
'''
with open('symbol_table.pickle', 'rb') as handle:
    symbol = pickle.load(handle)

def print_symbol_table():
    print("*" * 50)
    for i in symbol:
        print("Variable name = ", i['name'])
        print("Type = ", i['type'])
        print("Value = ", i['value'])
        print("width = ", i['width'])
        print("scope = ", i['scope'])
        print("*" * 25)
    print("*" * 50)

print("Symbol Table!!")
print_symbol_table()
'''
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

lines2 = []

for i in lines:
    if(i):
        lines2.append(i)

def solve(operands , operation):
    if(operation == '+'):
        return operands[0] + operands[1]
    elif(operation == '-'):
        return operands[0] - operands[1]
    elif(operation == '/'):
        return operands[0] / operands[1]
    elif(operation == '*'):
        return operands[0] * operands[1]
    elif(operation == '%'):
        return operands[0] % operands[1]
    elif(operation == '&&'):
        return operands[0] and operands[1]
    elif(operation == '||'):
        return operands[0] or operands[1]
    elif(operation == '^'):
        return operands[0] ^ operands[1]
    elif(operation == '=='):
        return operands[0] == operands[1]
    elif(operation == '!='):
        return operands[0] != operands[1]
    elif(operation == '<'):
        return operands[0] < operands[1]
    elif(operation == '>'):
        return operands[0] > operands[1]
    elif(operation == '<='):
        return operands[0] <= operands[1]
    elif(operation == '>='):
        return operands[0] >= operands[1]


op = ['+', '-', '/', '*', '%', '&&', '||', '^', '==', '!=', '<', '>', '>=', '<=']

def constant_fold():
    for i in range(len(lines2)):
        x = lines2[i].split('=')
        if(len(x) == 2):
            expr = x[-1]
            numbers = 0
            operation = ''
            for j in expr:
                if(j in op):
                    operation += j
                    break
            if(operation):
                operand_list = expr.split(operation)
                operands = []
                try:
                    int(operand_list[0])
                    if(int(operand_list[0]) == float(operand_list[0])):
                        operands.append(int(operand_list[0]))
                    else:
                        operands.append(float(operand_list[0]))
                except:
                    #print("operand 1 is not constant!!")
                    pass
                try:
                    int(operand_list[1])
                    if(int(operand_list[1]) == float(operand_list[1])):
                        operands.append(int(operand_list[1]))
                    else:
                        operands.append(float(operand_list[1]))
                except:
                    #print("operand 2 is not constant!!")
                    pass
                if(len(operands) == 2):
                    res = solve(operands, operation)
                    print(x[0], "=", res)
                else:
                    print(lines2[i])
            else:
                print(lines2[i])
        else:
            print(lines2[i])

print("\n\nAFTER CONSTANT FOLDING\n\n")
constant_fold()
print("\n")
