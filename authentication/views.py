from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import Userserializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RegisterView(GenericAPIView):
    serializer_class = Userserializer

    def post(self, request):
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
