## dict

```
for 변수 in 딕셔너리:              # 모든 키를 꺼내옴
    반복할 코드
 
for 키, 값 in 딕셔너리.items():    # 모든 키와 값을 꺼내옴
    반복할 코드
 
for 키 in 딕셔너리.keys():         # 모든 키를 꺼내옴
    반복할 코드
 
for 값 in 딕셔너리.values():       # 모든 값을 꺼내옴
    반복할 코드
```

```
{키: 값 for 키, 값 in 딕셔너리}
{key: value for key, value in dict.fromkeys(['a', 'b', 'c', 'd']).items()}
dict({키: 값 for 키, 값 in 딕셔너리})
 
{키: 값 for 키, 값 in 딕셔너리 if 조건식}
{key: value for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items() if value != 20}
dict({키: 값 for 키, 값 in 딕셔너리 if 조건식})

```

## set

```
세트 = {값1, 값2, 값3}        # 세트 만들기
세트 = set(반복가능한객체)    # 세트 만들기
 
값 in 세트        # 세트에 특정 값이 있는지 확인
값 not in 세트    # 세트에 특정 값이 없는지 확인
 
len(세트)    # 세트의 요소 개수(길이) 구하기
```

```
for 변수 in 세트:
    반복할 코드

{식 for 변수 in 반복가능한값}

{i for i in 'apple'}

set(식 for 변수 in 반복가능한값)

{식 for 변수 in 세트 if 조건식}

{i for i in 'pineapple' if i not in 'apl'}

set(식 for 변수 in 세트 if 조건식)
```
