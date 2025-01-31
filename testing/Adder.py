import logging


class Adder:
    a: int
    b: int

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def result(self):
        return self.a + self.b


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    a = 10
    b = 20
    r = Adder(a, b).result()
    logging.info(f"{a} + {b} = {r} ")
