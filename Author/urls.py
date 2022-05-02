from django.urls import path
from .import views

app_name='Author'

urlpatterns=[
    path('create_user/',views.register,name='adduser'),
    path('edit_user/<int:id>',views.update_user,name='edituser'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]