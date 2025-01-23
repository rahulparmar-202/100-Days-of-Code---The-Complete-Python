
# *args & **kwargs :- names can be different but asterisk(*) is important

# *args :- used for Unlimited Positional Argument

def add(*args):
    sum_n = 0
    for n in args:
        sum_n += n
    return sum_n

print(add(2,3,5))


def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]  # 2 + 3 = 5 = n
    n *= kwargs["multiply"] # 5 * 5 = 25 = n
    print(n)


calculate(2,add=3, multiply=5)


class Car:

    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw.get("color")
        self.seat = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline GTR 35")
print(my_car.make, my_car.model)