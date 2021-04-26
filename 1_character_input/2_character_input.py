def you_are_100_in_year():
    name = input("What is your name?")
    age = int(input("What is your age?"))
    remain_till_100 = 100 - age
    year_in_100 = remain_till_100 + 2021
    print('Dear, %s you will be 100 years in Year %s' % (name, year_in_100))
    

you_are_100_in_year()
