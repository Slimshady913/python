class Person():
    def __init__(self, name):
        self.name = name
        self.money = 1000000
        
    def __del__(self): # 인스턴스가 삭제될 때 실행
        print('인스턴스가 삭제되었습니다.')
    
    def pay(self, money, Obj): # 돈 주기, 인자 : 돈과 줄 사람
        self.money -= money
        Obj.money += money
        print(f'{self.name}이 {Obj.name}에게 {money}원을 줬습니다.')

class Owner(Person):
    def __init__(self, name):
        super().__init__(name)

class Customer(Person):
    def __init__(self, name):
        super().__init__(name)
    def order(self, menu, Obj):
        Obj.order = menu
        self.order = Menu(menu)
        for x in self.order.order:
            print(f'{self.name}이 {x}을(를) {menu[x]}개 주문했습니다.')
        

class Worker(Person):
    def __init__(self, name):
        super().__init__(name)
        self.order = ''
    def delivery(self, Obj):
        print(f'{self.name}이 {Obj.name}에게 요리(주문)를 줬습니다.')

class Cook(Worker):
    def __init__(self, name):
        super().__init__(name)

class Server(Worker):
    def __init__(self, name):
        super().__init__(name)
        
class Menu():
    def __init__(self, menu):
        self.order = menu
        self.price = 0
        for x in menu:
            if x == '정식':
                self.price += menu[x]*5000
            elif x == '특식':
                self.price += menu[x]*7000
            elif x == '콜라':
                self.price += menu[x]*2000
            elif x == '사이다':
                self.price += menu[x]*2000
            else:
                print('메뉴가 없습니다.')

o = Owner('사장')
s = Server('서빙 담당')
co = Cook('요리 담당')
c1 = Customer('손님1')
c1.order({'정식':1,'사이다':1}, s)
s.delivery(co)
co.delivery(s)
s.delivery(c1)
c1.pay(c1.order.price, s)
s.pay(c1.order.price, o)

c2 = Customer('손님2')
c3 = Customer('손님3')
c2.order({'특식':2,'콜라':2}, s)
s.delivery(co)
co.delivery(s)
s.delivery(c2)
c2.pay(c2.order.price, s)
s.pay(c2.order.price, o)
o.pay(50000, s)
o.pay(50000, co)
print(f'장사를 마치고 {o.name}이 가진 잔액은 {o.money}입니다.')