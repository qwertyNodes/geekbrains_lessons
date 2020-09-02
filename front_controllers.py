from urllib.parse import parse_qs

import utils


def get_query_request_params(request):
    query = request['QUERY_STRING']
    request['QUERY_DICT'] = None
    if len(query) > 1:
        request['QUERY_DICT'] = parse_qs(query)

    if utils.has_body(request):
        request['BODY'] = parse_qs(utils.read_body(request))


controllers_list = [
    get_query_request_params
]
