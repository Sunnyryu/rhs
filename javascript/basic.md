```
#웹 컨텍스트의 모든 에러에 대해서 전역으로 에러 처리 페이지를 설정할 수 있습니다.
#웹 컨텍스트의 web.xml 설정파일에 다음 요소들로 정의합니다.
<error-page>
  <error-code></error-code><!-- 404, 500 -->
  <location></location>
  </error-page>
  <error-page>
  <exception-type>java.lang.NullPointerException</exception-type>
  <location></location>
  </error-page>

# 게시판의 유스케이스
- 게시물 작성  -- 사진, 파일 첨부(확장), 비밀번호설정(포함)
- 게시물 목록
- 게시물 보기 -- 댓글(확장)
- 게시물 수정 -- 비밀번호 체크(포함)
- 게시물 삭제 -- 비밀번호 체크(포함)

- 댓글 작성  -- 비밀번호설정(포함)
- 댓글 수정  -- 비밀번호 체크(포함)
- 댓글 삭제  -- 비밀번호 체크(포함)

#게시글의 데이터
제목
내용
작성자
작성일
조회수
글번호
첨부파일(multi?)
비밀번호

#댓글의 데이터
글번호
게시글번호(부모키)
작성자
내용
비밀번호






// 한 페이지에 보일 게시물의 수
int final PAGE_SIZE = 10;
// 그룹의 크기
int GROUP_SIZE =10;
// 요청 페이지: linkPage 값이다.
String reqPage;
// 현재 페이지
int curPage;
// 전체 게시물의 수
int totalCount;
// 전체 페이지의 수
int pageCount;

int curPage = 1;
//curPage 파라미터값이 없으면 현재페이지를 1로 설정
if(request.getParameter("curPage")!=null ){
     curPage = request.getParameter("curPage");
     }


if(curPage > 1){
rs.absolute((curPage-1)*PAGE_SIZE);
// 전체 게시물 기준으로 현재 페이지의 게시물 번호를 표시하기 위한 변수
i = i-((curPage-1)*PAGE_SIZE);
 }



// 전체 게시물 수와 페이지 크기를 가지고 전체 페이지 개수를 계산한다.
// 소수점에 따라 계산 상의 오류가 없도록 두 가지 중 한 가지를 이용한다.
방법 1 : pageCount = totalCount / PAGE_SIZE;
if((totalCount % PAGE_SIZE) !=0)
pageCount++;

방법 2 : pageCount = (int)Math.ceil(totalCount / (PAGE_SIZE+0.0));


// 현재 페이지 그룹 설정
int curGroup = (curPage-1) / GROUP_SIZE;

linkPage = curGroup * GROUP_SIZE;
// 첫 번째 그룹이 아닌 경우
if(curGroup > 0) {
 out.println("<a href=list-page.jsp?page="+linkPage+"><<이전</a>");
 }
 // 다음 링크를 위해 증가시킨다.
linkPage++;

 int loopCount = GROUP_SIZE;
 // 그룹 범위 내에서 페이지 링크를 만든다.
 while((loopCount > 0) && (linkPage <= pageCount)) {
 out.println("[<a href=list-page.jsp?page="+linkPage+">"+linkPage+"</a>] &nbsp;");
 linkPage++;
 loopCount--;
 }

// 다음 그룹이 있는 경우
if(linkPage <= pageCount) {
out.println("<a href=list-page.jsp?page="+linkPage+">다음 >></a>");
}
```
