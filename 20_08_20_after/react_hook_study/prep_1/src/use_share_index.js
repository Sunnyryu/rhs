import React, {Component, useState} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import App from './App';

const App = () => {
  const [ count, setCount] = useState(0);
  // count는 변수 / setCount는 행ㅎ하는 함수! , ,useState(0) => 시작점이 0!
  const [ email, setEmail] = useState("");
  const updateEmail = (e) => {
    console.log(e.target.value)
    const {
      target: {value}
    } = e;
    //console.log(e, "123")
    setEmail(value);
    //console.log(e.target.value)
  };
  return (
    <div>
    {count}
    <button onClick={() => setCount(count + 1 )}>Increment</button>
    <button onClick={() => setCount(count - 1 )}>Decrement</button>
    <input placeholder="Email" value={email} onChange={updateEmail}/>
    </div>
  )
}

ReactDOM.render(
    <App />,
  document.getElementById('root')
);

