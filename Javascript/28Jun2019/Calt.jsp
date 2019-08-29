<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title></title>
</head>
<body>
	<h3 id='header'>계산기</h3>
	<div id='main' style='text-align:center'>
		<br><br> 
		<form method=post action="./calt" >
		<table style='border:1px #0000FF dotted;text-align:center'>
		  <tr><td>num1</td>
		    <td><input type=number name="num1"></td></tr>
		  		<tr><td>math sign<td>
		    	<select name="mathsign">
    			<option value="+"></option>
    			<option value="-">-</option>
    			<option value="*">*</option>
    			<option value="/">/</option>
					</select></tr>
		  <tr><td>num2 </td>
		    <td><input type=box name=num2></td></tr>
		  <tr><td colspan=2 style='text-align:right'>
			<input type=submit value='계산'>
			
		</table>
	</form></div></body></html>