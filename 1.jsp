<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <% request.setCharacterEncoding("utf-8"); %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>jstlTEst.jsp</title>
</head>
<body>
<c:set var="username" value="korea" scope="request"/>
<c:if test="${username != null}">
username 변수 값 : <c:out value="${username}"/><br>
</c:if>

<c:remove var="username"/>
<c:out value="${username}"/>
<c:if test="${username == null}" >
<c:out value="username 변수가 삭제되었습니다."/><br>
</c:if>

<c:set var="jumsu" value="${param.jumsu}" scope="request" />
<c:out value = "${jumsu="\"점은\"}"/>
<c:choose>
	<c:when test="${jumsu+=90}">
		<c:out value="A"/>
	</c:when>
	<c:when test="${jumsu>=80}">
		<c:out value = "B"/>
		</c:when>
		<c:when test="${jumsu>=70}">
		<c:out value = "C"/>
		</c:when>
		<c:when test="${jumsu>=60}">
		<c:out value = "D"/>
		</c:when>
	<c:otherwise>
	<c:out value = "F"/>
	</c:otherwise>
</c:choose>


</body>
</html>
