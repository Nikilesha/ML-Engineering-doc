from abc import ABC, abstractmethod


# Create a Person class with attributes name and age. Create two objects and print their data.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person(name="Nick", age=20)

print(person1.name)
print(person1.age)


# Create a Movie class with attributes like title, director, and year. Use a method to display the details.


class Movie:
    def __init__(self, title, director, year, success):
        self.title = title
        self.director = director
        self.year = year
        self.success = success

    def disp(self):
        print(self.title)
        print(self.director)
        print(self.year)
        print(self.success)


movie = Movie("Mersal", "Atlee", 2016, "yes")
movie.disp()


# Create a BankAccount class with:Public name Protected _balance Private __pin Implement deposit, withdraw, and balance check using proper encapsulation.


class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self._balance = balance
        self.__pin = pin

    def return_pin(self):
        return self.__pin

    def check_pin(self, user_pin):
        self.user_pin = user_pin
        if self.__pin == user_pin:
            return True
        else:
            return False

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        self._amount = amount
        self._balance += self._amount
        return f"new balance is{self._balance}"

    def withdraw(self, amount):
        self._amount = amount
        self._balance -= self._amount
        return f"new balance is{self._balance}"


user = BankAccount("Nikilesha", 5000, 1234)
on = True
print()
print("-----Welcome to bank-----")
pin = int(input("Enter pin: "))
if type(pin) == int and pin == user.return_pin():
    while on:
        print()
        print(f"Welcome Nikilesha")
        print("-----What you want to do: -------")
        print(f"\t1.balance enquiry")
        print(f"\t2.deposit amount")
        print(f"\t3.withdraw amount")
        print(f"\t4.Exit")
        choice = int(input("Enter the number of choice: "))

        if choice == 1:

            print("Your balance is: ", user.check_balance())
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount > user._balance:
                print("Insufficient Balance")
            else:
                user.withdraw(amount)

        elif choice == 4:
            on = False
            print("Thank you")
else:
    print("Enter the correct pin")
    print("Transaction declined")


# Real life university course management project


class Users:
    data = {}

    def __init__(self, name, password):
        self._name = name
        self._password = password

    @abstractmethod
    def getUserData(self):
        pass


class Student(Users):
    def __init__(self, name, password, student_id, grades):
        super().__init__(name, password)
        self.__student_id = student_id
        self._grades = grades

    def getUserData(self):
        data = {
            "name": self._name,
            "password": self._password,
            "student_id": self.__student_id,
            "grades": self._grades,
        }
        return data


class Professors(Users):
    def __init__(self, name, password, prof_id, salary):
        super().__init__(name, password)
        self.__prof_id = prof_id
        self.__salary = salary

    def getUserData(self):
        data = {
            "name": self._name,
            "password": self._password,
            "prof id": self.__prof_id,
            "salary": self.__salary,
        }
        return data


class Department:
    def __init__(self, department_name, department_head):
        self.department_name = department_name
        self.department_head = department_head


class Course(Department):
    def __init__(
        self,
        department_name,
        department_head,
        course_name,
        course_id,
        enrolled_students,
    ):
        super().__init__(department_name, department_head)
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = enrolled_students


if __name__ == "__main__":
    student1 = Student("Nikilesha", 132012, "S001", {"Mahts": 95, "CS": 98})
    print("Student data: ", student1.getUserData())

    prof1 = Professors("Dr. Ravi", "teach2001", "p1001", "9000")
    print(f"Professor data: {prof1.getUserData()}")
