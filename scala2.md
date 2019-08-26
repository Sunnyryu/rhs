## start sclar 2

#### 스칼라

```
함수는 def로 선언 함수를 선언할 때 리턴문과 리턴 타입은 생략이 가능하고, 매개변수의 파라미터 타입은 생략할 수 없음
리턴값이 없는 함수를 선언할 때는 Unit을 이용 /
함수의 매개변수는 불변 변수이기 때문에 재할당 할 수 없음

리턴 타입을 생략하면 컴파일러가 반환값을 이용하여 자동으로 추론
리턴문이 생략되고, 리턴 타입이 Unit이 아니면 함수의 마지막 값을 리턴

이름 없는 함수 만들 수 있음(익명함수), 이름 없는 함수를 다른 함수나 식에 넘기거나 val에 저장 가능
함수가 여러 식으로 이루어진 경우 {}를 사용해 이를 위한 공간 만들기 가능!
```

```
ex)
scala> def name () : Int = {
     | val a = 10
     | return a
     | }
name: ()Int

scala> name()
res7: Int = 10

scala> def name2() : Int = {
     | val a = 10
     | return a
     | }
name2: ()Int

scala> name2()
res8: Int = 10

scala> def name3() = { //error?
     | val a = 10
     | return a
     | }
<console>:13: error: method name3 has return statement; needs result type
       return a
       ^
```

```
ex2)
scala> (x: Int) => x + 1
res14: Int => Int = <function1>

scala> (x: Int) => x + 1
res15: Int => Int = <function1>

scala> val addOne = (x: Int) => x + 1
addOne: Int => Int = <function1>

scala> addOne(1)
res16: Int = 2

scala> def timesTwo(i: Int): Int = {
     | println("hello world")
     | i * 2
     | }
timesTwo: (i: Int)Int

scala> {i : Int => println("hello world")
     | i*2
     | }
res17: Int => Int = <function1>
```

```
인자의 일부만 사용해 호출하기(부분 적용, Partial application)
함수 호출시 _(밑줄)을 사용해 일부만 적용 가능 / 새로운 함수 얻음 / 스칼라에서 밑줄은 문맥에 따라 의미 다름
인자 중에서 원하는 어떤것이든 부분 적용 가능
```

```
ex
scala> def adder(m: Int, n: Int) = m * n
adder: (m: Int, n: Int)Int

scala> val add2 = adder(2, _:Int)
add2: Int => Int = <function1>

scala> add2(3)
res18: Int = 6
```

```
커리 함수 : 함수의 인자 중 일부를 적용하고 나머지는 나중에 적용하게 남겨두는 경우 있음
```

```
ex)
scala> def main(args: Array[String]): Unit = {
     | val g = f _
     | println(f(1))
     | }
main: (args: Array[String])Unit
```

```
재귀함수
```

```
scala> def default(a: Int = 4, b: Int = 5) : Int = a+b
default: (a: Int, b: Int)Int

scala> println("기본값은" + default())
기본값은9

scala> println("기본값은" + default(11,22))
기본값은33
```

```
apply는 매번 매서드 이름을 적는 것을 피하기 위해 사용
  변수를 받아 함수에 적용시켜 결과를 만들어내는 설정자와 같은 역할을 함
  new A(...) 또는 a.method() 형태 호출 대신 A(...) 또는 a(...)와 같은 간결한 형태로 코드 작성
ex)
  scala> class SomeClass {
       | def apply(m: Int) = method(m)
       | def method(i: Int) = {
       | println("method(Int) called")
       | i+i
       | }
       | def method2(s: String) = 5
       | }
  defined class SomeClass

  scala> val something = new SomeClass
  something: SomeClass = SomeClass@3fe11091

  scala> println(something(2))
  method(Int) called
  4

```

```
암묵적 형변환
implicit는 에러는 바로 나지 ㅇ않고 해당하는 함수가 있으면 그것을 사용해서 암묵적으로 형 변환을 도와줘 함수의 활용도를 높임
```
scala> def sayHello(p:Person): Unit = {
     | print("Hello,"+p.name)
     | }
sayHello: (p: Person)Unit

scala> sayHello("Korea")
<console>:13: error: type mismatch;
 found   : String("Korea")
 required: Person
       sayHello("Korea")
                ^
- implicit가 없으면 에러가 나니 참고 !
```

```
스칼라에서는 연산자와 메서드를 포함한 모든 것이 객체입니다.
객체 생성법
  클래스를 통한 인스턴스화 - new를 사용하여 계속 인스턴스 생성가능
  object 예약어를 통해 객체 생성 - 싱글턴 객체로서 유일한 객체 생성
클래스
  클래스 안에서 메소드는 def로 필드는 val로 정의한다. 메소드는 단지 클래스(객체)의 상태

스칼라에서는 object 예약어를 통해 처음부터 메모리에 객체를 생성하고 컴파일러는 객체에 main이라는 이름이 있으면 main의 시작점으로 컴파일
축약 방식으로 클래스를 만들면 멤버 변수들이 모두 private 생성
```

```
케이스 클래스는 자동으로 멤버 변수를 만들어주며, 외부에서도 멤버 변수에 접근 가능 하도록 함 (toString, hashCode, equals)
ex)
scala> case class Fruit2(name: String)
defined class Fruit2

