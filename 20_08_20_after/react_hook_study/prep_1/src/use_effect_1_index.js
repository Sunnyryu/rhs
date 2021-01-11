import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";


const App = () => {
  const sayHello = () => console.log(number);
  const [number, setNumber] = useState(0);
  const [anumber, setAnumber] = useState(0);
  useEffect(sayHello, [number]);
  // 앞은 하려고 하는 함수, 뒤에는 조건!
  return (
  <div className="app">
  <div>hi</div> 
  <button onClick={() => setNumber(number+1)}>{number}</button> 
  <button onClick={() => setAnumber(anumber + 1)}>{anumber}</button> 
  </div> 
  );
};


const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
