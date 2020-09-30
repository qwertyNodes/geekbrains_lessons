from urllib.parse import parse_qsl

import utils


def get_request_params(request):
    query = request['QUERY_STRING']
    request['query_dict'] = None
    if len(query) > 1:
        request['query_dict'] = dict(parse_qsl(query))

    if utils.has_body(request):
        request['body'] = utils.parse_form_data(parse_qsl(utils.read_body(request)))
        print(request['body'])
        pass


controllers_list = [
    get_request_params
]
