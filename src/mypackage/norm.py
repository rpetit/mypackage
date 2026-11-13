import numpy as np


def norm(x, y, ord=2):
    if ord == 2:
        res = np.sqrt(x**2 + y**2)
    elif ord == 1:
        res = np.abs(x) + np.abs(y)
    else:
        raise ValueError("The only values allowed for ord are 1 and 2")
    print(f"l{ord} norm: {res}")
    return res
