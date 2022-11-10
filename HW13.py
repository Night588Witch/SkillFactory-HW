numtic = int(input('Введите количество билетов, которые хотите приобрести:'))
cost = 0
for i in range(numtic):
        age = int(input('Введите ваш возраст:'))
        if age < 18:
            cost = cost + 0
        elif 18 < age < 21:
            cost = cost + 990
        else:
            cost = cost + 1390
if numtic > 3:
    cost = cost*0.9
print(round(cost))
