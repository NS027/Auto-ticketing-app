"""
This is a automatic getting ticket programm.
It is just for testing.

"""

import os
from selenium import webdriver
import time
import pickle  # to memorized the info

# main webpage
damai_url = "https://www.damai.cn/"
# login page
login_url = "https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F"
# target page ‘Jay Zhou'
target_url = "https://detail.damai.cn/item.htm?id=768159593718"


class Concert:
    """Initiating the defualt setting"""

    def __init__(self):
        self.status = 0  # for current status
        # {0: simulation for login, 1: using cookie to login}
        self.login_method = 1
        self.driver = webdriver.Chrome()

    """cookies: information for login the webpage"""

    def set_cookies(self):
        self.driver.get(login_url)
        print("###Please scan the QR code to login###")
        time.sleep(10)
        print("###Successfully Login###")
        # create the cookie.pkl
        # wb stands for binary write
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
        print("###Cookie has been saved###")
        # move to target webpage
        self.driver.get(target_url)

    """cookie.pkl has been already created"""

    def get_cookies(self):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            cookie_dict = {
                "domain": ".damai.cn",
                "name": cookie.get("name"),
                "value": cookie.get("value"),
            }
            self.driver.add_cookie(cookie_dict)
        print("###Loading cookie successful")

    """Login"""

    def login(self):
        """Simulation for login"""
        if self.login_method == 0:
            self.driver.get(login_url)
        elif self.login_method == 1:
            # if there is no cookie.pkl
            if not os.path.exists("cookies.pkl"):
                # for login
                self.set_cookies()
            else:
                self.dirver.get(target_url)
                # Using selenium to pass login info
                self.get_cookies()

    """Open browser"""

    def enter_concert(self):
        print("###Entering the webpage###")
        self.login()
        self.driver.refresh()
        self.status = 2
        print("###Successful login###")

    # Buy the ticket and add to cart
    """Selection for ticket"""

    def choose_ticket(self):
        if self.status == 2:
            print("=" * 30)
            print("### Select for the ticket and data")
            while self.driver.title.find("确认订单") == -1:
                buybotton = self.driver.find_element_by_class_name("buybtn").text
                if buybotton == "提交缺货登记":
                    self.driver.refresh()
                elif buybotton == "立即购买":
                    self.driver.find_element_by_class_name("buybtn").click()
                elif buybotton == "选座购买":
                    self.driver.find_element_by_class_name("buybtn").click()
                    self.status = 4
                else:
                    self.status = 100
                title = self.driver.title
                if title == "选座购买":
                    # execution select for seats
                    self.status = 10
                elif title == "确认订单":
                    # to buy the ticket
                    while True:
                        print("### Loading ###")
                        self.check_order()
                        break

    def check_order(self):
        print("###  Starting ordering ###")
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[2]/div[2]/div[1]/div/label'
            ).click()
        except Exception as e:
            print("### Information error ###")
            print(e)
        time.sleep(0.5)
        # 确认并下单
        self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[9]/button'
        ).click()


if __name__ == "__main__":
    con = Concert()
    con.login()
    con.choose_ticket()
    con.check_order()
