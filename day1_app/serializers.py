from rest_framework import serializers

# This will convert complex python into native python 
class Friends_serializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    age=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    gender=serializers.CharField(max_length=1)