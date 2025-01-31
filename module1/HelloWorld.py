import sys

from matplotlib import pyplot as plt

if __name__ == '__main__':
    print("echo")
    a = [1, 2, 3, 4]
    b = [-1, 2, -3, 4]
    print("a=", a, "b=", b)
    plt.plot(a, b)
    plt.show()
    print(sys.version)
