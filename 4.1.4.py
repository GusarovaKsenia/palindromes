def f(x):
    return x[::-1] == x
b = input('Введите строку:')
if f(b) is True:
    print('true')
else:
    print('false')
