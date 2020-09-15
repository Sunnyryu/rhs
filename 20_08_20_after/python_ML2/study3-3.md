#study

```python

#순수한 파이썬 구현에 비해 LIBLINEAR와 LIBSVM은 많은 선형 분류기를 아주 빠르게 훈련할 수 있는 장점이 있음! / 데이터셋이 커서 용량이 안맞을 수도 있음 ! / 사이킷런은 이에대해서 SGDClassfier를 제공 / partial_fit 메서드를 제공하여 온라인 학습 지원 (아달린을 위해 구현한 확률적 경사 하강법과 비슷!) 


from sklearn.linear_model import SGDClassifier

ppn = SGDClassifier(loss='perceptron')
lr = SGDClassifier(loss='log')
svm = SGDClassifier(loss='hinge')

```

```python

#커널 SVM을 사용하여 비선형 문제 풀기(SVM은 비선형 분류 문제를 위해 커널 방법을 사용할 수 있음!)

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
X_xor = np.random.randn(200, 2)
y_xor = np.logical_xor(X_xor[:, 0] > 0,
                       X_xor[:, 1] > 0)
y_xor = np.where(y_xor, 1, -1)

plt.scatter(X_xor[y_xor == 1, 0],
            X_xor[y_xor == 1, 1],
            c='b', marker='x',
            label='1')
plt.scatter(X_xor[y_xor == -1, 0],
            X_xor[y_xor == -1, 1],
            c='r',
            marker='s',
            label='-1')

plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# 양성클래스와 음성클래스를 선형 초평면(결정 경계)로 구분할 수 없을 것 같음... 커널방법을 이용하여 다룸
# 매핑함수를 사용하여 원복 특성의 비선형 조합을 선형적으로 구분되는 고차원 공간에 투영하는 것!

# 매핑함수를 사용하여 훈련 데이터를 고차원 특성 공간으로 변환 -> 새로운 특성 공간에서 데이터를 분류하는 선형 SVM 모델을 훈련 -> 동일한 매핑 함수를 사용하여 새로운 본 적 없는 데이터를 변환하고 선형 SVM 모델을 사용하여 분류 

# 비용이 비쌈 / 그래서 소위 커널 기법이 등장 / 두포인트 사이 접곰을 계산하는데 드는 높은 비용을 절감하기 위해 커널 함수를 정의함! 

# 커널이란 샘플간의 유사도 함수라고 생각할 수 있음 (음수 부호가 거리측정을 유사도 점수로 바꾸는 역할을 함! / 지수함수로 얻게되는 유사도 점수는 1 (매우 비슷) / 0 (매우다른 샘플)

svm = SVC(kernel='rbf', random_state=1, gamma=0.10, C=10.0)
svm.fit(X_xor, y_xor)
plot_decision_regions(X_xor, y_xor,
                      classifier=svm)

plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

# r(감마를 크게하면) 서포트 벡터의 영향이나 범위가 줄어듬 / 결정경계가 더욱 샘플에 가까워지고 구불구불 해짐!


svm = SVC(kernel='rbf', random_state=1, gamma=0.2, C=1.0)
svm.fit(X_train_std, y_train)

plot_decision_regions(X_combined_std, y_combined,
                      classifier=svm, test_idx=range(105, 150))
plt.scatter(svm.dual_coef_[0,:], svm.dual_coef_[1,:])
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

svm = SVC(kernel='rbf', random_state=1, gamma=100.0, C=1.0)
svm.fit(X_train_std, y_train)

plot_decision_regions(X_combined_std, y_combined, 
                      classifier=svm, test_idx=range(105, 150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

# 감마(r) 매개변수가 과대적합을 조절하는 중요한 역할도 한다는 것을 알 수 있음!

```


