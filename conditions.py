# exp = 2 + 2 == 4 
# print(exp)
# print(type(exp)) # bool - логический (Ttrue / False)
# if exp:
#     print("Вы видите эту строку")

# age = int(input("Введите свой возраст: "))
# if age == 14:
#     print("Тебе 14 лет")
# if age >= 14:
#     print("Вам 14 лет или больше этого")
# if age <= 14:
#     print("Вам меньше 14-ти лет или у вас такой же возраст")
# if age != 14:
#     print("Тебе не 14")
    
# number = int(input("Введите число: "))
# if number % 2 == 1:
#     print("Число нечетное")
# else:
#     print("Число четное")
    
temp = int(input("Введите температуру воздуха: "))
if temp < 0:
    print("Холодно")
elif temp < 15:
    print('Прохладно')
elif temp < 20:
    print("Тепло")
elif temp < 30:
    print("Жарко")
else:
    print("...Press F to pay respect...")