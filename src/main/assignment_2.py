import numpy
import numpy as np

if __name__ == '__main__':
    # Question 1, using the Neville's Method
    # List out all the x and y values and the approximate value x
    x_0 = 3.6
    x_1 = 3.8
    x_2 = 3.9
    y_0 = 1.675
    y_1 = 1.436
    y_2 = 1.318
    x = 3.7

    # Using the Neville's method to find Q1,1
    p = x_1 - x_0
    q = (x - x_0) * y_1
    r = (x - x_1) * y_0
    Q11 = (q - r) / p

    # Using the Neville's method to find Q2,1
    s = x_2 - x_1
    t = (x - x_1) * y_2
    u = (x - x_2) * y_1
    Q21 = (t - u) / s

    # Using the Neville's method to find Q2,2, the 2nd degree interpolating value
    v = x_2 - x_0
    w = (x - x_0) * Q21
    y = (x - x_2) * Q11
    Q22 = (w - y) / v
    print(Q22, "\n")

    # Question 2
    # Listing all the x and y values
    x0 = 7.2
    x1 = 7.4
    x2 = 7.5
    x3 = 7.6
    y0 = 23.5492
    y1 = 25.3913
    y2 = 26.8224
    y3 = 27.4589

    # using Newton's forward method formula to find degree 1
    degree1 = (y1 - y0) / (x1 - x0)

    # using Newton's forward method formula to find degree 2
    a = (y2 - y1) / (x2 - x1)
    b = degree1
    c = x2 - x0
    degree2 = (a - b) / c

    # using Newton's forward method formula to find degree 3
    d = (y3 - y2) / (x3 - x2)
    e = x3 - x1
    f = (d - a) / e
    g = degree2
    h = x3 - x0

    degree3 = (f - g) / h

    # Setting the precision of numpy so the output comes out correctly
    numpy.set_printoptions(precision=20)
    k = np.array([degree1, degree2, degree3])
    q2 = list(k)
    print(q2, "\n")

    # Question 3
    # Approximating f(7.3) using each of the polynomials
    m = degree1 * (7.3 - x0)
    n = degree2 * (7.3 - x0) * (7.3 - x1)
    o = degree3 * (7.3 - x0) * (7.3 - x1) * (7.3 - x2)
    p1 = y0 + m
    p2 = p1 + n
    p3 = p2 + o
    print(p3, "\n")

    # Question 4
    print("no answer", "\n")

    # Question 5
    print("no answer", "\n")
