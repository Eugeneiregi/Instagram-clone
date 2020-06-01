from django.conf import settings
from . import views
from django.contrib.auth import views as  auth_views
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns =  [
    url('', views.index, name='index'),
    # url('register', views.register, name="register-authentication"),
    url('accounts/profile/',views.profile_info,name='profile'),
    url('profile_edit', views.profile_edit, name='profile_edit'),
    url('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url('search', views.search_results, name='search_results'),
    url('new_comment/', views.CommentCreateView.as_view(),name='new_comment')
]