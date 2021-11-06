from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ask', views.ask, name='ask'),
    path('question', views.question, name='question'),
    path('tag', views.tag, name='tag'),
    path('settings', views.settings, name='settings'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]