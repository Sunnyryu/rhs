import React, { Component} from 'react';
import ReactDOM from 'react-dom';
import logo from './logo.svg';
import './App.css';
import SmallImage from './small.png';
import BigImage from './big.png';
import TodoList from './TodoList';
import './test.css';

class App extends Component {
  render(){
    return (
      <div className="App">
      <img src={BigImage} alt=""/>
      <img src={SmallImage} alt=""/>
      <TodoList/>
      </div>
    )
  }
}
console.log(`NODE_ENV = ${process.env.NODE_ENV}`);
export default App;
