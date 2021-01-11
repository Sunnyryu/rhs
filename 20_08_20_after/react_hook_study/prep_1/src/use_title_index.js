import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";

const useTitle = (initialTitle) => {
  const [title, setTitle] = useState(initialTitle);
  console.log(title)
  const updateTitle = () => {
    const htmlTitle = document.querySelector("title");
    htmlTitle.innerText = title;
  };
  console.log(title)
  useEffect(updateTitle, [title]);
  return setTitle;
};
// const App = () => {
// const sayHello = () => console.log("hello");
// const [number, setNumber] = useState(0);
// const [anumber, setAnumber] = useState(0);
// useEffect(sayHello, [number]);
// return (
// <div className="app">
{
  /* <div>hi</div> */
}
{
  /* <button onClick={() => setNumber(number + 1)}>{number}</button> */
}
{
  /* <button onClick={() => setAnumber(anumber + 1)}>{anumber}</button> */
}
{
  /* </div> */
}
// );
// };
const App = () => {
  const titleUpdater = useTitle("Loading...");
  setTimeout(() => titleUpdater("Loading..."), 5000);
  return (
    <div className="App">
      <div>Hi</div>
    </div>
  );
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
