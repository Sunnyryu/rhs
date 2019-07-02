## JSP

#### JSP, Web

###### Basic


- http 요청 메시지로부터 헤더 정보 추출
  - 예) http://ip:port/web1/header 요청  -> @WebServlet("/header")
  - 선언된 서블릿이 요청을 처리  
  - HttpServletRequest.getHeaderName() :Enumeration<String>
    - Enumeration.hasMoreElement() : boolean
    - Enumeration.nextElement() : String
    - HttpServletRequest.getHeader() : header이름으로 저장된 value를 반환(String)
    - HttpServletRequest.getHeaders() :header이름으로 저장된 value가 하나 이상이면 String[] 반환


- http 요청 메시지를 전송한 클라이언트 ip 정보 추출
    - HttpServletRequest.getRemoteAddr()

- http 요청 메시지를 전송한 방식 정보 추출
    - HttpServletRequest.getMethod()

- WAS가 서비스하는 웹 컨텍스트를 생성하면 웹 컨텍스트를 추상화한 객체
    - ServletContext

- HttpServletRequest.getServletContext()
  - 요청한 웹 컨텍스트의 객체를 반환하는 메서드

- 클라이언트가 form태그내에 data를 서버 웹 컴포넌트로 전송,서버 웹 컴포넌트에서 클라이언트가 보낸 form 데이터 추출하려면
-
```
HttpServletRequest.getParameter("input 요소의 name속성값")
checkbox input요소의 checked 요소의 value들을 추출 String[] 반환
HttpServletRequest.getParameterValues("input 요소의 name속성값")
예) 1. memberform.html요청 (단순페이지요청 : GET방식)
    2. HttpListener가 html페이지 응답
    3. 클라이언트가 데이터 입력하고 form data 전송
       <form  action="./join"  method=""  encType="multipart/formdata"  >
    4. @WebServlet("/join") 선언된 서블릿이 요청을 받아서 응답 처리
       파일 업로드 처리하는 서블릿에 선언할 Annotation?
       @MultipartConfig(location="" , maxFileSize="", maxRequestSize="")
       업로드된 파일의 메타정보와 스트림등을 추출하기 위해 반환 객체
       HttpServletRequest.getPart() : Part
       HttpServletRequest.getParts() : Collection<Part>
       Part.getName() : 업로드된 파일 이름 반환
       Part.getContentType() :업로드된 파일의 내용 유형을 반환
       Part.getSize() : 업로드된 파일 크기 반환
       Part.write() :업로드된 파일을 @MultipartConfig의 location에 출력(서버에 파일로 기록, 생성)
```    

- 요청을 동일한 웹 컨텍스트의 다른 servlet 또는 jsp에 전송 가능
  - ServletContext sc = request.getServletContext(); //요청 웹 컨텍스트 객체 반환
  - RequestDispatcher rd = sc.getRequestDispatcher("/다른 servlet 또는 jsp 경로"); //요청을 전달할 다른 서블릿 또는 JSP 경로
      - rd.forward(request, response);
      - rd.include(request, response);

      - HttpServletRequest.setAttribute(키로 사용될 객체, 값 객체);
      - HttpServletRequest.getAttribute(키): Object로 반환되므로 실제 저장한 타입으로 DownCasting해서 사용

      - <a href="./xxx?paramName=paramValue&paramName=paramValue">요청 전달 </a>
        - 전송 방식은 Get방식

- Http 특성은 요청시 Connection되며, 응답이 전송되면 disconnect
  - 비연결형 protocol
  - 상태 정보를 저장할 방법 :  
```
1.클라이언트 브라우저에 저장 (key=value) : Cookie  , setMaxAge()
2.  url의 쿼리 스트링으로 요청시마다 전송
3. 요청을 전송하는 페이지에 form요소로 <input type="hidden" name="" value=""> 로 전송
4. 웹 서버에 객체로 저장 : Session, 클라이언트의 브라우저 종료되어 세션이 종료될때까지만 상태 정보 유지
```
```
1.클라이언트가 특정 웹 서버(tomcat)로 최초 요청을 전송
2.웹 서버(tomcat)가 클라이언트 요청에 대해 응답을 할때 해시 함수 기반JSessionID 값을 생성해서 쿠키로 전송합니다.
3. 클라이언트가 웹 서버로 두번째, 세번재,....요청할때 마다 브라우저 자체적으로 요청 웹 서버에서 보내준 쿠키 정보를 찾아서 전송
4. 웹 서버의 웹 컴포넌트(서블릿)에서 여청과 함께 전송된 쿠기 정보를 추출하려면
   HttpServletRequest.getCookies(): Cookie[]
```

- new Cookie(key, name)객체를 응답으로 전송하려면
  - HttpServletResponse.addCookie()
```
예) 1. http://ip:port/web1/cookieLogin 요청 (GET방식)
    2. @WebServet("/cookieLogin") 서블릿의 doGet() 요청 처리
       - 쿠키 정보 추출 request.getCookies(), userid키로 저장된 값 검색
       - 추출한 쿠키 정보를 request.setAttribute("userid" 쿠키값);
       - RequestDispatcher를 사용해서 "/cookie_login.jsp"로 전달
    3. form태그 전송 ( action="cookieLogin" method="post")
    4.  @WebServet("/cookieLogin") 서블릿의 doPost() 요청 처리
       - 로그인 처리
       - 아이디 저장 checkbox 선택된 경우 userid를 쿠키로 저장
       - RequestDispatcher를 사용해서 "/main.jsp"로 전달
    5. main.jsp에서 로그아웃(/cookieLogout) 요청 (GET 방식)
    6. @WebServet("/cookieLogout") 서블릿  의 doGet() 요청 처리
       -쿠키 정보 삭제  request.getCookies(), 쿠키 정보 추출해서 cookie.setMaxAge(0)으로 삭제
       - RequestDispatcher를 사용해서 다시 로그인 페이지로 전송
  ```     

#####JSP
- 스크립트, HTML태그와 함께 java코드 포함
  - View와 로직이 분리 안되어서..재사용성이 낮음, 페이지단위로 개발
```
Servlet -> JSP -> EJB(망함)  ->  MVC패턴 적용 웹 애플리케이션 구현 (View페이지는 JSP, Controller는 Servlet, data 영속성과 비지니스로직은 JavaObject)

현재 JSP는 MVC구조에서  View로만 제한하며,  태그와 EL(Expression Language)만 사용 권장
```
- JSP요소
```
정적 지시자 <%@ page ~~~%>
            <%@ include  ~~ %>
            <%@ taglib ~~~%>
동적 지시자 <jsp:include ~ ></jsp:include>
            <jsp:useBean ~><jsp:getProperty  ~~~ /><jsp:setProperty ~~/></jsp:useBean>

declare scriptlet <%!  
                     변수 선언 초기화; //변환된 서블릿의 멤버변수로 정의
                     public void method(){
                        문장;
                      } ////변환된 서블릿의 멤버 메서드로 정의
                  %>
scriptlet <%
             자바 실행 문장 ;  //변환된 서블릿의 _service()의 실행문장으로 포함
             ....
          %>                    

expression <%= 출력내용 %> 은 <% out.println(출력내용) %>또는 ${출력내용 }와 동일함
```
