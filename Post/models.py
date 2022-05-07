from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Tag(models.Model):
    '''Tag model to associate tag with content'''

    tag_name=models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name

class Content(models.Model):
    '''Content model to store the content'''

    topic=models.CharField(max_length=100)
    content=models.TextField(max_length=200,blank=True)
    createdon=models.DateTimeField(auto_now_add=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='contents')
    tag_name=models.ManyToManyField(Tag)

    def __str__(self):
        return self.content

class Comment(models.Model):
    '''Comment associated with content'''

    comment=models.CharField(max_length=100,blank=True)
    content=models.ForeignKey(Content,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.comment






