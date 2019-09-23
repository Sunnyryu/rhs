## Funny Openstack

#### Openstack

##### OpenStack 공부 전 클라우드 컴퓨팅 study


1. 클라우드 컴퓨팅

  - 클라우드 컴퓨팅이란 인터넷이 가능한 디바이스(pc,스마트폰 등)로 제 3의 공간인 클라우드에서 데이터를 읽고 쓰고 정보를 분석해 처리하며, 이를 저장하고 관리하는 컴퓨팅 시스템
  1-1. 종류
    - 무엇을 서비스 하느냐에 따라 Iaas, PaaS, SaaS로 나눔 (DaaS나 BaaS 등으로도 나눔)


      1-1-1. IaaS
        - infrastructure as a Service라하며, 서버, 스토리지, 네트워크를 가상화 환경으로 만들어 필요에 따라 인프라 자원을 사용할 수 있게 해주는 서비스 (에로 웹서버, 에플리케이션 서버로 사용할 리눅스나윈도 서버를 임대하는 것..)
        - 인프라 자원을 서비스로 제공(물리환경)
      1-1-2. PaaS
        - Plaform as a Service라 하며, 개발 플랫폼으로 확장한 것으로 웹에서 개발 플랫폼을 쉽게 빌려 쓸 수 있는 서비스 !
        - ex) 케이웨더에서 제공하는 날씨 정보를 이용하여 웹페이지를 개발한다고 했을 때 api 서비스도 PaaS 서비스의 일종
      1-1-3. SaaS
        - Software as as Service라고 하며, IaaS와 PaaS 위에 올라가는 소프트웨어를 말함, 온디맨드 소프트웨어라고 함 ( 중앙에서 호스팅되는 소프트웨어를 웹 브라우저 등의 클라이언트로 이용하는 서비스)
        - ex) IaaS에서 서비스되는 가상 인스턴스(가상 서버)에 웹 서버와 WAS를 설치, DB 서버에 연동해 웹 사이트를 구축했다면 이것이 SaaS가 됨. 클라우드 환경에서 동작하는 모든 application이 바로 SaaS임!
        - ex2) google docs가 SaaS의 예 / 오피스 프로그램 없이도 인터넷에서 작성가능, 공유도 가능!
      1-1-4. DaaS
        - Desktop as a Service로 클라우드 인프라를 이용해 일반 사용자용 윈도 등 데스크톱 운영체제가 설치된 인스턴스를 서비스받는 것임!
        - ex) 개인용 컴퓨터가 없이도 클라우드 서비스와 연결 가능한 단말기만 있으면 언제든지 클라우드에  접속해 일할 수 있음!( 은행처럼 보안이 중요한 곳에서 불법 소프트웨어 방지나 데이터 유출 방지 가능
      1-1-5. BaaS
        - Backend as a Service로 모바일 환경에서 구현하기 복잡하고 힘든 서버 사이드 서비스를 API 서비스로 제공해서 모바일 웹이나 웹을 개발할 때 UI/UX를 집중할 수 있도록 하는 서비스!
        - 클라우드 서비스, 모바일, IoT 산업이 활성화 -> 무겁고 어려운 비즈니스 로직을 직접 구현 x, 필요에 따라 클라우드 서버에 이미 구축된 Backend 서비스는 주로 모바일 환경에 사용했지만 최근에는 모바일이 아닌 환경으로도 확산되어짐!


  1-2. 클라우드 공개 범위
  - 공개 범위에따라 퍼블릭,프라이빗, 하이브리드 클라우드로 나뉨.
        1-2-1. 퍼블릭 클라우드
        - 아마존이나 구글, MS 등 서비스 제공자에게서 서버나 스토리지를 제공받아 PaaS 같은 개발 환경이나 SaaS 등에 해당하는 소프트웨어 서비스를 하는 것을 통칭해서 퍼블릭 클라우드라고 하며, 인터넷만 되면 언제 어디서든 접근이 가능한 서버, 스토리지, 개발환경, 소프트웨어를 칭함
        1-2-2. 프라이빗 클라우드
        - 퍼블릭 클라우드의 반대라고 생각하면 쉽지요!, 인터넷에 공개되지 않는 것, 외부에 공개하면 곤란한 시스템, 사내 인트라넷 시스템
        - 별도의 서버나 스토리지 자원으로 클라우드 컴퓨팅 시스템 구축, 거기서만 사용하는 개발환경, 소프트웨어 등을 칭함
        1-2-3. 하이브리드 클라우드
          - 퍼블릭과 프라이빗, 두가지를 모두 관리할 수 있는 시스템, 퍼블릭 영역에 있는 인스턴스를 언제든지 프라이빗 클라우드 영역으로 가져올 수 있고 프라이빗 클라우드 영역에 있는 것을 퍼블릭 으로 내보낼 수 있는 시스템임!!

  1-3. 컴퓨트 서비스
  - 사용자가 원하는 운영체제가 탑재된 컴퓨터나 서버를 인터넷에서 사용할 수 있게 제공하는 유로 또는 무료 서비스!
  - 클라우드 서비스를 이용하면 매우 순식간에 서버 구축이 가능해짐
  - 컴퓨트 서비스는 시스템을 구축할 때 필요한 서버를 가상으로 할당해주는 서비스로, 이때 할당되는 가상 서버가 인스턴스임
  - 인스턴스를 생성하는 기준은, CPU, 메모리, 하드디스크 용량을 고려해서 생성 가능, 어떤 운영체제를 사용하느냐에 따라 인스턴스를 생성 가능하며, 개발 환경이 구축된 인스턴스도 선택 가능, 인스턴스는 생성과 부팅이 쉬워 요구 사항의 변화에 따라 서버 용량을 빠르게 증설/축소 가능

  1-4. 스토리지 서비스
  - ex) N 드라이브, Cloudlike, Dropbox 등은 스토리지 서비스임 (아마존 드라이브, 구글 드라이브, skydrive, 통신사의 클라우드 등도 포함)
  - 스토리지 서비스는 사용자가 소유한 데이터나 음악, 동영상, 문서 파일을 인터넷에 있는 스토리지에 저장, 삭제, 공유할 수 있는 서비스 ( 인터넷이 가능한 스마트폰, 스마트패드, 스마트TV, 노트북 등 컴퓨터만 있으면 언제 어디서든지 클라우드 스토리지에 접근해서 파일을 읽고 쓰기 가능)
  - ex2) 모바일 앱을 이용해 찍은 사진을 클라우드 스토리지에 저장 하고 사진을 스마트폰 없이도 팔요에 따라 데톱이나 노트북에서 내려받을 수 있으면 클라우드 스토리지 서비스를 사용하는 거임!
  - IaaS는 하드웨어 같은 인프라를 제공하는 서비스, Paas는 개발 환경 같은 플랫폼을 제공하는 서비스, SaaS는 소프트웨어를 제공하는 서비스이지만 스토리지 서비스는 컴퓨트 서비스와 다르게 어떤 서비스를 제공하느냐에 따라 IaaS의 범위/SaaS의 범위에 해당하는 서비스일 수 있음
  - 일반적으로는 IaaS보다는 SaaS에 가까움
  - 사진이나 음악, 동영상 등 파일을 올리고 확인 가능한 사이트나 모바일 웹 등 완성된 software를 제공한다면 SaaS임
  - 스토리지와 스토리지에 접근할 수 있는 REST API만을 제공하는 서비스(REST API 만을 제공하는 스토리지 - 아마존의 S3, OpenStack의 오브젝트 스토리지인 Swift)

  1-5 하이퍼바이저
  - 호스트 컴퓨터 한 대에서 운영체제 다수를 동시에 실행하는 논리적 플랫폼임! (VMM- 가상 머신 모니터 - Virtual Machine Monitor)
  - 하이퍼바이저는 하드웨어를 직접 설치해서 실행되는 Native(베어메탈)/ 일반 에플리케이션처럼 프로그램으로 설치되는 Hosted 방식이 있음
  - Native 방식의 하이퍼바이저는 해당 하드웨어에 직접 설치 실행 / 게스트 운영체제는 이미 하드웨어 설치된 하이퍼바이저에서 두번째 수준으로 실행 / 하드웨어에 운영체제 대신 Xen, KVM, Xen Server 같은 하이퍼바이저가 설치, 설치된 하이퍼바이저 위에 서로 다른 운영체제가 실행되는 방식임 / TYPE1이라고도 함
  - Xen, XenServer, VMware(ESX Server), L4 microkernel, TRANGO, IBM(Power 하이퍼바이저-PR/SM), MS의 Hyper-V, Parallels Server 등이 있음 / 플랫폼의 펌웨어에 하이퍼바이저를 넣은 히다치의 VIrtage와 KVM도 TYPE1에 속함
  - Hosted 방식은 일반 프로그램처럼 호스트 운영체제에서 실행되며, 가상 머신 안에서 동작되는 게스트 운영체제는 하드웨어에서 세 번째 수준으로 실행 / 쉡게 집에 있는 윈도 맥, 리눅스에 오라클 VirtualBox, VMware를 설치하고 다른 운양체제를 띄우는 것이 해당됨
  - VMware Server, VMware Fusion, QEMU, MS(Virtual PC), Virtual Server, SWsoft(Parallels Workstation, Parallels Desktop) 등이 TYPE2에 해당함

    1-5-1 가상화방식에 따른 하이퍼바이저
    - 전가상화 방식은 하드웨어를 모두 가상화한 것임, 전가상화 방식은 하드웨어를 모두 가상화했기 때문에 게스트 운영체제를 변경 X, 다양한 운영체제로 이욯라 수 있는 장점이 있음 / 물리적인 가상화를 지원하는 CPU의 가상화 기술을 이용해야만 함!!
    - 즉 전가상화 기술을 이용하려면 CPU가 가상화 기술을 지원해야하 , Intel VT, AMD-V 등이 요구됨
    - Native 방식과 같은 개념이라고 생각하면 됨! (하드웨어 아키텍처 위에 가상화 레이어(Virtualization Layer)가 올라가고 해당 가상화 레이어로 서로 다른 가상의 하드웨어, 운영체제, 소프트웨어를 실행)
    - 가상화를 지원하는 CPU를 직접사용하므로 윈도를 설치할 수 있음 (오픈스택의 기본 하이퍼바이저인 KVM은 윈도를 게스트로 살치할 수 있으므로 전가상화 방식 지원함!)
    - 리눅스 같은 오픈 소스를 설치할 수 있으면 반가상화 방식이라고 생각하면 됨!
    - 반가상화 방식은 하드웨어를 완전하게 가상화하지 않은 것!, 게스트 운영체제가 하드웨어를 직접 제어할 수 없고 하이퍼바이저로만 제어가 가능 / 하이퍼바이저가 모든 것을 제어하므로 높은 성능 유지 가능 /
    - 그러나 게스트 운영체제의 커널 일부분을 변경해야하는 단점이 있기에, 오픈 소스가 아닌 운영체제에서는 운영할 수 없다는 문제점이 있음!
    - 가상화를 지원하지 않은 CPU가 잇는 서버에 오픈스택을 설치하면 KVM이 아닌 QEMU가 설치되는데 QEMU는 반가상화의 대표적 예임
    - KVM은 QEMU에서 실행되는 하이퍼바이저이기에, 전가상화,반가상화 모두 지원함!!
  1-5-2 다양한 종류의 하이퍼바이저
      - KVM
        - 오픈스택의 기본 하이퍼바이저인 KVM(for Kenel-based Virtual Machine)은 커널을 기반으로 전가상화 방식을 지원하는 오픈 소스 하이퍼바이저 중 하나/ 반드시 가상화가 지원되는 Intel VT나 AMD-V가 있어야만 사용가능
        - KVM을 사용하면 리눅스나 원도 이미지를 수정하지 않고 여러 가상머신으로 실행가능 / KVM으로 각 가상머신은 네트워크 인터페이스 카드, 디스크, 그래픽 어댑터 같은 가상화된 하드웨어를 가질 수 있음
      - Xen / Xen Server
        - 2003년에 케임브리지 대학교에서 시작되어 공개 버전을 발표한 오픈소스 하이퍼바이저임 / 초기에는 반가상화만 지원해 게스트운영체제를 실행하려면 게스트 운영체제르 Xen에서 실행 할 수 있게 수정해야 했지만 지금은 그렇게 안해도 가능!(3.0 이후!)
        - 다만 QEMU 같은 CPU 에뮬레이터가 아닌 전통적인 하이퍼바이저이기에,호스트와 다른 아키텍쳐의 게스트를 실행 X, 모든 기능을 커맨드로 관리해야 하기 때문에 리눅스 환경에 익숙하지 않은 사람은 사용이 어려웠지만 커머셜 오픈 소스 업체가 부가기능을 추가해서 제품을 만들었는데 오라클 VirtualBox가 그 예임
        - 에플리케이션 가상화 기술을 확대해 서버 가상화와 데스크톱 가사화로 발전시킴!
        - Xen Server는 XAPI와 XenCenter를 이용한 관리 기능, 스토리지 지원과 실시간 마이그레이션, 고가용성 기능처럼 데이터 센터에서 요구하는 확장 기능을 제공!
      - Hyper-V
        - MS에서 ㅜ인도 서버 2008에 추가해서 공개한 하이퍼바이저이며, 디바이스 드라이버가 부모 파티션에 올라가 있음 / 그래서 콘솔 OS 역할을 부모 파티션이 수행
        - 다른 VMware 등 하이퍼바이저에 비해 크기가 휠씬 작아 오류 코드가 포함될 확률이 낮음, Intel VT, AMD-V x64를 지원하는 하드웨어가 있어야 가상화가 가능!
      - VMware vSphere ESX
        - 적은 하드웨어에서도 어플리케이션을 통합할 수 있도록 서버를 가상화해주는 무료 베어메탈 하이퍼바이저임
        - ESX는 vSphere 하이퍼바이저에 이쓴ㄴ 많은 서비스 중 하나 / VMkernel이 핵심으로 가상머신의 업무를 지원하는 역할을 함
        - 약 20만 라인 정도의 코드로 개발, 크기는 32MB / ESX는 가상 머신이 발생시킨 명령어를 하이퍼바이저가 받아 재작업한 후 가상 환경에서 잘 구동하도록 바이너리 변환 방식을 사용
        - Hyper-V와 다르게 가상화 지원 디바이스가 없이도 가상화 구현 가능!
      - DocKer
        - 리눅스 기반의 컨테이너 런타임 오픈 소스/ 가상 머신과 기능이 유사, 가사 머신보다 휠씬 가벼운 형태로 배포가 가능 / DocKer는 컨테이너 개념으로 가상 머신처럼 Docker Engine을 호스트 위에서 수행하지만, 리눅스 기반의 운영체제만 수행 가능
        - 가상머신 처럼 하드웨어를 가상화하는 것이 아니라 게스트 OS를 분리시켜줌
        - ex) 호스트 운영체제가 우분투, 컨테이너 OS가 CentOS라면 컨터네이너에 CentOS Full 이미지가 모두 들어이쓴ㄴ 것이 아님, 우분투와 차이가 나는 부분만 별도로 패키징해서 컨테이너 안에서 명렁어를 수행하면 실제로는 호스트 운영체제인 우분투에서 그 명령어를 수행
        - 즉 호스트 운영체제의 프로세스 공간을 공유!!
      - VirtualBox
        - 현재는 오라클에서 개발하고 배포! / 다른 하이퍼 바이저와 비교할 때 기능이 부족하다고 할 수 있지만 원격 데스크톱 프로토콜(RDP), iSCSI 지원, RDP를 거치는 원격 디바이스의 usb 지원처럼 원격으로 가상 컴퓨터를 제어할 수 있는 기능이 있으며, HYPER-K의 가상 디바이스를 지원
      - VMware Workstation
        - 게스트 운영체제에 설치할 수 있는 드라이버 및 기타 소프트웨어 묶음으로, 게스트 머신이 고해상도 화면에 접근할 수 있게하는 VESA 호환 그래픽스, 네트워크 인터페이스 카드(NIC)용 네트워크 드라이버, 호스트와 게스트 간 클립보드 공유, 시간 동기화 기능 제공!
      - Parallels Desktop
        - 맥에서 지원하며, 다양한 운영체제를 가상화 할 수 있음
    1-5-3. 하이버 바이저별 이미지 포맷

          하이퍼바이저  |  지원 이미지 포맷
          --|--
          KVM  |  img, qcow2, vmdk
          VMware  |  vmdk
          VirtualBox  |  vdi, vmdk, qcow2, vhd
          Hyper-V  |  vhd, vmdk, vdi
          Xen, XenServer  |  qcow2, vhd


          이미지 포맷  |  설명
          --|--
          qcow2  |  QEMU Copy On Write 2
          vdi  |  Virtual Disk Image
          vmdk  |  VMware Virtual DIsk Development Kit
          vhd  |  Virtual Hard Disk
  1-6. 클라우드에서 알아햘 네트워크 개념
  - 고정 ip 주소 / 유동 ip 주소
    - 고정 ip : 회사나 집에서 사용하는 컴퓨터에 연결된 이너넷 회선에 IPTime 같은 인터넷 공유기를 연결해 고정으로 할당받는 IP를 말함
    - 가상 머신간 내부 통신만 가능(클라우드 컴퓨트 서비스는 우리가 설치한 클라우드 플랫폼에서 IP를 할당받기 떄문에)
  - 유동 ip : 가상 인스턴스에 인터넷 프로바이더에게서 할당받은 인터넷 ip를 할당하면 됨 -> 이것을 유동 ip라고 함! / 가상 인스턴스가 외부에서 접근할 수 있도록 할당하는 인터넷이 가능한 ip임 (필요에따라 부여하거나 삭제가능)
  - ip 클래스/ ip 범위
    - 클라우드 플랫폼에서 많은 인스턴스 생성 - 가상 인스턴스 생성될 때마다 나누어질 ip 테이블이 있음(테이블의 범위를 ip 범위라고 함)
    - ip 범위를 설정하려면 ip 클래스를 먼저 알아야함
    - ip 클래스는 A 클래스, B 클래스, C 클래스와 다른 몾거으로 예약된 D,E 클래스로 나눔
    - A 클래스는 가장 높은 단위의 클래스로 범위가 1~126이며, 서브넷 마스크를 보면 2.3.4 단위는 사용자(호스트)에게 부여 가능
    - B 클래스는 두번쨰로 높은 단위의 클래스로 128~191 사이의 범위를 가짐, 두 번째 단위는 B 클래스가 접속할 수 있는 네트워크, 세 번째와 네 번째 단위는 사용자에게 부여할 수 있음
    - C 클래스는 최하위 클래스로 IP 구성에서 첫번째 단위가 192~ 223 사이의 범위를 가짐, 2~3 번쨰의 단위는 C 클래스가 접속할 수 있는 네트워크임, 4번째 단위만 사용자에게 IP 부여 가능
    - IP 범위는 컴퓨터에 할당할 수 있는 IP 개수, IP는 네트우커ㅡ 부분과 호스트 부분으로 나눌 수 있음
    - 네트워크 부분은 말 그대로 네트워크 이름 / 호스트 부분은 개별 컴퓨터에 부여
    - ex) 203.240.100.1 이라는 ip가 있고 서브넷 마스크가 255.255.255.0이면 203.240.10은 네트워크이며, 1은 호스트 1번이라 할 수 있음
    - 클래스라는 명칭은 네트워크와 호스트 수에 따라 구분, IP 클래스의 범위, 서브넷 마스크, 할당 가능한 호스트 IP 개수를 나타내면

  분류(CLASS)  |범위   |  서브넷마스크 |서브넷마스크 비트 수   | 호스트 비트 수  |  할당 가능한 호스트 IP 개수
