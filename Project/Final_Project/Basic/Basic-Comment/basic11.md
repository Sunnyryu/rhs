## Basic8

#### JS1


```
Naming Convention
- LowerCamelCase
- 일반적인 Camel case
- UpperCamelCase
- snake_case (_ 형태로 나눔 )
- Hungarian notation ( 해당 변수 앞에 타입을 명시하는 방법 )
ex) u16number => unsigned 16 bit 로 저장되는 것이다. 
ex2) s32num => signed 32 bit로 저장되는 것
- kebab-case (dash(-)로 구분하는 것 )

JS의 변수 ! 

let => 변수 타입 (값을 재할당할 수 있는 변수를 선언하는 키워드 ) 선언은 1번만 가능 !!, 재할당은 가능!, block
const : 선언도 1번만 가능, 재할당은 불가능 !, block
var : ES6 이전에 문제가 많이 발생하였음!

조건문 
if / else if 로 구성 

loop 문 (while, for)

- while 문 
- for 문 
 - for of 
 - for in 

화살표 함수 
- 익명 함수
- function 표현에 비해 구문이 단순함
- 생성자로 사용할수가 없음
-사용법( function을 생략 가능 !, 인자가 1개인 경우 괄호도 생략 가능! , return과 {}도 생략이 가능)

 - 배열 (array)

 - Object

 - JSON
   - 문자열이기에 object로 쓰기위해 변환과정이 필요.
   - JSON -> object
      parse
   - object -> JSON
     stringify

   - object : JS 의 Key:value 의 자료구조
   - JSON : 데이터를 표현하기 위한 단순 스트링

 - Array Helper Method
   - 자주 사용하는 로직을 재활용 할 수 있게 만든 일종의 라이브러리
  - forEach, filter, find, map, every, some, reduce

 -forEach
 - array.forEach(callback(element, index, array))

 - map 
  - array.map(callback(element, index))

 -filter 
  - array.filter(callback(element,..))

 - reduce 
  - array.reduce(callback(acc, element, idx,), acc init_value)

 - find 
   - array.find(callback(element, index, array))

 - some & every
   - some 
   - every 
```
