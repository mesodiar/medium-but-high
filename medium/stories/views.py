from django.shortcuts import render
from django.http import HttpResponse

from .models import Story


def index(request):
    stories = Story.objects.all()    
    context = {'stories': stories}
    return render(request, 'stories/index.html', context)


def detail(request, story_id):
    story = Story.objects.get(id=story_id)

    context = {'story': story}
    return render(request, 'stories/detail.html', context)