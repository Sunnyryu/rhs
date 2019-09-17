<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>result.jsp</title>
<style>
  #blue {
    font-size: 20px;
    color: blue;
  }
  
  #green {
    font-size: 20px;
    color: green;
  }
</style>
</head>
<body>
  <h3>메시지 전송 결과</h3>
  message.jsp에서 보낸 파라미터 메시지 :
  <p id="blue">
  <%
    out.println(request.getParameter("msg") +"<br>");
  %>
  </p>
  MessageServlet에서 보낸 추가 정보 :
  <p id="green">
  <%
    String msg2 = (String)request.getAttribute("msg2");
    out.println(msg2 +"<br>");
  %>
  </p>

</body>
</html>