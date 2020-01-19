import numpy as np 

# version 
print(np.__version__)
# 1.17.4
# null vector of size 10 !!

null_1 = np.zeros(10)
print(null_1)
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# memory size of any array 

null_2 = np.zeros((10,10))
print("%d bytes" % (null_2.size*null_2.itemsize))
# 800 bytes 

# %run'pyton-c "import numpy; numpy.info(numpy.add)" => CUI !!

# size가 10인 널 벡터를 만들고 5번 째를 1로 채워 넣기 ! (create nul vector of size 10 and fifth value is 1)

null_3 = np.zeros(10)
null_3[4] = 1
print(null_3)
# [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]

# 10에서 49 사이의 숫자로 이루어진 벡터 만들기 ! (crate a vector with values ranging from 10 to 49)
vector_1 = np.arange(10,50)
print(vector_1)
# [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]

# 위의 벡터를 뒤집어서 만들기 ( reverse a vector)

vector_1[::-1]
print(vector_1[::-1])
# [49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10]

# 3 x 3 행렬을 만드는데 0에서 8로 사이의 숫자로 만들기 ! ( create 3x3 matrix / value ranging from 0 to 8)

vector_2 = np.arange(0,9)
reshape_1 = vector_2.reshape(3,3)
print(reshape_1)
#[[0 1 2][3 4 5] [6 7 8]]

# 0이 아닌 요소를 갖는 인덱스의 위치 => 벡터의 위치를 알려줌 ! indices of non-zero elements!

vector_3 = [1,2,0,0,4,0]
print(np.nonzero(vector_3))
# (array([0, 1, 4]),)

# 3x3 identity matrix (eye 이용하기 ! )
vector_4 = np.eye(3,3)
print(vector_4)
# [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]] / 대각선에는 모두 1이 들어감 !!

# 3x3x3 배열에 랜덤 값을 넣어서 만들기 (3x3x3 array with random values)
vector_5 = np.random.random((3,3,3)) 
# 총개수, 행, 열
print(vector_5)
#[[[0.9255092  0.95530594 0.29900561] [0.47960083 0.77545899 0.16977816] [0.79925177 0.77456633 0.06650057]]
# [[0.66841894 0.52028855 0.96369219]  [0.12841918 0.38948324 0.52071745]  [0.44862125 0.66612855 0.0876454 ]]
# [[0.00427464 0.76776768 0.21947966]  [0.01656348 0.30296708 0.6946442 ]  [0.65127963 0.62877297 0.0545745 ]]]


#10x10 배열에 랜덤 값을 넣고 큰 값과 작은 값을 찾기 ! (create 10x10 array / random values and gain max and min values)

vector_6 = np.random.random((10,10))
print("max value:", vector_6.max(), "min value:", vector_6.min())
# max value: 0.9942610604261098 min value: 0.0015498573951100436

# 30인 사이즈인 랜덤 벡터와 평균값을 구하기(random vector of size 30 and mean value)
vector_7 =np.random.random(30)
print(vector_7.mean())
# 0.45686408229140046

# 2d array / 1 on the border and insdie 

vector_8 = np.ones((10,10))
vector_8[1:-1,1:-1] = 0 
# 0행 0열을 제외한 모든 성분을 0으로 바꿔준다 ! / 처음과 끝만 1임 !!
print(vector_8)

# [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]

# add a border around an existing array !

vector_9 = np.ones((5,5))
vector_9 = np.pad(vector_9, pad_width=1, mode='constant', constant_values=0)
# np.pad를 통해 새로운 공간에 값을 채워주고 pad_width는 가장자리를 채울 값을 설정이 가능하며, 안의 값을 0으로 채우기 위해 constant_values=0으로 함!

print(vector_9)
#[[0. 0. 0. 0. 0. 0. 0.]
# [0. 1. 1. 1. 1. 1. 0.]
# [0. 1. 1. 1. 1. 1. 0.]
# [0. 1. 1. 1. 1. 1. 0.]
# [0. 1. 1. 1. 1. 1. 0.]
# [0. 1. 1. 1. 1. 1. 0.]
# [0. 0. 0. 0. 0. 0. 0.]]

#nan => 숫자가 아닌 거 !inf => angkseo !!
# ex) np.nan / np.inf 

