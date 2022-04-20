from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {'card': {'title': "Hello My First Post", 'post': "Hi , this is my first post to test the now function I have added to teh HTML Page I have created , Its very happy Moment for me I ove beting my selt something something meri jaan , kar le hamse ek baar pyar ki meethi baaten chaar oo soniye ...  "}})