$(document).ready(function(){
	$("#login").click(function(){
		var uid = $("#userid").val();
		var upwd = $("#userpwd").val();
		$.ajax({
			url: "partPage.jsp",
			data: {userid: uid, userpwd:upwd},
			sucess : function(data){
				var result = $(data).find("result").text();
				var name = $(data).find("id").text();
				if (result == 1){//사용자 인증성공시
		      var str="<table><tr><td align='center'><b>"+name+"</b> 님 오셨구려..</td></tr>"
		      str+="<tr><td align='center'><input type='button' id='logout' value='로그아웃' onclick ='logoutMethod()'/></td></tr></table>"
		    	  $("#confirmed").html( str );
		    }else if(result==0){//사용자 인증실패시 - 비밀번호가 틀림
		      alert("비밀번호가 맞지 않습니다.\n다시 입력해 주시기 바랍니다.");
		     $("userid").val(name);
		     $("userpwd").val("");
				 $("userpwd").focus();
		    }else{//사용자 인증실패시 - 아이디가가 틀림
		      alert("아이디가 맞지 않습니다.\n다시 입력해 주시기 바랍니다.");
					$("userid").val("");
					$("userpwd").val("");
					$("userid").focus();
				}
			}
		})
	})
})

/*
function logoutMethod(){
	var url = "partPagelogout.jsp?timestamp="+ new Date().getTime(); //요청 URL설정
	xhr.onreadystatechange = logoutProcess; //응답결과를 처리메소드인 logoutProcess()메소드 설정
    xhr.open("Get", url, "true");//서버의 요청설정 - url변수에 설정된 리소스를 요청할 준비
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhr.send(null);//서버로 요청을 보냄
}


function logoutProcess(){//partPageDBUselogout.jsp페이지에서 응답결과가 오면 자동으로 실행
	if(xhr.readyState == 4){ //요청객체의 상태가 모든 데이터를 받을 수 있는 상태로 완료된 경우
	  if(xhr.status == 200){ //서버로부터 응답받는 HTTP상태가 정상인 경우 수행

		 var str="<table><tr><td>아이디</td><td><input type='text' id='id' size='15' maxlength='12'/></td></tr>";
         str+="<tr><td>비밀번호</td><td><input type='password' id='passwd' size='15' maxlength='12'/></td></tr>";
         str+="<tr><td colspan='2' align='center'><input type='button' id='login' value='로그인' onclick ='startMethod()'/></td></tr></table>" ;

         document.getElementById("confirmed").innerHTML = str;
	  }
	}
}
*/
