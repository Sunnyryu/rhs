const greeting = function(name){
  return "hello ${name}"
}

// 1. function 키워드 생략 
const greeting = (name) => {
  return 'hello ${name}'
}

// 2. 인자가 1개인 경우 괄호 생략 가능 
const greeting = name => {
  return 'hello ${name}'
}

// 3. body의 표현식이 1줄일 때 
const greeting = name => 'hello ${name}'

//  실습 

let square = function(num){
  return num ** 2 
}

let square = num => num** 2

// 인자가 없다면

let noArgs = function(){
  return 'no Args'
}
let noArgs = () => 'no Args'
let noArgs = _ => 'no Args'

// object 형식으로 반환이 된다면 ? 
let returnObj = () => { 
  return {key: 'value'}
}

let returnObj = () => ({key: 'value'})

let seyHi = function(name="pengsu"){
  return 'hi ${name}'
}

let sayHi = (name="pengsu") => 'hi ${name}'

// 즉시 실행함수 !

const cube = function(num){
  return num ** 3
}

console.log(function (num) {return num ** 3 } (4) )
