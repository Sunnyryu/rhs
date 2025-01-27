## GCP Review

#### 1

```
클라우드 컴퓨팅의 정의 => NIST의 기준을 표준으로 함 -> 네트워크, 서버, 스토리지, 애플리케이션, 서비스 등 구성 가능한 컴퓨팅 리소스의 공유 풀에 대해 편리하고 언제든지 엑세스 할 수 있으며, 최소한의 관리 노력 또는 서비스 제공업체 간의 상호 작동에 의해 신속하게 제공되어 이용할 수 있는 모델 중 하나

클라우드 모델 및 특징

(서비스 모델 / 배치 모델로 분류 / 클라우드가 갖춰야할 다섯 가지 중요한 특성 제시)
1. 온디맨드 셀프 서비스 ( 사용자는 원하는 시점에 서비스를 바로 사용 가능 - ex) 홈페이지에서 혼자 가능해야함 !!)
2. Broad 네트워크 접근 ( 클라우드 서비스 제공자는 네트워크 기반으로 서비스에 접속가능해야함 -> 다양한 클라이언트에 의해 접속 가능 )
3. 자원 풀( 물리적 자원이나 가상화된 자원은 풀로 관리 -> 사용자의 요청에 의해 사용자에게 할당되거나 다시 풀로 반환됨, 없으면 안되유!)
4. 신속한 확장성( 사용자의 요구에 따라 시스템의 확장 및 축소를 즉시 수행할 수 있어야함)
5. 측정 가능한 서비스(자원의 사용량이 실시간으로 수집되고 모니터링 되어야함 !!)

서비스 모델

Infrastructure as a Service (IaaS) / Plaform as a Service (PaaS) / Software as a Service(SaaS)

배치 모델

Public / Private / Hybride( public + private, public +온프로미스 => 서로 다른 타입의 클라우드가 만났어요.!?) / community cloud (ex) 정부용 클라우드?, 국방부를 위한 클라우드.. / 특정한 목적으로 만들어진 클라우드 ..... => nist가 나눈 것에는 들어가 있지만.. 크게 목록으로 나누진 않음!)

클라우드 플랫폼 ..

프로비저닝... (우리는 이러이러 한 것이 필요해요 !(CPU, Memory, Disk, OS 등...))

고전적인 방식 => 호스트 -> OS -> APP

cloud = host ->  hypervisor ->VM -> OS -> APP
cloud(Type-2 /) host -> os -> hypervisor -> VM -> di -> APP
(Type-1 / Type-2 )

물리적인 머신 -> 하이퍼바이저(+VM) -> OS

VM(file type으로 존재 / 컴퓨팅 네트워크와 스토리지에서 각각 가져옴!!__?? )

클라우드 상태에서는 마이그레이션 상태가 많이 옴 -> 라이브 마이그레이션
갑자기 문제가 생기면 라이브는 아니지만 마이그레이션을 해줌..
```

```
VM 요청 흐름 파악
(사용자가 서버에 페이지 요청 -> 서버가 DB에 요청 -> DB에서 결과 전송 -> 서버가 페이지를 사용자에게 보냄 !!)

GCP 요청 흐름 (기본)
(VM 서버에 요청 -> DB에 요청 -> DB가 서버에 결과 전송 -> 서버가 사용자에게 보냄/서버가 GCP에 사용자 컨텐츠 업로드 -> 브라우저가 정적 콘텐츠를 GCP에 요청 -> GCP에서 정적 콘텐츠를 제공 !! )
```

```
소프트웨어 디파인에서는 컨트롤러가 가지고 있는데.. 그걸 구글은 다해줌..

구글은 하나의 네트웤!!!! => 기존의 홉 네트웍이랑은 다름!!
(곧 회선 임대업자에게 의존이 거의 없음.. 단.. 우리가 사용하는 인터넷 회사와의 구글 간에는 의존이 조금 있음... )

Zone -> Region -> MultiRegion ->  구글 자체의 네트웤(글로벌 서비스!!= 하나의 네트웤)
(ZONE은 가용성이 낮지만 가장 구축하기 쉬운 서비스, 속해 있는 ZONE이 다운되면 ZONE 서비스는 같이 다운)
(Region은 단일 지역의 여러 영역에 걸쳐 복제되어 있음! / 한 존이 안되더라도 다른 존의 인스턴스로 전환)
(리전은 3개의 존이 합쳐짐)
(리전은 어떤 지역에 3개의 idc가 있음 (곧 idc = zone이라고 생각하자))
(리전에다가 기본적으로 3개이상을 씀..) -> 리전들을 묶어서 멀티 리전이라고 함
(멀티 리전 -> 여러 다른 리전으로 구성됨 !-> 최소한의 중단 시간에 계속 실행 가능!)

ex) VM 하나 - Zone / 구글의 ip -> 글로벌 서비스 !

```

