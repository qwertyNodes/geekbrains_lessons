import views
import form_handlers


url_patterns = {
    '/': views.index,
    '/about': views.about,
    '/contact': views.contact,
    '404': views.error404,
    '/form': form_handlers.dist
}
