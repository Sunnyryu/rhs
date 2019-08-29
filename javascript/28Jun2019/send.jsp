<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>send.jsp</title>
</head>
<body>
<h3>메세지 전송</h3>
<form action="./PostServlet" method = "post">
메세지를 입력하세요:
<input type = "text" name= "msg" size= 50><br>
<br>
<input type = "submit" value="전송">
</form>
</body>
</html>