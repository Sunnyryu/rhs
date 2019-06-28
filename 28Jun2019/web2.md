## Web

#### Web

###### 복습
```
ex) http://id:port/web1/header 요청
  @webServlet("/header")로 선언된 서블릿이 요청을 처리함
  HttpServletRequest.getHeaderName : Enumeration<String>
  Enumeration.hasMoreElement() : boolean
  Enumeration.nextElement() : String
  header 이름으로 저장된 value가 하나이면
  HttpServletRequest.getHeader()를 이용해 저장된 value 변환(String)
  header 이름으로 저장된 value가 하나 이상이면
  HttpServletRequest.getHeaders()를 이용하여 value 변환
```

```
http 요청 메세지를 전송한 클라이언트 ip 정보 추출?
HttpServletRequest.getRemoteADDR()

http 요청 메세지를 전송한 방식 정보 추출?
HttpServletRequest.getMethod()

WAS가 서비스하는 웹 컨텍스를 생성하면 웹 컨텍스트를 추상화한 객체 : Servlet.context()

요청한 웹 컨텍스트의 객체를 반환하는 메서드 : HttpServletRequest.getServletContext()
```

```
클라이언트가 form태그내에 data를 서버 웹 컴포넌트로 전송,
서버 웹 컴포넌트에서 클라이언트가 보낸 form 데이터 추출하려면?
HttpServletRequest.getParameter("input 요소의 name속성값")
checkbox input요소의 checked 요소의 value들을 추출 : String[] 변환
HttpServletRequest.getParameterValues("input 요소의 name속성값")
ex) 1. memberform.html 요청 (단순페이지 요청 : GET방식)
    2. HttpLisner가 html페이지 응답
    3. 클라이언트가 데이터를 입력하고 form data 전송
    4. <form action="ex)./join" method="" encType="multipart/formdata">
       @webServlet("/join") 선언된 서블릿이 요청을 받아서 응답처리
       파일 업로드 처리하는 서블릿에 선언된 Annotation?
       @MultipartConfig(location="",maxFileSize=""(기본이 바이트 단위), maxRequestSize="")
       업로드된 파일의 메타정보와 스트림 등을 추출하기 위해 반환 객체
       HttpServletRequest.getPart() : Part
       HttpServletRequest.getParts() : collection<part>
       Part.getName() : 업로드된 파일 이름 반환
       Part.getContentType() : 업로드된 파일의 내용 유형을 반환
       Part.getSize() : 업로드된 파일 크기 반환
       Part.write() : 업로드된 파일을 @MultipartConfig의 location에 출력
 ```

 ```
 요청을 동일한 웹 컨텍스트의 다른 servlet 또는 jsp에 전송 가능
    ServletCOntext sc = request.getServletContext(); // 요청 웹 컨텍스트 객체 반환
    RequestDispatcher rd = sc.getRequestDispatcher("/다른 servlet 또는 jsp 경로")
    rd.forward(request, response);
    rd.include(request, response);

    HttpServletRequest.setAttribute(키로 사용될 객체, 값 객체);
    HttpServletRequest.getAttribute(키): object로 반한되므로 실제 저장한 타입

    <a href="./xxx?parameterName=parameterValue%parametername=parameterValue">요청 전달</a> : 전송 방식은 get방식

    Http 특성은 요청시 disConnection 됌. -> 비연결형 protocol
    상태 정보를저장할 방법 : 클라이언트 브라우저에 저장(key=value) : Cookie, setMaxAge()
    url의 쿼리 스트링으로 요청시마다 전송
    요청을 전송하는 페이지에 form요소로 <input type="hidden" name="" value="">
    웹 서버에 저장하는 방식이 있음 = Session, 클라이언트의 브라우저 종료되어 세션이 종료 될 때 까지
```

```
    클라이언트가 특정 웹 서버로 최초에 요청을 전송
    웹서버가 클라이언트 요청에 대해 응답을 할때 해시 함수 기반 실행 JSessionID 값을 생성해서 쿠키로 전송함
    클라이언트가 웹 서버로 두번째, 세번째, .... 요청할때 마다 브라우저 자체적으로 요청 웹서버에서 보내준 쿠키 정보를 찾아서 Request 시마다 전송
    웹 서버의 웹 컴포넌트에서 여청과 함께 전송된 쿠키 정보를 추출하려면
    HttpServletRequest.getCookies() : Cookie[]

    new Cookie(key, name) 객체를 응답으로 전송하려면 HttpServletResponse.addCookie()
    ex) 1. http://ip:port/web1/cookieLogin 요청 (GET방식)
        2. @webServlet("/cookieLogin") 서블릿의 doGet() 요청 처리
          - 쿠키 정보 추출 request.getCookies(), userid키로 저장된 값 검색
          - 추출한 쿠키 정보를 request.setAttribute("userid" 쿠키값);
          - getRequestDispatcher를 사용해서 "/login.jsp"로 전달
        3. form 태그 전송 (action = "cookieLogin" method="post")
        4. @webServlet("/cookieLogin") 서블릿의 doPost() 요청 처리
          - 로그인 처리
          - 아이디 저장 checkbox 선택한 경우 userid를 쿠키로 저장
          - RequestDispatcher를 사용해서 "/main.jsp"로 전달
        5. main.jsp에서 로그아웃(CookieLogout) 요청 처리
          - 쿠키 정보 삭제, request.getCookies), 쿠키 정보 추출해서 cookie.setMaxAge(0)으로 삭제
          - RequestDispatcher를 사용해서 다시 로그인 페이지로 전송
