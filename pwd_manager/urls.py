from django.contrib import admin
from django.urls import path
from pwd.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('signup/',signup, name='signup'),
    path('login/',login, name='login'),
    path('dashboard/',dashboard, name='dashboard'),
    path('delete-pwd/<str:dname>/',delete_pwd, name='delete_pwd'),
]
