import views
import form_handlers


url_patterns = {
    '/': views.Index(),
    '/about': views.About(),
    '/contact': views.Contact(),

    '/categories': views.CategoriesList(),
    '/create-category': views.CreateCategory(),
    '/create-course': views.CreateCourse(),
    '/courses': views.CoursesList(),

    '/create-user': views.CreateUser(),
    '/users': views.CreateUser(),

    '404': views.Error404(),
    '/form': form_handlers.FormDistribution()
}