```

결정 트리 학습 (결정 트리 분류기는 설명이 중요할 떄 아주 유용한 모델 / 결정 트리라는 이름처럼 일련의 질문에 대한 결정을 통해 데이터를 분해하는 모델로 생각할 수 있음)

훈련 데이터에 있는 특성을 기반으로 샘플의 클래스 레이블을 추정할 수 있는 일련의 질문을 학습함 / 범주형 변수를 사용한 결정 트리를 설명하고 있지만 동일한 개념이 실수형 특성에서도 사용! / 결정 알고리즘을 사용하면 트리의 루트에서 시작해서 정보이득이 최대가 되는 특성으로 데이터를 나눔! / 리프 노드가 순수해질 때까지 모든 자식 노드에서 이 분할 작업을 반복함! / 이 노드의 모든 샘플은 동일한 클래스에 속함! / 노드가 많은 깊은 트리가 과대적합이 될 가능성이 있기에 최대 깊이를 제한하는 트리를 가지치기함!

정보이득 최대화 자원을 최대로 활용!
(가장 정보가 풍부한 특성으로 노드를 나누기 위해 트리 알고리즘으로 최적화할 목점 함수를 정의함! / 목적 함수는 각 분할에서 정보 이득을 최대화함! / D_p, D_f는 부모와 f번쨰 자식 노드의 데이터셋임, I는 불손도 지표 / N_p는 부모 노드에 있는 전체 샘플 개수! / N_f는 f번째 자식 노드에 있는 샘플 개수임!, 정보 이득은 단순히 부모 노드의 불순도와 자식 노드의 불손도의 합의 차이! / 자식 노드의 불순도가 낮을수록 정보 이득이 커짐! / 구현을 간단하게 하고 탐색 공간을 줄이기 위해 (사이킷런을 포함해서) 이진 결정 트리를 사용함 -> 부모 노드는 대부분 자식노드 2개로 나눠짐 / 결정하는 세 개의 불손도 지표 또는 분할 조건은 (지니 불손도, 엔트로피, 분류오차!))

한 노드의 모든 샘플이 같은 클래스이면 엔트로피는 0! / 클래스 분포가 균등하면 엔트로피는 최대가 됨! / 이진 클래스에서 P값이 1이거나 0이면 엔트로피는 0! / 균등하게 분포되어있으면 1 , 지니 불순도는 잘못 분류될 확률을 최소화하기 위한 기준으로 이해할 수 있음! , 엔트로피와 비슷하게 지니 불손도는 클래스가 완벽하게 섞여 있을때 최대가 됨! 

지니 불순도와 엔트로피 모두 매우 비슷한 결과가 자주나옴 , 불순도 조건을 바꾸어 트리를 평가하는 것보다 가지치기 수준을 바꾸면서 튜닝하는 것이 더 나쁘지 않음!

분류오차는 노드의 클래스 확률변화에 덜 민감하기 떄문! 
```

```python

import matplotlib.pyplot as plt
import numpy as np


def gini(p):
    return p * (1 - p) + (1 - p) * (1 - (1 - p))


def entropy(p):
    return - p * np.log2(p) - (1 - p) * np.log2((1 - p))


def error(p):
    return 1 - np.max([p, 1 - p])

x = np.arange(0.0, 1.0, 0.01)

ent = [entropy(p) if p != 0 else None for p in x]
sc_ent = [e * 0.5 if e else None for e in ent]
err = [error(i) for i in x]

fig = plt.figure()
ax = plt.subplot(111)
for i, lab, ls, c, in zip([ent, sc_ent, gini(x), err], 
                          ['Entropy', 'Entropy (scaled)', 
                           'Gini Impurity', 'Misclassification Error'],
                          ['-', '-', '--', '-.'],
                          ['black', 'lightgray', 'red', 'green', 'cyan']):
    line = ax.plot(x, i, label=lab, linestyle=ls, lw=2, color=c)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
          ncol=5, fancybox=True, shadow=False)

ax.axhline(y=0.5, linewidth=1, color='k', linestyle='--')
ax.axhline(y=1.0, linewidth=1, color='k', linestyle='--')
plt.ylim([0, 1.1])
plt.xlabel('p(i=1)')
plt.ylabel('Impurity Index')
plt.show()
```

```python

#결정 트리 만들기 -> 특성 공간을 시각 격자로 나누기 떄문에 복잡한 결정 경계를 만들 수 있음! /결정 트리가 깊어질수록 결정 경계가 복잡해지고 과대적합이 되기 쉽기에 주의! 

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(criterion='gini', 
                              max_depth=4, 
                              random_state=1)
tree.fit(X_train, y_train)

X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_regions(X_combined, y_combined, 
                      classifier=tree, test_idx=range(105, 150))

plt.xlabel('petal length [cm]')
plt.ylabel('petal width [cm]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

dot_data = export_graphviz(tree,
                           filled=True, 
                           rounded=True,
                           class_names=['Setosa', 
                                        'Versicolor',
                                        'Virginica'],
                           feature_names=['petal length', 
                                          'petal width'],
                           out_file=None) 
graph = graph_from_dot_data(dot_data) 
graph.write_png('tree.png')

#out_file =None일 경우 tree.dot 중간 파일을 디스크에 만들지 않고 dot 데이터를 dot_data 변수에 할당 
```

