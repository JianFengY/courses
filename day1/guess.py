"""
Created on 2018/2/5
@Author: Jeff Yang
"""

my_age = 22
count = 0
while count < 3:
    guess_age = int(input("Guess age:"))

    if guess_age == my_age:
        print("Yes, you got it!")
        break
    elif guess_age > my_age:
        print("Think smaller...")
    else:
        print("Think bigger...")
    count += 1
else:  # 循环正常执行完就执行这个else里的代码，循环break了就不执行
    print("You have tried too many times.")
