## start sclar 3

#### 스칼라

```
case class : 패턴 매치를 위한 최적화된 클래스
컴패니언 객체와 객체 생성을 위한 apply(), 패턴 매치를 위한 unapply()가 자동으로 생성
(hashCode(), copy(), equlas(), toString() 등도 자동 생성)

패턴 매치
(매치할 변수) match {
  case (...) => ...
  case (...) => ...
}

기본형이 아닌 큐플을 사용하는 경우 튜플 형식으로 변수를 정의해야한다. <key, value> 형태
리스트의 경우도 각 위치에 해당하는 값이 변수에 할당
케이스 클래스의 경우 클래스 형태로 그대로 사용하여 속성 정보를 매칭할 수 있음!
```

```scala
ex)
scala> def matchFunction(input: Any): Any = input match {
     | case 100 => "hundread"
     | case "hundread" => 100
     | case etcNumber: Int => "입력값은 100이 아닌 Int형 정수입니다."
     | case _ => "기타"
     | }
matchFunction: (input: Any)Any
scala> println(matchFunction(100))
hundread
scala> println(matchFunction("hundread"))
100
scala> println(matchFunction(1000))
입력값은 100이 아닌 Int형 정수입니다.
scala> println(matchFunction(1000.5))
기타
scala> println(matchFunction("thousand"))
기타
```

```scala
scala> case class Person(name: String, age: Int)
defined class Person

scala> val alice = new Person("Alice", 25)
alice: Person = Person(Alice,25)

scala> val bob = new Person("Bob", 32)
bob: Person = Person(Bob,32)

scala> val charlie = new Person("Charlie", 32)
charlie: Person = Person(Charlie,32)

scala> for (person <- List(alice, bob, charlie)) {
     | person match{
     | case Person("Alice", 25) => println("Hi Alice!")
     | case Person("Bob", 32) => println("Hi Bob!")
     | case Person(name, age) => println( "Age: " + age + " year, name: " + name + "?")
     | }
     | }
Hi Alice!
Hi Bob!
Age: 32 year, name: Charlie?
```

```
Extractor로 패턴 매칭
  Extractor는 패턴 매칭을 해야 하는 대상 값을 가져와서 필요한 값을 추출한 후 가공해서 내보낼 수 있음
  추출자의 역할을 하는 unapply()를 구현해야 함. - 하나로 뭉쳐진 데이터에서 필요한 값들을 따로 추출할 수 있는 기능
```

```
컬렉션
배열  -  초기 값을 지정해서 배열을 선언하는 경우 자료형을 표시하지 않더라도 알아서 자료형을 할당 !!
리스트 - 앞뒤가 연결된 리스트로서 내부적으로 리스트를 붙이거나 나누는데 효율적인 구조를 가지고 있음
        list는 추상클래스 형태 혹은 이미 완성된 객체 형태로 존재하기 때문에 new 사용 x
        ::는 리스트의 각 요소 결합 / :::는 여러 리스트를 병합
맵    - 키를 통해 요소에 접근, 인덱스가 필요치 않음
```

```scala
ex)
scala> val list1 = "a" :: "b" :: "c" :: Nil
list1: List[String] = List(a, b, c)

scala> for(x <- 0 until list1.size)
     | println(list1(x))
a
b
c

scala> val list2 = "d" :: "e" :: Nil
list2: List[String] = List(d, e)

scala> val list0 = list1 ::: list2
list0: List[String] = List(a, b, c, d, e)

scala> for(x <- 0 until list0.size)
     | println(list0(x))
a
b
c
d
e

scala> val list3 = "a" :: "b" :: "c" :: Nil
list3: List[String] = List(a, b, c)
scala> val list4 = 1 :: 2 :: 3 :: Nil
list4: List[Int] = List(1, 2, 3)
scala> val list5 = 2 :: 2 :: 4 :: Nil
list5: List[Int] = List(2, 2, 4)
scala> println(list3 ++ list4)
List(a, b, c, 1, 2, 3)
scala> println(list3.apply(0))
a
scala> println(list3.reverse)
List(c, b, a)
scala> println(list4.max)
3
scala> println(list4.min)
1
scala> println(list4.sum)
6
scala> println(list4.mkString(","))
1,2,3
scala> println(list4.exists(a => 0 > 3))
false
scala> println(list4.exists(_ > 3))
false
scala> println(list4.contains(1))
true
scala> println(list4.isEmpty)
false
scala> println(list4.distinct)
List(1, 2, 3)

```

