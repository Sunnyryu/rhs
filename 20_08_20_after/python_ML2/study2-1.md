## study

```

붓꽃 데이터 셋에서 퍼셉트론 훈련 
퍼셉트론 규칙이 2차원 뿐만아니라 다중 클래스 분류로 확장할 수 있음(일대다 저략 등!)

pands를 이용하여 dataframe을 로드!
```

```python

import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/'
'machine-learning-databases/iris/iris.data', header=None)
df.tail()

import matplotlib.pyplot as plt
import numpy as np

# setosa와 versicolor를 선택함!
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# 꽃받침 길이와 꽃잎 길이를 추출함 
X = df.iloc[0:100, [0,2]].values

# 산점도를 그립니다.
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()
"""
이 산점도는 붓꽃 데이터 셋에 있는 샘플들이 꽃받침 길이와 꽃잎 길이 두 개의 특성 축을 따라 분포된 형태를 보여줌! / 이런 2차원 부분 공간에서는 선형 결정 경계로 꽃들을 구분하기 충분! 
"""
```

```python
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):

    # 마커와 컬러맵을 설정합니다(s=사각형, x:곱셈기호, o:원 , ^:삼각형, v: 뒤집힌 삼각형)
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # 결정 경계를 그립니다
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # 샘플의 산점도를 그립니다
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.8, 
                    c=colors[idx],
                    marker=markers[idx], 
                    label=cl, 
                    edgecolor='black')
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')

plt.show()
"""
color와 makers를 정의하고 import한 것을 이용하여 colors 리스트에서 컬러맵을 만들고 두 특성의 최대 최소값을 찾고 이 벡터로 넘파이 meshgrid 함수로 그리드 배열 xx1과 xx2 쌍을 만듬 / 두 특성의 차원에서 퍼셉트론 분류기를 훈련했기 때문에 그리드 배열을 펼치고 훈련 데이터와 같은 개수의 열이 되도록 해열ㄹ을 만듬 / predict 메서드로 그리드 각 포인트에 대응하는 클래스 레이블 z를 예측!

클래스 레이블 Z를 xx1, xx2 같은 차원의 그리드로 크기를 변경한 후 matplotlib의 contourf 함수로 등고선 그래프를 그림! 
"""

```

```
적응형 선형 뉴련 / 아달린

아달린은 연속 함수로 비용 함수를 정의하고 최소화하는 핵심개념! 
아달린규칙은 퍼셉트론과 다르게 단위 계단 함수 대신, 선형 활성화 함수를 사용함! / 
그렇지만 최종 예측을 만드는 데는 여전히 임계함수를 사용함 ! 

가중치 등을 입력 ->최종입력 함수 -> 활성화함수 -> 오차가 있다면 다시 가중치들을 업데이트 -> 없다면 임계함수 -> 출력

아달린은 진짜 클래스 레이블과 선형 활성화 함수의 실수 출력 값을 비교하여 모델의 오차 계산 / 가중치 업데이트
퍼셉트론은 진짜 클래스 레이블과 예측 클래스 레이블을 비교!

경사 하강법
지도 학습 알고리즘의 핵심 구성 요소는 학습 과정 동안 최적화하기 위해 정의한 목적함수! / 최소화하려는 비용함수가 목적함수가 되기도 함 ! 

아달린은 계산된 출력과 진짜 클래스 레이블 사이의 제곱 오차합으로 가중치를 학습할 비용 함수를 정의! 

선형 활성화 함수를 사용하는 장점은 비용함수가 미분이 가능해짐! / 블록함수 라는 것! 

경사 하강법을 적용하여 데이터셋의 샘플을 분류하도록 비용 함수를 최소화하는 가중치를 찾을 수 있음 ! 

이면에 있는 핵심 아이디어를 지역 또는 전역 최솟값에 도달할 때까지 언덕을 내려오는 것으로 묘사하고 있음 / 각 반복에서 경사의 반대 방향으로 진행 / 진행 크기는 경사의 기울기와 학습률로 결정! 

비용 함수의 그래디언트 반대 방향으로 조금씩 가중치를 업데이트함! / 가중치 변화량은 음수의 그래디언트에 학습률 곱함 !  / 비용함수 그래디언트를 계산하려면 각 가중치 w_f에 대한 편도함수를 계산해야함 / w := w + w의 변화량

아달린은 실수 클래스 레이블! /  (배치 경사 하강법)
```

```python

class AdalineGD(object):
    """적응형 선형 뉴런 분류기

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
      에포크마다 누적된 비용 함수의 제곱합

    """
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
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
            # Please note that the "activation" method has no effect
            # in the code since it is simply an identity function. We
            # could write `output = self.net_input(X)` directly instead.
            # The purpose of the activation is more conceptual, i.e.,  
            # in the case of logistic regression (as we will see later), 
            # we could change it to
            # a sigmoid function to implement a logistic regression classifier.
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        """최종 입력 계산"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        """선형 활성화 계산"""
        return X

    def predict(self, X):
        """단위 계단 함수를 사용하여 클래스 레이블을 반환합니다"""
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

ada1 = AdalineGD(n_iter=10, eta=0.01).fit(X, y)
ax[0].plot(range(1, len(ada1.cost_) + 1), np.log10(ada1.cost_), marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Sum-squared-error)')
ax[0].set_title('Adaline - Learning rate 0.01')

ada2 = AdalineGD(n_iter=10, eta=0.0001).fit(X, y)
ax[1].plot(range(1, len(ada2.cost_) + 1), ada2.cost_, marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('Sum-squared-error')
ax[1].set_title('Adaline - Learning rate 0.0001')

plt.show()

"""
퍼셉트론처럼 개별 훈련 샘플마다 평가한 후 가중치를 업데이트하지 않고 전체 훈련 데이터 셋을 기반으로 그래디언트를 계산함! 절편(0번째 가중치)는 self.eta * errors.sum()이고 가중치 1에서 m까지는 self.era * X.T.dot(errors)임 / X.T.dot(errors)는 특성 행렬과 오차 벡터간의 행렬-벡터 곱셈!

activation 메서드는 단순한 항등 함수이기에 아무련 영향을 끼치지 않음 / 입력 데이터의 특성에서 최종 입력, 활성화, 출력 순으로 진행 / (로지스틱 회귀 모델은 활성화 함수와 비용 함수만 다르고 아달란과 비슷!)
"""

```