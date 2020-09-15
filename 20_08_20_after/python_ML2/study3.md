#study

```

분류 모델의 예측 성능과 계산 성능은 학습에 사용하려는 데이터에 크게 의존 

머신러닝 알고리즘을 훈련하기 위한 다섯 가지 주요 단계
특성을 선택하고 훈련 샘플을 모음 -> 성능 지표를 선택 -> 분류 모델과 최적화 알고리즘 선택 -> 모델 성능 평가 -> 알고리즘 튜닝!
```

```python
# 150개의 꽃 샘플에서 꽃잎 길이와 꽃잎 너비를 특성 행렬 x에 할당하고 이에 상응하는 꽃 품종에 해당하는 클래스 레이블을 벡터 y에 할당!

from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

print('클래스 레이블:', np.unique(y))

#np.unique함수는 iris.target에 저장된 세개의 고유한 클래스 레이블을 반환함! (이미 클래스 이름이 정수로 저장되어있음! 
# 사이킷런의 많은 함수와 클래스 메서드는 문자열 형태의 클래스 레이블을 다룰 수 있음! 
# 정수 레이블이 권장되는 이유는 사소한 실수를 피할 수 있고 작은 메모리 영역을 차지하므로 계산 성능을 향상!

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y)

print('y의 레이블 카운트:', np.bincount(y))
print('y_train의 레이블 카운트:', np.bincount(y_train))
print('y_test의 레이블 카운트:', np.bincount(y_test))
# train_test_split 함수를 사용해서 X와 y배열을 랜덤하게 나눔! / 30%는 테스트 데이터 / 70% 훈련데이터 (45 / 105)
# train_test_split 분할 되기 전에 데이터셋을 미리 섞음 (그렇지 않으면 0과 1이 훈련 세트에 들어가고 테스트 세트는 클래스2의 샘플 45개만으로 구성됨, 무작정 섞기 위해 random_state 매개변수로 고정된 랜덤시드를 전달 -> 고정하면 실행결과 재현 가능! 
# staratify=y를 통해 계층화 기능 사용 / 여기에서는 split 함수가 훈련 세트와 테스트 세트의 클래스 레이블 비율을 입력 데이터 셋과 동일하게 만든다는 의미! / bincount 함수는 배열에 있는 고유한 값의 등장 횟수를 헤알릴 수 있음!)

#많은 러닝 알고리즘과 최적화 알고리즘은 최상의 성능을 위해 특성 스케일 조정이 필요함 (아래의 예에이는 proprocessing 모듈의 standardScaler 클래스를 사용하여 특성을 표준화함!)
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
# proprocessing 모듈에서 standardScaler 클래스를 로드하고 새로운 스탠다드스케일러 객체를 sc변수에 할당! / fit 메서드는 훈련 세트의 각 특성차원 마다 u(샘플 평균)와 o(표준편차)를 계산 / transfrom 메서드를 호출하면 계산된 샘플평균과 표준 편차 사용하여 훈련세트를 표준화함! / 훈련세트와 테스트 세트의 샘플이 서로 같은 비율로 이동되로고 동일한 샘플평균과 표준편차 사용하여 표준화함! 

#사이킷런의 알고리즘은 대부분 OvR방식을 사용하여 다중분류를함 ! (one versus Rest) 
from sklearn.linear_model import Perceptron

ppn = Perceptron(max_iter=40, eta0=0.1, tol=1e-3, random_state=1)
ppn.fit(X_train_std, y_train)

#리니어모듈에서 퍼셉트론 클래스 로드  새로운 퍼셉트론 객체 생성 fit을사용해 모델훈련 ! / max_iter는 훈련 세트를 반복할 에포크 횟수 정의! / 에포크마다 훈련 세트를 섞은 결과가 나중에 그대로 재현되도록 랜덤스테이트 매개변수 사용(학습률이 너무 크면 전역 최솟값을 지나치고 너무 작으면 학습속도가 느림!)

y_pred = ppn.predict(X_test_std)
print('잘못 분류된 샘플 개수: %d' % (y_test != y_pred).sum())

# 잘못 분류된 샘플 개수를 이용해 전체를 나눠 오차를 가할 수 있고 1에서 오차를 뺴면 분류 정확도임!


from sklearn.metrics import accuracy_score

print('정확도: %.2f' % accuracy_score(y_test, y_pred))
# 정확도는 위의 메트릭스의 정확도 식을 이용해 계산! / y_test는 진짜 클래스 레이블 , y_pred는 앞서 예측한 클래스 레이블! 

print('정확도: %.2f' % ppn.score(X_test_std, y_test))

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):

    # 마커와 컬러맵을 설정합니다.
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # 결정 경계를 그립니다.
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.8, 
                    c=colors[idx],
                    marker=markers[idx], 
                    label=cl, 
                    edgecolor='black')

    # 테스트 샘플을 부각하여 그립니다.
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(X_test[:, 0],
                    X_test[:, 1],
                    facecolors='none',
                    edgecolor='black',
                    alpha=1.0,
                    linewidth=1,
                    marker='o',
                    s=100, 
                    label='test set')
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

plot_decision_regions(X=X_combined_std, y=y_combined,
                      classifier=ppn, test_idx=range(105, 150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()


```