document.addEventListener("DOMContentLoaded", () => {
  // submit 때의 동작 정의하기! 
  document.getElementById("comment-form").onsubmit = () => {
    // 코멘트 입력(input 요소 ) 추출하기
    const commentInput = document.getElementById("comment-input");

    if (commentInput.value === ""){
      // 코멘트가 입력되지 않았다면 아무것도 하지 않기
      return false;
    }
    //입력한 코멘트를 기반으로 li 요소 만들기
    const newComment = document.createElement("li");

    // 생성한 li 요소를 DOM에 넣기 
    newComment.innerText = commentInput.value;
    document.getElementById("comments").appendChild(newComment);

    // 코멘트를 입력한 input의 내용 지우기 
    commentInput.value = "";
    return false;
  }
})
