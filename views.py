import jinja2


TEMPLATES_FOLDER = 'html/'


def render(template_path, **kwargs):
    with open(TEMPLATES_FOLDER + template_path, encoding='utf8') as f:
        t = jinja2.Template(f.read())

    return t.render(**kwargs)


def about(request, **kwargs):
    kwargs.update({'page_title': 'About page'})

    return '200 OK', render('about.html', **kwargs)


def index(request, **kwargs):
    kwargs.update({'page_title': 'Index page'})

    return '200 OK', render('index.html', **kwargs)


def error404(request, **kwargs):
    kwargs.update({'page_title': '404 not found'})

    return '404 ERROR', render('404.html', **kwargs)


def contact(request, **kwargs):
    kwargs.update({'page_title': 'Contact us'})

    return '200 OK', render('contact.html', **kwargs)
