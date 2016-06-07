import random
"""
list=[]

for each in range(1,46):
    list.append(each)
"""
user_input=int(input("How many quick picks? \n >>>"))


for each in range(user_input):
    list=[]
    for each in range(6):
        while True:
            quick_picks = random.randint(1,45)
            if quick_picks in list:
                continue
            else:
                list.append(quick_picks)
                break
    print("{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d}" .format(list[0],list[1],list[2],list[3],list[4],list[5]))

