<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>PostResult.jsp</title>
<style>
#blue(color : blue;)
</style>
</head>
<body>
<h3>메세지 전송 결과</h3>
<%
if(request.getParameter("msg")!=null && request.getAttribute("address")!=null){
	

%>
send.jsp에서 보낸 파라미터 메세지 : <%= request.getParameter("msg") %><br>
PostServlet에서 보낸 메세지:<%= request.getAttribute("address") %><br>
<%
}else{
%>
sendRedirect()로 요청을 전달하면,
요청된 페이지에 새로운 request의 response객체가 전달되므로<br>
파라미터와 Attribute를 request로부터 추출할 수 없습니다.<br>
<%
}
%>

</body>
</html>