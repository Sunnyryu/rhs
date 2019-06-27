<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>main.jsp</title>
</head>
<body>
<%=request.getAttribute("userid") %>님 환영합니다.^^<br>
<a href="cookieLogout"><button>로그아웃</button></a>

</body>
</html>
