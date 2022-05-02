from  django.forms import ModelForm
from .models import Content
from .models import Tag


class PostForm(ModelForm):
    class Meta:
        model=Content
        fields=['topic','content']

class TagForm(ModelForm):
    class Meta:
        model=Tag
        fields=['tag_name']