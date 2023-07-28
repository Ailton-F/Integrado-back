from django.contrib import admin
from django.urls import path, include
from .router import router
from livresse.views.userViews import UserLogin, UserView, UserLogout
from livresse.views.bookViews import BookView
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

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
    path("api/books/", BookView.as_view(), name="books"),
    path("api/books/<int:id>", BookView.as_view(), name="book-detail"),
    path('api/users/<int:id>/', UserView.as_view(), name='user-view'),
    path('api/users/login/', UserLogin.as_view(), name='user-login'),
    path('api/users/logout/', UserLogout.as_view(), name='user-logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)