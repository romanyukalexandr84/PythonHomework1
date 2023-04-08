num = 0
while num < 100 or num > 999:
    num = int(input("Введите трехзначное число: "))
print("Сумма цифр введенного числа =", num % 10 + num//10 % 10 + num//100)