#5x 5 matrix with values 1,2,3,4 just below the diagonal

vector_10 = np.diag(1+np.arange(4), k= -1)
# 대각 성분 외에 모든 값을 0으로 만들어주는 대각행렬이며, 0,1,2,3에 +1을 해서 1,2,3,4로 만들고 k=-1로 하여 시작점을 (1,0)에서 대각으로 출력시킴 !
print(vector_10)
#[[0 0 0 0 0]
# [1 0 0 0 0]
# [0 2 0 0 0]
# [0 0 3 0 0]
# [0 0 0 4 0]]

# 8x8 matrix / checkerboard pattern
vector_11 = np.zeros((8,8))
vector_11[1::2,::2] = 1
# [start : stop : step] / slicing 해서 값을 넣음 
vector_11[::2, 1::2] = 1
print(vector_11)
#[[0. 1. 0. 1. 0. 1. 0. 1.]
# [1. 0. 1. 0. 1. 0. 1. 0.]
# [0. 1. 0. 1. 0. 1. 0. 1.]
# [1. 0. 1. 0. 1. 0. 1. 0.]
# [0. 1. 0. 1. 0. 1. 0. 1.]
# [1. 0. 1. 0. 1. 0. 1. 0.]
# [0. 1. 0. 1. 0. 1. 0. 1.]
# [1. 0. 1. 0. 1. 0. 1. 0.]]

# considera (6,7,8 ) shape array , 100th elements!!
vector_12 = np.unravel_index(100,(6,7,8))
#np.unrabel_index(indices, dims, order='c') 
# 플랫 인덱스 또는 플랫 인덱스 배열을 좌표 배열의 튜플로 변환한다 / C = 행 주요 / F = 열주요!
print(vector_12)
#(1, 5, 4)

# checkerboard 8x 8 matrix using the tile function ! 

vector_13 = np.tile(np.array([[0,1],[1,0]]),(4,4))
print(vector_13)
# np.array로 0,1 / 1,0을 만들고 가로, 세로 4번을 반복해줌 !!
#[[0 1 0 1 0 1 0 1]
# [1 0 1 0 1 0 1 0]
# [0 1 0 1 0 1 0 1]
# [1 0 1 0 1 0 1 0]
# [0 1 0 1 0 1 0 1]
# [1 0 1 0 1 0 1 0]
# [0 1 0 1 0 1 0 1]
# [1 0 1 0 1 0 1 0]]

# normalize 5x5 random matrix 
vector_14 = np.random.random((5,5))
normallize_1 = (vector_14 - np.mean(vector_14))/np.std(vector_14)
print(normallize_1)
# 정규화를 하기 위한 식임 !! np.std(분산 )
#[[ 1.45032233 -1.00213887  0.31620026 -1.7113164  -1.79484189]
# [-0.45306893  1.05526136 -0.80814361 -0.39013432  0.73320205]
# [-0.32610602  0.67521799  1.42345003  0.44763019  0.55762475]
# [-0.16879177  0.87260775  0.73826218 -1.828397   -0.26430307]
# [-0.65308507  1.67687849 -1.26737293  0.47932298  0.2417195 ]]

# create custon dtype / color as four unsigned bytes (RGBA)
color = np.dtype([("r", np.ubyte, 1), ("g", np.ubyte, 1),("b", np.ubyte, 1),("a", np.ubyte, 1)])
print(color)
# dtype[('r', 'u1'), ('g', 'u1'), ('b', 'u1'), ('a', 'u1')]

# multiply a 5x3 matrix by a 3x2 matrix 
vector_15 = np.ones((5,3)) @ np.ones((3,2))
print(vector_15)
# np.dot(np.ones((5,3)), np.ones((3,2)))도 가능 !!
# @를 통해 mat product를 할 수 있음 
#[[3. 3.]
# [3. 3.]
# [3. 3.]
# [3. 3.]
# [3. 3.]]

# given a 1D array / all elements which are betwwen 3 and 8, in place 

vector_16 = np.arange(11)
vector_16[(vector_16>3) & (vector_16<8)] *= -1
print(vector_16)
# [ 0  1  2  3 -4 -5 -6 -7  8  9 10]
