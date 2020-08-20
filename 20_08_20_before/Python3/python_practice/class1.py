class Cclass(object): # 예약어 class, 클래스 이름 Cclass, 상속 클래스 object 추가
    
    def __init__(self, name): # 객체 생성 후 초기화 함수로 객체의 속성 추가
        self.name = name
    
    def getName(self): # 객체의 속성 조회
        return self.name

c = Cclass("객체 생성")

c.name # 객체의 속성에 직접 이름으로 접근 가능

c.getName() # 메소드를 사용해 객체의 속성 조회 가능!

isinstance(c, Cclass) # 클래스와 객체의 생성관계를 내장함수 isinstance로 확인 ! 

Cclass.__dict__

Cclass.__init__

Cclass.__init__(c, "함수로 갱신")

c.name

c.__init__

c.__init__("메소드로 갱신")

c.name


