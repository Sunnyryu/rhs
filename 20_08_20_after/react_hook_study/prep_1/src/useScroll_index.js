import React, { useState, useRef, useEffect } from "react";
import ReactDOM from "react-dom";

const useScroll = () => {
  const [state, setState] = useState({
    x: 0,
    y: 0
  });
  const onScroll = () => {
    console.log(window.scrollY);
    setState({ y: window.scrollY, x: window.scrollX });
  };
  useEffect(() => {
    window.addEventListener("scroll", onScroll);
    return () => {
      window.removeEventListener("scroll", onScroll);
    };
  }, []);
  return state;
};
const App = () => {
  const { y } = useScroll();
  console.log({y})
  return (
    <div className="App" style={{ height: "1000vh" }}>
      <h1 style={{ postion: "fixed", color: y > 100 ? "red" : "blue" }}>hi</h1>
    </div>
  );
};
const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
