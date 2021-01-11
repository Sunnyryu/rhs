import React, { useState, useEffect, useRef } from "react";
import ReactDOM from "react-dom";

const useClick = (onClick) => {
  const element = useRef();
  
  useEffect(() => {
    if (element.current) {
      console.log(element.current);
      element.current.addEventListener("click", onClick);
    }
    return () => {
      if (element.current) {
        element.current.removeEventListener("click", onClick);
      }
    };
  }, []);
  setTimeout(console.log("sunny hi" + element), 2000);
  console.log(element)
  return element;
};
const App = () => {
  const title = useClick();
  return (
    <div className="App">
      <h1 ref={title}>Hi</h1>
    </div>
  );
};
const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
