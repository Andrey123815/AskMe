from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from app.models import *


def paginate(objects_list, request, limit=3):
    paginator = Paginator(objects_list, limit)
    page_num = request.GET.get('page')

    return paginator.get_page(page_num)


def new_questions(request):
    content = paginate(Question.objects.all(), request)
    popular_tags = Tag.objects.popular_tags()

    return render(request, 'index.html', {'questions': content, 'popular_tags': popular_tags})


def create_ask(request):
    popular_tags = Tag.objects.popular_tags()

    return render(request, 'ask.html', {'popular_tags': popular_tags})


def question_page(request, pk):
    question = Question.objects.get(id=pk)
    answers_page = paginate(Answer.objects.by_question(pk), request, limit=1)
    popular_tags = Tag.objects.popular_tags()

    return render(request, 'one_question_page.html', {'questions': question, 'content': answers_page,
                                                      'form': form, 'popular_tags': popular_tags})


def hot_questions(request):
    content = paginate(Question.objects.hot(), request)
    popular_tags = Tag.objects.popular_tags()

    return render(request, 'index.html', {'questions': content, 'popular_tags': popular_tags})


def questions_by_tag(request, tag):
    questions_page = paginate(Question.objects.by_tag(tag), request)
    popular_tags = Tag.objects.popular_tags()

    return render(request, 'question_by_tag.html', {'content': questions_page, 'tag': tag,
                                                    'popular_tags': popular_tags})


def settings(request):
    popular_tags = Tag.objects.popular_tags()

    return render(request, 'settings.html', {"popular_tags": popular_tags})


def login_view(request):
    popular_tags = Tag.objects.popular_tags()

    return render(request, 'login.html', {'popular_tags': popular_tags})


def signup(request):

    return render(request, 'signup.html', {'popular_tags': popular_tags})
