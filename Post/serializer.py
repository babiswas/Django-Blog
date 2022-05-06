from rest_framework import serializers


class TagSerializer(serializers.Serializer):
    tag_name=serializers.CharField(max_length=100)
