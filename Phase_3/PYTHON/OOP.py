class Dog:
    def __init__(self, name, breed, age=7):
        self.name = name
        self.breed = breed
        self.age = age
        
    def get_name(self):
        return self.name

my_dog = Dog("Buddy", "Golden Retriever")
second_dog = Dog("Simba", "German Shepherd")


print(Dog.get_name(self))



