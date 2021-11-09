from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.new_questions, name='index'),
    path('ask/', views.create_ask, name='create_ask'),
    path('question/<int:pk>/', views.question_page, name='question'),
    path('hot/', views.hot_questions, name='hot_questions'),
    path('tag/<str:tag>/', views.questions_by_tag, name='question_by_tag'),
    path('settings', views.settings, name='settings'),
    path('login/', views.login_view, name='login'),
    path('signup', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
