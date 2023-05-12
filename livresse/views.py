# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from livresse.models import User
from livresse.serializer import UserSerializer
import jwt, datetime

# Create your views here.

# class UsersViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserRegister(APIView):
    queryset = User.objects.all()
    permission_classes = []

    def post(self, req):
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class UserLogin(APIView):
    queryset = User.objects.all()
    permission_classes = []

    def post(self, req):
        email = req.data['email']
        password = req.data['password']
        user = User.objects.filter(email=email).first()
        
        if user is None: raise AuthenticationFailed('User not found')
        if not user.check_password(password): raise AuthenticationFailed('Incorrect password')

        expiration_data = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        payload = {
            'id': user.id,
            'exp': expiration_data,
            'iat': datetime.datetime.utcnow(),
        } 
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        res = Response()
        res.data = {
            'token': token
        }
        res.set_cookie(
            key='jwt', 
            value=token, 
            httponly=True,
        )

        return res

class UserView(APIView):
    queryset = User.objects.all()
    permission_classes = []

    def get(self, req):
        token = req.COOKIES.get('jwt')
        if not token: raise AuthenticationFailed('Unauthenticated!')

        try: payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class UserLogout(APIView):
    queryset = User.objects.all()
    permission_classes = []

    def post(self, req):
        res = Response({
            "message": "Logout complete"
        })
        res.delete_cookie("jwt")
        return res