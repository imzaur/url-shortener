from django.conf.urls import url

from .views import HomeView, RedirectView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<shortcode>.*)/$', RedirectView.as_view(), name='redir'),
]
