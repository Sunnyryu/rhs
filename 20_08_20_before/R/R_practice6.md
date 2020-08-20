## R Practice

#### R Study

```R
# ex1)
product <- read.csv("./data/product2.csv", header=TRUE, fileEncoding = "CP949")
product
x <- sample(1:nrow(product), 0.7*nrow(product))  #70% 표본 추출, 행번호 추출
train <- product[x, ] #학습데이터
test <- product[-x, ] #검정데이터
train
test


model <- lm(formula= 제품_만족도 ~ 제품_적절성+제품_친밀도, data=product)
summary(model)
head(train, 1)
pred <- predict(model, test)
cor(pred, test$제품_만족도)


#ex2)
library(ggplot2)

formula <- price ~ carat + table + depth
head(diamonds)
result <- lm(formula, data=diamonds)
summary(result)



```

```R
단계1 : 학습데이터(train), 검정데이터(test)를 7 : 3 비율로 샘플링
idx <- sample(1:nrow(product), 0.7*nrow(product))
train <- product[idx,] # result중 70%
dim(train) # [1] 184 3
train # 학습데이터
test <- product[-idx, ] # result중 나머지 30%
dim(test) # [1] 80 3
test # 검정 데이터


단계2 : 학습데이터 이용 회귀모델 생성
변수 모델링) y변수 : 제품_만족도, x변수 : 제품_적절성, 제품_친밀도
model <- lm(formula=제품_만족도 ~ 제품_적절성 + 제품_친밀도, data=train)
summary(model) # 학습데이터 분석 : p-value: < 2.2e-16


단계3 : 검정데이터 이용 모델 예측치 생성
pred <- predict(model, test) # 예측치 생성
단계4 : 모델 평가 : cor() 함수 이용
cor(pred, test$제품_만족도) # 모델 평가


library(ggplot2)
data(diamonds)

# diamonds에서 비율척도 대상으로 식 작성
formula <- price ~ carat + table + depth
head(diamonds)
result <- lm(formula, data=diamonds)
summary(result) # 회귀분석 결과

#Coefficients:
#Estimate Std. Error t value Pr(>|t|)
#(Intercept) 13003.441 390.918 33.26 <2e-16 ***
#carat 7858.771 14.151 555.36 <2e-16 ***
#table -104.473 3.141 -33.26 <2e-16 ***
#depth -151.236 4.820 -31.38 <2e-16 ***
해설>carat은 price에 정(+)의 영향을 미치지만, table과 depth는 부(-)의 영향을 미친다.



```
