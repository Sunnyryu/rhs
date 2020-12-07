# React

```
Function component는 function이고 뭔가를 리턴함 그리고 스크린에 표시

class component는 class임, react component로부터 확장되고 screen에 표시..
render method 안에 넣어야만함

react는 자동적으로 모든 class component의 render method를 실행함! (자동))

class component의 state

state는 object이며, component의 data를 넣을 공간이 있고 데이터는 변함

바꿀 데이터를 state에 넣고 state를 render에 넣자!


this.add() => 즉시 / this.add 작동 시에

state에 넣고 render를 통해 다시 호츨할 필요가 있음!

this.state.count를 이용해서 할 수 있지만 그건 좋은 밥법이 아니기에 current를 활용해보쟈

component가 render 된 후에 호출되는 다른 function이 존재

# 동적인 리스트를 만들 때마다 적절한 키를 할당할 것을 강력하게 추천합니다.
Mounting => component가 태어남 (constructor=> class 만들 때 호출(JS))
getDerivedStateFromProps() => screen에 표시될 떄 constructor를 호출!
render()
componentDidMOunt() => 컴포너트가 처음 렌딩 되었어!
updating => 업데이트 (state 변경시 업데이트!)
getDerivedStateFromProps()
shouldComponentUpdate()
render()
getSnapshotBeforeUpdate()
componentDidMountUpdate() = 렌더가 호출 후에 업데이트가 되면 알려줌!
Unmounting => Component가 죽음( 페이지가 바뀔 떄?)
componentWillUnmount => 컴포넌트가 언마운트 되면 알려줌!

많이 연습하기! / api 요청해서 동영상 얻기.. 새로운 시도 해보기! /
state를 갖기위해 class component를 가질 필요가 없음!
(react hook이 있음!)
react.js 문서에 보면 class comonent를 가르치고 있음!


```
