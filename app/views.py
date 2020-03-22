import os
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
from .BD import get_conn
from .BD import search_by_emoji


def index(request):
    return render(request, "index.html")


def choose_emoji(request):
    return render(request, "choose_emoji.html")


def emoji_books(request):
    emojy_name = request.GET.get("id", 0)
    emojis = {
        'Смешные': '😂',
        'Романтичные': '❤️',
        'Умные': '🤯',
        'Жестокие': '🔪',
        'Мистика': '👻',
        'Экшн': '😎',
        'Сексуальные': '🔞',
        'Вдохновение': '🤔',
        'Страшные': '😱',
        'Странные': '😟',
        'Молодежные': '🤪',
        'Трогательные': '😥',
        'Научные': '🤖',
        'Волнующие': '😰',
        'Добрые': '😊',
        'Грустные': '😔'
    }
    emoji = emojis[emojy_name]

    db_data = search_by_emoji(emojy_name)

    data = {}
    data["emoji"] = emoji
    data["emojy_name"] = emojy_name
    # print(db_data[:]['img'])

    for i in range(len(db_data)):
        data['book_img_path' + str(i)] = 'static/img/books/' + db_data[i]['img'].replace(' ', '')
        data['book_name' + str(i)] = db_data[i]['book_name']
        data['author' + str(i)] = db_data[i]['author']
        data['description' + str(i)] = db_data[i]['description']
        data['check_img' + str(i)] = os.path.exists('static/img/books/' + db_data[i]['img'].replace(' ', ''))
        print(os.path.exists('static/img/books/' + db_data[i]['img'].replace(' ', '')))
        if i == 5:
            break

    data["i"] = i
    get_conn().close()
    return render(request, "emoji_books.html", data)



def profile(request):
    return render(request, "profile.html")
