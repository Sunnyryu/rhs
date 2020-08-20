## R Practice

#### R Study

```R



Quiz01>
교육수준(education)과 흡연율(smoking) 간의 관련성을 분석하기 위한 연구가설을 수
립하고, 각 단계별로 가설을 검정하시오. [독립성 검정]
연구가설(H1) : 교육수준에 따라 흡연율의 차이가 있다.
귀무가설(H0) : 교육수준에 따라 흡연율의 차이가 없다.   

smoke <- read.csv("./data/smoke.csv", header=TRUE)
head(smoke)

education : 1:대졸, 2:고졸, 3:중졸
smoking : 1:과다흡연, 2:보통흡연, 3:비흡연
smoke$smoking2[smoke$smoking==1] <- "과다흡연"
smoke$smoking2[smoke$smoking==2] <- "보통흡연"
smoke$smoking2[smoke$smoking==3] <- "비흡연"
smoke$education2[smoke$education==1] <- "대졸"
smoke$education2[smoke$education==2] <- "고졸"  
smoke$education2[smoke$education==3] <- "중졸"

chisq.test(smoke$smoking2, smoke$education2)
data:  smoke$smoking2 and smoke$education2
X-squared = 18.911, df = 4, p-value = 0.0008183

# 유의확률이 0.0008183이 유의 수준(a = 0.05)보다 작으므로 귀무가설을 기각할수 있음
# 카이제곱검정통계량 18.911 > 14.860보다 크므로 귀무가설을 기각가능
# 교육수준에 따라 흡연율의 차이가 있음

Quiz02>
나이(age3)와 직위(position) 간의 관련성을 단계별로 분석하시오. [독립성 검정]

연구가설(H1) : 나이에 따라 직위의 차이가 있다.  
귀무가설(H0): 나이에 따라 직위의 차이가 없다.


data <- read.csv("./data/cleanData.csv", header=TRUE, fileEncoding = "CP949")
data <- subset(data, !is.na(position), c(age, position))

data$newage[data$age3==1] <- "청년층"
data$newage[data$age3==2] <- "중년층"
data$newage[data$age3==3] <- "장년층"
data$newposition[data$position==1] <- 1
data$newposition[data$position==2] <- 2
data$newposition[data$position==3] <- 3
data$newposition[data$position==4] <- 4
data$newposition[data$position==5] <- 5
table(data$newage, data$newposition)
chisq.test(data$newage, data$newposition)

data:  data$newage and data$newposition
X-squared = 287.9, df = 8, p-value < 2.2e-16

# 유의확률이 2.2^e-16 < 0.05 귀무가설을 기각할 수 있음
# 카이제곱 검정통계량이 287.9 > 21.955보다 크므로 귀무가설을 기각 가능
# 나이에 따라 직위의 차이가 있음
Quiz03>
직업유형에 따른 응답정도에 차이가 있는가를 단계별로 검정하시오.[동질성 검정]

연구가설(H1) :  직업 유형에 따라 응답 정도의 차이가 있다.
귀무가설(H0) :  직업 유형에 따라 응답 정도의 차이가 없다.

response <- read.csv("./data/response.csv", header=TRUE)
head(response)
response$job2[response$job==1] <- "학생"
response$job2[response$job==2] <- "직장인"
response$job2[response$job==3] <- "주부"
response$response2[response$response==1] <- "무응답"
response$response2[response$response==2] <- "낮음"
response$response2[response$response==3] <- "높음"
table(response$job2, response$response2)
chisq.test(response$job2, response$response2)
data:  response$job2 and response$response2
X-squared = 58.208, df = 4, p-value = 6.901e-12

# 유의 확률이 6.901e^-12 이므로 0.05보다 작아 귀무가설을 기각 가능
# 카이제곱 검정 통계랑이 58.208 > 14.860보다 크므로 귀무가설을 기각 가능
# 직업 유형에 따라 응답의 차이가 있음
