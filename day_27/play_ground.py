def add(*args):
    # the data type for arg is tuple
    print(args[2])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5, 6))

def calculate(n, **kwargs):
    # kwargs or keyword arguments as dictionaries as it's data type
    # an arg n can be added
    print(kwargs)
    # for key, value in kwargs.items():
        # print(key)
        # print(value)
        # print(kwargs["add"])
    n += kwargs["add"]
    n -= kwargs["subtract"]
    print(n)


calculate(3, add=2, subtract=4)


class Car():

    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        # But the best option is to use get function because it returns a None
        # when the keyword doesn't exit in the dictionary rather than an error
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.num_of_seats = kw.get("seats")



my_car = Car(make="Toyota", model="2010")

print(my_car.make)
print(my_car.num_of_seats)