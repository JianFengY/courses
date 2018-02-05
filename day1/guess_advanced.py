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
    if count == 3:
        continue_comfirm = input("Do you want to keep guessing?(Enter 'n' to quit.)")
        if continue_comfirm != 'n':
            count = 0
# else:  # 循环正常执行完就执行这个else里的代码，循环break了就不执行
#     print("You have tried too many times.")
