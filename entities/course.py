from abc import ABC, abstractmethod

from entities.category import *
from entities.user import *


class CourseAbstract:
    pass


class CourseLive:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories


class CourseWebinar:
    pass


class CourseFactory:
    types = {
        'online': CourseWebinar,
        'offline': CourseLive,
    }

    @staticmethod
    def create_course(form_data):
        return CourseFactory.types[form_data['course_type']]()



















