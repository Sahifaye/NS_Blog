from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('designation','address', 'country','phone', 'bio', 'linkedin', 'image' )