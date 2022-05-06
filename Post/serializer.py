from rest_framework import serializers
from rest_framework import serializers
from .models import Content


class TagSerializer(serializers.Serializer):
    tag_name=serializers.CharField(max_length=100)


class ContentSerializer(serializers.ModelSerializer):
    comments=serializers.StringRelatedField(many=True)
    class Meta:
        model=Content
        fields=['topic','content','createdon','comments']
