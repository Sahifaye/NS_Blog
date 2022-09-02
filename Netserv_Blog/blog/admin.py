from django.contrib import admin
from .models import Blog_Post, Like

# Register your models here.

@admin.register(Like)
class Like_PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author')
@admin.register(Blog_Post)
class Blog_PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_at')
    list_filter = ('author', 'created_at' )
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = "created_at"
    ordering = ('created_at',)



