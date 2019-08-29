<%@ page contentType="text/html;charset=utf-8" %>
<%@ page import="java.util.Date" %>
<%-- jsp주석 : HTML태그 + Java코드 포함 --%>
<html>
<head>
<meta charset="utf-8"/>
<title>Hello.jsp</title>
</head>
<body>
  처음 만들어보는 JSP페이지입니다.<br>
  <%
  Date now = new Date();
  out.println(now);
  %>
</body>
</html>
  <!-- 자바 코드 영역>
</body>
</html>