```
ex) Google CLoud Datastore의 요구에 따라 2개의 다중 지역 배포 옵션을 제공하는 app engine이 있음! 

클라우드에서는 개인 정보 보호 / 가용성 / 내구성이 보안적으로 안전해야함!

안전한 시설 / 암호화 / 복제 / 백업 등을 해줄 수 있어야함 !!

```

```
Cloud SQL 
- RDBMS를 사용하게 해주는 것!
- Mysql 같은 아이를 실행하는 vm! / 설정을 변경하기 위해 ssh를 사용하지 않아도 되는 mysql 같은 아이와 호환되는 서버 ! / 
- cloud console, SDK, REST API, 명령줄 도구로 모든 설정 변경 가능! 
- 구성에서 cloud sql 인스턴스를 가리키도록 호스트 이름 변경하는 것만으로도 가능!
- GCP에서는 sql 섹션에서 인스턴스를 생성하는 것으로 출발!
- ip 주소를 이용해서 ip/32 등의 cidr 표기법을 이용해서 정확한 ip에서부터 접근 허용 가능 !
- Cloud SQL을 사용하면 전송하는 데 있어 SSL을 쉽게 사용 가능!
- 서버의 CA 인증서 / 클라이언트 인증서 / 클라이언트 개인키 !!
(server-ca.pem으로 ca 인증서 다운 가능! / create a cLIENT Certificate 버튼을 이용해 인증서의 이름을 입력)
(client-keypem, client-cert.pem이 있어야함)
- 복제본을 만들어서 주 db이 손상을 대비하기 쉬움 ! / 읽기 복제본과 기본 복제본을 나눠서 관리가 가능하며 읽기 복제본을 이용해서 
- 각종 상황에 대비 가능! 
- gcp는 Cloud sql의 백업을 자동으로 할 수 있게 설정할 수 있음 
- 연결된 복제본은 백업 복원하기 전에 인스턴스를 삭제해야함 !
- Cloud SQL은 Cloud Storage를 사용해 데이터의 관리형 가져오기 및 내보내기를 하며, db에서 mysqldump 명령을 이용해서 
cloud storage의 버킷에 넣음 ! 
- 구조적으로 정의된 스키마를 적용하여 구조환 데이터를 저장 / 쿼리 기능을 제공하는 언어이며, 데이터를 묻는 질문이 있다면
cloud sql은 매우 탁월 / 내구성은 매우 좋음 / 데이터가 증가하면 쿼리 속도가 느려짐! 
- 외래키 참조를 사용하여 다른 데이터와 관련된 data 저장시 매우 적합
```

```
Cloud DataStore
- Nosql 구조 / 앱 엔진으로 쓰였음 !
- 문서 조장소 같은 느낌 ( 비관계형 저장소의 형태 ! 
- 키를 사용함 ( datastore의 키에는 데이터 유형과 데이터의 고유 식별자가 모두 포함됨! )
- 같은 부모를 가지는 키는 같은 엔티티 그룹에 속함!
- 데이터의 kind가 쓰이는 것은 Datastore
- datastore는 문서를 작성하는 항목, 엔티티느는 키라는 고유한 식별자와 결합된 속성 및 값의 모음 
- datastore은 booleans , string , integer, float, date or time, binary data의 기본적인 속성을 가질 수 있음
- 리스트(문자열), 다른 엔티티르 가리키는 키, 하위 엔티티 역할을 하는 임베디드 엔티티 등에도 사용
- 참조가 유효하다는 것을 강제할 방법이 없어 참조를 최신으로 유지 해야함
- get(해당 키를 사용하여 엔티티 가져옴), put(키를 사용하여 엔티티 저장 / 업데이트), delete(해당키로 엔티티 삭제)
- 색인과 쿼리를 모두 논의해야함 ! / datastore는 조인이 없으며, 색인은 고급 쿼리를 가능하게 쓰임 
- 색인의 경우 자동 생성됨 ! ( 각 속성에 대한 색인이...)
- datastore는 2단계 커밋을 이용하는 프로토콜 사용 (준비 / 완료 단계로 나눔) 
- datastore는 강한 일관성에는 아쉬움을 보임 !!
- datastore는 클라우드 콘솔에서 활성화 해야함 ! /
- 백업은 특별한 상황을 제외하곤 잘 하지 않음.
- 백업 기능은 정기적인 datastore 쿼리에서 cloud storage 버킷으로 내보낼 수 있는 기능(많은 데이터를 )
- 반구조화된 데이터를 관리하는데 뛰어남 , 동일한 종류의 모든 엔티티에 대해 단일 스키마 제공x
- 일반적인 관계형 성격을 지원 x, 참조 무결성이 없음, 특정 쿼리는 색인을 사용하도록 설정 
- 내구성이 매우 좋음! 
- 처리량이 매우 좋음! - 처리량만큼 트래픽 수용가능 ! / 동시 쓰기 조작으로 확장 가능! 
- 상호작용하는 데이터가 많을 수록 비용이 많이 듬!

```

