import React, { useState, useEffect, useRef } from "react";
import ReactDOM from "react-dom";

//import App from "./App";
const useHover = (onHover) => {
  const element = useRef();
  useEffect(() => {
    if (element.current) {
      element.current.addEventListener("mouseenter", onHover);
      setTimeout(console.log("sunny hi" + element), 2000);
    }
    return () => {
      if (element.current) {
        element.current.removeEventListener("mouseenter", onHover);
      }
    };
  }, []);
  return element;
};

const App = () => {
  const abc = useHover();
  return (
    <div className="App">
      <h1 ref={abc}>Hi</h1>
    </div>
  );
};
const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
