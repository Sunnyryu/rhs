var req; //XMLHttpRequest객체를 저장할 변수를 전역변수로 선언
window.onload= function(){ //브라우저가 로드 되었을 때 처리를 실행하는 메소드(이벤트 핸들러)를 정의
	req = new XMLHttpRequest(); //XMLHttpRequest객체 생성
	document.getElementById("login").onclick = startMethod;
};

function startMethod(){
	var uid = document.getElementById("userid").value;
    var upwd = document.getElementById("userpwd").value;
    var url = "partPage.jsp"; //요청 URL설정
	req.onreadystatechange = resultProcess; //응답결과를 처리메소드인 resultProcess()메소드 설정
    req.open("post", url, "true");//서버의 요청설정 - url변수에 설정된 리소스를 요청할 준비
    req.setRequestHeader("Content-type",
    		"application/x-www-form-urlencoded");
	req.send("userid="+uid+"&userpwd="+upwd);//서버로 요청을 보냄
};

function resultProcess(){//partPageDBUse.jsp페이지에서 응답결과가 오면 자동으로 실행
	if(req.readyState == 4){ //요청객체의 상태가 모든 데이터를 받을 수 있는 상태로 완료된 경우
	  if(req.status == 200){ //서버로부터 응답받는 HTTP상태가 정상인 경우 수행
		 confirmedProcess(); //cofirmedProcess()메소드 호출
	  }
	}
}

function confirmedProcess(){//로그인의 성공과 실패에 따라 표시되는 내용을 결정하는 메소드
    var result =req.responseXML.getElementsByTagName("result")[0].firstChild.data;
    var name = req.responseXML.getElementsByTagName("id")[0].firstChild.data;

    if (result == 1){//사용자 인증성공시
      var str="<table><tr><td align='center'><b>"+name+"</b> 님 오셨구려..</td></tr>"
      str+="<tr><td align='center'><input type='button' id='logout' value='로그아웃' onclick ='logoutMethod()'/></td></tr></table>"
    	  document.getElementById("confirmed").innerHTML = str;
    }else if(result==0){//사용자 인증실패시 - 비밀번호가 틀림
      alert("비밀번호가 맞지 않습니다.\n다시 입력해 주시기 바랍니다.");
      document.getElementById("userid").value=name;
      document.getElementById("userpwd").value="";
      document.getElementById("userpwd").focus();
    }else{//사용자 인증실패시 - 아이디가가 틀림
      alert("아이디가 맞지 않습니다.\n다시 입력해 주시기 바랍니다.");
      document.getElementById("userid").value="";
      document.getElementById("userpwd").value="";
      document.getElementById("userid").focus();
    }
}



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
