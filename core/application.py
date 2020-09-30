class Application:
    def __init__(self, url_patterns, front_controllers):
        self.url_patterns = url_patterns
        self.front_controllers = front_controllers
        print('Application started')

    def __call__(self, environ, start_response):
        request = environ.copy()

        path = request['PATH_INFO']

        if len(path) > 1 and path.endswith('/'):
            path = path[:-1]

        view = self.url_patterns['404']
        if path in self.url_patterns:
            view = self.url_patterns[path]

        for front in self.front_controllers:
            front(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode()]
