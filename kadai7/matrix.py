import numpy as np

def ex4():
    a = np.array([[1, 2], [3, 4]])  # 左上右上左下右下
    b = np.array([[3, 2], [0, -1]])
    e = np.eye(2)  # 単位行列
    o = np.zeros((2, 2))  # 零行列

    result_1 = 3 * b

    result_2 = 2 * a - b

    result_3 = a + b

    identity_matrix = e
    zero_matrix = o

    print(f"---(4-1)----\n{result_1}\n")
    print(f"---(4-2)----\n{result_2}\n")
    print(f"---(4-3)----\n{result_3}\n")
    print(f"---(4-4)----\n単位行列:\n{identity_matrix}\n零行列:\n{zero_matrix}\n")

def ex5():
    a = np.array([[1, 2], [2, 1]])
    b = np.array([[1, 1], [2, -1]])
    e = np.array([[1, 0], [0, 1]])

    result_1 = np.dot(a, b)
    result_2 = np.dot(a, e)

    print(f"---(5-1)----\n{result_1}\n")
    print(f"---(5-2)----\n{result_2}\n")

    a = np.array([[1, 2], [0, 1], [1, 0]])
    b = np.array([[0, 0, 1], [1, 0, 1], [1, 0, 0]])
    c = np.array([[1], [3], [0]])
    d = np.array([[0, 1, 0]])

    result_3 = np.dot(b, a)
    result_4 = np.dot(d, c)
    result_6 = np.dot(b, c)

    print(f"---(5-3)----\n{result_3}\n")
    print(f"---(5-4)----\n{result_4}\n")
    print(f"---(5-6)----\n{result_6}\n")

def ex6():
    A = np.array([[2, 3], [5, -2]])  # 係数行列 A
    B = np.array([31, 30])  # 定数ベクトル

    result_1 = A  # 係数行列A
    result_2 = np.linalg.inv(A)  # 係数行列Aの逆行列
    result_3 = np.dot(result_2, B)  # 連立方程式の解

    print(f"---(6-1)----\n{result_1}\n")
    print(f"---(6-2)----\n{result_2}\n")
    print(f"---(6-3)----\n{result_3}\n")

def main():
    ex4()
    ex5()
    ex6()

if __name__ == "__main__":
    main()