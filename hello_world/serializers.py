from rest_framework import serializers
from hello_world.models import Iata
import re

def validate_input(value):
    value = re.sub(r'[^A-Z,a-z]','',value)
    if len(value) != 3:
        raise serializers.ValidationError("Invalid Input")
    return value

class InputSerializer(serializers.Serializer):
    iata_code_1 = serializers.CharField(
                label="IATA Code 1",validators=[validate_input,],
                max_length=3,
                style={
                    "placeholder":"Enter Three Characters,eg XXX",
                    "max_length":"3"
                    })
    iata_code_2 = serializers.CharField(
                label="IATA Code 2",validators=[validate_input,],
                max_length=3,
                style={
                    "placeholder":"Enter Three Characters,eg XXX",
                    "max_length":"3"
                    })
