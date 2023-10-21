salary = 6900
veg_sale = 0.7
cucumber = 90
tomato = 150
strawberry = 385
cookies = 140 + 140

buy = (cucumber * 5 + tomato * 4) * veg_sale + cookies #сумма покупки
print(f"У таксиста Вани из {salary} рублей после траты {buy} рублей осталось лишь {salary - buy}")

print(10 // 3) #целочисленное деление
print(10 % 3) #остаток от деления

left = salary - buy
stock = 134.65
travel = 36

print(f"Таксист Ваня сможет купить {left // stock} акций")
print(f"У таксиста Вани останется {int(left % stock)} рублей, проезд стоит {travel} рублей")

side = int(input("Введите длину квадрата: "))
s = side * side
print(f"Площадь квадрата со стророной {side} равна {s}")
p = side * 4
print(f"Периметр квадарата со стороной {side} равна {p}")

