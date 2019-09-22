## Funny Openstack

#### Openstack

##### OpenStack study


1. 오픈스택과 아키텍처
  1-1. 정리(1)
  - 처음 릴리즈 때는 하이퍼바이저와 연동해서 인스턴스를 생성하고 삭제하는 컴퓨트서비스, 운영체제 이미지를 관리하는 이미지 서비스, 이미지를 백업하는 오브젝트 서비스 밖에 없었음
  - 상황별 오픈스택 구성 요소
    - HTC (High Throughput Computing)
      - 수십만 개의 코어로 확장할 수 있게 설계된 클라우드를 구축할 때, HTC 사용자는 Nova compute로 전환해 Horizon 대시보드로 단일 API 엔드포인트를 사용자에게 제공 / Keystone은 일반적으로 사용자 계저이 저장되는 LDAP 백엔드를 연결하는데 사용
      - 아래와 같은 서비스가 필요함
      - 대시보드 서비스(Horizon)
      - 텔레미터 서비스(Ceilometer)
      - 블록 스토리지 서비스(Cinder)
      - 오케스트레이션 서비스(Heat)
      - 이미지 서비스(Glance)
      - 인증 서비스(Keystone)
      - 컴퓨트 서비스(Nova)
    - 웹호스팅
      - 웹 호스팅하는데 오픈스택을 사용할 때, 일반적인 코어 서비스를 이ㅛㅇ하여, 사용자 계ㅓㅇ 데이터를 수집, 요금 청구시 일부 기술로 Ceilometer를 활용
      - 네트워크 서비스(Neutron)
      - 대시보드 서비스(Horizon)
      - 텔레미터 서비스(Ceilometer)
      - 이미지 서비스(Glance)
      - 인증 서비스(Keystone)
      - 컴퓨트 서비스(Nova)
    - 퍼블릭 클라우드 (Iaas를 제공하는 퍼블릭 클라우드를 지원 - 오픈스택!)
      - 일반적인 코어서비스, Swift를 사용해 오브젝트 스토리지 서비스를 제공, Designate는 DNSaaS를 제공(DNS as a Service)
      - 네트워크 서비스(Neutron)
      - 도메인 네임 서비스 (Designate)
      - 블록 스토리지 서비스(Cinder)
      - 이미지 서비스(Glance)
      - 오브젝트 서비스 스토리지(Swift)
      - 인증 서비스(Keystone)
      - 컴퓨트 서비스(Nova)
    - 웺서비스, 전자상거래
      - 오픈스택을 이용해 웹서비스, 전자상거래의 백엔드로도 사용 / 오픈스택 클라우드는 PCI 표준처럼 엄격한 규정 준수 요건을 충족 + 구성 / Trove는 내부 고객에서 DaaS(Database as a Service)를 제공 / 네트워크 정의 소프트웨어 SDN은 Neutron 제공
      - 네트워크 서비스(Neutron)
      - 대시보드 서비스(Horizon)
      - 데이터베이스 서비스(Trove)
      - 블록 스토리지 서비스(Cinder)
      - 이미지 서비스(Glance)
      - 인증 서비스(Keystone)
      - 컴퓨트 서비스(Nova)
    - 컴퓨터 스타터 키트
      - 스타터 키트는 추가 기능으로 클라우드를 확장할 수 있는 방법을 문서화로 제공하는 단순한 프로젝트를 말함
      - 네트워크 서비스(Neutron)
      - 이미지 서비스(Glance)
      - 인증 서비스(Keystone)
      - 컴퓨트 서비스(Nova)
    - 빅데이터
      - 빅데이터 분석 서비스인 Sahara 프로젝트는 오픈스택 위에 빅데이터 응용프로그램(Hadoop or Spark)를 간단하게 제공할 수 있는 방법 제공 / 다양한 데이터 처리 프레임 워크 지원 !
      - 네트워크 서비스(Neutron)
      - 대시보드 서비스(Horizon)
      - 베어메탈 서비스(Ironic)
      - 빅데이터 서비스(Sahara)
      - 이미지 서비스(Glance)
      - 인증 서비스(Keystone)
      - 컴퓨트 서비스(Nova)
    - DBaaS
      - 여러 SQL 및 NoSQL 백엔드를 지원함 / Ironic 프로젝트는 데이터베이스의 성능을 극대화하려고 베어메탈 프로비저닝을 제공
      - 네트워크 서비스(Neutron)
      - 대시보드 서비스(Horizon)
      - 데이터베이스 서비스(Trove)
      - 도메인 네임 서비스 (Designate)
      - 베어메탈 서비스(Ironic)
      - 블록 스토리지 서비스(Cinder)
      - 오브젝트 서비스 스토리지(Swift)
      - 이미지 서비스(Glance)
      - 인증 서비스(Keystone)
      - 컴퓨트 서비스(Nova)
    - 비디오 처리와 콘텐츠 전달
      - 제작 스튜디오나 주요 케이블 서비스 제공업체 같은 곳의 비디오 처리와 콘턴체 전달은 오픈스택의 보편적인 사용 예임
      - 네트워크 서비스(Neutron)
      - 오브젝트 서비스 스토리지(Swift)
      - 인증 서비스(Keystone)
      - 컴퓨트 서비스(Nova)
    - 컨테이너 서비스
      - 오픈스택은 신기술과 통합해 사용자가 가상 멋니, 컨테이너, 베어메탈에서 실행되는 워크로드를 단일 클라우드에서 운영할 수 있도록 개발
      - 오픈스택 사용자는 Kubernetes, Mesos, Docker와 같은 새로운 컨테이너 오케스트레이션 엔진(COE, Container Orchestaration Engines)과 통합하려고 Magnum 프로젝트에 엑세스할 수 있음
      - 네트워크 서비스(Neutron)
      - 대시보드 서비스(Horizon)
      - 베어메탈 서비스(Ironic)
      - 블록 스토리지 서비스(Cinder)
      - 이미지 서비스(Glance)
      - 인증 서비스(Keystone)
      - 컨테이너 서비스(Magnum)
      - 컴퓨트 서비스(Nova)

 1-2. 서비스 종류 + 아키텍처
    - Nova(가상 서버를 생성하는 컴퓨트)
      - 컴퓨트 서비스의 핵심, 하이퍼바이저, 메시지 Queue, 인스턴스 접속을 하는 콘솔 등 다양한 기능이 유기적으로 연결되어 가상 서버를 생성할 수 있는 시스템 구상
      - 논리 아키텍처의 Nova
        - Nova-api(대시보드나 콘솔 호출) -> 메시지 Queue(인스턴스 생성하라는 명렁어) -> nova-compute(하이퍼 바이저 라이브러리를 이용해 하이퍼바이저에 인스턴스를 생성하라는 명렁어 전달) -> 하이퍼바이저가 인스턴스 생성 -> 생성된 인스턴스는 nova-api로 접근할 수 있으며 Nova의 모든 기능은 메세지 Queue로 처리 가능
        - 오픈스택의 기본 하이퍼바이저는 KVM/QEMU임,
        - 지원하는 그룹을 3개로 나누어보면, A그룹은 자체 테스트를 완료해 안정적인 서비스를 할 수 있는 하이퍼바이저 드라이버(QEMU, KVM), 그룹B는 프로바이더가 테스트하는 하이퍼바이저 드라이버인 Hyper-V, VMware, Xen Server, Xen via Libvirt이며, C그룹은 몇 번의 테스탐 하는 하이퍼바이저 드라이버인 베어메탈, Docker, LXC via librvirt임
      - 노드별로 설치되는 Nova 프로세스
        - 
