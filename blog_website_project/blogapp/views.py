from django.shortcuts import render
from .models import Blog


# Create your views here.

def homepage(request):
    return render(request, 'blogapp/homepage.html',
                 context={'blog':Blog.objects.all()})