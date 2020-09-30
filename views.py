from collections import namedtuple

from jinja2 import FileSystemLoader
from jinja2.environment import Environment
import os


TEMPLATES_FOLDER = 'templates/'


def render(template_name, folder='templates', **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)

    css_path = folder + '/css'
    css = ''

    for file in os.listdir(folder + '/css'):
        with open(css_path + '/' + file) as fc:
            css += fc.read()

    kwargs.update({'css': css})

    return template.render(**kwargs)


class About:
    def __call__(self, *args, **kwargs):
        kwargs.update({'page_title': 'About page'})

        return '200 OK', render('about.html', **kwargs)


class Index:
    def __call__(self, *args, **kwargs):
        kwargs.update({'page_title': 'Index page'})

        return '200 OK', render('index.html', **kwargs)


class Contact:
    def __call__(self, *args, **kwargs):
        kwargs.update({'page_title': 'Contact us'})

        return '200 OK', render('contact.html', **kwargs)


class Error404:
    def __call__(self, *args, **kwargs):
        kwargs.update({'page_title': '404 not found'})

        return '404 ERROR', render('404.html', **kwargs)


class CreateCategory:
    def __call__(self, *args, **kwargs):
        """
        :param kwargs:
            all_categories - for parent categories list
            category_name - to show created category name
        """
        kwargs.update({'page_title': 'Create category'})

        return '200 OK', render('create_category.html', **kwargs)


class CreateCourse:
    def __call__(self, *args, **kwargs):
        """
        :param kwargs:
            all_categories - to choose category for the course
            course_name - to show created course name
            teachers - to choose teacher(s) for the course
        """
        Category = namedtuple('Category', 'name')

        categories = []
        for i in range(10):
            categories.append(Category('Category {}'.format(i)))

        kwargs.update({'page_title': 'Create course'})
        kwargs.update({'all_categories': categories})

        return '200 OK', render('create_course.html', **kwargs)


class CreateUser:
    def __call__(self, *args, **kwargs):
        """
        :param kwargs:
            user_name - to show created user's name
            nickname - to show created user's nickname
            user_type - to show what user type was created
        """
        kwargs.update({'page_title': 'Create user'})

        return '200 OK', render('create_user.html', **kwargs)


class CategoriesList:
    def __call__(self, *args, **kwargs):
        kwargs.update({'page_title': 'Categories list'})

        return '200 OK', render('categories_list.html', **kwargs)


class CoursesList:
    def __call__(self, *args, **kwargs):
        kwargs.update({'page_title': 'Courses list'})

        return '200 OK', render('courses_list.html', **kwargs)


class UsersList:
    def __call__(self, *args, **kwargs):
        kwargs.update({'page_title': 'Users list'})

        return '200 OK', render('categories_list.html', **kwargs)
