## Basic

#### 2. CSS

```
css

inline(style 뒤에 선언 하는 방법)
embed 하거나 파일에 따로 저장하는 방식도 있음

크기단위 px, em, rem

em : 해당 배수 단위... 부모 속성 폰트의 배수...
(ex 기본이 10이라면 자식은 ... 크기는 2em라고 하면 10*2 = 20px이라고 할 수 있음 )

rem은 root 폰트 기준으로 배수로함.

root가 10이고 2rem이면 20px로 설정 되옵니다.

viewport .. 상대적이 단위로 만든 것..

(w 너비 / h 높이 / min 촤소/ max 최대)

색상표현단위
HEX, RGB , RGBA
hex : #fffffff
RGB : rgb(0,0,0)
RGBA(투명도 까지 추가) : rgba(0,0,0,0.5)


Box Model
(Content(실제 내부) , Border(테두리 영역)), Padding(테두리 내부), Margin(테두리 외부) )

폰트, 공백, 위치 등을 잡을 수 있음

위치
static => 기본 위치

absolute (절대위치) => static을 제외 / 가장 가까이 있는 부모 / 조상 요소로 위치를 결정
relative
fixed(고정위치)

bootstrap4

js와 css에 해당하는 것을 html에 넣어주면 기본 구축 완료

밑의 그림은 grid와 관련된 것임

그리드(grid)는 12분할로 나눠지며, 각각 다르게 설정 가능!

```
![11](https://i.imgur.com/0NsDETR.png)
