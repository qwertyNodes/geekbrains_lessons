class User:
    id_ = 1


class Teacher(User):
    def __init__(self, name):
        self.id = User.id_
        self.name = name

        User.id_ += 1


class Student(User):
    def __init__(self, name):
        self.id = User.id_
        self.name = name

        User.id_ += 1


class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher,
    }

    @classmethod
    def create_user(cls, name, type_):
        return cls.types[type_](name)


class Course:
    # def __init__(self, name, type_, category, level, address=None):
    #     self.name = name
    #     self.type = type_
    #     self.name = address
    #     self.category = category
    #     self.level = level
    pass


class CourseWebinar(Course):
    def __init__(self, name, category, address):
        self.name = name
        self.category = category
        self.address = address


class CourseLive(Course):
    def __init__(self, name, category, link):
        self.name = name
        self.link = link
        self.category = category


class CourseAbstractFactory:
    types = {
        'webinar': CourseWebinar,
        'live': CourseWebinar,
    }


class Category:
    categories_count = 1

    def __init__(self, name):
        self.id = Category.categories_count
        self.name = name
        self.courses = []

        Category.categories_count += 1


class UserAbstractFactory:
    pass


class TrainingSite:
    def __init__(self):
        self.courses = []
        self.teachers = []
        self.categories = []
        self.students = []

    def create_user(self, type_):
        pass

    def create_category(self, name, category=None):
        pass

    def find_category_by_id(self, id_):
        pass














