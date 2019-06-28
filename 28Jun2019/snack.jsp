<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title></title>
</head>
<body>
	<h3 id='header'>과자슈퍼</h3>
	<div id='main' style='text-align:center'>
		<br><br> 
		<form method=post action="./snack " >
		<table style='border:1px #0000FF dotted;text-align:center'>
		<tr><td></td><td>가격</td><td>개수</td></tr>
		  <tr><td>새우깡</td>
		  	<td><input type="number" max="1000" min="0" step = "10" name="price1" ></td>
		    <td><input type="number" max="5" maxlength="1" min="0" name="value1" ></td></tr>
		     <tr><td>바나나킥</td>
		  	<td><input type="number" max="1200" min="0" step = "10"  name="price2" ></td>
		    <td><input type="number" max="5" maxlength="1" min="0" name="value2" ></td></tr>
		      <tr><td>양파링</td>
		  	<td><input type="number" max="1300" min="0" step = "10"  name="price3" ></td>
		    <td><input type="number" max="5" maxlength="1" min="0" name="value3" ></td></tr>
		  <tr><td colspan=2 style='text-align:right'>
			<input type=submit value='계산'>
			
		</table>
	</form></div></body></html>