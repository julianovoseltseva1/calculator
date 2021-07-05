operation = input('''Будь-ласка оберіть операцію, яку хочете виконати: 
+ для додавання 
- для віднімання 
* для множення 
/ для ділення
** для піднесення до степеня (2 число є степінь)
''')
number_1 = int(input('Введіть перше число:'))
number_2 = int(input('Введіть друге число:'))
if operation  == '+':
    print('{} + {} = '.format(number_1, number_2))
    print('number_1 + number_2')
elif operation == '-':
    print("{} - {} = ".format(number_1, number_2))
    print(number_1 - number_2)
elif operation == "*":
    print("{} * {} = ".format(number_1, number_2))
    print(number_1 * number_2)
elif operation == "/":
    print("{} / {} = ".format(number_1, number_2))
    print(number_1 / number_2)
elif operation == '**':
    print ('{} ** {} ='.format(number_1, number_2))
    print (number_1 ** number_2)
else:
    print (' Такої операції не існує, будь ласка почніть спочатку')