--|---|---|---|---|--
A  |  1.0.0.0 ~ 126.255.255.255 |  255.0.0.0 |  8비트 |   32비트|  약 1600만개
B  |  128.0.0.0 ~ 191.255.255.255 |255.255.0.0   |16비트  |   16비트|  약 6만5000개
C  |  192.0.0.0 ~ 223.255.255.255 | 255.255.255.0  |  24비트 |  8비트 |  254개
D  | 224.0.0.0 ~ 239.255.255.255  |멀티   |캐스트용   |으로   |예약된 클래스  
E  |  240.0.0.0 ~ 154.255.255.255 | 연구  |개발을  |목적으로   |예약된 클래스  

  - CIDR(Classless Inter-Domain Routing)
    - 클래스가 없는 도메인 간 라우팅 기법으로 기존 ip 할당 방식인 네트워크 클래스를 대체 / IP 영역을 여러 네트워크 영역으로 나눌 때 기존 클래스 방식에 비해 장정이 있음!
      - 급격히 부족해지는 IPv4 주소를 좀 더 효율적으로 사용할 수 있음
      - 접두어를 이용한 주소 지정 방식의 계층적 구조 사용 / 인터넷 라우팅의 부담 덜어줌
    - 기본적으로 비트 단위 ip를 체크하는 표준 분석 방식 / 그래서 일련의 ip들을 하나의 라우팅 테이블 항목에 넣는 것으로 라우팅 실행
    - CIDR 블록에 포함된 여러 IP는 이진 표기를 했을 때 일련의 초기 비트가 같음
    - IPv4 CIDR 블록은 IPv4 주소와 형태가 비슷, 점과 숫자로 구성된 네 부분의 주소와 '/' 뒤의 0에서 32까지 숫자로 되어 있음 (A, B, C D/N 같은 형태 가짐)
  - SDN(Software Defined NetWorking)
    - 네트워크 제어 기능이 물리적 네트워크와 분리되도록 프로그래밍한 네트워크 구조
    - 특징 짓는 두 가지 포인트가 있음
      - 1. 네트워크 제어 기능을 데이터 전달 기능과 분리해서 구현해야함
      - 2. 네트워크 제어 기능이 개발되고 실행될 수 있는 환경을 분리해 낮은 성능의 CPU가 있느 ㄴ하드웨어 스위치에 더 이상 위치시키지 않음
    - 다시말해서 SDN이라면 네트워크 제어 기능을 기존 스위치나 라우터 등 하드웨어와 별도로 분리해야 하고 데이터 전달 기능과도 분리해서 개발 및 실행될 수 있는 네트워크 구조여야 함 !
    - SDN은 오픈플로 기술을 이해 알려짐
  - 오픈플로(OpenFlow)
    - SDN의 근간이 되는 기술 / 네트워크 프로젝트인 Quantum에 포함된 기술
    - SDN 아키텍처의 컨트롤 레이와 인프라스트럭쳐 레이어 사이에 정의된 최초의 표준 통신 인터페이스
    - 오픈플로 스위치/컨트롤러로 구성
    - 흐름 정보로 패킷의 전달 경로와 방식을 제어함 (오픈플로 컨트롤러와 지원 네트워크 장비(라우터, 스위치) 사이에서 커뮤니케이션 역할을 담당)
    - 소프트웨어 컨트롤러로 플로 테이블을 조작하고 데이터 경로를 설정해서 사용자, 어플리케이션, 세션 계층 수준에서 실시간 변화에 대응할 수 있음
  - 네트워크 장비
    - 라우터
      - 인터넷 등 서로 다른 네트워크를 연결할 때 사용하는 장비 (지능이 있는 경로 배정기)
      - 경로 결정과 스위칭 기능을 함
      - 경로 결정은 데이터 패킷이 목적지까지 갈 수 있는 경로를 검사해서 어느 곳으로 가는 것이 가장 적절한지 결정(경로가 결정되면 결정된 길로 데이터 패킷을 스위칭함)
    - 허브
      - 컴퓨터와 컴퓨터를 연결해 네트워크 구성 !
      - UTP 랜 케이블을 사용해서 가까운 거리에 있는 컴퓨터들을 연결해주는 네트워크 장비
      - UTP 랜 케이블은 케이블 길이가 100M 넘어가면 신호 감뢰 현상이 발생하는데 허브는 감쇠된 신호를 증폭시키는 역할도 함
      - 멀티포트 리피터라고 할 수 있음 (들어오는 데이터를 그대로 재전송함)
      - 5개의 컴퓨터가 있을 때 1,5번이 2번에게 컴퓨터로 데이터를 보내려고 하면 CSMA/CD에 따라 충돌이 발생
      - 위를 같은 콜리전 도메인에 있다라고 하며 이것을 해결하기 위해 브리지를 씀
    - 브리지
      - 말 그대로 콜리젼 도메인을 나누어 서로 통신이 가능하도록 다리처럼 연결해주는 네트워크 장비
      - 브리지를 사용하여 하나의 네트워크망에 물려있는 콜리젼 도메인을 서로 다른 콜리전 도메인으로 분리하고 분리된 도메인을 세그먼트라고 함
      - 같은 세그먼트 안의 컴퓨터끼리 통신할 때에는 다른 세그먼트로 데이터가 전송되는 것을 막는 역할을 함
    - 스위치
      - 브리지와 역할을 동일하지만 하드웨어적으로 처리하는 스위치가 소프트웨어적으로 처리하는 브리지보다 속도가 더빠름
      - 브리지보다 더 많은 포트 개수를 제공하며, 브리지는 Store-and-forward라는 프레임 처리 방식만 지원하지만, 스위치는 Car-through, Store-and-forward라는 프레임 처리 방식을 지원함

