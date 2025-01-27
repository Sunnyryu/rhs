## Lecture for MariaDB

#### Mariadb !!

##### mariadb 주최 컨퍼런스 !!

1. MariaDB 소개 (홍성구 지사장님)
  - Founded 2009(2014) - 오픈소스를 사용하기 위해 퇴사하고 창립함 / 2014년에 회사를 본격 설림함..
  - mysql과 mariadb의 모태는 핀란드임 !
  - 한국에서는 3월에 시작함
  - (40배의 효율이 좋음) 빠르고 가볍고 가장 적응력이 있음!!
  - 하나의 노드에 2개 소켓, 12코어라고 가정할 때( 3년 Total Cost of Ownership)
  - (O사 1백만달러 / mariaDB 약 2만9천불 )
  - 오픈 소스 ... VS 클로오즈드 소스
    - EX) 요즘은 하이브리드한 시대, DB을 사용한다고 가정했을 때....
    - EX2) 22년에는 70%의 소프트웨어가 오픈소스로 나올 수 있고 RDBMS는 50% 정도가 오픈소스로 쓰일 예정
  - 오픈소스가 왜 ??
    - IBM이 RedHat을 인수하고 엘라스틴이 상장하고, 마이크로소프트가 github를 인수하고 뮬소프트를 세일즈포스가 인수하고 몽고DB가 공공으로 가고 있음.
    - 현재 오라클 -> 마리아 DB로 넘어가는 비율이 커짐..
    - MariaDB는 한국에서도 많이 쓰이고... 주요 대기업이 사용하고 있음 !!
    - 은행에서도 사용하고 있고 외국 대기업에서 쓰이고 있음 !!(DBS Bank, ServiceNow)
    - 외국의 5대 텔레콤 업체 중에서 4개가 사용하고 있음
  - 마리아DB Cloud
    - DBPaaS의 성장이 매우 증가할 예정..
    - MariaDB에서 SKY SQL을 출시할 예정(클라우드)
  - 커뮤니티 VS 기업
    - 물을 그대로 VS 물을 가공해서 마시겠습니까..의 차이.. (나의 책임 VS DB업체가 문제가 나면 책임을 져줌!)
  ```
  enterprise 지원 여부 등은 .. 따로 기록은 해두지 않을 예정 ~~~
  ```
