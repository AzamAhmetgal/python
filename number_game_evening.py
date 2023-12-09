import random
print('Добро пожаловать в игру "Угадай число".')
print("Угадайте число от 1-ого до 100-а.")
secret_num = random.randint(1, 100)
attempts = 10
while attempts != 0:
    print(f"У вас осталось {attempts} попыток")
    user_number = input("Введите число: ")
    if "Джедай" in user_number:
        print("Поздравляю! Вы нвшли пасхалку! Да прибудет с вами сила и успешно пройденный ноябрь")
    elif "Покажи число" in user_number:
        print(f"Вы ввели чит-код. Секретное число - {secret_num}")
    if not user_number.isdigit():
        print("Тебя просили ввести число, а не буквы; гений!") 
        continue
    user_number = int(user_number)
    attempts -= 1
    
    if user_number > secret_num:
        print("Загаданое число меньше.")
    elif user_number < secret_num:
        print("Загаданное чилсо больше.")
    elif user_number == secret_num:
        print("Вы угадали число.")
        break
    if attempts == 0:
        print(f"Вы проиграли. Правильный ответ: {secret_num}")
        break
    