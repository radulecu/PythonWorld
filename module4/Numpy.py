import logging as log

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    log.basicConfig(level=log.INFO)
    a = np.array([1.13, 3.14, 2, 9, 14])
    log.info(f"a={a}, and is of type {type(a)} and contains data of type {a.dtype}")
    log.info(f"a has size {a.size} and dim {a.ndim} and shape {a.shape}")
    a[1] = 314
    log.info(f"a si now {a}")
    log.info(f"a[1:4] is now {a[1:4]}")
    log.info(f"a[:4] is {a[:4]}")
    log.info(f"a[4:] is {a[4:]}")
    log.info(f"a[[0, 4, 1, 3, 2]] is {a[[0, 4, 1, 3, 2]]}")
    log.info(f"a[1:5:2] is {a[1:5:2]}")
    a[3:6] = 90, 140
    log.info(f"a si now {a}")

    b1 = np.array([[100., 101], [110, 111]])
    b2 = np.array([[200., 201], [210, 211]])

    log.info(f"b1={b1}, and is of type {type(b1)} and contains data of type {b1.dtype}")
    log.info(f"b1 has size {b1.size} and dim {b1.ndim} and shape {b1.shape}")
    log.info(f"{b1} transposed is {b1.T}")
    log.info(f"b1[1, 1] is {b1[1, 1]}")
    log.info(f"b1[1][1] is {b1[1][1]}")
    log.info(f"b1[1, 0:2] is {b1[1, 0:2]}")
    log.info(f"b1[1][0:2] is {b1[1][0:2]}")
    log.info(f"b1[0:2, 1] is {b1[0:2, 1]}")
    log.info(f"b1[0:2][1] is {b1[0:2][1]}")

    log.info(f"sum of {b1} and {b2} is {b1 + b2}")
    log.info(f"difference of {b1} and {b2} is {b1 - b2}")
    log.info(f"multiplication of {b1} and {b2} is {b1 * b2}")
    log.info(f"division of {b1} and {b2} is {b1 / b2}")
    log.info(f"dot multiplication of b1={b1} and b2={b2} is np.dot(b1 * b2)={np.dot(b1, b2)}")
    log.info(f"addition of {b1} with a scalar 200 is {b1 + 200}")
    log.info(f"multiplication of {b1} with a scalar 2 is {b1 * 2}")
    log.info(f"multiplication of {b1} with a scalar 2 is {b1 * 2}")

    log.info(f"min of {b1} is {np.min(b1)}")
    log.info(f"max of {b1} is {np.max(b1)}")
    log.info(f"mean of {b1} is {np.mean(b1)}")
    log.info(f"standard deviation (std) of {b1} is {np.std(b1)}")

    c = [0, np.pi / 2, np.pi]
    log.info(f"sin of {c} is {np.sin(c)}")

    log.info(f"np.linspace(0, 2, num=5) = {np.linspace(0, 2, num=5)}")
    log.info(f"np.linspace(1, 3, num=7) = {np.linspace(1, 3, num=7)}")

    x = np.linspace(0, 2 * np.pi, 361)
    log.info(f"np.linspace(0, 2 * np.pi, 361) = {x}")
    sinx = np.sin(x)
    log.info(f"np.sin(np.linspace(0, 2 * np.pi, 361)) = {sinx}")
    plt.plot(x, sinx)
    plt.show()

    d1 = np.array([[0, 1, 1], [1, 0, 1]])
    d2 = np.array([[1, 1], [1, 1], [-1, 1]])
    log.info(f"dot multiplication between {d1} and {d2} is {np.dot(d1, d2)}")
