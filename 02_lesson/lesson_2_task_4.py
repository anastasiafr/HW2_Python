def fizz_buzz(n):
    for m in range(1, n+1):
        if m % 3 == 0 and m % 5 == 0:  # Проверка на кратность 3 и 5
            print("FizzBuzz")
        elif m % 3 == 0:               # Проверка на кратность 3
            print("Fizz")
        elif m % 5 == 0:               # Проверка на кратность 5
            print("Buzz")
        else:
            print(m)


n = int(input("Введите число: "))
fizz_buzz(n)
