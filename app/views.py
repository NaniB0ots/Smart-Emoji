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
    book_name = db_data[0]['book_name']
    author = db_data[0]['author']
    data = {}
    data["emoji"] = emoji
    data["emojy_name"] = emojy_name

    for i in range(len(db_data)):
        data['book_img_path' + str(i)] = 'static/images/books/Book.png'  # + db_data[i]['img']
        data['book_name' + str(i)] = db_data[i]['book_name']
        data['author' + str(i)] = db_data[i]['author']
        if i == 5:
            break

    data["i"] = i
    # data = {
    #     "emoji": emoji,
    #     "book_img_path": "static/images/books/book1.jpg",
    #     "book_name": book_name,
    #     "author": author
    # }
    get_conn().close()
    return render(request, "emoji_books.html", data)
