import React from 'react';
// import Potato from "./Potato";
//
function Food(props) {
 console.log(props.fav);
 return <h2>I love {props.fav}. </h2>;
 }
// props로 fav 등 다양한 것을 가져올 수 있음!
// component는 대문자 ! / props는 component에 넣는 것들!
// function Food({fav}) {
  // console.log(fav);
  // return <h2>I love {fav}. </h2>;
// }

function App() {
  return <div><h2>Hello </h2>
  <Food fav = "kimchi"/>
  <Food fav = "chicken"/>
  <Food fav = "love"/>
  <Food fav = "ramen"/>
  </div>;
}

export default App;
