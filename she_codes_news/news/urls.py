from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('accounts/', include('django.contrib.auth.urls')),
]