2. MariaDB 강의 (몬티 -마이클 와이드너스 CTO님)
  - Why Open Source / Why MariaDB
  - 오픈 소스의 장점 / 마리아DB의 현황을 공유!!
  - Basic
    - Using open standards
    - good Softwore(no fee) & free software
  - Open Source
    - 좋은 소프트웨어를 쉽고 잘 쓸 수 있고 많이 개발할 수 있고 좋은 코드, 많은 테스트, 많이 퍼트릴 수 있음
    - 다양한 기업, 다양한 참여자가 오픈소스를 이용해서 문제를 해결하고 다 같이 참여할 수 있음
    - 오픈소스의 원리는 ? (아무 돈이나 댓가도 받지 않는 것인가?)
      - 대부분은 필요한 소프트웨어를 다운 받는 것에 출발 -> 점점더 겪고 있는 문제를 해결하기 위해서, 변경, 진화 시킴
      - 본인의 문제를 해결위해 코드를 공유해주면서 스스로 문제 해결, 다른이의 해결도 하면서 발전해나감
      - thenextweb에서 오픈 소스 fad를 내놓았는데 ppt를 통해 확인 할 수 있음 (False / True / confused)
    - 많은 서버들이 오픈소스 작동 시스템으로 실행됨
    - 많은 기술, 좋은 솔루션임(빅데이터나 하둡등도 오픈소스 기반!)
    - 오픈소스는 광범위하게 채택하지 못한 곳은 모바일 어플리케이션 공간임 ...
    - 많은 정보들에 트랩 도어가 숨어있지 않을까 하지만 .. 오픈 소스야 말로 100% 최고라는 부분임.
    - 개발자에게 오픈소스는 매우 좋은 이익임 (접근이 쉽고 코드를 사용할 수 있고 볼수 있음)
    - 오류나 버그를 찾을 수 있고 그 것을 공유할 수 있음
    - 사용하는 것이 자유임(read, buid and change 등
    - 오픈소스는 배울 수 있는 기회이며, 오픈 소스 환경에서 공헌할 수 있음
    - 라이센스가 없음 ..!! (YES - 몬티도 라이센스 없는 것이 좋다고 하더라고요 0v0 )
    - 벤더가 사라지더라도 벤더 락인을 없애고 사용할 수 있고 당장 멈추지 않음 !!
    - Vendor Lock in을 없애고 사용시킬 수 있는 것!!
    - 오픈소스를 사용하는데 갑자기 문제가 발생했을 때, 어떤 타격이 있을까하면 ?? 타격이 없다면 오픈소스가 더 좋고 타격이 있을거라면 벤더가 필요할 수도 있음(여기서 말하는 벤더는 closed 벤더가 아닌 오픈소스를 제공해주는 벤더임..)
- MYSQL(몬티의 딸 이름을 따서 지음!!) / MariaDB (둘째 딸의 이름을 따서 지음)
  - 인터넷의 등장, 가상형 회사, 많은 자유가 있음, 설치가 쉽고 사용이 쉬움 !
  - 친근하고 유용함.. 생산까지 투자 , 좋고 훌륭함
- MariaDB 소개
  - 사람을 저장하고 제품을 저장항!
  - Mysql의 기능을 함꼐 유지!
  - 확실한 자유 버전의 mysql의 항상 존재함
  - 하나의 커뮤니티로 개발 시키고 브랜치로서 유지하기 위해
  - 무료로 많은 사람들이 사용할 수 있기에!!
  - MariaDB는 오픈소스로 언제나 개발하고자 하기 위해 회사를 만듬 .. (wow)
  - 깃허브에 mariadb에 관한 것을 리포짓 해두었음
  - 열린 개발을 통해 같이 참여할 수 있음 !!
  - 다양한 나라에서 많이 쓰임 (공부를 더 해야하겠다.. ~~)
  - 쉽고 빠르게 업그레이드 가능함 (업그레이드에는 조금의 시간만이 필요하며, 매우 간단함, 단번에 예전 버전에서 업데이트 가능함)
  - 릴리즈를 자주하려고 하며 버그가 있으면 신속하게 처리하려고 노력함
  - 깃헙에 가서 스타좀 주세요 .. ㅎㅎㅎㅎㅎㅎㅎ (몬티의 말슴... 깃헙의 위대함인가... )
  - mysql과 mariadb의 차이를 기자들꼐서 여쭤봤다고 했는데...
    - mariadb에서만 최근 4-5년간 혁신을 넣었으며, 휠씬 광범위한 분야에서도 기능과 선택폭이 있음
    - mariadb는 유연하게 쓰이는 가장 유용한 DB임
    - (Access to other databases through JDBC and ODBC)
    - 그밖에 많은 것을 하고 있음 (Sequence, OQgraph,Sphinx,S3)
    - PL/SQL 지원 / Packages / ROW data Type / TYPE OF / Instant ADD COLUMN, DROP COLUMN
    - 오라클에서 Mariadb로 변경없이 옮길 수 있음 !!
    - 시스템 버저닝 for InnoDB
    - mariadb 10.5에서는 clustrix (storage engine with write scaling) - 마리아 db 서버에서 저장소 엔진 인터페이스를 이노DB와 클리스트릭스로 공유할 수 있음 ! - Join과 aggregation을 할 수 있음
    - 마리아 db간에 데이터를 공유할 수 있음 (실시간으로 !! 성능 저하없이 - 마리아 db와 클러스트릭스를 함꼐!!)
    - 마리아 db에서 read 쪽은 매우 잘되어 있었지만 write의 스케일링이 부족했었는데 클러스트릭스를 인수하면서 부족함을 채웠고 다른 것보다 훌륭해졌다고 자부할 수 있음
    - 마이락스 스토리지 엔진(페이스북), DBS(PL/SQL)을 협의하여 마리아 DB에 넣고 있음
    - 리눅스에서도 사용하고 있었음
    - 2년전에 레드헷이 마리아 DB로 넘어올떄 버그가 없었고 마이그레이션이 매우 잘됨
    - 현재는 마이SQL보다 마리아 DB가 세계적으로 많이 쓰이게 됨 (SERVER 기준 )
    - LinuxQuestions.org에서 6년 연속 데이터베이스를 사용한 세계인들에게 투표하여 상을 탐(... 세계적인 db구나)
    - 마리아db로 변경해야하는 이유
      - mysql을 써야할 이유가 없음
    - Q&A - 에코시스템에서의 mariadb 호환성이 부족한 것이 있었는데 라는 질문이 나옴
      - mariadb에서 정규화가 되어 락인도 없고 여러가지 장점이 있으며, mariadb foundation에서도 mysql과의 호환을 위해 노력하고 있음 !!
      - 개발이나 멀티 소프트웨어 측면의 부분에서도 mairadb에서 안되는 부분이 있는 것은 지금 진행중이며, 해결을 할 예정입니다.
      - mysql보다 프로토콜의 호환성을 확보하기 위해 mariadb는 노력하고 있음
    - Q&A 2 - 퍼포먼스 측면에서 10.3과 10.4이 MYSQL 8.0보다 낫는가?
      - MYSQL의 성능이 나쁜지 않다는 것을 경험하였고 풀로 한 결과는 나오진 않았지만 oracle에서의 거대 장비에서는 좋게 나오지만 일반 사용자에게는 그런 장비가 없고 mariadb가 mysql보다 효율성이 좋고 새로운 하드웨어에서도 mariadb에서는 테스트하고 구현을 하고 있음!

3. Introducing MariaDB Platform X3 and the rise of hybrid everything
  - 하이브리드 워크로드
    - 데이터베이스 워크로드
      - 트랜젝셔널 / 애닐리티컬
        - 트랜젝서널에서는 대부분 현재 데이터 범위 쿼리, 노운 쿼리들이 쓰임
        - 애널리티컬에서는 히스토리컬 데이터와 어그리게이트 쿼리, 언노운 쿼리들이 쓰임
        - 트랜잭셔널에서는 로우베이즈드 스토리지, 인덱스, 클러스트/레플리케이트를 사용
        - 애널리티컬에서는 컬러널 스토리지 / 노 인덱스/ 분산환경의 아키텍처 사용
      - application development에서는 OLTP
      - datascience 팀에서는 OLAP이 쓰임
      - 두개의 팀 사이에는 큰벽이 있음 ( 어플리케이션 데이터팀은 TX에 퍼포먼스 레인지가 있고 데이터 사이언스팀에는 AX에 퍼모먼스 레인지가 있음 )
      - 이커머스 사례에서는 구매에 따른 , 재고에 따른, 대부분을 보여줌 -> 요즘은 고객이나 사용자가 원하는 정보를 애널리티컬 부분을 요구하여 매출과 서비스 확장이 이루어짐
      - Hybirid workloads 에서는 문제가 발생하는데 두개를 같이 쓰려고 할 떄에 그래서 app/dev에 transaction과 analytic을 실시간으로 같이하고 analytic와 OLAP의 ANALYTICS를 연동하여 해결을 함
  - 마리아DB x3
    - 스토리지 구조임 !
    - mariadb MaxScale과 server를 같이 구성 (tx)
    - mariadb MaxScale / server 를 같이구성
    - 위의 2가지를 x3에 합쳐서 maxscale / server 2개를 설정하고
    - 서버 안에 innoDB 1개 / columnStore 1개를 구성함 !
    - 현재는 x4를 준비중임
    - 마리아DB maxscale 2.3은 server 1개에는 TX를, 다른 server는  AX를 해주면
    tx의 server에서 ax server로 CDC를 해줌
    - 컨테이너 지원(Kubenetes(Helm패키지) / Docker(Compose)
    - spark connector , c/java/python api로 벌크 데이터를 임포트하여 columnStore에 넣거나 카프카 커넥트도 넣을 수 있고 C, JDBC, ODBC, Node js도 지원
    - sql diagnostic manager, SQLyog, mariaDB Backup, MariaDB Flashback를 지원해줌
  - 확장성 (scalability)
    - Row storage(OLTP) / Sharded(spider로 지원) / Columnar storage(OLAP) / Disk-based / Distributed 모두 지원 해줌
    - 마리아DB X3를 쓰면 MaxScale에서 한가지 서버와 트랜잭션 1가지 서버와 analytical를 하며, 어플리케아션과 맥스스케일이 연동함
  - 실제 예
    - 마켓 리서치 (Retail)
      - 트랜잭셔널과 애널리티컬 모두 DB(Hybrid)에서 지원을 해줌!
      - 필요한 부분에 맞춰서 1가지를 사용하면 되요!
    - ip telephone - SaaS
      - 위와 마찬가지!
  - 하이브리드 클라우드
    - 다른 워크로드를 다른 스트럭쳐에 사용할 수 있음 !
  - 데이터베이스 콘솔리데이션
    - 기본적으로 하나의 서비스가 아닌 여러가지 서비스를 하고 있는경우가 많은데 니즈의 요구사항에 맞게 솔루션을 채택하게 되는데, 구매, 카트, 클릭스트림을 하게되는데 마리아 db 플랫폼 x3을 사용하면 1가지로 모두 사용가능 !!
    - 각각에 맞는 것을 하나의 통일된 서포트를 받을 수 있음 !(3개의 회사에서 1개의 회사로!)
  - 도커
    - 마리아 db 플랫폼에는 도커나 쿠버네티스를 지원함
    - X3를 테스트하고 싶다면 github.com/mairadb-corporation/mariadb-platform-docker/tree/master/single-container에서 해볼 수 있음

4. RDB확장성 어떻게 해결할 것인가..?
  - 일반적으로 쓰는 RDB를 잘쓰는가를 강구했나!
    - RDB 확장과 서비스 확장은 필수적 관계
      - 서비스관점(더나은 사용자 경험, 더많은 사용자 처리, 더많은 거래의 처리)
      - 확장
        - 출근 길 엘리베이터 병목현상과 출근시간에 지하철의 예로 가정하면
        - 엘리베이터를 늘리거나, 공간을 늘리는 것이 방법이 됨
        - 4개의 엘리베이터를 동시에 운영함
        - 정상 서비스를 운영하기 전에 문제가 생김(어디가 문제 인지, 어디가 애매한지가 나옴)
        - 중층을 기준으로 나눠서 4단계로 나눈 것이 있음
        - 50층에 환승층을 두는 방법이 있음
        - 이런 고민들이 database를 사용하는데 고민의 요소가 되어짐!
        - 이제 본론으로 들어가보자면  
        - 고객 테이블에 자주사용되는 컬럼과 가끔 사용되는 컬럼으로 나눔
        - pk 고민 (CRUD 중 무엇을 가장 잘 처리하는가...)
        - 테이블 / 클러스터드 인덱스 , 해쉬 나누기와 hot contention
        - index right growing reverse index 와 hot contention으로 나눔
        - 쓰기 성능이 매우 매우 중요한 시스템이라면 쓰기 성능과 해당 테이블 로우 컬럼 개수
        - pk index = concat(index columns, primary key)
        - 몇가지 myth "pk는 작게를 auto_increment로 오용"
        - auto_increment를 안쓰고 pk를 잘선정해서 쓰는 것이 좋음!!!!
        - 인덱스 설계를 해줘야함
        - index 컬럼의 구성요소와 순서/ 컬럼의 데이터 타입 및 길이/ 컬럼별 / 복합 컬럼별 등
