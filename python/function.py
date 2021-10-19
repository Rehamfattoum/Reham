def sum (number1,number2):
    return number1 + number2
def min (number1,number2) :
    return number1-number2
def multi (number1,number2):
    return number1*number2
def div (number1,number2):
    try:
        return number1/number2
    except ZeroDivisionError :
        print ("please don't enter Syntax ")
        sys.exit (0)
    