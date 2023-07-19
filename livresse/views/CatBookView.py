from rest_framework import viewsets
from livresse.models import Category, CatBook
from livresse.serializers.CatBookSerializer import CatBookSerializer, CategorySerializer

class CatBookView(viewsets.ModelViewSet):
    queryset = CatBook.objects.all()
    serializer_class = CatBookSerializer
    permission_classes = []

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []