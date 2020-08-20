## start sclar 1

#### 스칼라

```
스칼라란 ?
스칼라는 2004년 마틴 오더스키(Martin Odersky)가 발표한 객체 지향 언어의 특징과 함수형 언어의 특징을 함께 가지는 다중 패러다임 프로그래밍 언어!?

스칼라는 자바가상머신(JVM)에서 동작하는 JVML언어 입니다. JVML(Java Virtual Machine Language) 언어는 자바가상머신 위에서 동작하는 언어들로 scala, kotlin, Groovy 등 있음

자바 가상 머신 위에서 동작하기 때문에 자바의 모든 라이브러리를 사용할 수 있음. 스칼라는 스칼라 컴파일러를 통해 스칼라 코드를 바이트 코드로 변환하고, 바이트 코드는 JVM 상에서 자바와 동일하게 실행됨!

함수형 언어
스칼라는 함수형 언어의 특징을 가지기 때문에 자바에 비하여 코드길이가 짧습니다. 겟터, 셋터, 생성자를 제거하고, 표현식을 간소화 하여 자바대비 짧은 코드로 동일한 내용을 작성할 수 있음.

바이트 코드 최적화

바이트 코드를 최적화 하여하여 자바 보다 20% 정도 속도가 빠릅니다. 같은 일을 하는 프로그램을 작성하여도 자바에 비해 코드도 짧고, 속도도 빠름.

동시성이 강함

스칼라는 변경 불가능한 Immutable 변수를 많이 가지고 있습니다. 이를 통해 속성을 변경 불가능하게 하고, 순수 함수를 사용하여 병렬 프로그래밍 처리에 강함
```

```
스칼라는 객체지향 프로그래밍과 함수형 프로그래밍을 모두 완벽하게 지원하는 언어!
  스칼라는 모든 것이 객체, 함수가 first object
  함수를 마치 하나의 값으로 취급 / 변수 또는 파라미터로 넘길 수 있음
  모든 것을 함수로 해결하면 의도하지 않은 도작이 발생할 일이 없음
```

```
코드의 직관성과 신축성
풍부한 표현식과 연산자
  first-class function
  closure
간결함( 타입 추론, 함수 리터럴(Literal)
자바와 혼용 가능 (자바 라이브러리나 자바 도구 재사용 가능 / 성능 손실 없이 가능)

동시성에 강한 언어 / 결과를 반환하는 문장 중심 언어 / implicit 예약어를 사용하면 명시적인 표현을 감출 수 있음 !
```

```
순수 / 익명 / 고차

ex) public int add(int a, int b) {return a + b; } - 순수
ex2) Arrays.asList(1,2,3).stream().reduce((a,b) - > a-b).get(); - 익명
ex3) COllections.sort(new ArrayList<Intger>(), (x, y) -> x >= y ? -1 : 1);
```

```
scala
:history [num], :edit<id>|<line>, :help [command], imports [name name ...]
```

```
스칼라는 기본자료형, 함수, 클래스등 모든 것을 객체로 취급함. 객체는 Any를 최상위 클래스로 값(AnyVal) 타입과 참조(AnyRef) 타입을 상속 하여 구현합니다. Int, Byte, String 같은 기본 자료형은 AnyVal을 상속하고, 클래스는 AnyRef를 상속함

var = 가변 변수 / val = 불변 변수 (가변 변수는 바꿀 수 있지만 불변 변수는 선언하면 .... 재할당 불가능 !!)
```

```scala
데이터 선언
// 암시적인 선언
var x = 110
var y = "abc"

// 명시적인 선언
var b: Byte = 20
var s: Short = 30
var i: Int = 40
var l: Long = 50

// 값에 약어를 추가하여 명시적 선언
var f = 70.0f
var d = 80.0d

// 암시적인 선언, 컴파일러가 자동으로 타입을 선택
scala> var ii = 50
ii: Int = 50

scala> var ff = 12.0
ff: Double = 12.0
```

```
var t = true

if(t)
  println("참")
else
  println("거짓")

  scala> var m1:Char = 'a'
  m1: Char = a

  scala> var m2 = 'b'
  m2: Char = b
```

```
접두어 s 와 접두어 f
s : ${변수명}을 이용하여 문자열안의 변수를 값으로 치환. 계산식, 함수도 사용가능
val name = "sunny"

// ${name}이 sunny로 변환
scala> println(s"Hello! ${name}")
Hello! sunny

// 계산 값 치환 안됨
scala> println("${ 5 + 9 }")
${ 5 + 9 }

// s 접두어가 있으면 계산식 처리
scala> println(s"${ 5 + 9}")
14

f는 문자열 포맷팅을 처리합니다. 자바의 printf() 와 같은 방식으로 처리, 타입이 맞지 않으면 오류발생
val height:Double = 172.8
val name = "sunny2"

// f접두어를 이용한 값 변환 테스트
scala> println(f"$name%s is $height%2.2f meters tall")
James is 172.80 meters tall

raw : 특수 문자를 처리하지 않고 원본 문자로 인식 (특수문자를 그대로 입력해야 할 때 사용)
// \n으로 개행 처리
scala> s"가\n나"
res1: String =
가
나

// \n을 문자 그대로 인식
scala> raw"가\n나"
res3: String = 가\n나

문자열 처리 (ubuntu terminal에서 실행)
scala> var str3 = s"println $str1"
str3: String = println aaa

scala> println(str3)
println aaa

scala> println(s"2 * 3 = ${2*3}")
2 * 3 = 6

scala> def minus(x: Int, y: Int ) = x - y
minus: (x: Int, y: Int)Int

scala> println(s"${Math.pow(2, 3)}")
8.0

scala> println(s"${minus(2, 3)}")
-1
```

```scala
scala> for (x <- 1 to 10) {
     | println(x)
     | }
1
2
3
4
5
6
7
8
9
10

scala> for (x <- 1 until 10) {
     | println(x)
     | }
1
2
3
4
5
6
7
8
9

scala> for (i <- 1 to 10 ) if (i % 2 == 0 ) {
     | println(i)
     | }
2
4
6
8
10
scala> val lst = (10 to 100 by 10).toList
lst: List[Int] = List(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

scala> for ( (num, index) <- lst.zipWithIndex) {
     | println(s"$index : $num") }
0 : 10
1 : 20
2 : 30
3 : 40
4 : 50
5 : 60
6 : 70
7 : 80
8 : 90
9 : 100

```
