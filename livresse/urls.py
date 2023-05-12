from django.urls import path
from .views import UserRegister, UserLogin, UserView, UserLogout

urlpatterns = [
    path('register', UserRegister.as_view()),
    path('login', UserLogin.as_view()),
    path('user', UserView.as_view()),
    path('logout', UserLogout.as_view())
]