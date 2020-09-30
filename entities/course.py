from abc import ABC, abstractmethod


class CourseAbstract:
    pass


class CourseLive:
    pass


class CourseWebinar:
    pass


class CourseFactory:
    types = {
        'live': CourseLive,
        'webinar': CourseWebinar
    }

    @staticmethod
    def create_course(form_data):
        return CourseFactory.types[form_data['course_type']]()



















