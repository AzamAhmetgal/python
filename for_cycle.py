# user_diapozon = int(input("Введите начальное число диопозона: "))
# user_diapozon = int(input("Введите конечное число диопозона: "))
# for i in range(user_diapozon):
#     print("Silence is golden")

# for i in range(10, 51, 10):
#     print(i)


for i in "Andromeda":
    print(i)
    
menu = [
    "Цезарь",
    "Бургер",
    "Сэндвич",
    "Шашлык",
    "Шаурма",
    "Суши"
]
menu[3] = "Тофу" #Замена элеиента по индексу
for dish in menu:
    print(f"{dish} - это вкусно.")
    