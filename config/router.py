from rest_framework import routers
from livresse.views.bookViews import BookView
from livresse.views.userViews import AdmUserView
from livresse.views.bookUserViews import BuyBookView, DesireBookView, PutBookView
from livresse.views.CatBookView import CategoryView, CatBookView

router = routers.DefaultRouter()
router.register('adm_users', AdmUserView)
router.register('books', BookView)
router.register('buy', BuyBookView)
router.register('desire', DesireBookView)
router.register('sell', PutBookView)
router.register('category', CategoryView)
router.register('category_book', CatBookView)