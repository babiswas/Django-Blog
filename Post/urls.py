from django.urls import path
from .import views

app_name='Post'

urlpatterns=[
    path('create_post/',views.create_post,name='addpost'),
    path('all_post/',views.get_all_post,name='posts'),
    path('post/<int:id>',views.edit_post,name='postupdate'),
    path('post_details/<int:id>',views.content_details,name="postdetails"),
    path('alltags/',views.get_all_tag,name="tags"),
    path('addtag/',views.create_tag,name="addtag"),
    path('tagtopost/<int:postid>',views.add_tag_post_id,name="tagpost"),
]