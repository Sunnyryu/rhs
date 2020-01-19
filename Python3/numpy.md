## Python3

#### numpy & Pandas Rewind

```
Ndarray vs list => data / dimensions / strides vs length / items 
ndarray가 더 빠르게 처리됨!! 

ndarray => 데이터 관리 / data-type =>실제 데이터들의 값을 관리 / array scalar는 위치관리!

array( [element,element,element] dtype) 으로 구성 

0차원 => numpy array 생성 시 단일값을 넣으면 일반 타입 !!
ndim으로 1차원은 확인 가능 !!

3행 3열의 배열의 기준으로 어떻게 내부를 행과 열로 처리 !=> 2차원 배열 !!
numpy.array 생성시 sequence 각 요소에 대해 접근변수와 타입을 정함 - 3차원 배열 

변경을 방지하기 위해서는 새로운 ndarray르 만들어 사용 !(.copy() 메소드를 사용 !)

벡터화 연산으로 for문을 미사용 함 !!=> 원소만큼 자동으로 순환하여 반환함 !!

shape, dtype,strides이 인스턴스 속성이 생성됨 

ndarray.ndim ndarray 객체에 대한 차원 / ndarray.shape ndarray 객체에 대한 다차원 모습
ndarray.size ndarray 객체에 대한 원소의 갯수 / ndarray.dtype ndarray 객체에 대한 원소 타입
ndarray.itemsize ndarray 객체에 대한 원소의 사이즈 / ndarray.data ndarray 객체에 데이터는 itemsize 크기의 hex 값으로 표현
ndarray.real ndarray 에 생성된 복소수에서 실수값 / ndarray.imag ndarray 에 생성된 복소수에서 허수값
ndarray.strides ndarray 객체에 대한 원소의 크기 / ndarray.base ndarray 객체에 다른 곳에 할당할 경우 그 원천에 대한 것을 가짐
ndarray.flat ndarray 객체가 차원을 가질 경우 하나로 연계해서 index 로 처리 / ndarray.T ndarray 객체에 대한 역행렬
np.copy 와 ndarray.copy는 거의 비슷한 처리함 !!

ndarray 생성 => num1 = np.array([0,0,1,1,0,0], dtype= np.float) => [0., 0., 1., 1., 0., 0.]

ones를 사용하면 내부 원소들이 1을 가지게 됨 !! // zeros를 사용하면 zero 원소를 가지는 ndarray 생성 

np.empty 는 shape를 넣고 array를 생성해줌 !!
numpy.eye(n, m=None, k=0, dtype=<type 'float'>) => 생성시 숫자를 정의하면 정방행렬을 만들어주고 대각선이 1로 세팅되면 k 값을 줄경우 위치도 바꿔줌 !!

np.identity => 실제 정방형 ndarray 타입이 생기고 대각선으로 1이 정의됨 !!

np.linspace => 시작과 종료 그리고 요소의 개수로 생성 !!=> linspace(start, stop, num=50, endpoint=True, retstep=False)
(endpoint false 일 때 최종값은 포함되지 않음 !!)

np.arange => arange([start,] stop[, step,], dtype=None) 

asarray => list 등을 ndarray 타입으로 바꿔주는 함수 !!/ asarray(array_likes, dtype=None, order=None)

__getitem__ => 논리연산등 다양한 처리 허용 ! (a.__getitem__(1))
__setitem__ => index와 slice 처리 시 더 다양한 처리를 위해 사용 !

배열 접근하기 !=> 배열명[ 행 범위, 열 범위] 행으로 접근, 열로 접근 / 첫번째와 두번째 행과 두번째와 세번째 열로 접
근 / 행과 열의 인덱스를 지정하면 실제 값에 접근해서 보여줌

ndarray와 ndarray간의 비교연산. Scala 값은 broadcasting하므로 ndarray 동일 모형의 동일값으로 인지해서 처리된 후 bool값을 가지는 ndarray가 생성
1 차열 배열을 조회시 조건을 True 인 것을 조회할 수도 있음 !!/ 다차원 배열의 경우에도 True 인것을 조회할 수 있음 !
실제 배열의 원소들 값이 0보다 작을 경우 99으로 전환함 !/ 

정수배열을 사용한 색인(양수,음수를 이용)이며 행에 대한 정보를 list로 제공해서 3번째와 1번째를 출력


```
