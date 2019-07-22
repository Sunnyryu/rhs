## D3JS


#### D3JS

##### Basic

- D3(Data-Driven Documents) : 데이터 중심의 문서
```
D3JS
주어진 데이터를 시각적으로 표현하는 자바스크립트 라이브러리
아이디어에 따라 다양한 그래프를 그릴 수 있다
애니메이션을 적용 가능
버튼 조작에 따라 상호작용 가능
스마트 폰이나 태블릿에서도 동작
특정 종류의 그래프 그리기 기능이 없음 – HTML의 DOM요소나 SVG 요소, Canvas 요소를 이용하여 그래프를 그리는 것
페이지 위에 표시된 요소에 대해 속성이나 좌표를 지정하여 그래프를 표시
데이터를 처리하여 어디에 그릴 것인가를 좌표나 넓이 등으로 반환하는 기능이 있음
그리기 처리에 관해서는 브라우저의 지원 여부에 따라 달라짐
그래프를 그릴 때 주로 SVG(Scalable Vector Graphics)를 사용
d3객체 – 모든 기능이 들어 있는 객체
오픈소스 - Github에서 자유롭게 받을 수 있다.
API-Reference - https://github.com/mbostock/d3/wiki/API-Reference
실시간으로 온도 변화를 반영
지도와 연동하여 어느 곳으로부터의 접속이 많은가 등을 시각적으로 표현
```

```
D3JS 기능

d3 (core)
selections / 요소 조작
Transitions / 변환, 애니메이션 등의 처리
arrays / 배열 다루기
Math / 난수와 매트릭스 계산 수행
XHR / 비동기 통신 수행/외부 파일을 읽어들임
String / 문자열 처리/ 문자열 형식 처리
CSV / CSV 데이터 경로나 형식 처리
Localization / 지역화를 수행
Colors / 색상 처리를 수행
Namespaces / 네임스페이스 처리를 수행
Interanals / 내부적인 처리를 수행

d3.scale(Scales)
Quantitative / 양적인 처리를 수행(로그 역치)
Ordinal / 서수 처리를 수행

d3.svg (SVG)
Shapes / SVG에 준비된 기본 도형의 처리를 수행
Axes / 축의 처리를 수행
Controls /브러시 제어를 수행

d3.time (Time)
Formatting / 날짜 형식 처리
Scales / 타임스케일 처리 수행
Intervals / 시간 처리를 수행
객체
기능
d3.layout (Layout)

Bundle
번들 레이아웃
Chord
코드 레이아웃
Cluster
클러스터 레이아웃
Force
역학/ 포스 레이아웃
Hierarchy
계층화 레이아웃
Histogram
도수분포표/히스토그램 레이아웃
Pack
팩 레이아웃
Partition
파티션 레이아웃
Pie
원 레이아웃
Stack
누적 레이아웃
Tree
트리 레이아웃
Treemap
트리맵 레이아웃

```
