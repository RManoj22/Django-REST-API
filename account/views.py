from django.contrib.auth import authenticate,login
from . serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class UserRegistration(APIView):

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password1')
        email = request.data.get('email')
        user_name = User.objects.filter(username=username)
        print('username',user_name)
        if user_name:
            result = 'Username not available'
        
        elif request.data['password1'] != request.data['password2']:
            result = "Passwords doesn't match"
        
        else:
            User.objects.create_user(username=username, email=email,password=password)
            result = 'User created succesffully'
    
        return Response({'response':result})
    
class UserLogin(APIView):
    
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'errors': 'The requested user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    