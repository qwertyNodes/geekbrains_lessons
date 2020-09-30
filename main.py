from core.application import Application
import routing
import front_controllers


from wsgiref.simple_server import make_server


application = Application(routing.url_patterns, front_controllers.controllers_list)

httpd = make_server('127.0.0.1', 8000, application)
httpd.serve_forever()
