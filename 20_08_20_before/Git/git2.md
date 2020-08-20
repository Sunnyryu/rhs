## GIT

#### 1. merge / branch
 - (master) : 항상 동작하는 코드 (운영되는 코드)
 - develop
 - feature
 - hotfix
  ```
  - git branch {브랜치명} # 브랜치 생성
  - git checkout {브랜치명} #브랜치 이동
  - git branch -d {브랜치명} # 브랜치 삭제

  - git checkout -b {브랜치명} #브랜치 생성 및 이동

  - git merge {브랜치명} # 브랜치명을 지금 브랜치명으로 병합
  - (master) git merge fetch/index # fetch/index 브랜치를 master로 병합
  ```

  ```
  practice(fast-foward)
  1.feature/index branch 생성 및 이동
  2. 작업을 한 이후 commit
  3. master 이동
  4. master에 병합
  5. fast-fowarding(단순히 HEAD를 이동) -master 브랜치의 이력이 변화하지 않았기 떄문( 브랜치 생성 이후에 커밋이 추가되지 않음)
  6. branch 삭제

  practice(merge commit)
  1. feature / signout branch생성
  2. 작업을 한 이후 commit
  3. master로 이동 !!
  4. master에 추가 commit이 발생되어 있음~~
  5. master에 병합
  6. merge commit 발생
  7. 그래프 확인하기
  8. branch 삭제

  2가지 연습했던 부분의 차이는 merge commit에 대한 문제가 있음

  practice(merge commit 충돌)

  1. feature/signout branch 생성 및 이동
  2. 작업 완료 후 commit
  3. master 이동
  4. *master에 추가 commit 이 발생시키기!!*
     - 다른 branch에서 작업한 파일을 같이
  5. master에 병합
  6. 결과 -> *merge conflict발생*
  7. 충돌 확인 및 해결
    충돌 mark 를 확인하여, 코드를 알맞게 수정한다!
    git status 명령어 통해서 어느 파일이 충돌인지 확인한다.
  8. *merge commit 진행
     ```bash
     $ git commit
     ```
  9. 그래프 확인하기
  10. branch 삭제
  ```

  ```
  practice 1의 결과
root@sunny:/home/sunny/test# git branch fetch/index
root@sunny:/home/sunny/test# git branch
  fetch/index
* master
root@sunny:/home/sunny/test# git checkout fetch/index
'fetch/index' 브랜치로 전환합니다
root@sunny:/home/sunny/test# git add .
root@sunny:/home/sunny/test# git commit -m "test1"
[fetch/index 74b3936] test1
 1 file changed, 12 insertions(+)
 create mode 100644 test1/index2.html
root@sunny:/home/sunny/test# git checkout master
'master' 브랜치로 전환합니다
root@sunny:/home/sunny/test# git merge feature/index
merge: feature/index - 병합할 수 있는 항목이 아닙니다
root@sunny:/home/sunny/test# git merge fetch/index
업데이트 중 32b51fa..74b3936
Fast-forward
 test1/index2.html | 12 ++++++++++++
 1 file changed, 12 insertions(+)
 create mode 100644 test1/index2.html
 ```

 ```
 practice 2 결과
 root@sunny:/home/sunny/test# git branch feature/signout
root@sunny:/home/sunny/test# git checkout feature/signout
'feature/signout' 브랜치로 전환합니다
root@sunny:/home/sunny/test# git add .
root@sunny:/home/sunny/test# git commit -m "test2"
[feature/signout d9422a9] test2
 1 file changed, 12 insertions(+)
 create mode 100644 test1/index3.html
root@sunny:/home/sunny/test# git checkout master
'master' 브랜치로 전환합니다
root@sunny:/home/sunny/test# git add .
root@sunny:/home/sunny/test# git commit -m "add test2"
[master 4201b4f] add test2
 1 file changed, 12 insertions(+)
 create mode 100644 test1/index3.html
root@sunny:/home/sunny/test# git merge feature/signout
Merge made by the 'recursive' strategy.
*   b2f8553 (HEAD -> master) Merge branch 'feature/signout'
|\  
| * d9422a9 (feature/signout) test2
* | 4201b4f add test2
|/  
* 74b3936 (fetch/index) test1
* 32b51fa (test/master) test
```

