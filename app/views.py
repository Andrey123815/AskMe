from django.shortcuts import render

questions = [
    {
        "title": f"How to moon like {i}",
        "author": "Ivancher_556",
        "avatar_source_img": "C://img",
        "answers_count": f"{i + 1}",
        "text": "Выделяют две основные категории HTML-элементов, которые соответствуют типам их содержимого"
                "и поведению в структуре веб-страницы — блочные и строчные элементы. "
                "С помощью блочных элементов можно создавать структуру веб-страницы, строчные элементы"
                "используются для форматирования текстовых фрагментов (за исключением элементов и других)...",
        "tags_count": 4,
        "tags": ["success", "technopark", "vk", "study"],
        "references": ["#", "#", "#", "#"],
        "like_count": 100,
        "dislike_count": 100
    } for i in range(3)
]


def index(request):
    return render(request, 'index.html', {'questions': questions})


def ask(request):
    return render(request, 'ask.html')


main_questions = [
    {
        "title": f"How to moon like {i}?",
        "author": "Ivancher_556",
        "avatar_source_img": "C://img",
        "text": "Выделяют две основные категории HTML-элементов, которые соответствуют типам их содержимого"
                "и поведению в структуре веб-страницы — блочные и строчные элементы. "
                "С помощью блочных элементов можно создавать структуру веб-страницы, строчные элементы"
                "используются для форматирования текстовых фрагментов (за исключением элементов и других)...",
        "tags_count": 4,
        "tags": ["success", "technopark", "vk", "study"],
        "references": ["#", "#", "#", "#"],
        "like_count": 100,
        "dislike_count": 100
    } for i in range(1)
]

answers = [
    {
        "author": "Agent_007",
        "avatar_source_img": "C://img",
        "text": "Выделяют две основные категории HTML-элементов, которые соответствуют типам их содержимого"
                "и поведению в структуре веб-страницы — блочные и строчные элементы. "
                "С помощью блочных элементов можно создавать структуру веб-страницы, строчные элементы"
                "используются для форматирования текстовых фрагментов (за исключением элементов и других)...",
        "like_count": 100,
        "dislike_count": 100
    } for i in range(2)
]


def question(request):
    return render(request, 'one_question_page.html', {'main_questions': main_questions, 'answers': answers})


def tag(request):
    return render(request, 'tag.html', {'questions': questions})


settings = [
    {
        "login": "get_best_mark",
        "email": "technopark@mail.ru",
        "nickname": "Agent_007",
        "avatar_source_img": "C://img"
    } for i in range(1)
]


def settings(request):
    return render(request, 'settings.html', {'settings': settings})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
