import React, { useState, useRef, useEffect } from "react";
import ReactDOM from "react-dom";

const useFadeIn = (duration = 1, delay = 0) => {
  // if (typeof duration !== "number" || typeof delay !== "number") {
    // console.log("1");
    // return;
  // }
  const element = useRef();
  useEffect(() => {
    if (element.current) {
      const { current } = element;
      current.style.transition = `opacity ${duration}s ease-in-out ${delay}s`;
      current.style.opacity = 1;
    }
  });
  return { ref: element, style: { opacity: 0 } };
};

const App = () => {
  const fadeInh1 = useFadeIn(1, 2);
  const fadeInp1 = useFadeIn(5, 10);
  return (
    <div className="App">
      <h1 {...fadeInh1}>hello</h1>
      <p ref={fadeInp1.ref} style={fadeInp1.style}>lorem ipsum la</p>
    </div>
  );
};
const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
