from rest_framework import routers
from livresse.views.bookViews import BookView
from livresse.views.userViews import AdmUserView

router = routers.DefaultRouter()
router.register('books', BookView)
router.register('adm-users', AdmUserView)