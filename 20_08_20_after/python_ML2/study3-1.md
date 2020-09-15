#study

```

로지스틱 회귀를 사용한 클래스 확률 모델링!

퍼셉트론은 클래스가 선형적으로 구분되지 않을 때 수렴할 수 없음
그래서 선형 이진 분류 문제에 더 강력한 로지스틱 회귀를 사용(로지스틱 회귀는 회귀가 아닌 분류 모델임!)

로지스틱 회귀는 구현하기 매우 쉽고 선형적으로 구분되는 클래스에 뛰어난 성능을 내는 분류 모델입니다. 

오즈비(오즈는 특성 이벤트가 발생할 확률 P / (1-P) : P는 양성 샘플일 확률 (양성샘플은 예측하려는 대상!) , 자연로그를 이용해서 로짓함수로 정의할 수 있음!)

logit(P) = log(P/(1-P))

z = w^t * x (z는 가중치와 샘플 특성의 선형조합으로 이루어진 최종입력! 절편 * 입력!)

어떤 샘플이 특정 클래스에 속할 확률을 예측하는 것이 관심 대상이므로 로짓함수를 거꾸로 뒤집는게 로지스틱 시그모이드 함수(시그모이드 함수) / Wo는 절편을 의미함 / Xo(입력)이 1을 추가!
S(z) = 1 / (1+e ^-z) 
```

```python
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

z = np.arange(-7, 7, 0.1)
phi_z = sigmoid(z)

plt.plot(z, phi_z)
plt.axvline(0.0, color='k')
plt.ylim(-0.1, 1.1)
plt.xlabel('z')
plt.ylabel('$\phi (z)$')

# y 축의 눈금과 격자선
plt.yticks([0.0, 0.5, 1.0])
ax = plt.gca()
ax.yaxis.grid(True)

plt.tight_layout()
plt.show()
# z가 무한대로 가면 e^-z가 매우 작아지기에 시그모이드 함수가 1에 가까워짐 / 분모가 커지면 0에 수렴! / [0,1] 사이의 값으로 변환하며 s(0) = 0.5

# 입력과 절편을 받아 최종입력 함수로 와서 시그모이드 활성화 함수로 온 후에 오차가 있다면 다시 값을 받고 없다면 임계함수로 보내주고 예측 클래스 레이블로 보내는데, 시그모이드 함수에서는 입력 벡터 x가 주어졌을 떄 샘플 클래스 1에 속할 조건부 확률을 이용! / 예측확률은 임계 함수를 사용하여 이진 출력으로 바꿀 수 있음 S(z)>= 0.5 => 1 / 아니면 0 , 시그모이드 함수 그래프를 보면 z>= 0.0 이면 1 아니면 0
```

```python

#로지스틱 비용 함수의 가중치 학습! 
#로지스틱 회귀 모델을 만들 때 최대화하려는 가능도(L)을정의! 

def cost_1(z):
    return - np.log(sigmoid(z))


def cost_0(z):
    return - np.log(1 - sigmoid(z))

z = np.arange(-10, 10, 0.1)
phi_z = sigmoid(z)

c1 = [cost_1(x) for x in z]
plt.plot(phi_z, c1, label='J(w) if y=1')

c0 = [cost_0(x) for x in z]
plt.plot(phi_z, c0, linestyle='--', label='J(w) if y=0')

plt.ylim(0.0, 5.1)
plt.xlim([0, 1])
plt.xlabel('$\phi$(z)')
plt.ylabel('J(w)')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# 결과 그래프 x축은 0에서 1까지 범위의 시그모이드 활성화값( 시그모이드 함수의 입력인 z는 -10~10까지 / y축은 해당하는 로지스틱 비용)
# 클래스 1에 속한 샘플을 정확이 예측하면 비용이 0에 가까워짐을 알 수 있음 / 비슷하게 클래스 0에 속한 샘플을 y=0으로 정확히 예측하면 y축비용이 0에 가까워짐 / 잘못예측하면 비용이 무한히 커짐!!
```

```python

#아달린 구현을 로지스틱 회귀 알고리즘으로 변경

#비용함수 J를 새로운 비용함수로 바꾸기만 하면 아달린에서 로지스특 회귀로 구현가능! 
#해당 함수로 에포크 마다 모든 훈련 샘플을 분류하는 비용 계산 ! / 선형 활성화 -> 시그모이드 활성화 , 임계함수 (-1/1 -> 0/1)
class LogisticRegressionGD(object):
    """경사 하강법을 사용한 로지스틱 회귀 분류기

    매개변수
    ------------
    eta : float
      학습률 (0.0과 1.0 사이)
    n_iter : int
      훈련 데이터셋 반복 횟수
    random_state : int
      가중치 무작위 초기화를 위한 난수 생성기 시드

    속성
    -----------
    w_ : 1d-array
      학습된 가중치
    cost_ : list
      에포크마다 누적된 로지스틱 비용 함수 값

    """
    def __init__(self, eta=0.05, n_iter=100, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """훈련 데이터 학습

        매개변수
        ----------
        X : {array-like}, shape = [n_samples, n_features]
          n_samples 개의 샘플과 n_features 개의 특성으로 이루어진 훈련 데이터
        y : array-like, shape = [n_samples]
          타깃값

        반환값
        -------
        self : object

        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            
            # 오차 제곱합 대신 로지스틱 비용을 계산합니다.
            cost = -y.dot(np.log(output)) - ((1 - y).dot(np.log(1 - output)))
            self.cost_.append(cost)
        return self
    
    def net_input(self, X):
        """최종 입력 계산"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, z):
        """로지스틱 시그모이드 활성화 계산"""
        return 1. / (1. + np.exp(-np.clip(z, -250, 250)))

    def predict(self, X):
        """단위 계단 함수를 사용하여 클래스 레이블을 반환합니다"""
        return np.where(self.net_input(X) >= 0.0, 1, 0)
        # 다음과 동일합니다.
        # return np.where(self.activation(self.net_input(X)) >= 0.5, 1, 0)

X_train_01_subset = X_train[(y_train == 0) | (y_train == 1)]
y_train_01_subset = y_train[(y_train == 0) | (y_train == 1)]

lrgd = LogisticRegressionGD(eta=0.05, n_iter=1000, random_state=1)
lrgd.fit(X_train_01_subset,
         y_train_01_subset)

plot_decision_regions(X=X_train_01_subset, 
                      y=y_train_01_subset,
                      classifier=lrgd)

plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
```