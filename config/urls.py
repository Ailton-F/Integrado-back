from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from livresse import urls
# from livresse.views import UsersViewSet

router = routers.DefaultRouter()
# router.register(r'users', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('', include(router.urls)),
]
