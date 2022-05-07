from django.shortcuts import render
from .forms import UserForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from .serializer import AuthorSerializer,AuthorContentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from django.core.paginator import Paginator

def register(request):
        '''User can register himself using this function'''

        if request.method=='POST':
            user_form=UserForm(request.POST)
            if user_form.is_valid():
                   user_form.save()
                   return redirect("Post:posts")
            else:
                   return redirect("Author:adduser")
        else:
            user_form=UserForm()
            return render(request,"Author/author.html",{'form':user_form})




def update_user(request,id):
        '''User can edit the user deatils using this function'''

        user=User.objects.get(pk=id)
        if user==request.user:
            if request.method=="POST":
               user_form=UserForm(request.POST)
               if user_form.valid():
                  user_form.save()
                  return redirect("Post:posts")
            else:
                user_form=UserForm(user)
                return render(request,"Author/author.html",{'form':user_form})
        else:
            return HttpResponse("<h1>Unauthorized</h1>")


def login(request):
    '''User can login using login method'''

    if request.user.is_authenticated:
        return redirect("Post:posts")
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username)
        print(password)
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user!=None:
            auth.login(request,user)
            return redirect("Post:posts")
        else:
            return HttpResponse("<h1>Error</h1>")
    return render(request,"Author/login.html")



def logout(request):
    '''User can logout using this method'''

    auth.logout(request)
    return render(request,"Author/login.html")


def all_authors(request):
    users=User.objects.all()
    serializer=AuthorSerializer(users,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

@api_view(['GET',])
def all_author_contents(request):
    users=User.objects.all()
    paginator=Paginator(users,2)
    page=request.GET.get('page')
    page_obj=paginator.get_page(page)
    serializer=AuthorContentSerializer(page_obj,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')






