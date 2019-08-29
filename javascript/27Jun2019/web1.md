## JSP와 서블릿

#### JSP와 서블릿

##### 복습

  - 자바스크립트로 지도 보여주기
    ```
    navigator.geolocation.getCurrentPosition(success콜백함수, error콜백함수, [options] 객체형태)
    sucess콜백함수(Position객체){
      Position.coords.latitude
      Position.coords.lonitude
      ....
    }

    error콜백함수(error객체){
       error.message
       error.code
       ...

    }
    ```
  - servlet
    - www 웹 서비스를 제공하는 웹 서버에서 실행되는 웹 컴포넌트를 구현하는 기술
    - 웹 요청을 처리, 처리 결과를 동적으로 응답 페이지 (html) 생성, 응답
  - WAS
    - Web server + applicatio server를 결합
      - (http listener, http demon) + web container(서버에서의 실행되는 웹 컴포넌트의 실행환경을 제공, 네이밍 컨텍스트(이름)의 기능과 풀링 기능(반납)도 제공을 해줘야함.)
  - JSP
    - Java Server Page이며, script이다.
      - 웹 컨텍스트 표준 구조로 만들어짐
        - 웹 컨택스트(ex : http://ip:8080/web1)
          - [----- html, js, css, image, ....jsp]
          - [----- WEB-INF (보안 폴더)]
            - [----- classes(패키지형태 - 클래스파일)]
            - [----- lib - (jar파일 형태 - 외부 java로 만들어진 library)]
            - [----- web.xml(웹 컨텍스트 환결설정파일) - 컨텍스트의 파라미터, 리스너, 필터, 전역세선timeout, 전역error페이지, 서블릿, 리소스 참조, welcomepageList, ]
            - [----- src]
            - [----- tld, tags]

  - [servlet Spec]
    - 패키지 선언
    - public class로 선언
    - httpServlet 상속 받고
    - life cycle 메서드 override (안하면 부모 것으로 됌)
      - 반드시 override해야 메서드는 service(), doGet(), doPost(), doPut()... 등
      ```
      service(httpServletRequest request, httpServletResponse response) throws ServletException, IOException
      ```

  - [JSP Spec]
    - 정적 페이지 선언 <%@ page ..... %>



##### basic

  - 서블릿
    - 서블릿 클래스의 작성, 컴파일, 설치, 등록,  웹 브라우저로부터 데이터 입력받기
    - JSP는 서블릿 기술에 기반함
    - 서블릿 컨테이너
      - 자바가상머신을 내장한 서블릿 운영환경
      - JSP는 서블릿으로 변환되어 실행
      - 대부분 별도의 실행환경 없이 서블릿 컨테이너에 통합
    - 장점
      - 쓰레드를 기반으로 하므로 웹 애플리케이션 운영에 효율적
      - 자바를 기반으로 하므로 자바 API를 모두 사용
      - 영체제나 하드웨어에 영향 X
      - 한 번 개발된 애플리케이션은 다양한 서버 환경에서도 실행이 가능
      - 웹 애플리케이션에서 효율적인 자료 공유 방법을 제공
    - 서블릿 API
      - 서블릿은 자바 클래스로 제작됨.
      - javax.servlet.GenericServlet과 javax.servlet.http.HttpServle
        - HttpServlet 구조
          - 일반적으로 서블릿은 javax.servlet.http.HttpServlet 을 상속
          - service() 메서드는 컨테이너에서 호출
          - doGet(), doPost()  메서드를 오버라이드해서 처리에 필요한 기능을 구현
        - GET 방식, POST방식
          - GET 방식
            - 서버에 있는 정보를 가져오기 위해 설계, 240바이트까지 전달
            - QUERY_STRING 환경변수를 통해 전달
            - URL노출로 보안성이 요구되는경우엔 사용할 수 없음
            - 검색엔진에서 검색단어 전송에 많이 이용
          - POST 방식
            - 서버로 정보를 올리기 위해 설계
            - 데이터크기의 제한 없음
            - URL에 파러미터가 표시 안됨.
        - HttpServletRequest 클래스
          - HttpServlet 클래스의 doGet(), goPost() 메서드 호출시 파라미터로 전달
          - 사용자요청과 관련된 정보를 제공
          - HTML 폼 입력값을 가
