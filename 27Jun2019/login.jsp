<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>사용자 로그인</title>
</head>
	<body>
	<h3 id='header'>사용자 로그인</h3>
	<div id='main' style='text-align:center'>
		<br><br>
		<form method=post action="cookieLogin" >
		<table style='border:1px #0000FF dotted;text-align:center'>
		  <tr><td>사용자 ID </td>
		     <% if(request.getAttribute("userid")==null){
		     %>
		    <td><input type=text name=userid></td></tr>
		    <% }else{
		    	String uid = (String)request.getAttribute("userid");
		     %>
		     <td><input type=text name=userid value="<%=uid%>"></td>
		     <%} %>
		  <tr><td>사용자 암호 </td>
		    <td><input type=password name=passwd></td></tr>
		  <tr><td>아이디 저장 사용 </td>
		    <td><input type=checkbox name=cookie></td></tr>
		  <tr><td colspan=2 style='text-align:right'>
			<input type=submit value='로그인'>
			<input type=reset value='취소'></td></tr>
		</table>
	</form></div></body></html>
