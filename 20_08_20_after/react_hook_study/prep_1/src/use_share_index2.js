import React, {Component, useState} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import App from './App';

const App = () => {
  const [item, setItem] = useState(1);
  const incrementItem = () => setItem(item + 1);
  const decrementItem = () => setItem(item - 1);
  return (
  <div className="App">
    <h1>hello {item}</h1> 
    <h2>start editing to see some magic happe!</h2>
    <button onClick={incrementItem}>increment</button>
    <button onClick={decrementItem}>Decrement</button>
    </div> 
  )
}


ReactDOM.render(
    <App />,
  document.getElementById('root')
);

