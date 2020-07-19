from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView

from .models import Story
from .forms import StoryForm


def index(request):
    stories = Story.objects.all()    
    context = {'stories': stories}
    return render(request, 'stories/index.html', context)


def detail(request, story_id):
    story = Story.objects.get(id=story_id)

    context = {'story': story}
    return render(request, 'stories/detail.html', context)


def new_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = StoryForm()
    return render(request, 'stories/new_story.html', {'form': form})