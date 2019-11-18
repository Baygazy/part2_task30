spisok = input("Введите несколько одинаковых слов: ").split()
bylo = []
for i in spisok:
    if i not in bylo:
        print(i, spisok.count((i)))
    bylo.append(i)
