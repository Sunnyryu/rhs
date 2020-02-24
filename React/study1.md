## React 

#### 리액트 스터디 1 

```

리액트는 메모리상에 (인 메모리 가상 DOM을 만들 어서 조작함 ! ) => 가상 DOM 과 실제 DOM을 비교해 변경해야 되는 부분을 파악하고 모든 사항을 최신으로 유지하는 데 필요한 최소의 DOM 변경을 수행함(비교조정)

리액트는 비주얼한 요소를 하나의 큰 덩어리가 아니라 가급적 여러 컴포넌트로 작게 쪼개어 다루도록 권장함 !/리액트는 개념을 사용자 인터페이스와 관련도니 사고의 영역으로 확장 했다 많은 리액트의 핵심 API는 작은 비쥬얼 컴포넌트 제작을 쉽게 함으로써,
나중에 다른 컴포넌트와 결합해 더크고 복잡한 비주얼 컴포넌트를 만들 수 있도록 지원함 (마트로시캬 같은 느낌??)

리액트가 웹앱의 비주얼을 구축하는 우리의 사고방식을 단순화시킨 방법이라고 생각!

리액트는 자바스크립트 만으로 UI를 정의하여 템플릿 안에 모든 종류의 작업을 자바스크립트가 제공하는 풍부한 기능을 사용해 할 수 있으며, 자바스크립트가 지원하는 범위에 한해서는 어떤 제한도 없다는 것임 !! 
리액트는 HTML과 닮은 JSX라고 하는 문법을 사용해 비쥬얼을 지정할 수 있는 옵션을 제공함..

EX1 ) 
ReactDOM.render(

  <div>
  <h1>sunny</h1>
  <h1>tunny</h1>
  <h1>jenny</h1>
  </div>,
  destination
)
위와 같은 식으로 할 수 있다.. 자바스크립트로 작성한다면 

ReactDOM.render(React.createElement(
  "div",
  null,
  React.createElement(
    "h1",
    null,
    "sunny"
  ),
React.createElement(
  "h1",
  null,
  "tunny"
),
React.createElement(
  "h1",
  null,
  "jenny"
)
), destination)
위와 같은 식으로 작성해야한다.
JSX를 사용하면 친숙한 문법으로 비주얼을 정의 가능.. 자바스크립트가 제공하는 강력함과 유연함을 누릴 수 있음 .. 하나의 비주얼 컴포넌트의 모양과 동작을 정의하기 위해 더 이상 여러 파일 사이를 뛰어다닐 필요가 없다는 의미임 !!

리액트는 앱 개발의 모든 사항을 완전히 갖춘 프레임워크가 아니라.. 비쥬얼한 요소와 그 상태가 최신으로 유지하는 데 중점을 두는 뷰 레이어에서 작동한다. 이는 MVC 아키텍처에서 Model과 controller가 무엇이든 원하는 대로 사용할 수 있다는 것임..

JSX 다루기 
일반적인 웹앱은 HTML, CSS, JS로 구성됨! 어떤 JS(React,angular, jquery) 등을 쓰든 간에.. 반드시 웹앱의 조합이여야한다는 것이다.. 
그렇지만 리액트의 경우 일반적인 웹앱 구조에 JSX라는 리액트 코드를 작성해야 하기 때문!! 그런데 JSX는 브라우저가 알 수 없기에 우리는 자바스크립트로 변환을 시켜야함 .. sad

노드와 빌드 툴 등으로 구성된 개발환경을 구축, 빌드를 수행할 때마다 JSX의 모든 사항이 자동으로 JS에 변환되며, 다른 일반적인 자바스크립트 파일처럼 참조할 수 있도록 파일을 디스크에 저장됨..
JSX를 자동변환하는 자바스크립트 라이브러리를 사용함.. JSX를 직접 지정하면되고 나머지는 브라우저가 처리할 수 있음 ..

첫번째 방법은 웹 개발에서 대표적으로 쓰이는 방식임.. 두번째 방법은 개발 환경에 손을 대는 시간을 시간 절약.. 코드 작성에 집중 가능 .(스크립트 파일 하나만 참조하면 됨..)
서로의 장단점이 있는 만큼 상황에 따라 사용하면 낫베드!!

JS에 script로 하여 리액트 관련 라인을 추가해준다. ! 

무언가를 보여주고 싶을 때에는 render를 사용함..
render 메소드는 화면에 출력고 싶은 html 과 JSX를 렌더링해 보여줄 DOM 안의 위치를 설정한다 !

querySelector로 id를 받거나.. render 밖에서 인자를 선언후에 인자를 넣을 수도 있음 !!

계산은 함수를 이용해서 쉽게 할 수 있읍 !! 안에 변수를 선언하고 alert나 console로 띄워서 확인하면 충분히 가능 !!

JSX 팁: 인접한 여러 엘리먼트를 출력할 수 없음 .... 

커스텀 속성을 지정하여, 컴포넌트의 render 메소드에서 this.props를 통해 접근 가능 .. 자식 엘리먼트가 깊이 중첩된 구조의 최상위에 해당한다면 this.props.children 속성은 배열을 리턴한다.  

컴포넌트를 잘활용해야 함 !!

JSX 코드 조각이 HTML로 바뀌게 되염!

리액트는 css를 사용하지 않는 인라인 방식의 스타일링을 선호 .. 비주얼 컴포넌트의 재사용성을 더욱 높일 수 있음 !! 

React 안에서 var로 선언하여 스타일을 넣는 스타일 객체를 만들 수 있음 !!
리액트는 스타일 객체에 px를 생략할 수 있도록 허용함 ! (columnCount, fillOpacity, flex, flexGrow, flexShrink, fontWeight, lineClamp, lineHeight, opacity, order, orphans, widows, zIndex, zoom)

픽셀이닌 다른 것은 넣어줘야함 !!

각 변수에 bgcolor=?를 넣어주고 위의 스타일 객체에 this.props.bgcolor 이런식으로 작성한다면 배경색 커스터 마이징도 충분히 가능하다.

카드 라는 것이 있다고 치자 안에 사각형영역에 컬러를 보여주고 하단에는 16진스를 보여주는 영역이 있다고 보자! 

컴포넌트 식별 .. 한 컴포넌트는 한 역할만 해야하는 것이 규칙임 .. 카드는 컨테이너 역할 / 사각형은 컬러를 보여주는 역할을 할 수 있다.

레이블 자체.. 레이블이 없다면 헥스 값을 볼 수 없고 흰색 영역만 남음.. 흰색 영역은 컴포넌트라고 할 수 없음 ..

컴포넌트 계층 구조..

render 함수는 또 다른 컴퍼넌트의 render 함수에게 일부 html을 리턴함.. 

속성 전달 ..

리액트는 반드시 부모 컴포넌트에서 직계 자식 컴포넌트로만 속성이 내려가도록 하는 명령의 연쇄적인 실행만 가능함.. 속성을 전달할 때 중간 계층을 건너뛸 수 없다는 의미... 자식에서 부모로 속성을 거꾸로 올려보낼 수도 없음.. 소통은 부모로부터 직계 자식에게 일방적으로 이뤄짐 ..

ex) color ="purple" => color = {this.props.color} => color= {this.props.color} 
ex2) color="purple" , size="large" / color={this.props.color} size = {this.props.size}

일일이 넘겨주는 방식을 하면 문제점이 일어나지만 스프레드 연산자를 이용하면 해겨할 수 있음 .. 

var items = {"1", "2", "3"};
function printStuff(a,b,c){
  console.log("Printing: " +a + "" +b + "" + c);
}

printStuff(items[0], items[1], items[2]);
printStuff(...items);

items 배열 앞에 있는 ...이 바로 스프레드 연산자임!!
자식을 일일이 전달하지 않고 한꺼번에 할수 있음 !!

babel은 jsx를 브라우저가 이해할 수 있는 언어로 변환하는 일외에도 최신의 실험적인 기능을 모든 브라우저에 걸쳐 사용할 수 있도록 해줌! / 객체 리터럴에 스프레드 연산자를 사용할 수 있었던 이유, 여러 계층의 컴포넌트에 걸친 속성 전달의 문제를 해결할 수 있음!

JSX는 브라우저가 모르지만.. JSX를 자바스크립트로 변환해서 알 수 있는 것임 ..
JSX는 단 하나의 루트 노트만 리턴 가능함 !!/ 그래서 원하는 결과를 얻으려면 부모 앨리먼트로 감싸서 써야함 !!
JSX에서는 style 속성 안에 css를 포함할 수 없어 스타일 정보를 담은 객체를 참조해야함 !! / 

예약어와 className => break, case 등의 이름은 쓰면 안됨 !!
그래서 React의 JSX에서는 class가 아닌 className으로 해야함 class로 하면 . 동작하지 않음 !!

주석 

주석.. 태그의 자식 위치에 주석을 넣을 떄에는 {/* */} 이런 식으로 넣어줘야함 ..
주석을 태그 안에 넣을 경우에는 /* */로 중괄호 없이 사요가능 !!

대소문자 구별 .. HTML 엘리먼트를 나타날 때에는 소문자로 써야한다 !! 
그렇지만 컴포넌트를 나타날 때에는 그 이름에 대문자를 사용해야함 !! 

JSX 코드는 render나 return 함수 안에만 있는 것이아님..


setInterval 함수를 이용해서 1000밀리초마다 어떤 코드를 호출할 것임! (어떤 코드란 한 번에 100만큼 증가시키는 코드임 !)

getInitialState : 컴포넌트가 마운트 되기 전에 실행되며 컴포넌트의 state 객체를 변경할 수 있게 해줌!
componentDidMount: 이 메소드는 컴포넌트가 랜더링(마운트) 된 후에 실행됨
setState: 이 메소드는 state 객체의 값을 갱신할 수 있게 해줌!!
(리액트에서는 자동 바인딩 기능을 제공하여.. 컨텍스트를 유지하여.. 추가적으로 작업하지 않아도 됨)

데이터는 JSON 객체, 배열 또는 그 밖의 다른 데이터 구조의 형태를 가지며, 리액트 자체나 어떤 시각적 부분과도 관련이 없음.. 

함수를 만들어서 렌더에 뿌려줄 수 있음.. 표현식이 JSX를 리턴하는 한 중괄호 안에 원하는 사항을 넣을 수 있는 유연성이 장점이며, 자바스크립트가 render 함수 밖에 있음으로써 많은 일이 가능하다는 장점이 있음 

엘리먼트를 일종의 식별자로 마킹하는 방법 => 마킹은 JSX에서 엘리먼트를 명식적으로 지정할 때 자동으로 수행함 

이벤트 

무언가를 눌렀을 떄 반응하여 . 반영되는거..? 

이벤트 인자는 e / 시그니처를 보면 알 수 있음.. 

이벤트는 이벤트 핸들러에 인자로 전달.. 이벤트 인자는 이벤트의 종류에 따른 한 무더기의 속성이 들어있음 .. 마우스 이벤트라든가.. 키보드 이벤트 등이 있다..
컴
합성 이벤트 (DOM 이벤트를 직접 다루지 않고 SyntheticEvent를 다룸 .. 항상 브라우저의 네이티브 이벤트를 래핑하는 이벤트 타입을 인자로 받음)

bubbles, cancelable, currentTarget, defaultPrevented, eventPhase, isTrusted, nativeEvent, preventDefault(), isDefaultPrevented(), isPropagationStopped, target, timeStamp, type 등이 있음 

합성 이벤트와 그 속성을 사용할 때는 DOM 이벤트 문서를 참고하지 말고 리액트의 SyntheticEvent 문서를 참조(https://facebook.github.io/react/docs/events.html)

컴포넌트의 이벤트는 직접 리스닝할 수 없어서 .. 다른 컴포넌트를 추가해서 나타내야함 !!

모든 DOM 이벤트가 SyntheticEvent에 대응하지는 않음 .. 따라서 그런 경우에는 addEventLIstener를 사용해서 이벤트를 작동시켜야함 !!

컴포넌트가 소멸된 후에는 더 이상 이벤트 리스닝을 하지 않겠다는 입장을 하기 위해 .. ComponentWillUnmount 메소드 안에 removeEventLister 함수를 추가해야함!

this의 의미: 리액트가 아닌 일반적인 곳에서는 리스닝하는 대상 엘리멘트를 참조한다고 한다. 
그렇지만 리액트에서는 (React.createClass를 한 경우)에는  이벤트 핸들러가 속해있는 컴포넌트로 참조한다.

예를 들어 increase 이벤트에 this가 있다고 할 때 다른 컴포넌트를 참조하는 경우로 써준다. 이는 리액트가 컴포넌트 안의 모든 메소드를 this에 자동 바인딩 시켜준다. 
그렇지만 자동 바인딩 되는 경우는 오직 React.createClass를 통해 컴포넌트를 만든 경우엔느 사용된다.. 

컴포넌트 생명주기 

컴포넌트가 하는 일을 알기 위해 생명주기 메소드를 사용한다. 생명주기 메소드는 컴포넌트가 어떤 작업 단계에 진입할 때 자동으로 호출되는 특별한 메소드 !!

ComponentWillUnmount, componentDidMount, componentWillmount, componentWillUpdate, componentDidUpdate shouldComponentUpdate, componentWillReceiveProps이 있으며,

우리가 많이 쓰는 getInitialState, getDefaultProps, render등은 많이 쓰이는 메소드!! 

getDefaultProps : this.props의 기본값을 지정할 수 있음 . 메소드는 컴포넌트가 만들어지려 할 때나 부모로부터 속성이 전달되었을 때 호출! 
getInitialState: this.state의 기본값을 지정할 수 있게 해줌. getDefaultProps과 마찬가지로 컴포넌트가 만들어지기 전에 호출 
componentWillMount : 컴포넌트가 DOM 안으로 렌더링되기 전에 호출되는 마지막 메소드! . 이 메소드 안에 setState를 호출해도 컴포넌트가 다시 랜더링 되지 않음 .. 갱신되는 일은 없다는 거임..?
render : 컴포넌트에는 이 메소드가 정의되어야 하며, 단 하나의 루트 노드를 리턴하는 책임을 짐.. 랜더링 하고 싶지않으면 단순히 null이나 false를 씀 
componentDidMount: 컴포넌트가 랜다링돼 DOM에 자리잡은 직후 호출됨. RENDER 메소드를 제외한 이 모든 생명주기 메소드는 단 한번만 실행 (모든 준비가 된 컴포넌트라면 모두 이메소드 안에서 수행해야함!)
(초기 렌더링 getDefaultProps, getInitialStatem, componentWillMount render componentDidMount 순으로 쭉쭉 나감 ..)
상태변경시 렌더 메소드가 다시 호출한다.

shouldComponentUpdate : 상태가 변경됬어도 업데이트 변경을 바라지 않는 경우가 있는데 이 메소드르를 사용하면 .. 그와 같은 업데이트 여부를 제어할 수 있게됨!, true 진행, false 무시 .. 
componentWillUpdate: 이 메소드는 컴포넌트가 업데이트되기 직전에 호출..크게 주목할 만한 건 없으나 이 메소드 안에서 this.setState를 사용해 상탤르 변경시킬 수 없음 !!
render : shouldComponentUpdate가 false를 리턴함으로써 업데이터 작업을 건너뛰지만 않는다면 render 메소드가 다시 호출돼 컴포넌트가 올바로 보이게 해줌.
componentDidUpdate: 이 메소드는 컴포넌트가 업데이트 되고 render 메소드 실행이 끝난 다음에 호출됨. 업데이트 후에 수행하고 싶은 코드가 있다면 이 메소드가 가장 적합한 장소임 !
(상태변경: shouldComponentUpdate, componentWillUpdate, render, componentDidUpdate 순으로 쭉쭉 나감)

componentWillReceiveProps: 이 메소드는 하나의 인자를 받는데 그 인자는 새로 할당하고자 하는 속성 값이 포함된 객체임!!
(속성변경 시 componentWillReceiveProps, shouldComponentUpdate, componentWillUpdate, render, componentDidUpdate로 쭉쭉 나감!!)

언마운트 시에는 ComponentWillUnmount으로만 언마운트를 처리함!!

ref:  리액트는 DOM에서의 최종 HTML 엘리먼트와 JSX 사이클을 연결해주는 Ref(reference의 약자)라고 하는 것을 제공함 .. 
통상적으로는 ref 속성의 값에 자바스크립트 콜백 함수를 설정하게 된다. 그 함수는 현재 컴포넌트의 마운트가 끝나면 자동으로 호출됨. 만약 ref 속성의 값으로 단순히 DOM 엘리먼트의 참조를 저장하는 자바스크립트 함수를 지정한다

ES6를 이용하면 .. ref와 관련해 콜밸 함수를 다룰 때 화살표 함수를 사용하면 작업이 좀 더 간편해질 수 있음 (=> , ), 그렇게 되먄 self등을 안쓰고 도 간단하게 만들 수 있음 

Router 컴포넌트는 리액트 라우터 api의 일부로 라우팅과 관련된 모든 로직을 취급함. 컴포넌트 안에는 라우팅 설정을 함. 라우팅 설정은 URL과 뷰 사이의 매핑을 기술 할 때 사용하는 멋진 용어임! 라우팅의 구체적인 사항은 다음과 같은 Route 컴포넌트에 
의해 처리! 

Route 컴포넌트는 어떤 URL에 어떤 화면을 보여줄지 정의하는 데 필요한 여러 속성을 갖음 , path는 URL 경로. component 속성에는 보여주고자 하는 컴포넌트의 이름, 

ReactRouter 접두사의 생략 .. es6에서 접두사를 자동으로 붙이는 방법임 script 태그 안의 가장 윗부분에 다음과 같은 코드를 추가하면 됨 

var { Router, Route, IndexRoute, IndexLink, Link} = ReactRouter; (런타임 시에 자동으로 추가됨 !)

리액트 라우터에서 내비게이션 링크를 적용하는 방법은 a 태그와 href 속성을 사용해 경로를 직접하는 게 아닌 리액트 라우터의 Link 컴포넌트를 사용함! 
Link 컴포넌트에 to라는 속성을 지정하면 주소 표시줄에 표시될 URL을 지정할 수 있음, 리액트 라우터에게 사실상 내비게이션 대상을 알려주는 역할을함! 

리액트 툴 .. 
노드 ( 노드 js를 사용해서 JSX를 자바스크립트로 필요한 목적으로 엮는데 사용함!)
바벨: 자바스크립트 트랜스파일러로서 자바스크립트로 바꿔준다.. JSX나 최신 자바스크립트를 브라우저가 이해하는 자바스크립트로 변환해주는 아이다.

웹팩( 모듈 번들러.. 필요한 관련 코드만을 포함시킬 수 있는 기능을 함!)
```
