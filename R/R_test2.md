## R & 통계 연습 문제

#### Practice

```R
getwd()
setwd('/home/sunny/Workspace_R')
myeffect <- read.csv("./data/myeffect.csv",header =T)              
myeffect
myeffect$before
myeffect$after



myeffect2 <- subset(myeffect,after<999)
myeffect3 <- subset(myeffect,after!=999)
myeffect4 <- subset(myeffect,after<999, c(before,after))
myeffect5 <- subset(myeffect,after!=999, c(before,after))
myeffect5


#참가자의 빈도수와 before, after의 평균값
groupBE <- myeffect5$before
groupAF <- myeffect5$after
length(groupBE)
length(groupAF)
mean(groupBE)
mean(groupAF)
var.test(groupBE,groupAF, paired = T)
# p-value가 0.05보다 작으므로 두 집단의 평균이 등분산성 검정을 만족X
#귀무가설 : 한쌍의 두집단 평균의 차이X
#대립가설 : 한쌍의 두 집단 평균의 차이O
wilcox.test(groupBE,groupAF, paired = T)
# p-value가 0.05보다 작으므로 귀무가설 기각되고 대립가설 채택
#즉, 다이어트 효능식품 복용 전후의 몸무게 평균의 차이는 있는것으로 확인

human <- read.csv("./data/myhuman.csv", header=T)
head(human)
summary(human)
set.seed(1234)
idx = sample(1:nrow(human), 0.7*nrow(human))

training = human[idx,]
testing = human[-idx,]

library(rpart)
human_model = rpart(formula=Group~., data=training)
human_model

pred = predict(human_model, testing)
pred = ifelse(pred[,1] >= 0.5, 'Good','NA')

table(pred)


table(pred, testing$Group)


accuracy = (13+5) / nrow(testing)
accuracy #(13+5)/(21)


plot(human_model)
text(human_model, use.n=T, cex=0.7)

getwd()
library(arules)
mybasket.trans <- read.transactions("./data/mybasket.csv",format="basket",sep=",")
#1.전체 트랜잭션 개수와 상품아이템 유형은 몇 개인가?
summary(mybasket.trans)
#2.가장 발생빈도가 높은 상품아이템은 무엇인가?
itemFrequency(mybasket.trans)
itemFrequencyPlot(mybasket.trans)
#3. 지지도를 10%로 설정했을 때의 생성되는 규칙의 가짓수는?
mybasket.rules <- apriori(mybasket.trans,parameter=list(support=0.1,confidence=0.0))
summary(mybasket.rules)
#4.상품아이템 중에서 가장 발생확률이 높은 아이템과 낮은 아이템은 무엇인가?
sort(itemFrequency(mybasket.trans),decreasing=TRUE)
#5.가장 발생가능성이 높은 <2개 상품간>의 연관규칙은 무엇인가?
inspect(subset(mybasket.rules,subset=lhs %in%"clothes"&rhs %in%"snack"))
#6.가장 발생가능성이 높은 <2개 상품이상에서><제3의 상품으로>의 연관규칙은?
inspect(subset(mybasket.rules,subset=lhs %in%"clothes"&lhs %in%"snack"))

library(httr)
urlStr <- "https://openapi.naver.com/v1/search/blog.xml?"
#검색어 설정 및 UTF-8 URL 인코딩
searchString <- "query=백두산"
searchString <- iconv(searchString, to="UTF-8")
searchString <- URLencode(searchString )
searchString

etcString <- "&display=100&start=1&sort=sim"
reqUrl <- paste(urlStr, searchString, etcString, sep="")
reqUrl

clientID <- "0_Pr8NKYlWexLJttIolK"
clientSecret <- "iAkzgDXO0h"

apiResult <- GET(reqUrl, add_headers("X-Naver-Client-Id"="0_Pr8NKYlWexLJttIolK"
                                     , "X-Naver-Client-Secret"="iAkzgDXO0h"))
apiResult    #응답코드 status가 200이면 정상

str(apiResult)  
apiResult$content
str(apiResult$content)  
result <- rawToChar(apiResult$content)
result
Encoding(result) <- "UTF-8"
result  
refinedStr <- result
refinedStr <- gsub("<(\\/?)(\\w ?+)*([^<>]*)>", " ", refinedStr)
refinedStr
refinedStr <- gsub("[[:punct:]]", " ", refinedStr)
refinedStr
refinedStr <- gsub("[a-z]", " ", refinedStr)
refinedStr
refinedStr <- gsub("[0-9]", " ", refinedStr)
refinedStr
refinedStr <- gsub(" +", " ", refinedStr)
refinedStr
library(KoNLP)
library(rJava)
nouns<- extractNoun( refinedStr )
str(nouns)
nouns[1:50]
nouns <-nouns[nchar(nouns) > 1]
nouns
wordT <- sort(table(nouns), decreasing=T)[1:50]
wordT
install.packages("wordcloud2")
library(wordcloud2)
wordcloud2(wordT, size=3, shape="diamond")
```
