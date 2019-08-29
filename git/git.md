## GIT

#### git

> Git은 분산 버전 관리시스템(DVCS)이다. / 소스코드 이력 관리!

- 참고 문서
[Git scm] (http://git-scm.com/book/ko/v2/)
[git 입문] (http://backlog.com/git-tutorial/kr/)


```
git = Distributed Version Control System

DVCS vs CVCS
```

```
"git init"을 사용하여 깃 저장소를 만들 수 있음

git 저장소 안에 들어있는 폴더에 git init을 하는 것은 그렇게 좋지 않음.

git status - git bash(Commend Line Interface)의 상태를 확인 할 수 있는 것

git remote add origin https:///github.com/.... - 깃 원격 저장소에 저장

git remote add algo https://github.com/sunnyryu/alo.git (다른 원격 저장소에 쓰기 위한 것)

그리고 원격 저장소가 1개가 아니면 git push .이 아닌 각각 항목에 저장

git remote rm algo - git 원격 저장소 삭제
```

```
git log --oneline commit message와 간단하게 볼 수 있음
(HEAD -> master, origin/master)
```

### git Commend

#### 1. git setting
git 커밋을 하기 위해서는 초기에 작성자(author) 설정을 반드시 해야함
```GIT
$ git config --global user.name {user.name}
$ git config --global user.email {user.email}
```

현재 global로 설정된 환경설정을 확인하기 위해서는 아래의 명렁어 사용

```git
$git config --global --list
user.email = acsryu@live.co.kr
user.name = sunnyryu
```


#### 2. git basic

1. git 저장소 설정 (local)

```git
$ git init
/home/sunny/ubuntu/.git/ 안의 기존 깃 저장소를 다시 초기화했습니다
```

- 해당 디렉토리에 .git/폴더 생성
- 항상 git init 하기 전에는  해당 폴더가 이미 로컬 저장소인지((master) 여부) 확인 하여야 함

2. add
    ```git
    $ git add .
    $ git add READNE,md a.txt
    $ git add folder/
    $ git status
    ```
    - add 명렁어를 통해서 Working directory에서 Index(staging area)로 특정 파일들을 이동시킴
    - 해당 공간은 commit을 할 목록을 쌓는 것

3. commit
  ```git
    $ git commit -m '커밋메세지'
    $ git commit
    $ git log
    $ git log -2 (최근 2가지)
    $ git log --oneline (한줄로 보기)
    commit 85f1cc70bd8983e0f9fe598c4929df01e8ec37d0
    Author: sunnyryu <acsryu@live.co.kr>
    Date:   Wed Aug 28 09:05:59 2019 +0900
  ```

4. 현재 git 상태 알아보기(status)

    ***매우 중요***
  ```git
  $ git status
  ```

#### 3. 원격 저장소 (remote) 활용하기

#####1. 기초(basic)
  1. remote 저장소 등록
  ```git
  $ git remote add origin {github URL}
  ```
  - 원격 저장소를 ORIGIN 이라는 이름으로 URL을 등록한다.
  2. Remote 저장소 확인
  ```git
  $ git remote -v
  ```
  3.remote 저장소 삭제
  ```git
  $ git remote rm {저장소 이름}
  ```

#####2. Push  
  1. 원격 저장소로 push
  ```git
  $ git push origin master
  ```
  2. 원격 저장소로부터 가져오기 (pull)

  ```git
  $ git pull origin master
  ```

#
