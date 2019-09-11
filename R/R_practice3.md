## R

#### R Practice 3

```R
head(airquality)

names(airquality) <- tolower(names(airquality))
head(airquality)
> names(airquality) <- tolower(names(airquality))
> head(airquality)
  ozone solar.r wind temp month day
1    41     190  7.4   67     5   1
2    36     118  8.0   72     5   2
3    12     149 12.6   74     5   3
4    18     313 11.5   62     5   4
5    NA      NA 14.3   56     5   5
6    28      NA 14.9   66     5   6
```

```R
melt_test <- melt(airquality)
head(melt_test)


tail(melt_test)

melt_test2 <- melt(airquality, id.vars = c("month", "wind"), measure.vars = "ozone")
head(melt_test2)

> melt_test2 <- melt(airquality, id.vars = c("month", "wind"), measure.vars = "ozone")
> head(melt_test2)
  month wind variable value
1     5  7.4    ozone    41
2     5  8.0    ozone    36
3     5 12.6    ozone    12
4     5 11.5    ozone    18
5     5 14.3    ozone    NA
6     5 14.9    ozone    28
```

```R
names(airquality) <- tolower(names(airquality))
head(airquality)

aq_melt <- melt(airquality, id = c("month", "day"), na.rm = T)
head(aq_melt)
> aq_melt <- melt(airquality, id = c("month", "day"), na.rm = T)
> head(aq_melt)
  month day variable value
1     5   1    ozone    41
2     5   2    ozone    36
3     5   3    ozone    12
4     5   4    ozone    18
6     5   6    ozone    28
7     5   7    ozone    23
```

```R
aq_dcast <- dcast(aq_melt, month + day ~ variable)
head(aq_dcast)

acast(aq_melt, day ~ month ~ variable)

acast(aq_melt, month ~ variable, mean)

dcast(aq_melt, month ~ variable, mean)

> aq_dcast <- dcast(aq_melt, month + day ~ variable)
> head(aq_dcast)
  month day ozone solar.r wind temp
1     5   1    41     190  7.4   67
2     5   2    36     118  8.0   72
3     5   3    12     149 12.6   74
4     5   4    18     313 11.5   62
5     5   5    NA      NA 14.3   56
6     5   6    28      NA 14.9   66
>
> acast(aq_melt, day ~ month ~ variable)
, , ozone

     5  6   7   8  9
1   41 NA 135  39 96
2   36 NA  49   9 78
3   12 NA  32  16 73
4   18 NA  NA  78 91
5   NA NA  64  35 47
6   28 NA  40  66 32
생략 ~~

> acast(aq_melt, month ~ variable, mean)
     ozone  solar.r      wind     temp
5 23.61538 181.2963 11.622581 65.54839
6 29.44444 190.1667 10.266667 79.10000
7 59.11538 216.4839  8.941935 83.90323
8 59.96154 171.8571  8.793548 83.96774
9 31.44828 167.4333 10.180000 76.90000
>
> dcast(aq_melt, month ~ variable, mean)
  month    ozone  solar.r      wind     temp
1     5 23.61538 181.2963 11.622581 65.54839
2     6 29.44444 190.1667 10.266667 79.10000
3     7 59.11538 216.4839  8.941935 83.90323
4     8 59.96154 171.8571  8.793548 83.96774
5     9 31.44828 167.4333 10.180000 76.90000

```

```R
word_data <- readLines("./data/song.txt")
word_data

> word_data
 [1] "(1절)"                                                       
 [2] "동해물과 백두산이 마르고 닳도록"                             
 [3] "하느님이 보우하사 우리나라만세"                              
 [4] "(후렴)무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세"
 [5] ""                                                            
 [6] "(2절)"                                                       
 [7] "남산위에 저 소나무 철갑을 두른듯"                            
 [8] "바람서리 불변함은 우리기상 일세"                             
 [9] "(후렴)무궁화 삼천리 화려강산 대한사람 대한으로 길이보전하세"
[10] ""                                                            
[11] "(3절)"                                                       
[12] "가을하늘 공활한데 높고 구름없이 "                            
[13] "밝은달은 우리가슴 일편단심일세"                              
[14] "(후렴)무궁화 삼천리 화려강산 대한사람 대한으로 길이보전하세"
[15] ""                                                            
[16] "(4절)"                                                       
[17] "이 기상과 이 맘으로 충성을 다하여"                           
[18] "괴로우나 즐거우나 나라사랑하세"                              
[19] "(후렴)무궁화 삼천리 화려강산 대한사람 대한으로 길이보전하세"
[20] ""    

word_data2 <- sapply(word_data, extractNoun, USE.NAMES = F)
word_data2

add_words <- c("백두산", "남산", "철갑", "가을", "하늘", "달")
buildDictionary(user_dic = data.frame(add_words, rep("ncn", length(add_words))), replace_usr_dic = T)

word_data2 <- sapply(word_data, extractNoun, USE.NAMES = F)
word_data2

undata <- unlist(word_data2)
undata

word_table <- table(undata)
word_table

undata2 <- Filter(function(x) { nchar(x) >= 2}, undata)
word_table2 <- table(undata2)
word_table2

sort(word_table2, decreasing = T)

> sort(word_table2, decreasing = T)
undata2
    대한     강산   무궁화     보전     사람     화려     길이     가슴     가을 공활한데
       8        4        4        4        4        4        3        1        1        1
  구름없     기상     나라     남산     닳도     동해 바람서리 밝은달은   백두산     보우
       1        1        1        1        1        1        1        1        1        1
    불변     사랑   소나무     우리   우리기 우리나라 일편단심     철갑     충성 하느님이
       1        1        1        1        1        1        1        1        1        1
    하늘     하사
       1        1
```



```R
# 워드 클라우드
wordcloud2(word_table2)
```
![Deepin스크린샷_select-area_20190911104407](https://i.imgur.com/s9xoZRl.png)
```R
#워드 클라우드2
wordcloud2(word_table2, fontFamily = "맑은 고딕", size = 1.2, color = "random-light", backgroundColor = "black", shape = "star")
```

![Deepin스크린샷_select-area_20190911104553](https://i.imgur.com/oO2rq8T.png)


```R
# wordcloud2(demoFreq, size = 1.6, color=rep_len(c("red", "green"), nrow(demoFreq))) - 2가지 색 반복해서 워드클라우드 하려고 할 떄

# 일정한 방향으로 정렬된 워드 클라우드
wordcloud2(demoFreq, minRotation = -pi / 6, maxRotation = -pi / 6, rotateRatio = 1)
```
![Deepin스크린샷_select-area_20190911104956](https://i.imgur.com/hVYRfUm.jpg)
![Deepin스크린샷_select-area_20190911105024](https://i.imgur.com/zXcSejd.jpg)
