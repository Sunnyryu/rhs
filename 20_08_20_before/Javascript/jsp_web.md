## JSP, HTTP

##### basic

- http 프로토콜을 접속시 생성된 상태 정보를 유지하지 않는 stateless 프로토콜
- 접속시 웹 컨테이너에서 생성된 JSERSSION ID, 로그인 정보, 쇼핑 카트에 저장된 상품 정보 등 상태 정보를 유지하는 방법
  - url의 쿼리 스트림으로 추가
    - http://ip.port/생ㅅ웹컨텍스트/xxx.jsp/JSESSIONID=6341241414414
  - html페이지에 <input type=hidden name ="" value = '> form 전송
  - cookie 사용
    - client에 최초 요청(키와 벨류로 )을 응답으로 보냄
    - 해당 브라우저에서 자동으로 쿠키정보를 보냄 (보낼 때마다 자동으로 항상 보냄 )
```
Cookie = new Cookie(key, value);
HttpServletResponse.addCookie()로 응답(클라이언트에게 전송)
HttpServletRequest.getCookies() : Cookie[] (클라이언트 요청으로부터 쿠키를 추출) //초단위
쿠키 유효기간 설정 setMaxage()로 설정 / logout 때 쿠기정보 삭제 - setMaxAge(0)
```
  - Session 사용 - 웹 컨테이너의 메모리에 저장 (java 기반이므로 객체로 저장)
    - Session객체는 최초 요청 시에 웹 컨테이너가 HttpSession 구현 객체를 생성
    - 요청시에 생섣된 Session 객체를 받아오려면 HttpServletRequest.getSession()
    - setAttribute(key, value)
      - 추가적인 정보를 저장
    - removeAttribute(key)
      - 특정 정보를 삭제하기 위함
    - getAttribute()
    - 웹 컨테이너가 생성된 HttpSession 객체에 저장된 JSESSION ID 반환 메소드 getid()
      - getLastAccessTime()
    - 클라이언트 요청이 없어도 HttpSession을 웹 컨테이너의 메모리에 유지 시간 설정 setMaxInactiveInterval(초)

    - 웹 컨텍스트 전역으로 세션 시간 설정은 web.xml에 다음 설정을 추가함
      - <session-config><session-timueout>30</session-timeout></session-config>
    - 세션에 저장된 상태정보를 삭제하고 세션 객체를 만료시키려면 invalidate()
  - 요청을 재지정
    - 클라이언트가 요청한 Servlet이나 JSP에서 응답하는 대신 요청을 다른 자원(JSP, Servlet)에 전달하는 것
    - Request dispatcher 방식
      - 동일한 웹 컨텍스트의 JSP나 Servlet에게 요청 재지정 가능
      - url주소 표현은 처음 요청한 Servlet이나 jsp
      ```
      ServletContext sc = request.getServletContext();
      RequestDispatcher rd = sc.getRequestDispatcher();
      request.setAttribute(key, value);("/요청 재지정 자원 경로와 이름")
      rd.forward(request, response)
      동일한 웹 컨텍스트의 JSP나 Servlet에게 request를 이용해서 정보 공유 가능
      ```
    - redirect 방식
      - 동일한 웹 컨텍스트의 JSP나 Servlet에게 요청 재지정 가능
      - 다른 웹 컨텍스트의 JSP나 Servlet에게 요청 재지정 가능  
      - 다른 웹 서버로 요청 재지정 가능
      - url주소 표현은 최종 요청이 전달된 Servlet이나 JSP 또는 웹 서버의 주소
      - response.sendRedirect("url의 path형식"); // http://~로 시작, ,/ 상대경로, root context로부터 시작하느 /~ 절대경로 방식
      - 최초 요청시에 컨테이너가 생성된 request의 response는 소멸되고, 새로운 request와 response객체가 edirect된 자원으로 전달
      - 동일한 웹 서버내에 동일한 웹컨텍스트 또는 다른 웹 컨택스트에 공유해야 할 정보를 전달하려고 하면 HttpSession.setAttribute(key, value) 또는 ServletContext.setAttribute(key, value)
