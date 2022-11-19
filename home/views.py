from tkinter import E
from urllib import request, response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from home import serializers

# Create your views here.


class handleUpload(APIView):
    parser_classes=[MultiPartParser]
    def post(self, request):
         try:
            data = request.data
            serializer = serializers.files_list_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                
                return Response({"message": "successfully uploaded", "status": 200,"data":serializer.data})

            return Response({"message": "failed to upload", "status": 400, "data": serializer.errors})

         except Exception as e:
              print(e)   

def home(request):
    return render(request,'home.html')


