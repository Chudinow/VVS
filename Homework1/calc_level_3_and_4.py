import math as m

class Calculation:

    def __init__(self, num1 : int, num2 : int, oper, operation, corner : int):
        self.num1 = num1
        self.num2 = num2
        self.oper = oper
        self.operation = operation
        self.corner = corner

    def calculator_main(self) -> int:
        if oper == '+':
            return num1+num2
        elif oper == '-':
            return num1-num2
        elif oper == '*':
            return num1*num2
        elif oper == '/' and num2 != 0:
            return num1//num2
        else:
            return 'Ошибка!'
    def calculator_ingener(self) -> int:
        if operation == "cos":
            return m.cos(corner)
        elif operation == "sin":
            return m.sin(corner)

print("Выберите тип Main или Ingener")
type = input()
if type == "Main":
    print("Введите 2 числа:")
    num_1, num_2 = int(input()), int(input())
    print("Введите операцию:")
    oper = input()
    answer = Calculation(num1, num2, oper, 0, 0)
    print(answer.calculator_main())
elif type == "Ingener":
    print("Введите операцию")
    operation = input()
    print("Введите угол")
    corner = int(input())
    answer = Calculation(0, 0, 0, operation, corner)
    print(answer.calculator_ingener())
