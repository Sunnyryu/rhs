## Hello Spark

#### 스파크 !

```
스파크는 빅데이터 처리를 위한 오픈소스 병렬분산 처리 플랫폼!
(대량의 데이터를 고속 병렬분산처리!!)

복수의 컴포넌트로 구성!

스파크코어 !! / 여러가지 라이브러리 제공 / SQL 처리용 라이브러리(Spark SQL), 스트림처리용 라이브러리(스파크 스트리밍), 머신러닝용 라이브러리(MLlib), 그래프 처리용 라이브러리(그래프 X)가 있음 !

HDFS / Hive / HBase / PostgreSQL / MySQL / CSV (다양한 데이터소스 제공!)
```

```
스파크의 특징
  반복처리와 연속으로 이루어지는 변환처리의 고속화
      맵 리듀스와 다르게 스파크는 연속으로 이루어지는 처리에서 매번 불필요한 디스크와 네트워크 I/O가 발생하지 않도록 처리
  시행착오에 적합한 환경 제공
      RDD(Resilent Distributed Dataset)라는 데이터셋을 사용 - RDD가 제공하는 API로 변환을 기술하기만 하면 처리됨.
  서로 다른 처리를 통합에 이용할 수 있는 환경
      서로 다른 처리방식을 통합하여 다룰 수 있음 (배치, 스트림, SQL, 머신러닝, 그래프처리 등
```

```
스파크 처리 모델
  RDD(대량의 데이터를 요소로 가지는 분산 컬렉션)

  변환(transformation) / 액션(action)

  변환이란 RDD를 가공하고 그 결과 새로운 RDD를 얻는 처리 / 변환처리 후의 RDD가 가지는 요소는 변환처리 전의 RDD에 들어있던 요소를 가공하거나 필터링해 생성
    filter (요소를 필터링)
    map (각 요소에 동일한 처리를 적용)
    flatmap (각 요소에 동일한 처리를 적용, 여러 개의 요소를 생성)
    zip(파티션 수가 같고, 파티션에 있는 요소의 수도 같은 두 개의 RDD를 조합해 한쪽의 요소 값을 가로, 다른 한족의 요소 값을 value로 가지는 쌍(key-value pair)을 만듬
    reduceByKey (같은 키를 가지는 요소를 집약처리(같은 키를 가지는 요소들이 가지는 값을 합하는 처리!) )
    join(두 개의 RDD에서 같은 키를 가지는 요소끼리 조인!)

  액션이란 RDD 내용을 바탕으로 데이터를 가공하지 않고 원하는 결과를 얻는 조작
      saveAsTextFile (RDD 내용을 파일로 출력!)
      count(RDD의 요소 수를 샘!)
```

```
스파크 분산처리 환경

cluster 환경
  YARN (하둡의 클러스터 관리 시스템)
  Mesos (YARN과 마찬가지로 범용 클러스터 관리 시스템, 처리 할당하는 CPU 코어 수의 분배를 동적으로 바꿀 수 있는 등의 세세한 제어 가능)
  Spark Standalone (스파크에 번들되는 전용 클러스터 관리 시스템 / 별도의 클러스터 관리 시스템 없이 편리하게 이용 가능)

  스파크로 분산처리 할 때에는 RDD 생성과 일련의 변환으로 구성된 스파크 application을 클라이언트가 클러스터에 배포!
  클러스터 내 계산 리소스 확보 (마스터 노드가 각 워커 노드의 이용 가능한 리소스양과 클라이언트가 요청하는 이그제큐터 스펙을 고려 / 하나 이상의 워커 노드에 이그제큐터의 구동 요구)
  드라이버 프로그램 구동
  테스크 스케쥴링과 실행

드라이버 프로그램
  스파크 어플리케이션의 동작을 제어!
  드라이버 프로그램에 RDD의 생성과 변환, 액션의 로직 등을 기술!
  스파크에서는 다음과 같이 컬렉션을 다루듯 RDD 생성하거나 변환을 기술할 수 있음
테스크 스케쥴링
  RDD의 생성과 로드는 지연 평가됨 / 드라이버 프로그램에서 생성된 RDD에는 테스크 작성과 스케쥴링에 필요한 정보가 포함

RDD 영속화
  셔플이 발생하는 변환을 실행하기 직전의 RDD나 사용자에 의해서 명시적으로 영속화가 선언된 RDD 중 하나만 만족하면 영속화!!
```

```
spark context  - RDD 생성 - 스파크 클러스터 구성 - 분산 데이터로서 RDD로 함 - 파티션으로 분할함
```

```
SparkApplication => job
Spark 클러스터 환경에서 node들 : SparkClient, Masternode, Worknode

SparkClient : SparkApplication 배포, 실행 요청
Masternode : Spark 클러스터 환겨엥서 사용가능한 리소스들의 관리
Worknode : 할당받은 리소스(CPU core, memory)를 사용해서 SparkApplication 실행
Spark Workernode에서 실행되는 프로세스 - Executor는 RDD의 partition을 task단위로 실행

SparkApplication 구현 단계 :
  SparkContext 생성
   Spark애플리케이션과 Spark 클러스터와의 연결을 담당하는 객체
   모든 스파크 애플리케이션은 SparkContext를 이용해 RDD나 accumulator 또는 broadcast 변수 등을 다룸
   Spark 애플리케이션을 수행하는 데 필요한 각종 설정 정보를 담는 역할
  RDD (불변데이터 모델, parition가능) 생성
   collection, HDFS, hive , CSV 등..
  RDD 처리
    변환연산(RDD의 요소의 구조 변경, filter처리, grouping...)    
  집계, 요약 처리 - Action연산
  영속화
```

```
sc.textFile() : file로 부터 RDD생성
collect : 배열
map, flatMap()
mkString("구분자")
```
