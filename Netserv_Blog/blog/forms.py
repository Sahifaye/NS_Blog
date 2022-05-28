from django import forms
from .models import Blog_Post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = ('title', 'topic','slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'title'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content'}),
        }