## GCP Review

#### 3

```
BigQuery 
데이터 웨어하우스 !.
몇 초만에 대규모 데이터를 쿼리할 수 있는 관계형 클라우드 데이터베이스 !! , sql을 사용함 , 쿼리 실행.. 

mysql을 사용하여 탐색할 때의 문제점을 해결할 수 있음 
빅쿼리는 sql db와 매우 유사한 만큼 데이터 집합을 가지고 있음 !(데이터 셋 !), sql과 다르게 db안에 테이블이 아닌 데이터집합이라는 구조안에 테이블이 들어감! 
구조화된 스키마가 있음 ! , 스키마와 관련된 요청에 sql을 사용하지 않고 api로 보내고 스키마는 출력 결과가 되용! 

빅쿼리는 순간적으로 수천 대의 컴퓨터를 만들고 사용할 수 있도록 하여.. 테라바이트 단위의 데이터를 빠르게 분석할 수 있음 , OLTP 기능은 지원하지만 트랜젝션이 없음,
데이터 변경은 할 수 있지만 지양하도록 하자, 빅쿼리에서 데이터를 가져오거나 내보낼 때 Google Cloud Storage는 일반적으로 데이터를 보고나하기 위한 중간 장소 역할을 함! 

Cloud Dataflow 
데이터 처리 

cloud dataflow는 완전 관리형 파이프라인 러너, 다른 사전 구성 없이 파이프라인 제출하여 실행 가능 !

클라우드 데이터플로우 사용하는 파이프라인 실행 ->(컴퓨트 엔진 <-> 클라우트 스토리지 버킷 ) -> 버킷을 이용한 데이터 읽기(컴퓨트 엔진 -> 클라우드 스토리지 버킷) -> 컴퓨트엔진 처리, 데이터 변환 -> 출력을 다시 버킷에 쓰기

아파치 빔은 데이터 변환을 표현할 수 있는 오픈 소스 프레임워크이며, 많은 러너가 있는데 그중 하나가 Cloud Dataflow 

아파치 클라우드 채널을 사용하여 아파치 빔 파이프라인을 실행시킴(클라우드 데이터플로우!)

Cloud Pub/Sub
(관리 이벤트 퍼블리싱)
구글 자체 내부 인프라를 기반으로 구축한 완전 관리형 메시징 시스템!, 
주제, 메세지, 구독이라는 개념이 있음 !
주제: 정보 범주, 메세지를 퍼블리시하는 리소스, 메세지를 브로드캐스팅 할 때 주제가 필요함! 
메세지: 다른 곳에 브로드캐스트할 콘텐츠를 나타냄!, 메세지는 기본 64개의 인코딩된 페이로드와 일반 텍스트 속성 집합(키 값 맵으로 표시)으로 구성됨!
구독: 메세징 시스템에서 대기열이라고 함!, 특정 주체에 대한 메세지를 듣는 의도를 나타냄! 

메시징 패턴에는 팬 아웃 브로드캐스트 메시지와 작업 대기열 메세징으로 나눔!
팬 아웃 브로드캐스트 메세지 : 펍/섭을 사용해서 단일 발신자가 광범위한 청중에게 메세지를 브로드 캐스트함!
작업 대기열 메시징은 여러 소비자에게 작업을 배포하는 방식으로 이상적으로는 하나의 소비자만 각 메세지를 처리! 

메시징은 당사자간 (1대1, 1대 다, 다대다 )로 메세지를 보내는 것을 포함하여 프로세스 간에 데이터를 보내고 받는 개념!, 완전 관리형 고가용성 메시징 시스템, 생성자는 주제에 메세지를 보낼 수 있으며 , 소비자는 구독을 생성하여 구독 가능 
메세지는 수신자 또는 발신자에 의해 풀링 가능 !,
```
```

```