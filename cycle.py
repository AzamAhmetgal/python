# counter = 1
# while counter < 6:
#     print(counter)
#     counter += 1
    
# sandwich = 0
# while sandwich < 5:
#     sandwich += 1
#     print(f"Сделал {sandwich}-й бутер")
    
# sandwich = 4
# while sandwich < 15:
#     sandwich += 1
#     print(f"Сделал {sandwich}-й бургер")

# import time
# number = 60
# while number > 0:
#     time.sleep(0.1)
#     print(f"{number}...")
#     number -= 1
#     if number == 8:
#         continue
#     print("Время кончается")
#     if number == 0:
#         print("TIME IS OVER!")

rain = True

while rain:
    print("Сижу дома")
    stop = input("Дождь кончился? (да/нет): ")
    if stop.lower() == "да":
        print("Выхожу из дома")
        break
    elif stop.lower() == "нет":
        print("Сижу дома")
        break
    else:
        print("Такой команды нет, гений!")