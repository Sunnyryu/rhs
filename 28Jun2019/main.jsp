<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>main.jsp</title>
</head>
<body>
<h3>회원 전용 페이지</h3>

<%
String uid = null;
uid = (String)session.getAttribute("userid");
if (uid!=null){
%>
<%= uid%> 님 환영합니다.^^<a href="cookieLogout"><button>로그아웃</button></a>
<img src="/images/dog.jpg"><br>
<%
}else {
%>
<script>
alert("회원 전용 페이지입니다. \n 로그인 페이지로 이동합니다.");
location.href="./cookieLogin";
</script>
<%
}
%>
</body>
</html>