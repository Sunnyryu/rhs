## R

#### R Practice

```
x1 <- 1:5
y1 <- x1^2
z1 <- 5:1
(mat1 <- cbind(x1, y1, z1))

op <- par(no.readonly =  TRUE)
par(mfrow=c(2,3))
plot(y1, main="using index")
plot(x=x1, y=y1, main="x^2")
plot(mat1, main="using matrix")
plot(x1, y1, type="l", main="line")
plot(x1, y1, type="h", main="high dentsity")
plot(x1, y1, type="n", main="no plotting")
par(op)
```
![Deepin스크린샷_select-area_20190909173021](https://i.imgur.com/Cseig6A.png)
```
x <- rep(1:5, rep(5,5))
x

y<- rep(5:1, 5)
y
pchs <-c("&", "z", "Z", "1", "가")
plot(1:5, type="n", xlim= c(0, 7.5), ylim=c(0.5,5.5), main = " points by pch")
points(x, y, pch = 1:25, cex = 1.5) #(1)
text(x - 0.4, y, labels= as.character(1:25), cex = 1.2)
points(rep(6,5), 5:1, pch = 65:69, cex= 1.5) #(2)
text(rep(6, 5)- 0.4, y, labels = as.character(65:69), cex=1.2)
points(rep(7,5), 5:1, pch = pchs, cex= 1.5) #(3)
text(rep(7, 5)- 0.4, y, labels = paste("'",pchs,"'", sep = ""),cex = 1.2)
```
![Deepin스크린샷_select-area_20190909173703](https://i.imgur.com/FkZweHF.png)
```
cars[1:4,]
z <- lm(dist ~ speed, data = cars)
is(z)
z$coef
plot(cars, main = "abline")
#horizontal
abline(h = 20)#1
abline(h = 30)#2
#vertical
abline(v = 20, col="lightblue") #3
#y = a + bx
abline(a = 40, b=4 , col="lightpink") #4
#reg 인수
abline(z, lty = 2, lwd = 2, col="yellowgreen") #5
#coef 인수
abline(z$coef, lty = 3, lwd =2, col="yellow") #6
```
![Deepin스크린샷_select-area_20190909174106](https://i.imgur.com/PpS1bJE.png)