scala> val apple = new Fruit2("사과")
apple: Fruit2 = Fruit2(사과)

scala> println(apple.name)
사과

scala> val apple2 = new Fruit2("사과")
apple2: Fruit2 = Fruit2(사과)

scala> println(apple2.name)
사과

scala> println(apple2.equals(apple))
true

scala> println(apple.hashCode)
961505412

scala> println(apple.toString)
Fruit2(사과)
```

```
클래스
  스칼라에서는 생성자가 특별한 메소드를 따로 존재 x , 클래스 몸체에서 메소드 정의 부분 밖에 있는 모든 코드가 생성자 코드가 됌

  class Calculation(brand: String) {
       | val color: String = if(brand == "TI") {
       | "blue"
       | } else if (brand == "HP") {
       | "black"
       | } else {
       | "white"
       | }
       | def add(m: Int, n: Int): Int = m + n
       | }
  defined class Calculation

  val calc = new Calculation("TI")
calc: Calculation = Calculation@4205d1c9

scala> calc.color
res38: String = blue
```

```
상속 : 자식 클래스는 부모 클래스가 가진 모든 기능을 가집니다.
추상 클래스는 메소드 정의는 있지만 구현은 없는 클래스 이다. 대신 이를 상속한 하위클래스에서는 메소드를 구현하게 된다. 추상 클래스의 인스턴스를 만들 수는 없다.
scala> abstract class Shape {
     | def getArea() : Int
     | }
defined class Shape

scala> class Circle(r: Int) extends Shape {
     | def getArea(): Int = { r * r * 3 }
     | }
defined class Circle

scala> val s = new Shape
<console>:12: error: class Shape is abstract; cannot be instantiated
       val s = new Shape
               ^

scala> val c = new Circle(2)
c: Circle = Circle@327ac23
```

```
트레잇(trait)
: 하나의 완성된 기능이라기보다는 어떠한 객체에 추가될 수 있는 부가적인 하나의 특성
  클래스와 부가적인 특성으로 동작, 자체로 인스턴스화는 가능 x
  다른 클래스가 확장(즉 상속)하거나 섞어 넣을 수 있는 (이를 믹스인이라 함) 필드와 동작의 모음
  클래스는 여러 트레잇을 with 키워드를 사용해 확장 가능
  자유롭게 변수 선언 / 로직 구현 가능 / but 자바의 interface 비슷하나 interface와 다른 것은 static 뿐만 아니라 다른 것도 사용 가능, 로직을 구현하는 것이 자유로움

추상 클래스 대신에 트레잇을 사용해야 하는 경우
  확장하는 쪽에서 일부를 구현하는데에 차이가 있음 / 트레잇은 클래스와 다르게 여러개를 상속 받을 수 있음 / 생성자 매개변수가 필요한 경우라면 추상 클래스를 사용함
  (트레잇은 멤버 변수를 구현받을 수 없음)
```

```
scala> trait Car {
     | val brand: String
     | }
defined trait Car

scala> trait Shiny {
     | val shineRefraction: Int
     | }
defined trait Shiny

scala> class BMW extends Car {
     | val brand = "BMW"
     | }
defined class BMW

scala> class BMW extends Car, Shiny{
<console>:1: error: ';' expected but ',' found.
class BMW extends Car, Shiny{
                     ^
scala> class BMW extends Car, Shiny{
<console>:1: error: ';' expected but ',' found.
class BMW extends Car, Shiny{
                     ^

scala> class BMW extends Car with Shiny {
| val brand = "BMW"
| val shineRefraction = 12
| }
defined class BMW
```

```
scala> abstract class Robot {
     | def shoot = "뿡뿡"
     | }
defined class Robot

scala> trait M16 extends Robot {
     | override def shoot = "빵야"
     | }
defined trait M16

scala> trait Bazooka extends Robot {
     | override def shoot = "뿌앙뿌앙"
     | }
defined trait Bazooka

scala> trait Daepodong extends Robot {
     | override def shoot = "쾅쾅"
     | }
defined trait Daepodong

scala> class mazinga extends Robot with M16 with Bazooka with Daepodong
defined class mazinga

scala> val robot = new mazinga
robot: mazinga = mazinga@586737ff

scala> println(robot.shoot)
쾅쾅
```

```
scala> abstract class AnotherRobot {
     |      def shoot = "뿡뿡"
     |      }
defined class AnotherRobot

scala> trait AnotherM16 extends AnotherRobot {
     |      override def shoot = super.shoot + "빵야"
     |      }
defined trait AnotherM16

scala> trait AnotherBazooka extends AnotherRobot {
     |      override def shoot = super.shoot + "뿌앙뿌앙"
     |      }
defined trait AnotherBazooka

scala> trait AnotherDaepodong extends AnotherRobot {
     |      override def shoot = super.shoot + "쾅쾅"
     |      }
defined trait AnotherDaepodong

scala> class mazinga2 extends AnotherRobot with AnotherM16 with AnotherBazooka with AnotherDaepodong
defined class mazinga2

scala> val robot2 = new mazinga2
robot2: mazinga2 = mazinga2@dbc7e0a

scala> println(robot2.shoot)
뿡뿡빵야뿌앙뿌앙쾅쾅
```
