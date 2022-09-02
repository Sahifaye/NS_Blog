from re import search
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog_Post,Like
from .forms import BlogPostForm, SampleForm
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

@login_required(login_url='login')
def Add_Post(request):
    if request.method=="POST":
        print("------->")
        form = BlogPostForm(data=request.POST, files=request.FILES)
        print(form.is_valid())
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.slug = blogpost.title.replace(" ", "-")
            blogpost.author = request.user
            blogpost.image = form.cleaned_data.get('image')
            blogpost.save()
            obj = form.instance
            posts = Blog_Post.objects.filter(topic='personel_blog').order_by('-created_at')
            news_posts = Blog_Post.objects.filter(topic='news').order_by('-created_at')
            new_form = BlogPostForm()
            print("==========>> Here in the Post ")
            return render(request, "index.html",{'obj':obj,'form':new_form,'posts':posts, 'news':news_posts})
        else:
            print(form)
            posts = Blog_Post.objects.filter(topic='personel_blog').order_by('-created_at')
            news_posts = Blog_Post.objects.filter(topic='news').order_by('-created_at')
    else:
        form=BlogPostForm()
        posts = Blog_Post.objects.filter(topic='personel_blog').order_by('-created_at')
        news_posts = Blog_Post.objects.filter( topic='news').order_by('-created_at')
        print (posts)
    return render(request, "index.html", {'form':form,'posts':posts, 'news':news_posts})



@login_required(login_url='login')
def my_view_posts(request):
    posts = Blog_Post.personalBlog.order_by('-created_at')
    return render(request, "post_timeline_new.html", {'posts':posts})


@login_required(login_url='login')
def view_events(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.slug = blogpost.title.replace(" ", "_")
            blogpost.author = request.user
            blogpost.image = form.cleaned_data.get('image')
            blogpost.save()
            obj = form.instance
            posts = Blog_Post.objects.filter( topic='personel_blog').order_by('-created_at')
            news_posts = Blog_Post.objects.filter(topic='news').order_by('-created_at')
            new_form = BlogPostForm()
            return render(request, "index.html",{'obj':obj,'form':new_form,'posts':posts, 'news':news_posts})
    else:
        form=BlogPostForm()
        posts = Blog_Post.personalBlog.order_by('-created_at')
        news_posts = Blog_Post.newsBlog.order_by('-created_at')
    return render(request, "index.html", {'form':form,'posts':posts,'news':news_posts})



def like_post(request):
    if request.method == 'GET':
        print(request.GET['post_id'])
        post_id = request.GET['post_id']
        likedpost = Blog_Post.objects.get(id = post_id )
        m = Like( post=likedpost )
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

def post_details(request, year, month, day, post):
    post = get_object_or_404(
        Blog_Post, slug = post, 
        created_at__year = year,
        created_at__month = month,
        created_at__day = day
    ) 
    print( post)
    return render(request, 'post_details.html', {'post':post})



def post_delete(request):
    if request.GET.__contains__('post_id'):
        post_id = request.GET.get('post_id')
        q = Blog_Post.objects.filter(id = post_id).delete()
        return HttpResponse('success')

def annoucement(request):
    context = {}
    context['form'] = SampleForm()
    print(context)
    return render(request, 'form_test.html', context)

