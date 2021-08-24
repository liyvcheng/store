from threading import Thread
import time

# wallet = 3000
basket = 0              #篮子
class production(Thread):
    chef = ""           #厨师

    def run(self) -> None:
        global basket
        while True:
            if basket < 500:
                basket = basket + 1
                print("厨师",self.chef,"成功造了一个面包，总共造了",basket,"个面包")

            else:
                time.sleep(2)
                break


class production1(Thread):
    client = ""  # 客户
    # basket = 0  # 篮子
    wallet = 3000

    def run(self) -> None:

        global basket
        while True:
            if int(self.wallet) > 0:
                if basket <= 500:
                    basket = basket + 1
                    self.wallet = self.wallet - 3
                    print("顾客",self.client,"成功购买面包！",self.client,"还剩",self.wallet,"元")
                else:
                    time.sleep(2)
            elif int(self.wallet) == 0:
                print("顾客",self.client,"没钱了")
                break

p1 = production()
p2 = production()
p3 = production()
p1.chef = "c3"
p2.chef = "c2"
p3.chef = "c1"

p1.start()
p2.start()
p3.start()

p4 = production1()
p5 = production1()
p6 = production1()
p7 = production1()
p8 = production1()
p9 = production1()
p4.client = "cl1"
p5.client = "cl2"
p6.client = "cl3"
p7.client = "cl4"
p8.client = "cl5"
p9.client = "cl6"

p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p9.start()