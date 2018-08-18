from rest_framework import serializers
from hello_world.models import Iata

class InputSerializer(serializers.Serializer):
    iata_code_1 = serializers.CharField(max_length=3,style={"placeholder":"Enter Three Characters,eg XXX","max_length":"3"})
    iata_code_2 = serializers.CharField(max_length=3,style={"placeholder":"Enter Three Characters,eg XXX","max_length":"3"})