```
# JSP - HTML 또는 XML 기반의 동적인 웹 컨텐츠를 개발하는 스크립트
        응답되는 웹 페이지의 컨텐츠를 만들기 위해 사용(View로만 제한), 텍스트 기반의 문서
        자바 코드 로직을 가능한한 포함하지 않고 태그, el로만 컨텐츠를 생성 권장

# 정적 지시자
<%@ page contentType="text/html;charset=ut-8"  
         session
         buffer
         isThreadSafe
         errorPage
         isErrorPage
         info
         language
         import
         extends
         isELIgnored
         defferedSyntaxAllowedAsLiteral  %>


<%@ include file="" %>        #JSP 페이지내에 다른 JSP페이지를 포함   
- 포함될 JSP페이지에서 <html>, <head>, <body>를 제외하고, <body>태그의 내용의 컨텐츠만 ..


<%@ taglib  prefix="" uri="http://java.sun.com/jsp/jstl/~" %>
 JSP페이지내에 HTML 이 아닌 태그를 만나면 태그에 매핑된 Java class를 실행시켜서 실행 결과를 페이지의 컨텐츠로 처리
 JSTL(Java Standard Tag Library)을 사용하기 위한 선언 , core, sql, xml, 국제화 format처리 라이브러리등을 사용하기 위해 선언


 text/xml
 text/plain, text/json
 image/jpeg
 ...
 application/vnd.ms-    
 ${}
#{} 템플릿 컨텐츠  -  JSF의 표현식

최초 JSP 요청 -> 컨테이너가 변환된 서블릿 java파일을 검색 -> 존재하지 않으면 서블릿 java파일 변환 -> 컴파일 -> 클래스를 메모리 로딩 -> 서블릿 객체 생성 -> lifecycle 메서드 호출
# declare <%!  전역변수 또는 메서드 정의   %>  : 변환된 서블릿의 멤버로 정의
# scriptlet <%  자바 실행 문장;  %> : _jspService()메서드의 문장으로 포함
# expression <%=  출력내용   %> : 변수, 연산식, 값을 리턴하는 함수등 웹 페이지에 출력할 내용, <% out.println(출력내용) %> , ${출력내용}

jsp 주석
<%-- JSP 주석 --%>
<%
//주석
/*주석  */
%>
<!-- html & xml 주석 -->

```

- 동적인 요청을 처리하는 jsp을 요청과 응답을 처리하기 위해서 jsp 컨테이너가 서블릿으로 변환하면서 내장 객체들을 생성해서 (_jspService()로 전달)


```
- request - javax.servlet.http.HttpServletRequest
- response - javax.servlet.http.HttpServletResponse
- session - javax.servlet.http.HttpSession
- application - javax.servlet.ServletContext
- out - javax.servlet.jsp.JSFWritter
- exception - java.lang.Throwable
- page - java.lang.Object
- config - javax.servlet.ServletConfig
- pageContext - javax.servlet.jsp.pageContext

```

```
내장 객체들의 유효 범위 - 컨테이너 메모리에 유지되는 범위
page - 요청된 JSP가 수행되는 동안에만 유지
request - 요청이 종료될때까지...<jsp:include ~> <jsp:forward ~> 로 다른 JSP또는 서블릿으로 공유될때까지
session  - 세션 만료 될때까지 또는 inactive상태에서는 30분
application - 웹 켄텍스트가 웹 컨테이너로부터 삭제될때까지 또는 웹 컨테이너가 종료될때까지

page, request, session, application에 정보를 저장, 삭제, 반환 메서드
setAttribute(),
getAttribute()
removeAttribute()
getAttributeNames()
```

- 자주 구현하는 기능을 태그로 정의

```
표준 액션 태그
<jsp:useBean~~  JSP 스펙에 정의된 기능, 모든 JSP 컨테이너가 지원하므로 항상 JSP 구현에 사용 가능
커스텀 액션 태그
개발자가 직접 태그 클래스 ,  tld(xml형식) 파일을 정의해서 사용

EL(Expression Language)
표현언어, JSP2.0에서 추가    
<c:out ...> 또는 <jsp:getProperty ..> 보다 간결하게 사용가능
page, session, request, application 에 저장된 객체를 간결하게 표현함
```
