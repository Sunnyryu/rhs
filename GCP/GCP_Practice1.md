## GCP Practice

### 1. SDK 재설치

```
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main"|
sudo tee -a /etc/apt/sources.list.d/google-cloud-skd.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install google-cloud-sdk

gcloud components update

gcloud auth login => sdk에 로그인

gcloud auth application-default login => 로그인 자동..~

gcloud compute instances list

gcloud compute ssh instance-1

node.js로도 할수 있는데 해당 파일을 설정 하면 됨

const gce = require('@google-cloud/compute')({
  projectID: 'projectubuntu'
});

const zone = gce.zone('us-central1-b');

console.log('getting your VMs..');

zone.getVMs().then((data) => {
  data[0].forEach((vm) => {
    console.log('found a vm called', vm.name);
    //console.log('Stooping', vm.name, '...');
    //vm.stop((err, operation) => {
    //operation.on('complete', (err) => {
    //console.log('Stopped', vm.name)});
  });
  console.log('Done');
});

gcloud sqlusers set-paswword root "%" --password "password" --instance wordpress-db

=> sql 인스턴스 실행

실행 후 에 mysql에도 설정을 해줌..

=> vm에 연결하여 word press를 설치해주고 php 파일 편집 및 mysql 정보 수정!

실행 !!=>끝!!

cloud sql

mysql -h 104.155.184.195 -u sunny \ --paswword='password'

DB 생성및 테이블 생성을 해준다!

create database todo;

create table 'todolister' (
  'id' INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  'name' VARCHAR(255) NOT NULL
  ) ENGINE = InnoDB;

INSERT INTO todolister ('name') VALUES ("grocery"),
("summer party"),
("holiday plans");

후에 테이블에 항목을 추가 하여 정리를 한다!

버킷을 생성해서 GCS(Google Cloud Storage에도 보낼 수 있음!! / GCS 버킷에 보내줌!!)

Cloud DataStore

key, value로 이루어짐~~

data store을 만들고 node.js로 쿼리를 만든 후 출력하면 키와 네임스페이스, 아이디 , 카인드, 패스 , 데이터 등이 나옴!

gsutil mb -l US gs://my-export => buket 생성

gclud beta datastore export gs://my-export/export => gcs로 데이터 내보내기

gsutil du -sh gs://my-export/export-1 => 내보내기 데이터 크기 보기!

cloud spanner (클라우드 스패너 !!)

스패너 인스턴스 및 데이터 베이스를 만듬!
테이블을 만듬 !
데이터 추가를 해줌 !


gcloud spanner databases ddl update pract-database \
--instance=prac-instance\
--ddl="ALTER TABLE employees ALTER COLUMN name STRING(MAX) NOT NULLL"
DDL Updating...done.
- 스키마 변경 실행 !!

트랜잭션!!(ACID)

cloud bigtable

big table 인스턴스 생성( 인스턴스 유형, 저장소유형 , 클러스터 , 위치 , 노드 설정 )

스키마 만들기

js로 만들었으며 테이블은 instance.createTable을 이용함!

데이터를 삽입하거나 키로 데이터를 가져올 수 있음 !

mvn clean package -Dbigtable.projectID=projectubuntu \
-Dbigtable.instanceID=projectubuntu-id

dataproc 클러스터를 만들고 여기에 내보내기 작업을 할 수 있음 !!

cloud storage(GCS)

오브젝트 스토리지/ binery!

버킷과 객체로 쓰임!!gsutil 명렁어 사용 !

버킷을 만들고 파일을 업로드 해볼 수 있음

멀티 리전 / 리전 / 니어라인 / 콜드라인으로 나눔 !!

권한 제어는 ACL로 함 !

gsutil mb gs://first-bucket

gsutil cp a.txt gs://first-bucket (버켓에 업로드)

acl은 private , project-private, public-read(read-write) 등이 있음

gsutil logging을 사용하여 추적할 수 있음 !!

json 파일에 룰로 모아서 action type을 delete로 하면 삭제도 가능 !!


````
