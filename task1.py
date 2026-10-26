negative = []
zero = []
positive = []

while True:
    user_input = input("Введите целое число (или оставьте пустым для завершения): ")

    if user_input == "":
        break

    number = int(user_input)

    if number < 0:
        negative.append(number)
    elif number == 0:
        zero.append(number)
    else:
        positive.append(number)

print("\nРезультат:")
for num in negative:
    print(num)
for num in zero:
    print(num)
for num in positive:
    print(num)