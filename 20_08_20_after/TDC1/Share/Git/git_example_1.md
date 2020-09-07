## git Collaboration

#### git collaboration example 1
```
깃 기본 협업 예시

3명이 한다는 과정으로 작성하였습니다.
(A => repository 생성자 / B,C => collaborator)

1. A는 깃을 만들고 B,C를 collaborator로 초대하며,
기본적인 파일을 준비합니다. (파이썬의 경우 pip 관련 txt 파일, 기본적인 구성)

git init // 그 후에 git init을 하여 git 저장소를 만듭니다.
git add . // git에 추가를 합니다.
git commit -m "project start" // 깃에 커밋하여 메세지를 등록 
git push (origin master) // 푸쉬하여 올립니다.

2. B,C는 git clone을 이용해서 해당 파일을 가져옵니다. 

3. A,B,C는 브랜치를 각각 만들어서 프로젝트 준비를 합니다.
git branch tdcA
git branch tdcB
git branch tdcC

깃헙 공유 / 독립적인 로컬 repository를 갖고 있음 .. 
기능이나 페이지를 끝낼 때 깃헙에 브랜치 작업본 푸쉬해야함..
(병합이 필요할 때는 master 브랜치에 merge를 함 - 주기적으로 머지를 추천!( merge issue(conflict)의 대처를 위해))

4. C가 기능이나 페이지를 마치고 master에 병합을 합니다.

git add 
git commit -m "page finish"

git checkout master // master로 전환
git merge tdcC
git push origin master 

C는 깃헙 MASTER에 push 하기전에 자신의 브랜치에 git add & git commit을 진행하고 tdcC(자신의 브랜치)를 local repository에 있는 master 브랜치에 merge를 하고 push를 합니다.

＊ master 브렌치는 관리만 한다는 것으로 생각하고 최신코드를 push하고 pull하는 용도로 사용하는 것이 좋을 거 같음!!

5. A,B는 C가 수정한 최신판을 사용하기 위해서 master 브랜치를 pull하고 A,B는 pull 할 때 master 브랜치로 이동한 후 pull 해야 함! (브랜치 이동 시 작업을 마무리 짓고 commit 해야함!)

git checkout master // master로 전환
git pull origin master // github에 있는 git에서 최신판을 가져옴

git checkout tdcA // tdcA로 전환
git merge master // master 브랜치를 병합함!

＊ 이 떄 충돌이 일어날 수 있으니 주의를 바랍니다. (밑에 따로 작성할 예정)
6. bug 발생할 시 대처법

B가 테스트 도중 버그가 발생하여 이전 버전으로 돌아가야 하는 상황이 발생하였음 
B가 push를 하여 github에도 올라갔으면 revert를 사용해야 합니다.
(revert는 특정 버전으로 되돌아가며 되돌린 버전 이후의 버전들의 commit 이력은 남아있음)

github에서 커밋현황을 보거나 git log --online -10 (number)를 이용하여 로그 확인

git revert commit(number) => 해당 버전의 커밋번호를 복사하여 revert 명령어 실행 
-> 충돌발생한 것을 확인 가능! / 돌아가려는 버전 이후에 했던 부분을 제거합니다.

git add .
git commit -m "이전 버전으로 백업"
git push origin tdcB 
(이력을 남기느 것이 좋음 )
```

#### git collaboration solve problem
```
1. merge issue(conflicts)

위의 예시에서 머지 충돌이 일어났을 때에 해결방법입니다.

1.1. Fast-forword 방식으로 통합

master 브랜치 작업
git checkout master // 마스터로 전환
git add . // 깃 추가
git coomit -m "page finish" 

새로운 브랜치 생성해서 작업
git checkout -b example1
git branch

git add .
git commit -m "example1 finish"

깃 merge

git checkout master
git merge example1

(Fast-forward는 merge 할 브랜치의 커밋이 현재 branch의 commit보다 앞서 있기에 기존 브랜치의 커밋을 대상 브랜치 커밋으로 이동할 것이라는 것임 )


1.2. 충돌이 발생하는 병합

master 브랜치 작업
git add .
git commit -m "master file revise"
(example 1 브랜치보다 master 브랜치의 버전이 더 최신이 됌)

example1 브랜치 작업
git add .
git commit -m "master fiel revise"
master = example1 브랜치의 커밋 수가 같음

git merge
git checkout master
git merge example1

(작업내용이 같다면 충돌이 일어날 수 있기에 충돌이 일어나면 함께 해결하는 것이 좋을 뜻...)

1.3. 옵션

--squash (대상브랜치 병합 시, 커밋 이력을 모두 제거하고 작업된 내용만 병합) => 대상 브랜치에서 작업했던 히스토리를 하나의 메시지로 압축시키는 것!

--no-ff (fast-forword 관계에서 merge 시 merge 커밋 생략 -> --no-ff 옵션시 merge 할 때 커밋 생성)

2. bug 발생시 reset vs revert

reset은 특정 커밋으로 되돌아 갈수 있고 되돌린 버전 이후의 버전은 히스토리에서 삭제 
revert는 위의 부분을 참조

reset은 commit(number):특정 버전으로 되돌리지만 이력 삭제 / 파일내용은 유지, --hard {commit(number)}: 파일 내용까지 되돌림 , --soft{commit(number)}: 파일 내용은 그대로 유지하면서 staging area에 올림(add상태로!), -merge ORIG_HEAD : 바로 이전 병합 취소

revert는 {commit(number)}: 특정버전으로 될리는데 파일내용 유지, 되돌린 버전 이후의 모든 commit 이력 보존, --mainline number : 과거 병합을 취소, 숫자로 명시된 브랜치 라인을 기준으로 되돌아감!

추가로 git checkout -- {file} working directory에서 수정한 특정 파일을 현재버전으로 되돌릴 수 있음(git add 이전) 
2.1 되돌리기(작업 디렉토리 비우기!)

git add 
git commit -m "page finish"
git checkout -- {file}

모든 파일을 되돌리고 싶다면 git checkout . 명렁어 실행 / 폴더라면 git checkout { 폴더명}임!

2.2. rest 이용 
2.2.1 add 무효화

git add .
git status
git reset {filename}
git status
(add 이전 상태로 되돌림!)

2.2.2 버전 되돌리기

git add와 commit을 5번 반복했다고 했을 때

--hard 옵션 

git log --oneline -5 (5개의 깃 내역을 확인)

git reset --hard {versionname} => 위에서 깃내역을 확인해서 버전명을 확인하여 작성

옵션이 없다면 git reset {versionname}

--soft 옵션

git reset --soft{versionname} / add까지 된 staging area까지 적용되는 상태를 --soft 옵션을 추가해서 reset

2.3 revert 

git revert {versionname}
(커밋 이력이 남기에 같은 곳을 수정했다면 충돌이 발생하기에 위의 6번 예시처럼 하면 됩니다.)

2.4 reset으로 병합취소

git reset --merge ORIG_HEAD // 병합을 한 후에 바로 병합을 취소해야 할 떄 // ORIG_HEAD는 최신 커밋에 포인터를 지정함!

2.5 revert로 병합 취소 

조금 시간이 지난 병합을 취소시 revert 명령어로 병합을 취소 // 만약에 rebase 병합 시 merge의 커밋이력이 남지 않아 불가능함!!

git revert --mainline 1 {취소할 병합 commitID}

2.6 rebase 병합한 경우 

merge로 이루어진 것이 아니라 rebase를 통해 이뤄졌다면, 협업을 통해 커밋을 찾아 과거의 버전으로 되돌림

git checkout { 커밋ID }
```