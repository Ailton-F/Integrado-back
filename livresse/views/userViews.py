from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import viewsets, authentication, permissions
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from livresse.models import User
from livresse.serializers.userSerializer import UserSerializer
import jwt, datetime

class AdmUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class UserLogin(APIView):
    queryset = User.objects.all()
    permission_classes = []

    def post(self, req):
        email = req.data['email']
        password = req.data['password']
        last_login = datetime.datetime.utcnow()
        user = User.objects.filter(email=email).first()

        if user is None: raise AuthenticationFailed('User not found')
        if not user.check_password(password): raise AuthenticationFailed('Incorrect password')
        
        serializer = UserSerializer(user, data={'last_login':last_login}, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        expiration_data = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        payload = {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'username': user.idName,
            'admin': user.admin,
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

class UserLogout(APIView):
    queryset = User.objects.all()
    permission_classes = []

    def post(self, req):
        res = Response({
            "message": "Logout complete"
        })
        res.delete_cookie("jwt")
        return res

class UserView(APIView):
    queryset = User.objects.all()
    permission_classes = []

    def get(self, req, *args, **kwargs):
        token = req.COOKIES.get('jwt')

        if not token: raise AuthenticationFailed('Unauthenticated')

        try: payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: raise AuthenticationFailed('Unauthenticated')

        try:
            id = kwargs['id']
            if payload['admin'] and id != None:
                user = User.objects.get(id=id)
            else:
                user = User.objects.get(id=payload['id'])
            
            serializer = UserSerializer(user)
            
        except:
            if payload['admin']:
                user = User.objects.all()
                serializer = UserSerializer(user, many=True)
            else:
                user = User.objects.get(id=payload['id'])
                serializer = UserSerializer(user)

        # hasher = PBKDF2PasswordHasher()
        # print( hasher.decode(user.password) )
        return Response(serializer.data)

    def post(self, req):
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def put(self, req, *args, **kwargs):
        token = req.COOKIES.get('jwt')

        if not token:raise AuthenticationFailed('Unauthenticated')
        try:payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:raise AuthenticationFailed('Unauthenticated')

        try:
            id = kwargs['id']
            if payload['admin'] and id != None:
                user = User.objects.get(id=id)
            else:
                user = User.objects.get(id=payload['id'])
            
            serializer = UserSerializer(user)
            
        except jwt.MissingRequiredClaimError: raise AuthenticationFailed('You dont have permission to do that!')


        if not user:raise AuthenticationFailed('User not found')
        
        password = req.data.pop('password', None)
        if password is not None:
            user.set_password(password)

        serializer = UserSerializer(user, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)