```
Cloud Spanner
- SQL 구조에.... NoSQL DB 확장 속성을 가지는것!

Cloud Spanner도 콘솔에서 api를 사용하도록 설정해줘야함 !
Cloud Spanner 인스턴스 -> 많은 db를 보유하는 인프라 켄이터 역할을 함! / 스페너 데이터를 처리하는 데 궁극적인 책임이 있는 컴퓨팅 파워의 여러 개별 단위 관리! / 
Spanner 테이블은 다른 관계형 db와 비슷하지만 몇 가지 중요한 차이점이 있듬! 
스패터는 인터러브된 테이블에서.. 동적으로 분할하고 이동하여 리소스가 최적화 되게 사용 가능! ( 데이터 분할이 easy!)
ACID를 갖춤(원자성, 일관성, 고립성, 무결성)
트랜잭션의 경우 읽기 전용 / 읽기-쓰기 트랜잭션 이 있음!
구조적으로 매우 좋고, 쿼리 복잡도가 높으며, 내구성이 매우 좋고 속도나 처리량도 훌륭하다. 비용도 그만큼 비쌈
빅테이블 등의 고성능 및 가용성 제공에 중점을 둔 DB에서는 일반적으로 사용을 못하므로 클라우드 스패너의 좋은 기능임!

스패너는 비 관계형 DB의 확장기능을 가진 RDBMS이며, 사용자가 제공하는 힌트에 따라 자동으로 데이터를 청크로 분해할 수 있으며, 로드가 심한 경우 쿼리 대기 시간을 낮게 유지 + 
요청 부하를 여러 서버로 균등하게 분산가능 / 복제된 지역 구성에 배포, 여러 여영ㄱ에 여러 개의 완전한 복제본이 있음
일반적인 SQL DB의 기능이 필요, 비 관계형 시스템의 확장성이 필요할 때 적합 

Cloud BigTable
- 구글의 웹 검색 샌일을 위한 스토리지 시스템에서 .... 다른 스토리지 시스템을 지원하는 주요 기술중 하나.
- 페타바이트 단위의 데이터를 매우 높은 처리량을 보여줌!
- 검색색인의 전체 크기가 페타바이트 단위임!/ 낮은 지연, 높은 처리랑을 보여줌 !/ 급속하게 변화하는 데이터 
- 강력한 일관성, 행-수준 트랙잭션, 하위집합 선택 !!, 
- 빅테이블은 관리형 서비스로 동작! , 직접 노출되지 않는 태블릿 개념!, 인스턴스 -> 클러스터 -> 노드 개념으로 되어 있으며 클러스터에는 최소 3개의 노드로 되어있음
- 클러스터를 늘리면 비용은 증가하지만, 가용성은 증가함 !
- 태블릿은 특정 노드에 있는 데이터 청크를 참고하는 방법임 !( 분할 , 결합, 다른 노드로 이동가능! , 노드와 마찬가지로 직접 주소 지정x, )
- 데이터가 저장되고 클러스터에 영구적으로 적용되므로 필요한 vm 근처에 선택해야함! (빅테이터 데이터를 읽거나 쓰는데 있어서 !)
- 하둡 시퀀스 파일 형식을 사용하여 데이터 내보내고 가져오는 기능 지원함 !
- Bigtable에서 데이터를 내보낼 때, 서버 관리는 약간 혼란스러울 수 있음, Dataproc이라는 관리서비스를 이용해서.. 쉽게 가능! 
노드와 용량을 늘릴 수록 비용은 당연히 증가! 
- 매우 느슨한 구조, (열 한정자 자체가 데이터로 저장할 수 있음.. 즉석으로 만들기에, 열 한정자는 동적일 수 있음)
- 쿼리 또한 복잡하지 않음 / 영구 디스크에 저장되므로 데이터를 잃을 확률이 떨어지며, 속도와 처리량이 매우 훌륭함 
- 성능이 좋은 만큼 당연히 비용이 많이 듬 !!

- 복제되고 빠르게 변하는 대용량 데이터를 처리하도록 설계, 강력한 일관성을 유지하면서, 높은 동시성으로 신속하ㅔㄱ 쿼리할 수 있음 ! 
- 많은 양의 데이터를 가지거나 키 조회나 키 스캔을 사용하여, 액세스하는 경우에는 적합하지만 보조 색인 또는 관계형 쿼리가 필요한 경우에는 적합하지 않음 ! 
```

