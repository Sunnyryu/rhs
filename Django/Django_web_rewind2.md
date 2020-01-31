## Django 

#### Web 2

```
클래스형 제네릭 뷰

Base view : 뷰 클래스를 생성하고 다른 제네릭 뷰의 부모 클래스를 제공하는 기본 제네릭 뷰
Generic Display View : 객체의 리스트를 보여주거나 특정 객체의 상세 정보를 보여줌
Generic Edit View : 폼을 통해 객체를 생성 수정 삭제하는 기능을 제공 !
Generic Date View : 날짜 기반 객체의 연/월/일 페이지로 구분해서 보여줌 !!

Base View 

- View => 가장 기본이 되는 최상위 제네릭 뷰
- Templateview => 템플릿이 주어지면 해당 템플릿을 랜더링 해줌
- RedirectView => URL이 주어지면 해당 URL로 리다이렉트 시켜줌

Generic Display View 
- ListView => 조건에 맞는 여러 개의 객체를 보여줌 
- DetailView => 객체 하나에 대한 상세한 정보를 보여줌 !

Generic Edit View 
- FormView => 폼이 주어지면 해당 폼을 보여줌 
- CreateView => 객체를 생성하는 폼을 보여줌 
- UpdateView => 기존 객체를 수정하는 폼을 보여줌 
- DeleteView => 기존 객체를 삭제하는 폼을 보여줌

Generic Date View
- ArchiveindexView => 조건에 맞는 여러 개의 객체 및 그 객체들에 대한 날짜 정보를 보여줌 
- YearArchiveView => 연도가 주어짐녀 그 연도에 해당하는 객체들을 보여줌 
- MonthArchiveView => 연, 월이 주어지면 그에 해당하는 객체드르을 보여줌 ! 
- WeekArchiveView => 연도와 주차가 주어지면 그에 해당하는 객체들을 보여줌 !!
- DayArchiveView => 연, 월, 일이 주어지면 그 날짜에 해당하는 객체들을 보여줌 
- TodayArchiveView => 오늘 날짜에 해당하는 객체들을 보여줌 
- DateDetailView => 연, 월, 일 기본키가 주어지면 그에 해당하는 특정 객체 하나에 대한 상세한 정보 보여줌 !

클래스형 뷰에서 폼처리 
최초의 get => 사용자에게 처음으로 폼을 보여줌
유효한 데이터를 가진 post => 데이터를 처리함, 주로 리다이렉트 처리
유효하지 않은 데이터를 가진 POST => 보통은 에러 메세지와 함께 폼이 다시 출력됨 ! 

함수형 뷰의 경우 if, else문을 사용해야하며, 클래스형 뷰는 class 선언후 get과 post를 각각 만들어줘야 하지만,
제네릭 뷰로 폼을 처리 할 때에는 get,post의 메소드 정의가 불필요하게 됨 !

form_class => 사용자에 보여줄 폼을 정의한 forms.py 파일 내 클래스명 
template_name => 폼을 포함하여 렌더링할 템플릿 파일 이름 
success_url => 폼뷰 처리가 정상적으로 완료되었을 때 리다이렉트 시킬 URL
form_valid() 함수: 유효한 폼 데이터로 처리할 로직 코딩, super() 함수를 사용하면 success_url로 지정된 URL로 리다이렉션 처리함! 