```
practice 3 결과
root@sunny:/home/sunny/test# git branch a/branch
root@sunny:/home/sunny/test# git checkout a/branch
'a/branch' 브랜치로 전환합니다
root@sunny:/home/sunny/test# git add .
root@sunny:/home/sunny/test# git commit -m "test3"
[a/branch afffd48] test3
 1 file changed, 1 insertion(+), 1 deletion(-)
root@sunny:/home/sunny/test# git checkout master
'master' 브랜치로 전환합니다
root@sunny:/home/sunny/test# git add .
root@sunny:/home/sunny/test# git commit -m "test 7"
[master 5090d2e] test 7
 2 files changed, 6 insertions(+), 1 deletion(-)
 mode change 100644 => 100755 test1/index3.html
 create mode 100644 test1/index6.html
root@sunny:/home/sunny/test# git merge a/branch
자동 병합: test1/index3.html
충돌 (내용): test1/index3.html에 병합 충돌
자동 병합이 실패했습니다. 충돌을 바로잡고 결과물을 커밋하십시오.
root@sunny:/home/sunny/test# git merge a/branch
error: 병합하지 않은 파일이 있으므로, 병합할 수 없습니다.
힌트: 작업 폴더에서 문제를 바로잡은 다음, 'git add/rm <파일>'을 적절히
힌트: 사용해 해결 표시하고 커밋하십시오.
fatal: 해결하지 못한 충돌 때문에 끝납니다.
root@sunny:/home/sunny/test/test1# git add index3.html
root@sunny:/home/sunny/test/test1# git commit -m "test8"
[master c62bc5d] test8
*   c62bc5d (HEAD -> master) test8
|\  
| * afffd48 test3
* | 5090d2e test 7
|/  
*   69fd202 test3
|\  
| * 9b35591 test4
* | 2a5a0b4 test5
|/  
*   b2f8553 Merge branch 'feature/signout'
|\  
| * d9422a9 test2
* | 4201b4f add test2
|/  
* 74b3936 test1
* 32b51fa (test/master) test
```

#### stash - 임시 공간
 - 작업 중에 작업이 안료되지 않아서 커밋을 하기 애매한 상황에서 암시적으로 현재의 변경사항을 저장할 수 있는 공간이 있다!

1. 현재 작업 파일 stash로 이동
  - working directory 작업 이력을 stash로 이동시킴
  ```GIT
  $ git stash
  ```
2. working direcotry에 반영
  - 다시 작업 이력을 불러옴
  ```git
  $ git stash pop # apply + drop
  ```
  - 위의 명렁어는 아래의 두개의 명령어를 실행시키는 것과 동일 하다.
  ```Git
  $ git stash apply   # 불러오기
  $ git stash drop    # 삭제하기  
  ```
3. stash 확인
  ```git
  $ git stash list
  ```

4. 과거 시점으로 돌아가기(reset vs revert)
  1.reset
   - 특정 시점의 이력으로 되돌릴 수 있다.
   - 해쉬코드를 작성했던 시점으로 돌아감
```git
$ git reset {hashcode}
```
  - 특정 시점 - 변경사항을 Staging Area

```GIT
$ git reset --hard {hashcode}
```
  - hard를 사용하면 Working directory에 기존의 변경사항을 남겨주지 않음 (commit(이력)을 다 쌓았던 것을 다 날려버림..)

  2. revert  
    특정 시점의 이력으로 돌아갔다는 커밋과 함께 되돌릴 수 있다.
    ```
    $ git revert {commithashcode} 
    ```
