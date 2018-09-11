def discriminant_roots(a, b, c):
     discriminant = b**2 - 4 * (a * c)
     if discriminant < 0:
        return "уравнение не имеет корней"
     elif discriminant == 0:
        x = -b / (2 * a)
        return "уравнение имеет один корень: " + str(x)
     else:
        x_1 = (-b + (discriminant**(1/2))) / (2 * a)
        x_2 = (-b - (discriminant**(1/2))) / (2 * a)
        return "уравнение имеет два корня: " + str(x_1) + ", " + str(x_2)
def even_roots(a, b, c):
    if b%2 != 0:
        return "неверный ввод(коэффициент b не чётный)"
    else:
        k = b/2
        discriminant = ((k**2) -(a*c))*4
        if discriminant > 0:
            x_1 = (-k + ((k**2 - a*c))**1/2) /  a
            x_2 = (-k - ((k**2 - a*c))**1/2) /  a
            return "уравнение имеет два корня: " + str(x_1) + ", " + str(x_2)
        elif discriminant == 0:
            x = -k / a
            return "уравнение имеет один корень: " + str(x)
        elif discriminant < 0:
            return "уравнение не имеет корней"
def incomplete_roots(a, b, c):
    if b == 0 and c ==0:
        return "уравнение имеет один корень: 0"
    elif b == 0 and c != 0:
        if -c / a >0:
            x_1 = (-c / a)**1/2
            x_2 = (c / a)**1/2
            return "уравнение имеет два корня: " + str(x_1) + ", " + str(x_2)
        else:
            return "уравнение не имеет вещественных корней"
    elif b != 0 and c ==0:
        x_2 = -b/a
        return "уравнение имеет два корня: " + 0 + ", " + str(x_2)
def quadratic_equation(a, b, c):
    if b == 0 or c ==0:
        return incomplete_roots(a, b, c)
    elif b%2 == 0:
        return even_roots(a, b, c)
    else:
        return discriminant_roots(a, b, c)