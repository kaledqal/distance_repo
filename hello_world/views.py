
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from hello_world.models import Iata
from hello_world  import serializers


# Create your views here.
class HelloView(APIView):
    #
    serializer_class=serializers.InputSerializer

    def get(self,request,format=None):
        message = {
        "name": "Distance Calculator",
        "input 1": "IATA code for origin",
        "Input 2": "IATA code for destination",
        "Output":{
            "status": "Indicating success or failure",
            "code 1": "The origin IATA code",
            "code 2": "The destination IATA code",
            "distance": "The distance between the two points on the globe"
            }
        }
        return Response(message)

    def post(self,request,format=None):
        code_1=None
        code_2=None
        serializer = serializers.InputSerializer(data=request.data)
        if serializer.is_valid():
            code_1 = serializer.data.get('iata_code_1')
            code_2 = serializer.data.get('iata_code_2')

        return Response({"CODE 1":code_1,"CODE 2":code_2})
