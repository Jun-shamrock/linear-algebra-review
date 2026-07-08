import numpy as np
import matplotlib.pyplot as plt

v = np.array([1, 2])

plt.plot([0, v[0]], [0, v[1]], 'k-', label='Original vector') 
# matplot은 x들 따로, y들 따로 받음
# [0, 1] -> x 좌표들
# [0, 2] -> y 좌표들
# (0, 0), (1, 2)가 점들이 됨

for i in range(10):
    s = np.random.randn()
    sv = s * v
    plt.plot([0, sv[0]], [0, sv[1]], 'r-')  # r은 빨강, -는 실선

plt.grid(True)                          # 격자 표시
plt.legend()                            # 범례 켜기
plt.axis([-6, 6, -6, 6])                # 축 고정
plt.title('Randomly Scaled Vectors')    # 제목
plt.show()