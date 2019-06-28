<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>결과</title>
</head>
<body>
<% int result = (int)request.getAttribute("result");
	int result1 = (int)request.getAttribute("result1");
	int result2 = (int)request.getAttribute("result2");
out.println("계산서"+"<br>");
out.println("과자명"+"/"+"금액(단가*개수)"+"<br>"+"새우깡"+"/"+result+"<br>"+"바나나킥"+"/"+result1+"<br>"+"양파링"+"/"+result2+"<br>"+"총액"+"/"+(result+result1+result2)+"<br>");
%> 
</body>
</html>