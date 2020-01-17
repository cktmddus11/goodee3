'''
Created on 2020. 1. 17.

@author: GDJ_19
상속 예제, 오버라이딩, 
다중 상속 가능 => 자손 클래스의 부모 클래스가 여러개 가능 
'''
class Car:
    speed = 0
   # room = 3 다중상속에 위험성 : 동일한것이 있으면 어떤걸로 나올지 모름 
    def upSpeed(self, value):
        self.speed += value
        print("현재 속도(부모 클래스) : %d " %self.speed)

class Sedan(Car): #   상속 표현 - 단일 상속 => 자식 입장에서 부모가 하나
    pass # 추가되는 멤버 없는 경우

class Truck(Car):
    def upSpeed(self, value): # 오버라이딩
        self.speed += value
        if self.speed > 150:
            self.speed = 150
        print("현재 속도(자손 클래스) : %d" % self.speed)
        
class Container:
    room = 1

class MovingCar (Car, Container):  # 다중 상속
        pass
        
sedan1, truck1, mcar = None, None, None
truck1 = Truck()
sedan1 = Sedan()
mcar = MovingCar()
print("이동차량의 방 갯수 : ", mcar.room, ",  ", end="")
mcar.upSpeed(60)

print("트럭 => ", end="")
truck1.upSpeed(200)
print("승용차 =>", end="")
sedan1.upSpeed(200)



