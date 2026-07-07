import numpy as np

v1 = np.array([2, 5, 4, 7])
print(4 * v1)   # 스칼라곱: 방향은 그대로, 크기는 4배

v2 = np.array([4, 1, 0, 2])
print(v1 + v2)

print([2, 5, 4, 7] + [4, 1, 0, 2])
print(np.array([2, 5, 4, 7]) + np.array([4, 1, 0, 2]))
# 파이썬 list와 np.array의 차이, 리스트는 나열이고 np.array는 벡터합

v3 = 4 * v1 - 2 * v2    # 스칼라곱 + 원소별 뺄셈
print("v3 =", v3)