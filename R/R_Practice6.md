##R Practice

#### R

```R
#ex1)
hdtv <- read.csv("./data/hdtv.csv", header=TRUE)
hdtv$buy2[hdtv$buy==1] <- "no buy"
hdtv$buy2[hdtv$buy==2] <- "buy"

x <- hdtv$buy2
x
table(x)
freq(x)
summary(x)
binom.test(c(10,40), p=0.15)
data:  c(10, 40)
number of successes = 10, number of trials = 50, p-value = 0.321
alternative hypothesis: true probability of success is not equal to 0.15
95 percent confidence interval:
  0.1003022 0.3371831
sample estimates:
  probability of success
0.2
# p-value가 0.321으로 0.05보다 크므로 기존 구매비율(15%)와 차이가 없다.

#  방향성이 있는 단측가설 검정
binom.test(c(10,40), p=0.15, alternative="greater", conf.level=0.95)
#p-value=0.2089
binom.test(c(10,40), p=0.15, alternative="less", conf.level=0.95) #p-value =0.8801
해설> 방향성이 있는 단측가설은 모두 기각된다.

# 11% 기준 : 방향성이 있는 연구가설 검정
binom.test(c(10,40), p=0.11, alternative="greater", conf.level=0.95)
#p-value=0.04345
해설> 구매비율은 11%을 넘지 못한다.

#ex2)
student <- read.csv("./data/student_height.csv", header=TRUE)
student

x <- student$height
summary(x)
length(x)
mean(x, na.rm=T)
shapiro.test(x)

t.test(x, mu=148.5, alter="two.side", conf.level=0.95)

data:  x
t = 1.577, df = 49, p-value = 0.1212
alternative hypothesis: true mean is not equal to 148.5
95 percent confidence interval:
 148.2531 150.5469
sample estimates:
mean of x
    149.4

#p-value가 0.1212로 0.05(a)보다 크므로 차이가 적다.

#ex3)
student2 <- read.csv("./data/two_sample.csv", header=TRUE)
student2


student2$gender2[student2$gender==1] <- "남학생"
student2$gender2[student2$gender==2] <- "여학생"
student2$survey2[student2$survey==0] <- "불만족"
student2$survey2[student2$survey==1] <- "만족"
a <- student2$gender2
b <- student2$survey2
table(a, b, useNA="ifany")

n <- c(174,126)
x <- c(138,107)
x
prop.test(x = x, n=n, alternative = c("two.sided"), conf.level= 0.95)


# 기존 구매비율과 차이가 없음!

> prop.test(x = x, n=n, alternative = c("two.sided"), conf.level= 0.95)

	2-sample test for equality of proportions with continuity correction

data:  x out of n
X-squared = 1.1845, df = 1, p-value = 0.2765
alternative hypothesis: two.sided
95 percent confidence interval:
 -0.14970179  0.03749599
sample estimates:
   prop 1    prop 2
0.7931034 0.8492063
# 남자와 여자의 만족도 차이는 없음

#ex4)
mt <- read.csv("./data/twomethod.csv", header=TRUE)
ak <- subset(mt, !is.na(score), c(method, score))
ak
a <- subset(ak, method==1)
b <- subset(ak, method==2)

as <- a$score
bs <- b$score
mean(as)
mean(bs)
length(as)
length(bs)
var.test(as, bs)
t.test(as, bs, alter="two.sided", conf.int=TRUE, conf.level=0.95)

data:  as and bs
t = -5.6056, df = 43.705, p-value = 1.303e-06
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 -17.429294  -8.209667
sample estimates:
mean of x mean of y
 16.40909  29.22857

# p-value가 0.05(a)보다 작으므로 두 가지 방법에 따라 시험성적에는 차이가 있다!

 ```
