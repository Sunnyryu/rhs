## GIT

#### git

> Git은 분산 버전 관리시스템(DVCS)이다. / 소스코드 이력 관리!

- 참고 문서
[Git scm] (http://git-scm.com/book/ko/v2/)
[git 입문] (http://backlog.com/git-tutorial/kr/)
[git 참고사이트] ()


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

##### 1. 기초(basic)
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

##### 2. Push  
  1. 원격 저장소로 push
  ```git
  $ git push origin master
  ```
  2. 원격 저장소로부터 가져오기 (pull)

  ```git
  $ git pull origin master
  ```

##### 3. Push-Pull 시나리오
  - Local A, Local B, Github으로 활용하는 경우 원격저장소 이력과 달라져서 충돌이 발생할 수 있음 / 따라서 항상 작업을 시작하기 전에 pull을 받고 작업을 완료한 이후에 push를 진행하면 충돌 사항이 발생 x

  1. auto-merge
  - 동일한 파일을 수정하지 않은 경우 자동으로 merge commit이 발생 함

  ```
  1. Local A에서 작업 후 push
  2. Local B에서 작업 후 pull을 받지 않음.
  3. Local B에서 다른 파일 작업 후 commit -> push
  4. 오류 발생(~git pull~~)
  5. Local b에서 git pull
  6. 자동으로 vim coomit 할 수 있도록 뜸.
  7. 저장하면, merge commit 발생
  8. local B에서 git push!
  ```

2. merge conflict
  - 다른 이력(커밋)으로 동일한 파일이 수정되는 경우 merge conflict 발생
  - 직접 충돌 파일을 해결해야 한다!

  ```
  1. Local A에서 작업 후 push
  2. Local B에서 작업 후 pull을 받지 않음.
  3. Local B에서 다른 파일 작업 후 commit -> push
  4. 오류 발생(~git pull~~)
  5. Local B에서 git pull
  6. 충돌 발생(merge conflict)
  7. 직접 오류 수정 및 add, commit
  8. Local B에서 git push를
  ```

  - git status 명렁어를 통해 어느 파일에서 충돌이 발생하였는지 확인 가능!
  - 실제 파일 예시
  ```git
  <<<<<<< HEAD
  Local B작업
  ===========
  원격 저장소에 기록된 작업
  >>>>>>> fsafafafa12313214141
  ```
##### 4.undo

  ```git
  $ git commit --amend
  (commit 이력이 기록된 뒤에는 commit 메서지를 바꾸게 되면 hash값이 바뀌게 됨 !(ex :41241dasd -> 132dada))
  이력을 바꾸는 등의 행위를 할 때에는 조심해야 한다.

  $ git commit --amend
  (특정한 파일을 뺴놓고 했다면 명렁어로 인해서 커밋을 수정할 수 있음 - 보기가 안 좋음)

  $ git rm --cached 파일명
  rm '파일명'
  untrack 시키는 형태임
  ```
