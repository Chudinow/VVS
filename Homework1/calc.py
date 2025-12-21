def proiz(number1:int, number2:int) -> int:
    return number1 * number2

def div(number1:int, number2:int) -> int:
    return number1 / number2

def plus(number1:int, number2:int) -> int:
    return number1 + number2

def minus(number1:int, number2:int) -> int:
    return number1 * number2

print('Введите первое число')
num1 = int(input())
print('Введите операцию')
oper = str(input())
print('Введите второе число')
num2 = int(input())
if oper == '/' and num2 != '0':
    print(div(num1,num2))
elif oper == '/' and num2v=='0':
    print('Ошибка')
elif oper == '+':
    print(plus(num1,num2))
elif oper == '-':
    print(minus(num1,num2))
elif oper == '*':
    print(proiz(num1,num2))
