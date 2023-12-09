def plus(user_number, user_number2):
    return user_number + user_number2
def minus(user_number, user_number2):
    return user_number - user_number2
def multiply(user_number, user_number2):
    return user_number * user_number2
def divide(user_number, user_number2):
    if user_number2 == 0:
        print("На ноль нельзя делить, гений!")
    else:
        return user_number / user_number2
def step(user_number, user_number2):
    return user_number ** user_number2
def maroot(user_number):
    return round(user_number ** 0.5, 2)
def input_number(input_phrase):
    user_number = input(input_phrase)
    if not user_number.isdigit():
        print("Это не число, гений!")
        return input_number(input_phrase)
    return int(user_number)

while True:
    user_number = input_number("Введите первое число: ")
    user_o = input("Введите операцию (+, -, *, /, ^ [степень], @ [корень]): ")
    if user_o != "@":
        user_number2 = input_number("Введите второе число: ")
    
    if user_o == "+":
        result = plus(user_number, user_number2)
        print(f"{user_number} + {user_number2} = {result}")
    elif user_o == "-":
        result = minus(user_number, user_number2)
        print(f"{user_number} - {user_number2} = {result}")
    elif user_o == "*":
        result = multiply(user_number, user_number2)
        print(f"{user_number} * {user_number2} = {result}")
    elif user_o == "/":
        result = divide(user_number, user_number2)
        if result is not None:
            print(f"{user_number} / {user_number2} = {result}")
    elif user_o == "^":
        result = step(user_number, user_number2)
        print(f"{user_number} ^ {user_number2} = {result}")
    elif user_o == "@":
        result = maroot(user_number)
        print(f"√{user_number} = {result}")
    else:
        print(f"Такой команды в меню нет ({user_o}).")
   
