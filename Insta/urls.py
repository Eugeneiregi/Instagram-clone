from django.conf import settings
from . import views
from django.contrib.auth import views as  auth_views
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns =  [
    url('', views.index, name='index'),

]