```
Cloud Storage 

- 이미지 저장 가능! 
- 버킷은 데이터 를 제장하는 컨테이너 / 프로젝트의 고유한 이름이 아닌 전역적으로 고유한 이름뿐 아니라 지리적 위치 및 저장소 클래스 설정 
- 객체는 버킷 안에 넣는 파일 !
- 위치는 컴퓨트 엔진에서 사용될 수 있도록 버킷도 위치를 가질 수 있음 ! (버킷은 지역 레벨 또는 여러 지역에 걸쳐서 존재)
- VM 과 GCS의 데이터 사이의 대기 시간이 염려 될 경우 데이터에 대해 특정 지역 선택 가능 ! 
- console or SDK 사용 가능 !

- 멀티 지역 저장소 / 지역 저장소 / 니어라인 저장소(Nearline) / 콜드라인 저장소(Coldline) 
- 멀티 지역 저장소는 가장 일반적인 옵션, 선택된 위치 내부의 여러 지역에 걸쳐 데이터를 복제하기 때문에 가장 비쌈 !!
- 지역 저장소는 클래스 내의 여러 영역에 걸쳐 데이털르 복제 / 약간 낮은 가용성 / 대기 시간이 멀티 리전에 비해 약간 큼 
- 니어라인 저장소는 가용성이 약간 낮고 첫 번째 바이트에 대한 지연시간이 더 높음 !
- 콜드라인 저장소는 데이터 스펙트럼의 극단적인 목표, 니어라인에 비해 저렴..
- ACL을 사용한 액세스 제한 .. => 액세스 제어 목록이라는 보안 메커니즘을 통해 버킷 및 객체에 대한 세분화된 액세스 제어 허용 !
조회자/ 작성자 / 소유자로 생각해보쟈 !!
조회자 (버킷은 객체를 버킷에 있는 객체 목록으로 조회할 수 있으며, 객체 조회자는 객체의 내용을 다운로드 할 수 있음 
)
작성자 ( 버킷은 객체를 조회, 작성, 덮어쓰기, 삭제를 할 수 있음, 객체 작성자는 적용 x )

소유자( 버킷은 acl과 같은 메타 데이터를 업데이트 할 뿐만 아니라 조회자와 작성작 할 수 있는 모든 작업 가능 . / 객체 소유자는 조회자가 할수 있는 작업 뿐만 아니라 acl 등 메타 데이터 업데이터 가능 !)

- allusers => 모든 사용자 / allAuthenticatedUsers => 자신의 구글 계정으로 로그인한 사용자(올 유저와 비슷함)
- 그룹은 특정 구글 그룹의 모든 회원을 지칭함 
- 도메인은 구글 apps 관리 도메인 이름을 나타냄 !
- acl을 관리할 때는 최소한의 액세스를 허용하며, 소유자의 허가는 조심하고 의도적으로 공개로 액세스 허용은 조심, 기본 acl은 자동실행 => 합리적인 기본값 선택 

객체별 수명 / 고정 날짜 컷오프 / 버전 기록 / ㅚ신 버전 등의 객체 수명주기 가있음 (age/ createdBefore/NumberOfNewVersions/IsLive)
-cloud storage는 비구조적 스토리지 시스템 이며, 쿼리 복잡성이 매우 낮아.. 복잡한 쿼리를 처리할 수 없음 ... 내구성이 매우 강하며, 속도나 처리량 등이 매우 뛰어남, 비용도 매우 저렴한 편임 !!
- 클라우드 스토리지의 경우 주로 데이터 청크를 저장하느 ㄴ것이지만 이전 데이터에 대한 자동 삭제, 여러 버전의 데이터 저장, 고급액세스 제어 등의 기능을 제공 
- 클라우드 스토리지는 결국 다른 스토리지 시스템을 보완하므로 결과적으로 그것 대신이라기보다는 다른 스토리지 시스템과 함꼐 사용 
```

