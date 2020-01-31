## Django DRF 

#### Rewind 

```

REST는 WEB 관련 기술이다. 데이터를 주고받는 일종의 규약이다
(HTTP 기본 메서드 4가지(POST, GET, PUT, DELETE)를 통해 일관적인 컨벤션(관례)을 유지한다면 RESTful 하다고 한다)

직렬화를 하는 이유는 데이터를 전송가능한 형태(데이터 스트림)으로 바꾸기 위해 !!

직렬화를 할 때에는 데이터를 딕셔너리 형태로 바꾸고 이 것을 JSON 형태로 바꿔주는 작업을 함 !!

요청(request)을 받아서 응답(repsonse)을 반환해주는 호출 가능한 객체

REQUEST는 HttpRequest를 확장하여 요청을 분석(파싱)한다(REQUEST.data)

RESPONSE는 리턴할 컨텐츠 형태로 변환

@api_view => 함수 기반 뷰에서 사용 가능 
APIView => 클래스 기반 뷰에서 사용 가능 !!

다중 상속시에는 믹스인도 사용함 ! 

클래스를 사용하고자 하면 as_view()를 사용 !!/ dispatch() 메소드도 사용됨 !!


```
