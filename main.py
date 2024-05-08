number = int(input("Введіть 5-ти значне ціле число: "))


digit1 = number % 10

number //= 10
digit2 = number % 10

number //= 10
digit3 = number % 10

number //= 10
digit4 = number % 10

number //= 10
digit5 = number


reversed_number = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5
print("Зворотнє число:", reversed_number)