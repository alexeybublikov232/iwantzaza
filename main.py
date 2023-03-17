# class Dog:
#     def __init__(self, years=1):
#         self.age = years
# rex = Dog()
# print(rex.age)
# gav = Dog(years=6)
# print(gav.age)
#
# class Student:
#    height = 160
#    def __init__(self):
#        Student.height+=10
#        #self.height = 170
#
#    def printer(self):
#        print(self.height)
#
# nick = Student()
# nick.printer()
# ann = Student()
# ann.printer()
#
# class Chelovek:
#     def __init__(self, iq=99):
#         self.mozg = iq
# slavik = Chelovek()
# print(slavik.mozg)
# slavik.mozg = 101
# print(slavik.mozg)

class Car:
    def __init__(self, color = None):
        self.brand = input("Введите марку машины: ")
        self.color = color
        self.engine = input("Введите тип двигателя машины: ")

    def drive(self):
        print("DRIVE")

    def __str__(self):
        return f"Бренд: {self.brand} color: {self.color} engine: {self.engine}"

mashina = Car(color="black")
print(mashina)
mashina.drive()



