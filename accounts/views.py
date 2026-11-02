from django.shortcuts import render

from accounts.models import User
from accounts.serializers import UserSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class UserRegisterView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_intance=UserSerializer(data=form_data)
        if serializer_intance.is_valid():
            cleaned_data=serializer_intance.validated_data
            instance=User.objects.create_superuser(**cleaned_data)
            serializer_intance=UserSerializer(instance)
            return Response(data=serializer_intance.data)
        else:
            return Response(data=serializer_intance.errors)
