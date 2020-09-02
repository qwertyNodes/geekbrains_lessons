def get_email(request):
    return request['BODY']['email'][0]


def get_subject(request):
    return request['BODY']['subject'][0]


def get_message(request):
    return request['BODY']['message'][0]


def parse_params(url_data):
    if '?' in url_data:
        url_data = url_data.split('?')[1]
    return {x[0]: x[1] for x in [x.split("=") for x in url_data.split("&")]}


def has_body(request):
    return 'CONTENT_LENGTH' in request.keys() and len(request['CONTENT_LENGTH']) > 0


def read_body(request):
    content_length = int(request['CONTENT_LENGTH'])
    return request['wsgi.input'].read(content_length).decode()


