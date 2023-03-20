from rest_framework import serializers
from .models import *

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter Book Title")
    author=serializers.CharField(label="Enter Author Names")
    
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = "__all__"