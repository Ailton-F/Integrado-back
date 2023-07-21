from rest_framework import viewsets
from rest_framework.response import Response
from livresse.models import Book
from livresse.serializers.bookSerializer import BookSerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []

    def get(self, request):
        # Obtém o valor do parâmetro "limit" da URL (ou 10, se não for especificado)
        limit = int(request.GET.get('limit', 10))

        # Obtém os livros com base no valor do parâmetro "limit"
        books = Book.objects.all()[:limit]
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)