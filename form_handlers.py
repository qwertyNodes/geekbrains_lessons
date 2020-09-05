import utils
import views


def distrib(request):
    type = request['body']['form_type']

    if type in form_types.keys():
        return form_types[type](request)


def contact(request):
    form_data = {
        'email': request['body']['email'],
        'subject': request['body']['subject'],
        'message': request['body']['message']
    }
    utils.save_form_data(form_data)
    return views.contact(request, **form_data)


form_types = {
    'contact': contact
}
