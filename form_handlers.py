import json

import views


def dist(request):
    form_type = request['BODY']['form_type']
    pass


def contact(request):
    params = {
        'email': request['BODY']['email'][0],
        'subject': request['BODY']['subject'][0]
    }
    print('Message was sent successful!')
    print('Email:\n{}\n'.format(params['email']))
    print('subject:\n{}\n'.format(params['subject']))
    print('Message:\n{}'.format(request['BODY']['message'][0]))
    return views.contact(request, **params)
