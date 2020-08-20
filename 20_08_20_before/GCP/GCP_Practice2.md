## GCP Practice

### 2. 연습 2

```

gloud compute instances create instance-1


gcloud compute ssh --zone asia-east1-b instance-1

gcloud compute instances list

컨테이너 - 어플리케이션 구성 및 모든 종속성을 표준 형식으로 쉽게 패키징 할수 있도록 하여 소프트웨어 배포 문제를 해결하기 위한 인프라 도구 !

도커 - 컨테이너를 실행하기 위한 도구 ! / 컨테이너를 한 곳에서 다른 곳으로 운반하는 현대적인 컨테이너 선과 같은 역할 !!

컨테이너 이미지 정의 , 컨테인 ㅓ정희하는 환경 및 코드

도커파일을 사용 !

쿠버네티스 - 컨테이너를 관리하는 시스템 / 기본 단위로 컨테이너 !/ 클러스터 / 노드 (코드를 실행할 수 있는 단일 시스템) / 포드 - 특정 노드가 실행하는 개별 기능 단위가 동작하는 컨테이너 그룹 / 서비스 - 다양한 포드가 실행되는 위치 ! / 쿠버네티스 엔진 - 쿠버네티스 배포 관리 및 호스팅 !!

쿠버네티스엔진 사용을 위해서 express 파일을 node.js로 만들고 json 파일과 도커파일을 만들었다

docker run hello-world

docker build --tag hello-node .( 태그 지정)

docker run -d -p 8080:8080 hello-node

docker logs ID

docker stop ID

docker ps --format "table {{.ID}}"
docker images --format "table {{.Repository}}\t{{.ID}}"


docker tag hello-node gcr.io/project-id/hello-node:v1

docker images --format "table {{.Repository}}\t{{.Tag}}"

gcloud docker -- push gcr.io/project-id/hello-node:v1

gcloud compute instances list --filter "zone:us-central1-a name:gke-*" | awk '{print $1}'

gcloud components install kubectl

gcloud container clusters get-credentilas --zone us-central1-a firstcluster

그 후에 pod에 배포했는지 확인 후에 문제가 없다면 포트가 오픈되도록 kubectl expose 명령어를 사용하면 됨 !!

kubectl get services => 사용가능한 서비스 확인

kubectl proxy=> 쿠버네티스 프록시 연결

app engine

gcloud components install app-engine-python => 파이썬 확장판 엔진 설치!

GAE standard로 배포 후 확인 !

GAE flex => standard보다 지원해주는 것이 많음 !!
````
