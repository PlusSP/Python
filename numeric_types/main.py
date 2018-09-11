import square
import rectangle
import parallelogram
import degree
import radian
import year
import quadratic_equation

if __name__ == '__main__':
    user_input = input('''для вычисления площади квадрата введите: 1
        для вычисления площади прямугольника введите: 2
        для вычисления площади параллелограмма введите: 3
        для перевода градусов в радианы введите: 4
        для перевода радиан в градусы введите: 5
        для определения високосного года введите: 6
        для вычисления корней квадратного уравнения введите: 7
        : ''')
    if user_input == '1':
        user_input = input('введите сторону квадрата для вычисления площади: ')
        print("площадь квадрата = " , square.square(user_input))
    if user_input == '2':
        user_input1 = input('введите первую сторону прямоугольника: ')
        user_input2 = input('введите вторую сторону прямоугольника: ')
        print("площадь прямоугольника = " , rectangle.rectangle(user_input1,user_input2))
    if user_input == "3":
        user_input1 = input('введите длину основания параллелограмма: ')
        user_input2 = input('введите высоту параллелограмма: ')
        print("площадь параллелограмма равна: " , parallelogram.parallelogram(user_input1,user_input2))
    if user_input == "4":
        user_input = input('введите угол для перевода в радианы: ')
        print('угол равняется ', degree.degree_to_radian(user_input), "радиан")
    if user_input == "5":
        user_input = input('введите радианы для перевода в градусы: ')
        print('угол равняется ', radian.radian_to_degree(user_input), "градусов")
    if user_input == "6":
        user_input = int(input('введите год: '))
        print('год', year.year(user_input))
    if user_input == '7':
        user_input = int(input('введите коэффициент а квадратного уравнения: '))
        user_input1 = int(input('введите коэффициент b квадратного уравнения: '))
        user_input2 = int(input('введите коэффициент c квадратного уравнения: '))
        print(quadratic_equation.quadratic_equation(user_input, user_input1, user_input2))
    else:
        print("неверный ввод")