## JQuery

#### 복습

- jQuery - 모든 브라우저에서 동작하는(클라언트 side에서 실행) 자바스크립트로 만들어진 라이브러리
- html의 문서요소를 간결하게 처리할 수 있다.
```jQuery
<head>내에 <script src="로컬경로/jquery-3.x.x.js"></script>
           <script src="CDN서버 경로 "></script>
jQuery(문서 요소  | 함수)
$(문서 요소  | 함수)
```
- 일관된 이벤트 핸들러 등록 - on(), off()
  - on이벤트명 = function(){}
  - addEventListener("이벤트명", function(){}, false);
  - removeEventListener("이벤트명", 핸들러);
  - attachEvent()
  - detachEvent()

  - 효과
  - ajax처리 간결하면서 쉽게

  - load이벤트와 유사한 jquery의 이벤트는 ready 이벤트

  - $(document).ready(이벤트 핸들러 함수);
  - $("css select문법")

  - $("태그명")
  - $("#id값")
  - $("태그.class속성값")
  - $("부모태그> 자식태그")
  - $("부모태그  자손태그")


  - jquery는 메서드 체인형태로 사용합니다.
