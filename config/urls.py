from django.contrib import admin
from django.urls import path, include
from .router import router
from livresse.views.userViews import UserLogin, UserView, UserLogout

urlpatterns = [
    path('/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/<int:id>/', UserView.as_view(), name='user-view'),
    path('api/users/login/', UserLogin.as_view(), name='user-login'),
    path('api/users/logout/', UserLogout.as_view(), name='user-logout'),
]