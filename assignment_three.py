# Kevin Chen
# 09/20/17
# assignment three
# this is a program can calculate two roots of quadratic function


def print_instruction():
    """
    this function takes no parameters, no return values.
    :return:none
    """
    print("This program will calculate two roots of quadratic function")
    print("please enter three coefficients")


def first_coefficient():
    """
    takes no parameters. return the first_coefficient as float. Get input from user.
    :return: first_coefficient
    """
    a = input("enter a:")
    return float(a)


def second_coefficient():
    """
    takes no parameters. return the second_coefficient as float. Get input from user.
    :return: second_coefficient
    """
    b = input("enter b:")
    return float(b)


def third_coefficient():
    """
    takes no parameters. return the third_coefficient as float. Get input from user.
    :return: third_coefficient
    """
    c = input("enter c:")
    return float(c)


def quadratic_function(a, b, c):
    """
takes three parameters. return nothing
    :param a:first_coefficient
    :param b:second_coefficient
    :param c:thir_coefficient
    :return:none
    """
    root1 = (-b + ((b ** 2 - 4 * a * c) ** .5)) / (2 * a)
    root2 = (-b - ((b ** 2 - 4 * a * c) ** .5)) / (2 * a)
    print("two roots is", root1, root2)


def main():
    print_instruction()
    a = first_coefficient()
    b = second_coefficient()
    c = third_coefficient()
    quadratic_function(a, b, c)


main()
