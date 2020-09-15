#study

```python
#사이킷런을 사용하여 로지스틱 회귀 모델 훈련

# 사이킷런 로지스틱리그레이션의 fit 메서드를 사용하여 표준화 처리된 붓꽃 데이터셋의 클래스 세개를 대상으로 모델을 훈련!


from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(solver='liblinear', multi_class='auto', C=100.0, random_state=1)
lr.fit(X_train_std, y_train)

plot_decision_regions(X_combined_std, y_combined,
                      classifier=lr, test_idx=range(105, 150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

# 0.22에서는 liblinear에서 lbfgs로 변경될 예정! / 0.2에서 auto가 추가 auto로 설정하면 solver가 liblinear일경우 ovr / 그외에는 멀티노미얼을 선택 ! 

lr.predict_proba(X_test_std[:3, :]) 
#실행 시 배열이 나오는데 첫번째 행은 첫번째 붓꽃의 클래스 소속 확률 / 두번째 행은 두번째 꽃의 클래스 소속 확률에 해당 , 열을 모두 더하면 1 /행에서 가장 큰 값의 열이 예측 클래스 레이블이 됩니다. 
lr.predict_proba(X_test_std[:3, :]).sum(axis=1) 
lr.predict_proba(X_test_std[:3, :]).argmax(axis=1)  # 조건부 확률로 얻은 수동적인 방법
lr.predict(X_test_std[:3, :]) # 프레딕트 메서드를 호출
#사이킷런은 입력 데이터로 2차원 배열을 기대함 / 하나의 행을 2차원 포맷으로 먼저 변경해야함 ! reshape를 사용하여 새로운 차원을 추가!
lr.predict(X_test_std[0, :].reshape(1, -1))
```

```python
#규제를 사용하여 과대적합 피하기

#과대적합이란 모델이 훈련 데이터로는 잘 동작하지만 본 적 없는 데이터(테스트 데이터)로는 잘 일반화하지 않는 현상
# 모델이 과대적합일 때 분산이 크다고함 / 모델 파라미터가 너무 많아 주어진 데이터에서 너무 복잡한 모델 만듬 !
# 모델이 과소적합 일 수 도있음 / 훈련 데이터에 있는 패턴을 감지할 정도로 충분히 모델이 복잡하지 않다는 것을 의미! -> 새로운 데이터에서도 성능 낮음! (과소적합은 높은 편향을 가짐! )

#규제(레귤리제이션)는 공선성(특성 간의 높은 상관관계)를 다루거나 데이터에서 잡음을 제거하여 과대적합을 방지할 수 있는 매우 유용한 방법 / 규제는 과도한 파라미터(가중치) 값을 제한하기 위해 추가적인 정보(편향)을 주입하는 개념 (L2규제를 많이 사용함)

#로지스틱 호귀의 비용함수는 규제항을 추가하여 규제를 적용 (규제 항은 모델 훈련 고정에서 가중치를 줄이는 역할!)
#(규제 하이퍼 파라미터가 증가하면 규제 강도가 높아짐!)
# 매개변수 c는 규제 하이퍼파라미터의 역수 
weights, params = [], []
for c in np.arange(-5, 5):
    lr = LogisticRegression(solver='liblinear', multi_class='auto', C=10.**c, random_state=1)
    lr.fit(X_train_std, y_train)
    weights.append(lr.coef_[1])
    params.append(10.**c)

weights = np.array(weights)
plt.plot(params, weights[:, 0],
         label='petal length')
plt.plot(params, weights[:, 1], linestyle='--',
         label='petal width')
plt.ylabel('weight coefficient')
plt.xlabel('C')
plt.legend(loc='upper left')
plt.xscale('log')
plt.show()

# 역 규제 매개변수의 C값을 바꾸면서 열 개의 로지스틱 회귀 모델을 훈련 / 여기서는 클래스 1의 가중치 값만 사용 / 다중분류는 OvR 기법 / c가 감소하면 가중치 절댓값이 줄어듬 (규제강도 증가)
```

```python

#서포트 벡터 머신을 사용한 최대 마진 분류

# 서포트 벡터 머신(SVM)은 강력하고 널리 사용되는 학습 알고리즘 / 퍼셉트론의 확장 , SVM의 최적화 대상은 마진을 최대화하는 것
# 마진은 클래스를 구분하는 초평면(결정 경계)과 이 초평면에 가장 가까운 훈련 샘플 사이으이 거리로 정의 / 서포트 벡터(샘플)

#최대마진 
# 큰 마진의 결정 경계를 원하는 이유는 일반화 오차가 낮아지는 경향이 있기 때문임! / 작은 마질의 모델은 과대적합되기 쉬움 


#슬랙변수 : 선형적으로 구분되지 않는 데이터에서 선형 제약 조건 완화가 필요 / 적절히 비용을 손해보면서 오차가 있는 상황에서 최적화 알고리즘이 수렴! 

# 해당 변수에서 c가 크면 오차에 대한 비용이 커지고 C값이 작으면 분류오차에 덜 엄격해짐! 


from sklearn.svm import SVC

svm = SVC(kernel='linear', C=1.0, random_state=1)
svm.fit(X_train_std, y_train)

plot_decision_regions(X_combined_std, 
                      y_combined,
                      classifier=svm, 
                      test_idx=range(105, 150))
plt.scatter(svm.dual_coef_[0, :], svm.dual_coef_[1, :])
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
```

```
서포트 백터 머신은 로지스틱 회귀보다 이상치에 덜 민감함(조건부 가능도를 최대화하는 로지스틱과는 다르게...)
SVM은 결정 경계에 가장 가까운 포인트(소프트 벡터)에 대부분 관심을 두지만, 로지스틱 회귀는 모델이 간단하고 구현하기가 더 쉬운 장점이 있습니다! / 로지스틱 회귀모델은 업데이트가 용이하므로 스트리밍 데이터를 다룰 때 더 적합함!
```
