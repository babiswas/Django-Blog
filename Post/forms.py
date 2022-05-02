from  django.forms import ModelForm
from .models import Content
from .models import Tag
from .models import Comment


class PostForm(ModelForm):
    '''Content form to add content'''
    class Meta:
        model=Content
        fields=['topic','content']

class TagForm(ModelForm):
    '''Tag Form to add tag'''
    class Meta:
        model=Tag
        fields=['tag_name']

class CommentForm(ModelForm):
    '''Commet form to add comment'''
    class Meta:
        model=Comment
        fields=['comment']