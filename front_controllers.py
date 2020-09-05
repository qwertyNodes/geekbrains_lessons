from urllib.parse import parse_qsl

import utils


def get_request_params(request):
    query = request['QUERY_STRING']
    request['query_dict'] = None
    if len(query) > 1:
        request['query_dict'] = dict(parse_qsl(query))

    if utils.has_body(request):
        request['body'] = dict(parse_qsl(utils.read_body(request)))


controllers_list = [
    get_request_params
]
