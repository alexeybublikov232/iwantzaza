#Створення класу
# class Student:
#    print("Hi")

#Створемо екземпляр класу
# class Student:
#    print("Hi")
#
# first_student = Student()


#конструктор класу автоматично викликається під час створення екземпляра.
# class Student:
#    print("Hi")
#    def __init__(self):
#        self.height = 160
#        print("I am alive!")
#
# first_student = Student()

#self - посилання на самого себе
# class Student:
#    def __init__(self):
#        self.height = 160
#        print(self)
#
# first_student = Student()


#аналогічний виклик, але з використанням класу
# class Student:
#    def __init__(self):
#        self.height = 160
#        print(self)
#
# first_student = Student()
# Student.__init__(self=first_student)


#Отримаємо доступ до параметра
# class Student:
#    def __init__(self):
#        self.height = 160
#
# nick = Student()
# print(nick.height)

#в конструктор класу потрапляють початкові параметри,
# які передаються під час створення екземпляра
# class Student:
#    def __init__(self, height=160):
#        self.height = height
#
# nick = Student()
# kate = Student(height=170)
# print(nick.height)
# print(kate.height)

#створення атрибуту класу, який змінюватиметься
# відповідно до кількості оголошених екземплярів
# class Student:
#    amount_of_students = 0
#    def __init__(self, height=160):
#        self.height = height
#        Student.amount_of_students += 1
#
# nick = Student ()
# kate = Student(height=170)
# ann = Student()
# print(ann.amount_of_students)
# print(Student.amount_of_students)

#Оскільки об’єкт та екземпляр взаємопов’язані,
# то атрибут класу можна дістати з допомогою self
# class Student:
#    height = 160
#    def __init__(self):
#        print(self.height)
#
# nick = Student()

#зробимо так, щоби кожен наступний студент ставав вищим
# class Student:
#    height = 160
#    def __init__(self):
#        print(self.height)
#        self.height+=10
#
# nick = Student()
# kate = Student()
#Щось пішло не так :)
#якщо потрібно змінювати атрибут класу,
# звертатися до нього треба через сам клас


# Атрибути об’єкта перекривають собою атрибути класу
# class Student:
#    height = 160
#    def __init__(self):
#        self.height = 170
#
#    def printer(self):
#        print(self.height)
#
# nick = Student()
# nick.printer()


#Області видимості класів аналогічні таким у функціях.
# x = 10
# class Looker:
#    x = 15
#    print(x)
#    def func1(self):
#        x = 20
#        print(x)
#        def func2():
#            x = 30
#            print(x)
#        func2()
# some_object = Looker()
# some_object.func1()



#Методи класів

#додамо метод grow(), що збільшуватиме зріст студента та викличемо його
# class Student:
#    amount_of_students = 0
#    def __init__(self, height=160):
#        self.height = height
#        Student.amount_of_students+=1
#    def grow(self, height=1):
#        self.height+=height
#
# nick = Student()
# kate = Student(height=170)
# kate.grow()
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)

'''
щоби під час видруковування об’єкту не отриму-
вати рядок із незрозумілим вмістом, можна оголосити
метод __str__(), який має повертати рядок відповід-
ного змісту
'''
# class Student:
#    def __init__(self, name=None):
#        self.name = name
#    def __str__(self):
#        return f"I am a student. My name is {self.name}."
#
# nick = Student(name = "Nick")
# print(nick)


#видалити об’єкт дає змогу метод __del__(),
# який автоматично запускається наприкінці програми
# class Student:
#    def __init__(self, name=None):
#        self.name = name
#    def __del__(self):
#        print("Training is over. I am now an expert!")
#
# nick = Student()


'''
Іноді є завдання перевірити істинність об’єк-
ту або його довжину. Тоді стануть у пригоді методи
__bool__ () та __len__()
'''
# class Student:
#    def __init__(self, name=None, height=160):
#        self.name = name
#        self.height = height
#    def __bool__(self):
#        return self.name != None
#    def __len__(self):
#        return self.height
#
# nick = Student()
# #nick = Student(name="Nick", height=170)
# print(nick.__len__())
# print(nick.__bool__())
# print(len(nick))
# print(bool(nick))
#


#Симулятор студента

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.loneliness = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.loneliness -= 0.6

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.loneliness += 0.2

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.loneliness += 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.loneliness <= 5:
            print("Died alone at home")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Loneliness ={self.loneliness}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")

        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day+1)
