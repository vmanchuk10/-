s = "GATATATGCATATACTT"  # если я хочу ввести строку с клавиатуры, то буду использовать input
t = "ATAT"

if len(s) == 1000:
    print("Строка имеет длину ровно 1 килобазу")
elif len(s) > 1000:

    print("Строка превышает длину 1 килобазы,")
    s = input("Введите другую последовательность:")
else:
    print("Строка короче 1 килобазы")


def positionsall(s, t):

    positions = []
    start = 0

    while True:
        index = s.find(t, start)
        if index == -1:
            break
        positions.append(index)
        start = index + 1

    return positions


positions = positionsall(s, t)
print("Индексы всех вхождений:", positions)
