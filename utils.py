import csv
import json
import os


def get_email(request):
    return request['BODY']['email']


def get_subject(request):
    return request['BODY']['subject']


def get_message(request):
    return request['BODY']['message']


def parse_params(url_data):
    if '?' in url_data:
        url_data = url_data.split('?')[1]
    return {x[0]: x[1] for x in [x.split("=") for x in url_data.split("&")]}


def has_body(request):
    return 'CONTENT_LENGTH' in request.keys() and len(request['CONTENT_LENGTH']) > 0


def read_body(request):
    content_length = int(request['CONTENT_LENGTH'])
    return request['wsgi.input'].read(content_length).decode()


def save_contact_form_data(data):
    data_directory = 'data'
    file_name = 'contact_form.csv'
    file_path = f'{data_directory}/{file_name}'
    mode = 'a'

    if not os.path.isfile(file_path):
        mode = 'w'

    with open(file_path, mode, newline='') as fc:
        writer = csv.writer(fc, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if mode == 'w':
            writer.writerow(['email', 'subject', 'message'])

        writer.writerow([data['email'], data['subject'], data['message']])


def save_data(data):
    data_example = {
        'teachers': {
            'nickname': {
                'name': '',
                'courses': [],  # courses ids list
            }

        },
        'courses': {
            'id': {  # unique, if already there, return error
                'name': '',
                'description': '',
                'categories': [],  # categories id's list
            }
        },
        'categories': {
            'name': '',  # unique, if already there, return error
            'description': '',
            'parent_categories': [],  # categories id's list
        }
    }
    db_file = 'db.json'

    with open('data/' + db_file, 'r') as fdb:
        db_data = json.load(fdb)

    pass


def parse_form_data(form_data: list):
    params_dict = {}

    for data in form_data:
        if data[0] not in params_dict.keys():
            params_dict.update({data[0]: data[1]})
        else:
            if isinstance(params_dict[data[0]], list):
                params_dict[data[0]].append(data[1])
            else:
                t_data = params_dict[data[0]]
                params_dict[data[0]] = [t_data, data[1]]
    return params_dict


# save_data({})
