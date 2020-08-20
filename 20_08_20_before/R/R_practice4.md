## R

#### R Practice 4

```R
urlStr <- "https://openapi.naver.com/v1/search/blog.xml?"
#검색어 설정 및 UTF-8 URL 인코딩
searchString <- "query=코타키나발루"
#UTF-8 인코딩
searchString <- iconv(searchString, to="UTF-8")
#URL 인코딩
searchString <- URLencode(searchString )
searchString

#나머지 요청 변수 : 조회 개수 100개, 시작페이지 1, 유사도순 정렬
etcString <- "&display=100&start=1&sort=sim"

#URL조합
reqUrl <- paste(urlStr, searchString, etcString, sep="")
reqUrl

library(httr)
clientID <- "clientID"
clientSecret <- "clientSecret"

apiResult <-
  GET(reqUrl, add_headers("X-NAVER-Client-ID"="clientID",
                          "X-Naver-client-Secret"= "clientSecret"))
apiResult
> apiResult
Response [https://openapi.naver.com/v1/search/blog.xml?query=%EC%BD%94%ED%83%80%ED%82%A4%EB%82%98%EB%B0%9C%EB%A3%A8&display=100&start=1&sort=sim]
  Date: 2019-09-11 02:26
  Status: 200
  Content-Type: application/xml; charset=UTF-8
  Size: 68.6 kB
<BINARY BODY>

# Open API의 결과 구조 확인 (UTF-8로 인코딩된 XML 형식)
str(apiResult)   #XML응답값은 "content"에 담겨 있습니다.

apiResult$content
str(apiResult$content)  

#raw형식이므로 rawToChar()를 활용해 문자로 변환
result <- rawToChar(apiResult$content)
result

Encoding(result) <- "UTF-8"
result   #블러그 링크, 제목, 이름, 요약정보등을 제공
## 결과가 매우김!!
```
