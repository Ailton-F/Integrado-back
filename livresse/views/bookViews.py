from rest_framework.response import Response
from rest_framework import viewsets
from livresse.models import Book
from livresse.serializers.bookSerializer import BookSerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []