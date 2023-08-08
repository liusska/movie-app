from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/', include('movie_app.accounts.urls')),
    path('movies/', include('movie_app.movies.urls')),
)
