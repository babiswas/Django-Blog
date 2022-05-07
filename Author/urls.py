from django.urls import path
from .import views

app_name='Author'

urlpatterns=[
    path('create_user/',views.register,name='adduser'),
    path('edit_user/<int:id>',views.update_user,name='edituser'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('api/authors/',views.all_authors,name='authors'),
    path('api/author_content/',views.all_author_contents,name='author_content'),
]