```

랜덤 포레스트로 여러 개의 결정 트리 연결

랜덤 포레스트는 뛰어난 분류 성능, 확장성, 쉬운 사용법!

결정트리의 앙상블이라고 생각함 / 이면의 아이디어는 여러 개의 (깊은) 결정 트리를 평균 내는 것임, 개개의 트리는 분산이 높은 문제가 있지만 앙상블은 견고한 모델을 만들어 일반화 성능을 높이고 과대 적합의 위험을 줄임

n개의 랜덤한 부트스트랩 샘플을 뽑음(훈련 세트에서 중복허용, 랜덤하게 n개의 샘플 선택) -> 부트스트랩 샘플에서 결정트리 학습(각 노드에서 중복을 허용하지 않고 랜덤하게 d개의 특성을 선택하는 노드와 정보 이득과 같은 목적 함수를 기준으로 최선의 분할을 만드는 특성을 사용해서 노드를 분할하는 노드를 둠) -> 앞의 2단계를 k번 반복 -> 각 트리의 예측을 모아 다수결 투표로 클래스 레이블을 할당 

결정트리와는 다르게 랜덤하게 선택된 일부 특성만을 사용(훈련 시 각 노드에서 최선의 분할을 찾기위해 모든 특성을 하는 결정 트리와는 다름!)

랜덤 포레스트는하이퍼파라미터 튜닝에 많은 노력을 기울이지 않아도 되며 가지치기 할 필요가 없음 /개별 결정트리가 만드는 잡음으로 부터 안정되어 있음! / 랜덤 포레스트에서 신경쓸 파라미터는 트리 개수 하나임! / 트리 개수가 많을 수록 비용이 증가하지만 랜덤 포레스트 분류기의 성능이 올라감 

부트스트랩 샘플 크기가 작아짐녀 개별 트리의 다양성이 증가 (특정 훈련샘플이 부트스트랩 샘플에 포함될 확률이 낮기 때문!)
부트스트랩 샘플 크기 감소 -> 랜덤포레스트 무작위성 증가 , 과대 적합의 영향 줄어듬! 

훈련 성능과 테스트 성능 사이에 격차가 작아지지만 전체적인 테스트 성능이 감소.. 

부트스트랩 샘플 크기가 증가하면 과대적합 가능성이 늘어남, 원본 데이터셋에 가깝게 학습(결정트리와 서로 비슷해짐 )

사이킷런의 랜덤포레스트클래시파이어도 부트스트랩 샘플 크기를 원본 훈련 세트의 샘플 개수와 동일하게 함! (기본값은 (훈련 세트의 특성개수)^0.5)
```

```python
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(criterion='gini',
                                n_estimators=25, 
                                random_state=1,
                                n_jobs=2)
forest.fit(X_train, y_train)

plot_decision_regions(X_combined, y_combined, 
                      classifier=forest, test_idx=range(105, 150))

plt.xlabel('petal length [cm]')
plt.ylabel('petal width [cm]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
```

```
k-최근접 이웃 - KNN이라고 하며 게으른 학습기라고도 함 , 훈련 데이터에서 판별 함수를 학습하는 대신 훈련 데이터셋을 메모리에 저장하기 떄문임! KNN은 숫자 K와 거리 측정 기준을 선택 / 분류하려는 샘플에서 K개의 최근접 이웃을 찾음 / 다수결 투표를 통해 클래스 레이블을 할당! 

다수결 투표가 동일할 경우 사이킷런의 KNN 구현은 샘플에 더 가까운 이웃을 예측으로 선택 / 이웃들의 거리가 같다면 훈련 데이터셋에서 먼저 나타난 샘플의 클래스 레이블을 선택함! 

KNN은 차원의 저주가 일어날 수 있음(과대적합이 될 수 있음) -> 차원의 저주는 고정된 크기의 훈련 데이터셋이 차원이 늘어남에 따라 특성 공간이 점점 희소해지는 현상임! / 고차원 공간에서는 가장 가까운 이웃이라도 좋은 추정 값을 만들기에는 너무 멀리 떨어져 있다는 뜻
```

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5, 
                           p=2, 
                           metric='minkowski')
knn.fit(X_train_std, y_train)

plot_decision_regions(X_combined_std, y_combined, 
                      classifier=knn, test_idx=range(105, 150))

plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
```
