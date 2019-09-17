<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>message.jsp</title>
</head>
<body>
  <h3>메시지 전송</h3>
  <form id="f1" action="./message" method="post">
         메시지를 입력하세요<br>
    <input type="text" name="msg" size=50><br>
    <input type="submit" value="전송"><br>
  </form>

</body>
</html>