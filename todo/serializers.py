from rest_framework import serializers
from .models import Todomodel
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todomodel
        fields="__all__"