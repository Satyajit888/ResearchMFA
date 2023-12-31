from django.contrib import admin
# from django.urls import path
from django.contrib.auth import views as auth_views


from django.urls import path
from users import views as user_views

from django.views.static import serve
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.CustomLogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
