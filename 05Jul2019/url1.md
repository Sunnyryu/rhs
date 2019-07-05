#### URL PATH 방식 경로지정

```
url path 방식 경로지정  
1. full path ex) http://70.12.40.130/board/list.do
2. 절대 경로 방식  /board/list.do
3. 상대 경로 방식 ./list.do   (.은 현재 경로 , ..은 상위 경로)
<a href="url path 방식"></a>
<form action="url path 방식">
response.sendRedirect("url path 방식");

ServletContext 기반 경로 지정
ex)/listd.o  (/은 현재 컨텍스트 board아래를 의미함)
ServletContext.getRequestDispatcher("/list.do")
@WebServlet("/list.do")
web.xml의 <url-pattern>/* </url-patter> 또는 <url-pattern>/list.do </url-patter>
```
