from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
# Create your models here.

class PersonalBlogManager(models.Manager):
    def get_queryset(self):
        return super(PersonalBlogManager,self).get_queryset().filter(topic='personel_blog')
class NewsBlogManager(models.Manager):
    def get_queryset(self):
        return super(NewsBlogManager,self).get_queryset().filter(topic='news')
class Blog_Post(models.Model):
    ANNOUNCEMENT = 'announcement'
    PERSONAL_BLOG = 'personel_blog'
    NEWS = 'news'
    EVENTS = 'events'

    TOPICS = [
        (ANNOUNCEMENT, 'Announcement'), (PERSONAL_BLOG,
                                         'Personal_Blog'), (NEWS, 'News'), (EVENTS, 'Events')
    ]
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique_for_date='created_at')
    topic = models.CharField(max_length=20, choices=TOPICS, default=NEWS)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to="static/post_pics", blank=True, null=True)
    objects = models.Manager()
    personalBlog = PersonalBlogManager()
    newsBlog = NewsBlogManager()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('post_details', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,self.slug
        ])


class Like(models.Model):
    post = models.ForeignKey(Blog_Post, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.post)
        

