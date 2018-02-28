class Animal:
    wild = False

    def set_wild(self,wild):
        self.wild = wild


class Tiger(Animal):
    def __init__(self,color,noise):
        self.color = color
        self.noise = noise
        self.set_wild(True)


class Cat(Animal):
    def __init__(self,color,noise):
        self.color = color
        self.noise = noise
        self.set_wild(False)


def permission_to_go(permission):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if permission[0] == 'forest' and args[0]:
                return func(*args,**kwargs)
            elif permission == 'city' and not args[0]:
                return func(*args, **kwargs)
            else:
                raise Exception("You don't have permission to go there")
        return wrapper
    return decorator


@permission_to_go(['forest'])
def go_to_forest(animal):
    print ("The animal will go to the wild")


@permission_to_go(['city'])
def go_to_city(animal):
    print ("The animal will go to the city")


tiger = Tiger('white','roar')
cat = Cat('black','miau')
go_to_forest(tiger.wild)
go_to_city(cat.wild)


