from django.conf.urls import url
from home.views import HomeView, CreatePassword, home
app_name = 'home'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^password/create/$', CreatePassword.as_view(), name='create_password'),
    url(r'^password/create/generate/$', home, name='home_home'),
]