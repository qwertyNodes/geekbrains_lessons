import jinja2


TEMPLATES_FOLDER = 'html/'


def render(template_path, **kwargs):
    with open(TEMPLATES_FOLDER + template_path, encoding='utf8') as f:
        t = jinja2.Template(f.read())

    return t.render(**kwargs)


def about(request):
    return '200 OK', render('about.html', **{'page_title': 'About page'})


def index(request):
    return '200 OK', render('index.html', **{'page_title': 'Index page'})


def error404(request):
    return '404 ERROR', render('404.html', **{'page_title': '404 not found'})


def contact(request, **kwargs):
    kwargs.update({'page_title': 'Contact us'})

    return '200 OK', render('contact.html', **kwargs)
