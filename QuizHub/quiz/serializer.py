from rest_framework import serializers
from models import *

class OptionSerializer(serializers.ModelSerializer):
     class Meta:
        model = Option
        fields = [ "id", "question", "option_text", "is_correct", ]