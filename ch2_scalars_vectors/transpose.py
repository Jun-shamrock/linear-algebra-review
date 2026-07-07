import numpy as np

row = np.array([[2, 5, 4, 7]])  # 대괄호 2개 = 2차원
print(row.shape)    # shape는 (행, 열) 튜플로 나옴
print(row.T)        # .T = transpose, 행벡터를 열벡터로 세움
print(row.T.shape)  # 뒤집혀서 (1, 4) -> (4, 1)