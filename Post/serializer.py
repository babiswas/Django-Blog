from rest_framework import serializers
from .models import Content


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tag_name=serializers.CharField(max_length=100)


class ContentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    comments=serializers.StringRelatedField(many=True)
    class Meta:
        model=Content
        fields=['id','topic','content','createdon','comments']
