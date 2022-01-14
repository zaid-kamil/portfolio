from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]