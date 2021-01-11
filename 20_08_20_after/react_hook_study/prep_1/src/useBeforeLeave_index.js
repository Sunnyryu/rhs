import React, { useEffect, useState, useRef } from "react";
import ReactDOM from "react-dom";

const useBeforeLeave = (onBefore) => {
  // if (typeof onBefore !== "function") {
    // console.log("1");
    // return;
  // }
  const handle = (event) => {
    const { clientY } = event;
    if (clientY <= 0) {
      onBefore();
    }
  };
  useEffect(() => {
    document.addEventListener("mouseleave", handle);
    return () => document.removeEventListener("mouseleave");
  }, []);
};
const App = () => {
  const begForLife = () => console.log("Pls don`t leave");
  useBeforeLeave(begForLife);
  return <div className="App">hi</div>;
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
