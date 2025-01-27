## Basic8

#### JS1


```
Naming Convention
- LowerCamelCase
- 일반적인 Camel case
- UpperCamelCase
- snake_case (_ 형태로 나눔 )
- Hungarian notation ( 해당 변수 앞에 타입을 명시하는 방법 )
ex) u16number => unsigned 16 bit 로 저장되는 것이다. 
ex2) s32num => signed 32 bit로 저장되는 것
- kebab-case (dash(-)로 구분하는 것 )

JS의 변수 ! 

let => 변수 타입 (값을 재할당할 수 있는 변수를 선언하는 키워드 ) 선언은 1번만 가능 !!, 재할당은 가능!, block
const : 선언도 1번만 가능, 재할당은 불가능 !, block
var : ES6 이전에 문제가 많이 발생하였음!

조건문 
if / else if 로 구성 

loop 문 (while, for)

- while 문 
- for 문 
 - for of 
 - for in 

화살표 함수 
- 익명 함수
- function 표현에 비해 구문이 단순함
- 생성자로 사용할수가 없음
-사용법( function을 생략 가능 !, 인자가 1개인 경우 괄호도 생략 가능! , return과 {}도 생략이 가능)

 - 배열 (array)

 - Object

 - JSON
   - 문자열이기에 object로 쓰기위해 변환과정이 필요.
   - JSON -> object
      parse
   - object -> JSON
     stringify

   - object : JS 의 Key:value 의 자료구조
   - JSON : 데이터를 표현하기 위한 단순 스트링

 - Array Helper Method
   - 자주 사용하는 로직을 재활용 할 수 있게 만든 일종의 라이브러리
  - forEach, filter, find, map, every, some, reduce

 -forEach
 - array.forEach(callback(element, index, array))

 - map 
  - array.map(callback(element, index))

 -filter 
  - array.filter(callback(element,..))

 - reduce 
  - array.reduce(callback(acc, element, idx,), acc init_value)

 - find 
   - array.find(callback(element, index, array))

 - some & every
   - some 
   - every 
```
CallBack function
다른 함수에 인수로 넘겨지는 함수
function doSomething(task, callback){
  alert(`자, ${task} 준비를 해봅시다!!`)
  callback()
}

// callback함수에 익명함수 추가
//  doSomething('탕수육 먹을', function (){
//  alert(`뿜빠이로 맛난 탕슉 먹으로 갑시다!`)
// })

function whereGo(){
  alert(`탕슉 어디가 맛나나요??`)
}

doSomething('탕수육 먹을', whereGo)
EventListener - EvenTarget.addEventListener(type, callback)

EventTarget : 이벤트 리스너를 등록할 대상
type : 이벤트 유형을 뜻하는 문자열. 이벤트 종류
callback : 이벤트가 발생했을때 처리를 담당, e (event객체) - 이벤트가 발생했을때 실행되는 절차
무엇을? EventTarget 을
언제? type 이벤트가 발생했을때
어떻게? callback 함수에 구현된 내용을 실행한다.
BOM & DOM 1. BOM(Browser Object Model)

JS 브라우저와 소통하기 위한 모델
브라우저에 따라 다르게 구현되기도 하고 한정적임.
웹 브라우저의 버튼, URL 주소 입력, 타이틀바 같은 브라우저 일부분을 제어할 수 있다.
window 객체로 접근가능
전역 JS 객체, 함수, 변수들은 자동으로 window 객체의 맴버가 됨.
HTML DOM 역시 window 객체의 속성
window.print() // 인쇄창을 오픈
window.open()  // 탭 오픈
window.document // document도 브라우저 종속 -> window 전역 객체에 포함.
window.confirm() // 확인&취소 버튼이 있는 대화상자를 표시
2. DOM(Document Object Model)
- HTML 파일에 작성된 요소(Element)들을 조작할 수 있다.
- 요소에 이벤트를 등록해서, 특정 이벤트가 발생할시 특정 함수를 실행하도록 할 수 있다.
- HTML 문서에 작성하지 않은 내용도 새로운 요소를 생성해서 추가할수 있다.

- [DOM Tree](https://medium.com/@wooder2050/%EB%B0%94%EB%8B%90%EB%9D%BC%EC%BD%94%EB%94%A9-prep-course-12%EC%9D%BC%EC%B0%A8-eca7680613ac)
- __요소를 선택하여 변수를 할당__
  - document의 querySelector (getElementById, .... )
  - querySelector : 위에서 부터 css 선택자 요소를 찾으며 가장 먼저 찾아지는 요소를 반환
  - querySelectorAll : 일치하는 모든 요소를 반환
  ```
  const bg = document.querySelector('.bg')
  ```
  - __부모에서 자식요소 선택하기__
  ```
  const movcon = bg.querySelector('#movcon')
  ```
    - __요소 속성 확인__
    ```
    movcon.id // id값 확인
    movcon.src // src값 확인
    ```
    - __요소 속성 변경__
    ```
    movcon.src = '' // 이전에 설정된 값 삭제됨.
    movcon.src = '다시 값을 넣기' 
    ```
    - __요소의 스타일 변경__
    ```
    movcon.style
    movcon.style.width = '300px'
    ```
  - __요소 삭제 및 추가__
    - __요소 삭제__
    ```
    const movcon = document.querySelector('#movcon')
    movcon.remove() // 해당 요소를 삭제
    ```
    - __자식 요소 삭제하기__
    ```
    const bg = document.querySelector('.bg')
    // 1. 첫번째 자식요소 삭제 방법
    bg.firstElementChild.remove()

    // 2. 마지막 자식요소 삭제 방법
    bg.lastElementChild.remove()

    // 3. 특정 요소를 선택해서 삭제 방법
    const movcon = document.querySelector('#movcon')
    bg.removeChild(movcon)
    ```
  - __새로운 요소 생성__
    - createElement 함수를 통해 생성
    - 생성한 태그는 속성값이 없기에 일일히 할당해줘야함.
    ```
    // 이미지 태그 생성
    const newMovcon = document.creatElement('img')

    // 속성값 할당
    newMovcon.src = "원하는 이미지 주소"
    newMovcon.id = "movcon"
    newMovcon.alt = "movcon"
    ...
    ```
  - __생성된 요소를 목표대상에 추가하기__
    - 단순하게 태그를 생성만으로 DOM에 그려지지 않는다.
    - append 함수로 추가하거나 insertBefore 함수로 특정 요소전에 삽입가능.
    ```
    // div 태그에 요소 추가
    bg.append(newMovcon)

    // div 태그의 자식 태그 중에서 가장 처음 부분에 요소 추가
    bg.insertBefore(newMovcon, bg.firstElementChild)
```

```
