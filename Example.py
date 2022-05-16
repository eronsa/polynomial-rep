from polynomial import Polynomial

if __name__ == "__main__":

    p1 = Polynomial(1, 2, 3, 4)  # x³ + 2x² + 3x + 4
    p2 = Polynomial(2, 3, 2)  # 2x² + 3x + 2
    print(p1 + p2)  # outputs 4x³ + 6x² + 6x + 1