```scala
scala> val map = Map( "number1" -> "aa",
     | "number2" -> "bb",
     | 5 -> "cc")
map: scala.collection.immutable.Map[Any,String] = Map(number1 -> aa, number2 -> bb, 5 -> cc)
scala> println(map.isEmpty)
false
scala> println("whole map : " + map)
whole map : Map(number1 -> aa, number2 -> bb, 5 -> cc)
scala> println("keys : " + map.keys)
keys : Set(number1, number2, 5)
scala> println("values : " + map.values)
values : MapLike(aa, bb, cc)
scala> println(map("number1")
     | )
aa

scala> println(map)
Map(number1 -> aa, number2 -> bb, 5 -> cc)
scala> val map2 = Map("n1" -> 100, "n2" -> 200)
map2: scala.collection.immutable.Map[String,Int] = Map(n1 -> 100, n2 -> 200)
scala> map ++ map2
res42: scala.collection.immutable.Map[Any,Any] = Map(number1 -> aa, n2 -> 200, 5 -> cc, number2 -> bb, n1 -> 100)
scala> println(map)
Map(number1 -> aa, number2 -> bb, 5 -> cc)
scala> map + ("num4" -> 44)
res44: scala.collection.immutable.Map[Any,Any] = Map(number1 -> aa, number2 -> bb, 5 -> cc, num4 -> 44)
scala> map - ("num4")
res46: scala.collection.immutable.Map[Any,String] = Map(number1 -> aa, number2 -> bb, 5 -> cc)
scala> println(map)
Map(number1 -> aa, number2 -> bb, 5 -> cc)

- Set은 중복된 것은 1번만 나오게 함
scala> var basket: Set[String] = Set()
basket: Set[String] = Set()

scala> basket += "딸기"
scala> basket += "포도"
scala> basket += "포도"
scala> basket += "사과"
scala> basket += "포도"
scala> basket += "바나나"
scala> println(basket)
Set(딸기, 포도, 사과, 바나나)

scala> var basket2 : Set[String] = Set()
basket2: Set[String] = Set()
scala> basket2 += "토마토"
scala> basket2 += "당근"
scala> basket2 += "감자"
scala> basket2 += "사과"
scala> println(basket.diff(basket2))
Set(딸기, 포도, 바나나)
scala> println(basket|basket2)
Set(바나나, 감자, 사과, 딸기, 당근, 포도, 토마토)
```

```scala
scala> var t1 = (1, 2)
t1: (Int, Int) = (1,2)
scala> val t2 = ("a", 1, "c")
t2: (String, Int, String) = (a,1,c)
scala> val n1 = t1._2
n1: Int = 2
scala> val n1 = t2._3
n1: String = c
```

```
이터레이터
  컬렉션에서 데이터를 꺼내와서 차례대로 무언가를 실행할 때 사용하는 컬렉션
```

```
패키지 객체 - 스칼라에는 패키지에 변수나 클래스 등을 선언 가능
            패키지 객체를 이용하면 common과 같은 클래스를 정의 않고도 동일 패키지에서 사용하는 변수나 메서드 듣을 공유 가능
            package 키워드 사용 / type은 새로운 타입 선언 키워드
            import문을 사용해서 다른 클래스 메서드나 변수 사용
```

```
스칼라는 함수형 언어이므로 함수를 일반 변수와 같이 다룰 수 있음

제네릭은 클래스의 타입 파라미터를 지정하는 구문([] 기호를 사용)

함수 콤비네이터(combinator)
  구현된 로직에 따라 컬렉션을 변형한 후 동일한 자료형의 컬렉션을 반환하는 역할을 맡는 메서드
  map(), foreach() 등을 사용
```

```scala
scala> val o = List(1,2,3,4)
o: List[Int] = List(1, 2, 3, 4)
scala> println(o)
List(1, 2, 3, 4)
scala> val n = o.filter(i => i >= 3).map(i => i * 2)
n: List[Int] = List(6, 8)

scala> val n = o.map(i => i * 10 )
n: List[Int] = List(10, 20, 30, 40)
scala> println(n)
List(10, 20, 30, 40)

scala> val sum = o.foldLeft(0.0)(_ + _)
sum: Double = 10.0
scala> print(s"Sum = $sum")
Sum = 10.0
scala> val n = o.partition(i => i < 3)
n: (List[Int], List[Int]) = (List(1, 2),List(3, 4))
scala> val oo = List(5,6,7,8,9)
oo: List[Int] = List(5, 6, 7, 8, 9)
scala> val n = o zip oo
n: List[(Int, Int)] = List((1,5), (2,6), (3,7), (4,8))
scala> val nn = o ::: oo
nn: List[Int] = List(1, 2, 3, 4, 5, 6, 7, 8, 9)
scala> println(n)
List((1,5), (2,6), (3,7), (4,8))
scala> println(nn)
List(1, 2, 3, 4, 5, 6, 7, 8, 9)
scala> val n = o.find( i => i >= 2)
n: Option[Int] = Some(2)
scala> val nn = o.find(i => i ==9)
nn: Option[Int] = None
scala> val w = List(1,2,3,4,5,6,0)
w: List[Int] = List(1, 2, 3, 4, 5, 6, 0)
scala> val n = w.drop(4)
n: List[Int] = List(5, 6, 0)
scala> val nn = w.dropWhile( i => i < 3)
nn: List[Int] = List(3, 4, 5, 6, 0)
scala> val q = List(List(1,2,3,4), List(5, 6))
q: List[List[Int]] = List(List(1, 2, 3, 4), List(5, 6))
scala> q.flatten
res82: List[Int] = List(1, 2, 3, 4, 5, 6)
```

```scala
import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException

object Demo {
	def main(args: Array[String]) {
	  try {
		var f = new FileReader("input.txt")
	  } catch {
		case ex: FileNotFoundException => {
		    println("MIssing file exception")
		}
		case ex: IOException => {
		    println("IOException")
		}
	  } finally {
		println("Exiting finally...")
	  }
	}
}
```scala
object Demo {
	def main(args: Array[String]) {
		print("Please enter your input : ")
		val line = Console.readLine

		println("Thanks, you just typed: " + line)
	}
}
```

```scala
import scala.io.Source

object Demo {
	def main(args: Array[String]) {
		print("Following is the content read : ")

		Source.fromFile("Demo.txt" ).foreach {
			print
		}

	}
}
```
