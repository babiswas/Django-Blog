from rest_framework import serializers
from Post.serializer import ContentSerializer
from django.contrib.auth.models import User

class AuthorSerializer(serializers.Serializer):
    '''Serializer to display all authors'''

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    email=serializers.EmailField()


class AuthorContentSerializer(serializers.ModelSerializer):
    '''Serializer to display author related contents'''

    contents=ContentSerializer(many=True,read_only=True)
    class Meta:
        model=User
        fields=['id','username','email','contents']
