from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from lead.models import Lead
from lead.serializers import LeadSerializer

# Create your views here.
class LeadListCreateView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        instance=Lead.objects.filter(created_by=request.user)
        serializer_instance=LeadSerializer(instance,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=LeadSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(created_by=request.user)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class LeadRetriveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=LeadSerializer
    
    def get_queryset(self):
      return Lead.objects.filter(created_by=self.request.user)