from rest_framework import routers
from livresse.views.bookViews import BookView
from livresse.views.userViews import UserView

router = routers.DefaultRouter()
router.register('books', BookView)