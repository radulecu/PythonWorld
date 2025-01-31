import logging


def zero_division():
    global e
    try:
        logging.info("division result is 1")
        i = 1 / 0
    except ZeroDivisionError:
        logging.error("error %s", "err", exc_info=True, stack_info=True)


def naming_error():
    global e
    try:
        a = b + 3
    except NameError:
        logging.error("naming error", exc_info=True, stack_info=True)


def index_error():
    global e
    try:
        l1 = [1, 2, 3]
        logging.info("element at index 5 is %s", l1[5])
    except IndexError:
        logging.error("naming error", exc_info=True, stack_info=True)


def multiple_error():
    global e
    try:
        l1 = [1, 2, 3]
        logging.info("element at index 5 is %s", l1[5])
    except (IndexError, NameError, ZeroDivisionError):
        logging.error("multiple error", exc_info=True, stack_info=True)


def compute_multiplication():
    try:
        a = float(input("Please enter a number to divide a "))
        b = float(input("Please enter a number to divide b "))
        c = a / b
        logging.info("%f / %f = %f", a, b, c)
    except ValueError:
        logging.error("value error", exc_info=True, stack_info=True)
    except ZeroDivisionError:
        logging.error("zero division error", exc_info=True, stack_info=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    zero_division()
    print()

    naming_error()
    print()

    index_error()
    print()

    multiple_error()
    print()

    compute_multiplication()
    print()
