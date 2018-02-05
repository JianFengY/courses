"""
Created on 2018/2/5
@Author: Jeff Yang
"""

my_age = 22
for i in range(3):
    guess_age = int(input("Guess age:"))

    if guess_age == my_age:
        print("Yes, you got it!")
        break
    elif guess_age > my_age:
        print("Think smaller...")
    else:
        print("Think bigger...")
else:
    print("You have tried too many times.")