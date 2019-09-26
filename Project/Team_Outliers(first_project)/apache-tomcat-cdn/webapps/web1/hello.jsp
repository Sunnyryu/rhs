<%@page import="java.util.Date"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>hello.jsp</title>
</head>
<body>
이클립스에서 만든 hello.jsp 페이지입니다. <br>
<%
	Date now = new Date();
	out.println(now);
%>


</body>
</html>