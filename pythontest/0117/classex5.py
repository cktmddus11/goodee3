'''
Created on 2020. 1. 17.

@author: GDJ_19
추상 메서드 예제
'''

class SuperClass:
    # 추상 메서드
    def method(self):
        raise NotImplementedError #반드시 오버라이딩 해야함
                                                #  추상 메서드
class SubClass1(SuperClass):
    def method(self):
        print("SubClass1 에서 method() 를 오버라이딩 함")

class SubClass2(SuperClass):
    #pass
    def method(self):
        print("SubClass2 에서 method()를 오버라이딩 함")

sub1 = SubClass1()
sub2 = SubClass2()

sub1.method()
sub2.method()