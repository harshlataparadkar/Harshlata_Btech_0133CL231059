class Employee:
    __salary = 50000
    def increment(self):
        self.__salary += 10000
        print(f"salary added:{self.__salary}")

    def deduct(self):
        self.__salary -= 5000
        print(f"Salary deducted:{ self.__salary}")

    def get_salary(self):
        print(f"Total Salary:{self.__salary}")
e = Employee()
e.get_salary()
e.increment()
e.deduct()

    