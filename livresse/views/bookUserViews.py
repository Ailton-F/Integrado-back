from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from livresse.models import Buy, Desire, PutBook
from livresse.serializers.bookUserSerializer import BuySerializer, DesireSerializer, PutBookSerializer
import jwt

def is_loged(req):
    token = req.COOKIES.get('jwt')
    if not token: raise AuthenticationFailed('Unauthenticated')

    try: payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError: raise AuthenticationFailed('Unauthenticated')
    return payload

class BuyBookView(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer
    permission_classes = []

class DesireBookView(viewsets.ModelViewSet):
    queryset = Desire.objects.all()
    serializer_class = DesireSerializer
    permission_classes = []

class PutBookView(viewsets.ModelViewSet):
    queryset = PutBook.objects.all()
    serializer_class = PutBookSerializer
    permission_classes = []