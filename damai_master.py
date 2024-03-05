"""
This is a automatic getting ticket programm.
It is just for testing.

"""

from selenium import webdriver

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
        self.driver = webdriver.Chrome(executable_path="")

    """Login"""
