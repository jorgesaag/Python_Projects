def calculations(rate, contribution, balance):
    earnings = balance * rate
    additions = earnings + contribution
    return additions

def calculateRetirement(start_age, initial, working, retired):
    age = start_age
    years = int(start_age / 12)
    months = int(((age / 12) - years) * 12)
    balance = initial
    while age < (start_age + working[0]):
        for i in range(0, working[0]):
            print('Age {:3d} month {:2d} you have ${: .2f}'.format(years, months, balance))
            balance += calculations(working[2], working[1], balance)
            months += 1
            age += 1
            if months == 12:
                months = 0
                years += 1
            else:
                pass
    else:
        for x in range(0, retired[0]):
            print('Age {:3d} month {:2d} you have ${: .2f}'.format(years, months, balance))
            balance += calculations(retired[2], retired[1], balance)
            months += 1
            age += 1
            if months == 12:
                months = 0
                years += 1
            else:
                pass


if __name__ == "__main__":
    calculateRetirement(327, 21345, (489, 1000, (4.5 / 12 /100)), (384, -4000, (1 / 12 / 100)))