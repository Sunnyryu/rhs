class Person:
    def greeting(self):
        print('안녕하세요.')
 
class University:
    def manage_credit(self):
        print('학점 관리')
 
class Undergraduate(Person, University):
    def study(self):
        print('공부하기')
 
sunny = Undergraduate()
sunny.greeting()         # 안녕하세요.: 기반 클래스 Person의 메서드 호출
sunny.manage_credit()    # 학점 관리: 기반 클래스 University의 메서드 호출
sunny.study()            # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드
