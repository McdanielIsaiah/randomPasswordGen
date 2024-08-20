import random
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
car = ["?", "!", "#", "$", "%", "*"]
fillerlist = []
def gen(runnum):
    global alapha
    global fillerlist
    global nums
    global car
    for i in range(0, runnum - 2):
        rando = random.randint(1, 26)
        fillerlist.append(alpha[rando - 1])
        password = "".join(fillerlist)

    randonum = random.randint(1, 10)
    fillerlist.append(nums[randonum - 1])

    randospc = random.randint(1, 6)
    fillerlist.append(car[randospc - 1])

    password = "".join(fillerlist)
    print(password.capitalize())

numlength = int(input("How long do you want your password? "))
gen(numlength)

