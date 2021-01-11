import React, {Component, useState} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import App from './App';


const useInput = (initialValue, validator) => {
  const [value, setValue] = useState(initialValue);
  console.log(validator)
  console.log(initialValue)
  const onChange = (event) => {
    const {
      target: { value }
    } = event;
    let willUpdate = true;
    if (typeof validator === "function") {
      willUpdate = validator(value);
    }
    if (willUpdate) {
      setValue(value);
    }
  };
  return { value, onChange };
};

const App = () => {
  const maxlen = (value) => value.length <= 10;
  const name = useInput("Mr. ", maxlen);
  return (
    <div className="App">
      <h1>hello</h1>
      <input placeholder="Name" {...name} />
      {/* <input placeholder="Name" value={name.value} onChange={name.onChange}/> */}
    </div>
  );
};


ReactDOM.render(
    <App />,
  document.getElementById('root')
);

