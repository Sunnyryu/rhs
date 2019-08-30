## GIT

#### 1. merge / branch
 - (master) : 항상 동작하는 코드 (운영되는 코드)
 - develop
 - feature
 - hotfix

#### 2.
  - git branch {브랜치명} # 브랜치 생성
  - git checkout {브랜치명} #브랜치 이동
  - git branch -d {브랜치명} # 브랜치 삭제

  - git checkout -b {브랜치명} #브랜치 생성 및 이동

  - git merge {브랜치명}

  ```
  practice(fast-foward)
  1.feature/index branch 생성 및 이동
  2. 작업을 한 이후 commit
  3. master 이동
  4. master에 병합
  5. fast-fowarding(단순히 HEAD를 이동)


  practice(merge commit)
  1. feature / signout branch생성
  2. 작업을 한 이후 commit
  3. master로 이동 !!
  4. master에 추가 commit이 발생되어 있음~~
  5. master에 병합
  6. merge commit 발생
  ```
