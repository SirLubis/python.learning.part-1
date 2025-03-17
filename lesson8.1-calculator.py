num1 = input("Insert First Number : ")
num2 = input("Insert Second Number : ")
op = input("Insert Operation : ")

def calc():
    if not float(num1) and not float(num2) :
        return "Number or Operation Not Valid"
    elif op=="+":
        return ("Answer : " + str(float(num1)+float(num2)))
    elif op=="-":
        return ("Answer : " + str(float(num1)-float(num2)))
    elif op=="x"or op=="*" or op=="X":
        return ("Answer : " + str(float(num1)*float(num2)))
    elif op=="/":
        return("Answer : " + str(float(num1)/float(num2)))
    else:
        return "Ngetik kalkulator aja gabisa"
print(calc())