```
컴퓨트 엔진(가상머신)

영구 디스크는 보통 연결되지 않음 ... 읽기 전용 모드, 읽기/쓰기 모드로 부착되는 3가지가 있음 
스냅샷 - 디스크의 데이터에 대한 체크 포인트 역할을 할 수 있어 - 스냅샷을 디스크 인스턴스로 복원가능! 
이미지 - 스냅샷과 유사하지만 .. 디스크의 시작 템플릿으로 사용되는 반면 , 스냅샷은 특정 시간에 디스크의 내용을 정확히 나타내는 백업 형태 ! / 스냅샷과 다르게 이미지가 자동저장소를 사용하지 않아 비용이 조금 더 드는 편임!

로드 밸런싱
- 전체 시스템에서 처리해야 하는 전체 트래픽이 때떄로 단일 시스템에 비해 너무 많다보니... 머신을 더 크게 만들기 보단 더 많은 머신을 사용하고 로드 밸런서를 사용해서 사용가능한 리소스에 트래픽을 분할 하는 것임 !
- 많은 요청이 들어올 때 로드밸런서를 통해 모든 요청을 라우팅 하기에.. 인스턴스 그룹이 켜저 있는 모든 vm에서 자동으로 균형하게 조정하게 됨 !커

클라우드 CDN 
백엔드 서비스의 응답을 자동으로 캐시할 수 있는 구글 클라우드 CDN이 있음 !(로드밸런서, GCE와 함꼐 작동하도록 설계! )
사용자 요청 (클라우드 CDN이 처리 할수 있으면 응답 반환)-> 로드밸런싱 장치 요청 -> 백엔드 서비스 요청 -> 개별 VM에 대한 요청 -> 벡앤드 서비스 응답 -> 로드 밸런싱 장치에 대한 응답 -> 클라우드 CDN에 대한 응답 -> 최종 사용자에 대한 응답 
혹은 다른 엔드 포인트 CDN에게 요청을 하여 엔드포인트 CDN에게 응답받아 사용자에게 응답해주기도 함 ! 
캐시의 겨웅 모든 페이지를 캐시하려고 시도하며, 10MB보다 크거나 응답에 Set-Cookie 헤더가 있거나 요청 응답에는 캐시하지 말아야 하는 Cache-Control(no-store 등)이 있으면 특정 응답을 캐시하지 않을 수 있음 
(클라우드 cdn 활성 / get http 메소드 / 응답 코드 successful(203,200,300), 콘텐츠 길이 또는 전송 인코딩(표준 http 헤더에 지정)이 있어야 캐시 제어를 하기 위해 필수 조건임)

GCE(Google Cloud Compute Engine)의 경우 유연성이 좋으며, 단순하지 않지만 다른 컴퓨팅에 비해서는 나은 편, 베어 메탈에 가까운 성능으로 인해 매우 좋은편 ! / 상대적으로 낮은 비용이 있음 ! 

결론 : 가상 머신은 가상화된 컴퓨팅 리소스 이며, 실제 컴퓨터의 조각처럼 어딘가 에 있음, 템플릿을 기반으로 자동으로 기계를 켜고 끌 수 있으므로 시스템을 자동으로 확대 축소 가능 !
- 작업자는 vm을 바르게 쉽게 켜고 끌 수 있는 확장성이 뛰어난 작업 부하 떄문에 선점형 vm은 비용을 크게 절감할 수 있으며, 언제든지 종료 가능 ! , 컴퓨팅 리소스를 세부적으로 제어하고 가능한 한 물리적 인프라에 가까워지기를 원할 떄 베스트 ! 
```