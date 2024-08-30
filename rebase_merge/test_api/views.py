from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class mainView(APIView):
    @staticmethod
    def get(request):
        return Response({"message": "hello world"})