x = int(input('Введите координату точки по X: '))
y = int(input('Введите координату точки по Y: '))
if x == 0 or y == 0 :
    print('Вы ввели некорректные данные, повторите попытку')
elif x > 0 and y > 0 :
    print('1')
elif x < 0 and y > 0 :
    print('2')
elif x < 0 and y < 0 :
    print('3')
else:
    print('4')