from django.contrib import admin
from django.urls import path, include
from .router import router
from livresse.views.userViews import UserLogin, UserView, UserLogout
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('/', admin.site.urls),

    # Documentation paths's
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),

    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
    ), name='swagger-ui'),

    # API paths's
    path('api/', include(router.urls)),
    path('api/users/<int:id>/', UserView.as_view(), name='user-view'),
    path('api/users/login/', UserLogin.as_view(), name='user-login'),
    path('api/users/logout/', UserLogout.as_view(), name='user-logout'),
]