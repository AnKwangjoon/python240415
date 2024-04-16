class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def printInfo(self):
        print("ID:", self.id)
        print("Name:", self.name)


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        super().printInfo()
        print("Title:", self.title)


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        super().printInfo()
        print("Skill:", self.skill)


# 테스트 코드
# Person 클래스 테스트
print("Person 클래스 테스트")
person1 = Person(1, "John")
person1.printInfo()
print()

# Manager 클래스 테스트
print("Manager 클래스 테스트")
manager1 = Manager(2, "Jane", "Senior Manager")
manager1.printInfo()
print()

# Employee 클래스 테스트
print("Employee 클래스 테스트")
employee1 = Employee(3, "Alice", "Python")
employee1.printInfo()
print()

# 추가 테스트
print("추가 테스트")
# Manager 클래스 테스트
manager2 = Manager(4, "Tom", "Project Manager")
manager2.printInfo()
print()

# Employee 클래스 테스트
employee2 = Employee(5, "Bob", "Java")
employee2.printInfo()
print()

# 더 많은 테스트
print("더 많은 테스트")
person3 = Person(6, "Emma")
person3.printInfo()
print()

manager3 = Manager(7, "Mary", "Senior Director")
manager3.printInfo()
print()

employee3 = Employee(8, "David", "C++")
employee3.printInfo()
print()

person4 = Person(9, "Eva")
person4.printInfo()
print()

manager4 = Manager(10, "Michael", "Director")
manager4.printInfo()
