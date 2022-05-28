from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog_Post,Like
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def Add_Post(request):
    print (request.FILES)
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.slug = blogpost.title.replace(" ", "_")
            blogpost.author = request.user
            blogpost.image = form.cleaned_data.get('image')
            blogpost.save()
            obj = form.instance
            posts = Blog_Post.objects.filter(topic='personel_blog').order_by('-created_at')
            news_posts = Blog_Post.objects.filter(topic='news').order_by('-created_at')
            new_form = BlogPostForm()
            return render(request, "index.html",{'obj':obj,'form':new_form,'posts':posts, 'news':news_posts})
    else:
        form=BlogPostForm()
        posts = Blog_Post.objects.filter(topic='personel_blog').order_by('-created_at')
        news_posts = Blog_Post.objects.filter( topic='news').order_by('-created_at')
    return render(request, "add_blog.html", {'form':form,'posts':posts, 'news':news_posts})



@login_required
def view_posts(request):
    posts = Blog_Post.objects.filter(topic='personel_blog').order_by('-created_at')
    return render(request, "posts_timeline.html", {'posts':posts})


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
        posts = Blog_Post.objects.filter(topic='personel_blog').order_by('-created_at')
        news_posts = Blog_Post.objects.filter( topic='news').order_by('-created_at')
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