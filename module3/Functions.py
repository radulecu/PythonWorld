def printHelloFunction():
    print(hello_function())


def hello_function():
    """
    :return: Hello Function
    """
    return "Hello Function"


def hello_parameter(name):
    """
    Test hello function
    :param name: input name
    :return: Hello + provided name parameter
    """
    return "Hello " + name


def increment(i):
    """
    Increment input number
    :param i: input value
    :return: incremented value
    """
    return i + 1


def add_numbers(iterable):
    """

    :param iterable: Iterable
    :return: sum of elements
    """
    sum = 0
    for i in iterable:
        sum += i
    return sum


def function_with_variadic_arguments(*arguments):
    print("Inside function with variadic arguments.", arguments, type(arguments))


def mult_2_numbers(a, b):
    return a * b


def mult_numbers(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def mult_numbers_with_start(start, *numbers):
    result = start
    for number in numbers:
        result *= number
    return result


def function_incrementing_global_variable():
    global global_val
    global old_global_val
    old_global_val = global_val
    global_val += 1


def sum_with_defaults(p1=0, p2=0):
    return p1 + p2


def print_all_pairs(**dict):
    print(dict, type(dict))
    for key in dict:
        print(key + ":" + str(dict[key]))


if __name__ == '__main__':
    help(hello_function)
    help(hello_parameter)
    help(increment)
    help(add_numbers)
    help(sum)
    help(sorted)
    printHelloFunction()
    print("hello_function()", "=", hello_function())
    print("hello_parameter('Parameter')", "=", hello_parameter('Parameter'))
    print("increment(1)", "=", increment(1))
    print("add_numbers((1, 3, 6))", "=", add_numbers((1, 3, 6)))
    print("add_numbers({1, 3, 6})", "=", add_numbers({1, 3, 6}))
    print("add_numbers([1, 3, 6])", "=", add_numbers([1, 3, 6]))
    function_with_variadic_arguments()
    function_with_variadic_arguments(10, "string", 3.14)
    print("mult(5, 6)", "=", mult_2_numbers(5, 6))
    print("mult(2, 3.14)", "=", mult_2_numbers(2, 3.14))
    print("mult(2, 'string')", "=", mult_2_numbers(2, 'string'))
    print("mult_2_numbers('string', 2)", "=", mult_2_numbers('string', 2))
    print("mult_numbers(2, 3, 5)", "=", mult_numbers(2, 3, 5))
    print("mult_numbers()", "=", mult_numbers())
    print("mult_numbers_with_start(2, 3, 5)", "=", mult_numbers_with_start(2, 3, 5))

    global_val = 5
    function_incrementing_global_variable()
    function_incrementing_global_variable()
    function_incrementing_global_variable()
    print("global_val", "=", global_val)
    print("old_global_val", "=", old_global_val)
    print()

    print("sum_with_defaults()", "=", sum_with_defaults())
    print("sum_with_defaults(2)", "=", sum_with_defaults(2))
    print("sum_with_defaults(2, 3)", "=", sum_with_defaults(2, 3))
    print()

    print_all_pairs(Country='Canada', Province='Ontario', City='Toronto')
    print_all_pairs(One=1, Two=2, Three=3)
