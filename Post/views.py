from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Content
from .models import Tag
from .forms import TagForm
from .forms import CommentForm
from .models import Comment

def create_post(request):
    '''This method is used to create posts in the account'''

    if request.method=='POST':
        post_form=PostForm(request.POST)
        if post_form.is_valid():
           topic=post_form.cleaned_data.get('topic')
           content=post_form.cleaned_data.get('content')
           post = Content(topic=topic, content=content,author=request.user)
           post.save()
           return redirect('Post:posts')
    else:
        post_form=PostForm()
        return render(request,"Post/post_create.html",{'form':post_form})

def get_all_post(request):
    '''This method fetches
    all the post in the database'''

    posts=Content.objects.all()
    return render(request,"Post/all_post.html",{'posts':posts})

def edit_post(request,id):
    '''This method helps in updating content'''

    post=Content.objects.get(id=id)
    if request.user.username==post.author.username:
        if request.method == 'POST':
            post_form = PostForm(request.POST,instance=post)
            if post_form.is_valid():
                post_form.save(commit=True)
                return redirect("Post:posts")
        else:
            post_form = PostForm(instance=post)
            return render(request, "Post/post_create.html", {'form': post_form})
    else:
        return HttpResponse("<h1>Error</h1>")


def content_details(request,id):
    '''This method is add content details'''

    content=Content.objects.get(pk=id)
    tags=content.tag_name.all()
    comments=Comment.objects.filter(content=content)
    return render(request,"Post/content_details.html",{'content':content,'tags':tags,'comments':comments})


def create_tag(request):
    '''Method to create  tags'''

    if request.method=="POST":
        tag_form=TagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
            return redirect('Post:tags')
        else:
            return HttpResponse("<h1>Error</h1>")
    else:
        tag_form=TagForm()
        return render(request,"Post/tag_add.html",{'form':tag_form})


def get_all_tag(request):
    '''Method to list all tags'''

    tags=Tag.objects.all()
    return render(request,"Post/tag_list.html",{'tags':tags})

def add_tag_post_id(request,postid):
    '''Add tags to content'''

    post=Content.objects.get(pk=int(postid))
    tag_name=request.GET.get("tag_name",None)
    if tag_name:
       print(f"Entered in tag name block {tag_name}")
       tag=Tag.objects.filter(tag_name=tag_name)
       if list(tag):
          post.tag_name.add(tag[0])
          return redirect("Post:postdetails",id=postid)
       else:
          return HttpResponse("<h1>Tag not found</h1>")
    else:
        tag_search_form=TagForm()
        return render(request,"Post/add_tag_post.html",{"post":post,"form":tag_search_form})

def add_all_article_tag(request):
    '''Get all the articles by tag'''

    tag_form=TagForm()
    tag_name=request.GET.get("tag_name",None)
    if tag_name:
        tag = Tag.objects.filter(tag_name=tag_name)
        if list(tag):
           posts=tag[0].content_set.all()
           return render(request,"Post/all_post.html",{"posts":posts})
        else:
           return HttpResponse("<h1>No contents by this tag name</h1>")
    else:
        return render(request,"Post/tag_filter.html",{'form':tag_form})


def add_comment(request,id):
    content=Content.objects.get(pk=id)
    if request.method=="POST":
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=request.POST.get("comment")
            comm=Comment(comment=comment,content=content)
            comm.save()
            return redirect("Post:postdetails",id=content.id)
        else:
            return HttpResponse("<h1>Error</h1>")
    else:
        comment_form=CommentForm()
        return render(request,"Post/comment.html",{'form':comment_form})



















