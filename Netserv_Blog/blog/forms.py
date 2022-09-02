from django import forms
from .models import Blog_Post


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = ('title', 'topic', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
        }


class SampleForm(forms.Form):
    FRUIT_CHOICES = [
        ('orange', 'Oranges'),
        ('cantaloupe', 'Cantaloupes'),
        ('mango', 'Mangoes'),
        ('honeydew', 'Honeydews'),
    ]
    SAMPLE_CHOICES = (
        ('one', 'ONE'),
        ('two', 'TWO'),
        ('three', 'THREE'),)

    TYPE_SELECT = (
        ('0', 'Female'),
        ('1', 'male'),
    )
    SUBJECTS = [
        ('physics', 'PHYSICS'),
        ('chemistry', 'CHEMiSTRY'),
        ('biology', 'BIOLOGY'),
        ('english', 'ENGLISH'),
        ('hindi', 'HINDI'),
    ]

    first_name = forms.CharField(max_length=200, label="First Name", widget =forms.TextInput( attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, label="Last Name", widget =forms.TextInput( attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Age",widget =forms.TextInput( attrs={'class': 'form-control'}))
    gender = forms.CharField(max_length=11,widget=forms.RadioSelect(choices=TYPE_SELECT))
    subjects = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=SUBJECTS)
    phone_no = forms.IntegerField(label="Phone Number", widget =forms.TextInput( attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=200, label="City", widget =forms.TextInput( attrs={'class': 'form-control'}))
    favorite_fruit = forms.CharField(
        label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES, attrs={'class': 'form-control'}))
    choice = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(), choices=SAMPLE_CHOICES, label="Select your choice!")
