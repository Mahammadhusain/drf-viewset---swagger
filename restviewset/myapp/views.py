from unicodedata import name
from django.shortcuts import render
from numpy import roll

from myapp.admin import StudentModelAdmin
from restviewset.settings import BASE_DIR
from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class StudentViewSet(ViewSet):
    def list(self, request):
        
        a = StudentModel.objects.values_list('name','roll')
        print(a)
        stu = StudentModel.objects.all()
        
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = StudentModel.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)


    
    @swagger_auto_schema(
        request_body=StudentSerializers,
    )
    def create(self, request):
        print(repr(request.data))
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk):

        id = pk
        stu = StudentModel.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=StudentSerializers,
    )
    def partial_update(self,request, pk):
        id = pk
        stu = StudentModel.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    def destroy(self,request, pk):
        id = pk
        stu = StudentModel.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
