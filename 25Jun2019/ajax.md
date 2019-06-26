## AJAX

#### AJAX



- http
  - HTTP Request 메시지의 구성
    - 요청라인, 요청헤더, 공백라인, 메시지 본문
    - 서버의 주소와 요청 방식(GET or POST)를 포함하며, 그 외에 헤더 정보에는 클라이언트 환경을 알 수 있는 많은 정보들이 있음
  - HTTP Response 메시지의 구성
    - 상태라인, 응답헤더, 공백라인, 메시지 본문
    - 답상태와 헤더, 그리고 메시지 바디를 포함하며, 브라우저는 메시지 바디의 내용을 파싱하여 브라우저 화면에 보여줌.

  - HTTP 응답 메세지 코드
    - 100(continue - 일부 요청 받음, 나머지 정보 계속 요청)
    - 200(OK - 요청이 성공적으로 수행되었음)
    - 400(Bad request- 사용자의 잘못된 요청을 처리할 수 없음)
    - 403(Forbidden - 접근 금지, 디렉터리 리스팅 요청 및 관리자 페이지 접근 등을 차단하는 경우)
    - 404(Not Found -요청한 페이지 없음)
    - 500(Internal server error -웹 서버가 처리할 수 없음)

- Ajax(Asynchronous JavaScript)
  - JavaScript에 의한 비동기적인 통신으로 XML 기반의 데이터를 클라이언트인 웹 브라우저와 서버 사이에서 교환
  - 부분 갱신을함
    - 장점
      - 서버측의 부담 중 일부를 웹 클라이언트에게 넘겨주게 되어 서버어플리케이션 성능 향상
      - 웹 브라우저는 요청을 송신하면 응답을 기다리지 않음
      - 서버는 필요한 데이터만을 응답
  - ajax 구성 기술 요소
    -  Javascript
      - 사용자 이벤트가 발생히면 XMLHttpRequest 객체를 사용해서 웹 서버에 요청을 전달
      - XMLHttpRequest 객체로부터 응답이 오면 DOM, CSS 등을 사용해서 화면을 조작
    - DOM
      - 문서의 구조, 폼 등의 정보나 화면 구성을 조작할 때 사용
    - CSS
      - 글자색, 배경색, 위치, 투명도 등 UI와 관련된 부분을 담당
    - XMLHttpRequest
      - 웹 서버와 통신
        - 사용자의 요청을 웹 서버에 전송하고, 웹 서버로부터 받은 결과를 웹 브라우저에 전달
  ```
  Ajax - 사용자 요청 처리 과정

  사용자가 이벤트(마우스 클릭 등)를 발생,
  자바스크립트는 DOM을 사용해서 필요한 정보를 구함
  XMLHttpRequest 객체를 통해서 웹 서버에 요청을 전달
  웹 서버는 XMLHttpRequest로부터의 요청을 알맞게 처리
  웹 서버는 결과를 XML이나 단순 텍스트로 생성해서
  XMLHttpRequest에 전송
  클라이언트 브라우저로 서버로부터의 응답이 도착하면
  XMLHttpRequest 객체는 자바스크립트에 도착 사실을 알림
  자바 스크립트는 응답 데이터와 DOM을 조작해서 사용자 화면에 반
  영
  ```

  - XMLHttpRequest(XHR)객체
    - Ajax에서 서버와 클라이언트 간에 통신을 담당
    - 생성시 var httpRequest = new XMLHttpRequest(); 으로 생성
    - abort() - 중단
    - open(method, url, async) - 사용자의 요청을 설정
      - 요청의 초기화
      - GET/POST 선택
      - 접속할 URL입력
      - 동기/비동기 방식 지정
    - readyState - 요청 객체의 상태를 리턴
    - send()
      - 웹 서버에 요청 전송
    - onreadystatechange
      - 웹 서버로부터 응답이 도착할 때 호출될 함수를 지정
      - 콜백(callback)함수
      - 화면을 변경하거나 경고 창을 띄우는 등 응답 결과에 따라 알맞은 작업을 수행
      - 콜백함수는 readyState라는 프로퍼티의 값이 변경될때마다 호출

- $.ajax() 메서드
  - $.ajax(options);
  - $.ajax(url, options);
  - Ajax가 성공했을 때 자동으로 success 이벤트 실행
  - success 이벤트 핸들러의 첫 번째 매개 변수는 Ajax가 성공했을 때 받은 데이터
    - 문서 객체에 추가
  - $.ajax() 메서드의 매개 변수 url
  - 옵션 속성 중 data 속성 사용
    - 요청 매개 변수를 쉽게 지정 가능
  - $.get() 메서드 사용
  - $.post() 메서드 사용
    - HTML 태그 가져와 문서 객체에 출력할 때
    - $(selector).load() 메서드 사용하면 훨씬 간단
