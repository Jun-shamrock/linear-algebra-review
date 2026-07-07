# ch02 - Scalars & Vectors

## 파일
- 01_element_wise.py : 스칼라곱, 원소별 연산, 리스트 vs array
- 02_transpose.py : transpose와 shape 변화

## 배운 내용

### 스칼라곱
- 4 * v1 : v1의 방향은 같고 크기만 4배
- 각 원소에 4씩 곱해짐

### 원소별 연산 (element-wise)
- v1 + v2 : 같은 자리끼리 더해짐 (성분별 연산)
- v3 = 4 * v1 - 2 * v2 : 스칼라곱 + 원소별 뺄셈이 한 줄에

### 리스트 vs np.array
- 리스트 + : 이어붙이기 (나열) → [2,5,4,7] + [4,1,0,2] = [2,5,4,7,4,1,0,2]
- np.array + : 벡터합 (성분별 덧셈)
- 그래서 벡터 연산엔 np.array를 씀

### transpose
- .T : 행 <-> 열 뒤집기 (행벡터를 세로 열벡터로)
- 대괄호 2개 [[...]] = 2차원이어야 transpose가 먹힘
- shape 변화: (1, 4) → (4, 1)