## R

#### R Practice 2

```R
dau <- read.csv("./data/dau.csv", header = T, stringsAsFactors = F)
head(dau)
dpu <- read.csv("./data/dpu.csv", header = T, stringsAsFactors = F)
head(dpu)
install <- read.csv("./data/install.csv", header = T, stringsAsFactors= F)
head(install)

dauins <- merge(dau, install, by = c("user_id", "app_name"), all.x = T)
dauins
total <- merge(dauins, dpu, by=c("log_date", "app_name", "user_id"), all.x = T)
total
total$payment[is.na(total$payment)] <- 0



total$log_month <- substr(total$log_date, 3, 7)
total$install_month <- substr(total$install_date, 3, 7)
library("plyr")
total2 <- ddply(total, .(log_month, user_id, install_month), summarize, payment = sum(payment))
total2
total4 <- aggregate(payment~ install_month, total2, sum)
total4
total2
total2$user_type <- ifelse(total2$install_month == total2$log_month, "install", "existing")
total3 <- ddply(total2, .(log_month, user_type), summarize, total.payment = sum(payment))
head(total2)
install.packages("ggplot2")
library("ggplot2")
library("scales")
ggplot(total3, aes(x = log_month, y= total.payment, fill = user_type)) + geom_bar(stat= "identity", color= "green") + scale_y_continuous(label = comma)
```
![Deepin스크린샷_select-area_20190910172525](https://i.imgur.com/lszJ0hh.png)
```R
ggplot(total2[total2$payment > 0 & total2$user_type == "install",], aes(x= payment, fill = log_month)) + geom_histogram(position = "dodge", binwidth = 20000) + scale_x_continuous(label = comma)
```
![Deepin스크린샷_select-area_20190910172905](https://i.imgur.com/OGoweMA.png)
