<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>result.jsp</title>
<style>
#blue(color : blue;)
</style>
</head>
<body>
<h3>메세지 전송 결과</h3>
message.jsp에서 보낸 파라미터 메서지 :<br>
<p id="blue">
<%out.println(request.getParameter("msg")+"<br>");
%>
</p>
<p id = "green">
<% String msg2 = (String)request.getAttribute("msg2");
out.println("msg2"+"<br>");
%>
</p>
<br>
<input type = "submit" value="전송">
</body>
</html>
