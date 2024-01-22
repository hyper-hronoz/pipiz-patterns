class Student:
    def __init__(self):
        self.name = None
        self.date_of_birth = None
        self.address = None
        self.major = None

    def __str__(self):
        return f'name: {self.name}\nbirthday: {self.date_of_birth}\n' + \
               f'address: {self.address}\nmajor: {self.major}\n' + \
               f'{"-"*10}\n'

    @staticmethod
    def new():
        return StudentBuilder()


class StudentBuilder:
    def __init__(self):
        self.student = Student()

    def build(self):
        return self.student


class StudentInfoBuilder(StudentBuilder):
    def named(self, name):
        self.student.name = name
        return self


class StudentBirthdayBuilder(StudentInfoBuilder):
    def born(self, date_of_birth):
        self.student.date_of_birth = date_of_birth
        return self


class StudentAddressBuilder(StudentBirthdayBuilder):
    def lives(self, address):
        self.student.address = address
        return self


class StudentMajorBuilder(StudentAddressBuilder):
    def study_at(self, major):
        self.student.major = major
        return self


st1 = StudentMajorBuilder()
first_student = st1\
    .named('Ivan')\
    .born('01/01/2001')\
    .lives('Kaluga')\
    .study_at('IT')\
    .build()
print(first_student)

st2 = StudentMajorBuilder()
second_student = st2\
    .named('Maria')\
    .born('02/02/2002')\
    .lives('Moscow')\
    .study_at('Languages')\
    .build()
print(second_student)

