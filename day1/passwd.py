"""
Created on 2018/2/5
@Author: Jeff Yang
"""

import getpass

_username = "user"
_password = "1234"

username = input("username:")
# password = getpass.getpass("password:")  # 使密码不可见，但pycharm无法正常运行…
password = input("password:")

if _username == username and _password == password:
    print("Welcome user {user} login...".format(user=username))
else:
    print("Invalid username or password!")
