
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
        "input 1": "IATA code for the origin airport",
        "Input 2": "IATA code for the destination airport",
        "Output":{
            "Success status": {
                    "200":"Success",
                    "404":"One or both of the location IATA code is not in the database",
                    "412":"Invalid Input"},
            "IATA Code 1": "The origin IATA code",
            "IATA Code 2": "The destination IATA code",
            "distance": "The distance between the two airports on the globe"
            }
        }
        return Response(message)

    def post(self,request,format=None):
        import math
        code_1=None
        code_2=None
        serializer = serializers.InputSerializer(data=request.data)
        if serializer.is_valid():
            code_1 = serializer.data.get('iata_code_1').upper()
            code_2 = serializer.data.get('iata_code_2').upper()
            try:
                #get the latitude and longitudes from the user data
                lat1=float(Iata.objects.get(pk=code_1).lat)
                lng1=float(Iata.objects.get(pk=code_1).lng)
                lat2=float(Iata.objects.get(pk=code_2).lat)
                lng2=float(Iata.objects.get(pk=code_2).lng)

                delta_lat = math.radians(lat2-lat1)# change in latitude
                delta_lng = math.radians(lng2-lng1)# change in longitude

                lat1=math.radians(lat1)
                lat2=math.radians(lat2)

                RADIUS = 6371 #the radius of the earth
                haversine = (math.sin(delta_lat/2))**2 + math.cos(lat1)*math.cos(lat2)*(math.sin(delta_lng/2))**2 #works well up to this point
                mul  = 2 * math.atan2(math.sqrt(haversine),math.sqrt(1-haversine))
                distance = RADIUS * mul
                return Response({"Status":status.HTTP_200_OK,"IATA Code 1":code_1,"IATA Code 2":code_2,"Distance":distance})
            except:
                return Response({"Status":status.HTTP_404_NOT_FOUND,"CODE 1":code_1,"CODE 2":code_2})

        code_1 = serializer.data.get('iata_code_1').upper()
        code_2 = serializer.data.get('iata_code_2').upper()
        return Response({"Status":status.HTTP_412_PRECONDITION_FAILED})
