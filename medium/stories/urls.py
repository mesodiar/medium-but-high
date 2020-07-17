from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:story_id>/', views.detail, name='detail'),
    path('new-story/', views.new_story, name='new_story'),
]

