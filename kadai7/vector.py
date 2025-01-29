from scipy.spatial import distance
import numpy as np

def ex1():
    p1 = (0,0,0)
    p2 = (1,4,-3)
    dist_scipy = distance.euclidean(p1, p2)
    print(f"---(1-1)----\n{dist_scipy}")

    p1 = (1,4,-3)
    p2 = (-1,3,2)
    dist_scipy = distance.euclidean(p1, p2)
    print(f"---(1-2)----\n{dist_scipy}")

def ex2():
    a = np.array([1, 2, 3])
    b = np.array([2, 3, 1])
    c = np.array([3, 1, 2])
    
    # 1. cの大きさ (ノルム)
    magnitude_c = np.linalg.norm(c)

    # 2. a + b
    sum_ab = a + b

    # 3. a + b + c
    sum_abc = a + b + c

    # 4. a + 2b - 3c
    result_4 = a + 2 * b - 3 * c

    # 5. dの計算: 平行四辺形の4つ目の点
    # d = a + b - c
    d = a + b - c

    print(f"---(2-1)----\n[{magnitude_c:.6f}]")
    print(f"---(2-2)----\n{sum_ab}")
    print(f"---(2-3)----\n{sum_abc}")
    print(f"---(2-4)----\n{result_4}")
    print(f"---(2-5)----\n{d}")

def ex3():
    a = np.array([1, 1, 0])
    b = np.array([2, 0, 2])

    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    dot_ab = np.dot(a, b)

    cos_theta = dot_ab / (magnitude_a * magnitude_b)
    angle_ab = np.degrees(np.arccos(cos_theta))

    cross_ab = np.cross(a, b)
    unit_vector = cross_ab / np.linalg.norm(cross_ab) if np.linalg.norm(cross_ab) != 0 else cross_ab

    print(f"---(3-1)----\n[{magnitude_a}]")
    print(f"---(3-2)----\n[{magnitude_b}]")
    print(f"---(3-3)----\n[{dot_ab}]")
    print(f"---(3-4)----\n[{angle_ab}]")
    print(f"---(3-5)----\n{unit_vector}")

def main():
    ex1()
    ex2()
    ex3()

if __name__ == "__main__":
    main()