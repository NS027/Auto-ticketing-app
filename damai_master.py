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
        self.login_method = 1  # {0: simulation for login, 1: using cookie to login}
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
                'domain': '.damai.cn',
                'name': cookie.get('name'),
                'value': cookie.get('value')
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


if __name__ == "__main__":
    con = Concert()
    con.login()