1-7. 블록 스토리지 / 오브젝트 스토리지
  - 블록 스토리지
    - 클라우드 컴퓨팅에서 컴퓨터나 서버를 인스턴스라고 하는 것처럼 인스턴스에 추가하는 하드 디스크를 블록 스토리지라고 함
    - 운영체제가 설치된 인스턴스에 추가로 확장해 사용할 수 있는 디스크, 데이터나 파일 등을 보관하려는 목적의 저장 공간
    - 컴퓨터의 로컬 하드 디스크를 본체에서 분리해 다른 컴퓨터에 연결해서 사용할 수 있는 것처럼 인스턴스의 블록 스토리지도 원래 있던 인스턴스에서 연결 해제한 후 다른 인스턴스에 연결해서 사용 가능!
  - 오브젝트 스토리지
    - 사용자 계정벌로 저장 공간을 할당할 수 있는 오브젝트 스토리지 시스템(단독으로 구성가능, 사용자 계정 컨테이너에 파일이나 데이터를 저장할 수 있는 저장공간)
    - 사용자는 시스템에 로그인해야 스토리지 이용 가능!
    - ex) 네이버 클라우드, 드롭박스 등이 예임
  - 대표적인 스토리지 서비스
    - 아마존 EBS / S3
      - EBS(ELastic Block Store)는 블록 스토리지에 해당하는 서비스로 아마존의 EC2(Elastic Compute Cloud)에서 생성한 인스턴스에 확장해서 사용할 수 있는 스토리지! (1GB ~ 1TB)
      - S3는 오브젝트 스토리지에 해당하는 서비스, 사용자계정에 해당하는 Owner, 컨테이너에 해당하는 Bucket, 파일이나 데이터에 해당하는 오브젝트
    - 오픈스택 Cinder / Swift
      - Cinder는 cinder-volume,backup,scheduler, Volume Provider, cinder-api로 구성되며, Nova 에서 제공되는 인스턴스의 확장 스토리지로 사용가능!
      - Swift는 오픈스택의 기본 서비스 중 하나로 오브젝트 스토리지 서비스를 제공함
      - proxy-server, account-server, contatiner-server, object-server, swift-api로 구성
      - poxy-server는 여러 대의 스토리지 노드에 구성된 account-server, container-server, object-server를 관리
    - Ceph의 RBD, RADOS
      - Ceph는 모든 종류의 스토리지 서비스를 모아놓은 오픈 소스 서비스
      - RADOS라는 스토리지 노드 위에 LIBRADOS라는 RADOS 라이브러리가 있음
      - 오픈스택의 SWIFT와 연동하는 RADOSGW(게이트웨이), QEMU나 KVM에서 생성한 인스턴스의 블록 스토리지로 사용하는 RBD(RADOS Block Device), 사용자의 편의성을 제공하려고 POSIX(표준 운영체제 인터페이스)를 제공하는 Ceph FS로 구성되어 있음

  1.8. 클라우드 컴퓨팅을 활용한 다양한 IT 산업
    - 사물인터넷(Internet of Things)
      - 각종 사물에 센서와 통신 기능을 내장해 인터넷에 연결하는 기술 (사물은 가전제품, 모바일 장비, 웨어러블 컴퓨터 등 다양한 임베디드 시스템)
      - 사물은 자신을 구별할 수 있는 ip로 인터넷에 연결 / 외부 환경에서 데이터를 모으려고 센서를 내장할 수 있음
      - 서버에 이러한 것이 저장되고 서버에 저장된 데이터로는 다양한 앱을 개발할 수 있음
      - 이 떄 물리서버가 아닌 클라우드 환경에서 구축한 인스턴스 활용 가능 / 클라우드에서 구축한 가상서버에서는 다양한 용도로 서버를 추가하거나 삭제를 할 수 있음
    - 빅데이터
      - Hadoop(빅데이터를 구축할 수 있는 가장 대표적인 오픈 소스)
        - 하둡과 하둡의 에코 시스템, 로그 Flume, 수집한 로그와 데이터를 저장하는 HDFS, 코디네이션을 하는 Zookeeper, 데이터 추출하는 MapReduce, NoSQL에서 기존 RDBMS의 쿼리를 그대로 사용하려고 도와주는 Hive
    - 머신 러닝
      - 기계학습은 인공지능의 한 분야로 컴퓨터가 학습을 할 수 있게 하는 알고리즘과 기술을 개발하는 분야
    