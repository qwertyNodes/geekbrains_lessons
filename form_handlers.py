import utils
import views


class FormDistribution:
    def __call__(self, request):
        type_ = request['body']['form_type']

        if type_ in form_types.keys():
            return form_types[type_](request)


class ContactFormHandler:
    def __call__(self, request):
        data = request['body']
        form_data = {
            'email': data['email'],
            'subject': data['subject'],
            'message': data['message']
        }

        utils.save_contact_form_data(form_data)
        return views.Contact()(request, **form_data)


class CreateCategory:
    def __call__(self, request):
        data = request['body']
        form_data = {
            'category_name': data['category_name'],
            'parent_categories': data['parent_categories'],
            'category_description': data['category_description'],
            'new_added': True
        }

        utils.save_contact_form_data(form_data)
        return views.CreateCategory()(request, **form_data)


class CreateCourse:
    last_id = 1

    def __call__(self, request):
        data = request['body']
        print(data)
        form_data = {
            'course_name': data['course_name'],
            'course_description': data['course_description'],
            'teacher_select': data['teacher_select'] if 'teacher_select' in data.keys() else [],
            'course_category': data['course_category']
        }

        save_data = {
            CreateCourse.last_id: {  # unique, if already there, return error
                'name': form_data['course_name'],
                'description': form_data['course_name'],
                'categories': [],  # categories id's list
            }
        }

        utils.save_contact_form_data(form_data)
        return views.CreateCourse()(request, **form_data)


form_types = {
    'contact': ContactFormHandler(),
    'create_category': CreateCategory(),
    'create_course': CreateCourse()
}
