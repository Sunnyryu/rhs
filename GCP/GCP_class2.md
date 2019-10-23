## Google Cloud

#### GCP Class 2

```

Compute Engine

Virtual Networks

VPC(Virtual Private Cloud)

AWS는 VPC Network는 리저널 서비스이지만,
GCP는 VPC Network는 글로벌 서비스.....

project가 있어야하는 이유... 프로젝트가 있어야 리소스를 넣을 수 있음 !
프로젝트를 만들었다고 끝나는게 아니라... 내가 만든 프로젝트에다가 vm을 만들었는데... 원래는 VPC가 없으면 Networks가 안되지만.. gcp에서는 기본적으로 default VPC가 깔려 있음. 그래서 가능한거임!!(vpc를 만들지 않았지만.. default VPC가 있기 떄문에 VPC 문제가 일어나지 않음, so VPC = Networks라고 생각하면 쉽게 이해할 수 있음)

프로젝트를 만들고 VPC를 만들어야함.. 프로젝트에다가 만들 수 있는 VPC는 5개로 정해져 있음.. 네트웤을 여러개로 격리할 필요가 있을 수 있음.. 5개가 최대치지만, 쿼터를 늘릴 수 있음... 리퀘스트를 통해서 ... 그렇지만 일반적으로는 5개임!!

CIDR => (classless inter-Domain Routing) => 클래스가 없는 라우팅 기법 / 맨 뒤에 정해진 것이 없는 것을 사용... [뒤에 나온 length를 가지고 판단하겠다..!]

AWS는 VPC에 Ip range(CIDR)를 가지고 있지만 GCP는 가지고 있지 않음

GCP는 글로벌하는 영역을 가지고 있음....

GCP는
VPC 생성 -> VPC 서브넷을 생성 -> 서브넷에다가 CIDR을 부여할 수 있음... ->  만들어지는 서버는 CIDR ip range는 받을 수 있음...

구글에서의 서브넷은..... 리저널 서비스임..... (aws는 zone이라는 차이가 있음)
VPC와 서브넷은 스케일이 다를 뿐임....
HA(High Availablity) => 이중화..도 포함..
구글 네트웤은 스케일 업을 하며, HA을 함.... 서브넷을 크로스가 가능하게끔 





```
