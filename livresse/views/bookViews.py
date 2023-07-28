from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from livresse.models import Book
from livresse.serializers.bookSerializer import BookSerializer

class BookView(APIView):
    queryset = Book.objects.all()
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        # print('CAIU AQUI OW')
        try:
            id = self.kwargs["id"]
            if id != None:
                book = Book.objects.get(id=id)
                serializer = BookSerializer(book)
        except:
            # Obtém o valor do parâmetro "limit" da URL (ou 10, se não for especificado)
            # limit = int (request.GET.get('limit', 10))

            # Obtém os livros com base no valor do parâmetro "limit"
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
    
        return Response(serializer.data)
        
    def post(self, req, format=None):
        serializer = BookSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, *args, **kwargs):
        try:
            id = self.kwargs["id"]
            if id is not None:
                book = Book.objects.get(id=id)
                book.delete()
                return Response({"message": "Book deleted successfully"}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)