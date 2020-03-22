import sqlite3
import os

# __connection = None
# Подключение
# def get_connection():
#     global __connection
#     if __connection is None:
#         Base_DIR = os.path.dirname(__file__)
#         __connection = sqlite3.connect(Base_DIR + '/books.db', check_same_thread=False)
#         print("Connected to BD")
#     return __connection
def conection():
    Base_DIR = os.path.dirname(__file__)
    global conn
    conn = sqlite3.connect(Base_DIR + '/books.db', check_same_thread=False)
    return conn

def get_conn():
    return conn

# Инициализация ДБ
def init_db():
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys=on')

    # Создание таблицы books
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
              id_book     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              book_name   TEXT NOT NULL,
              author      TEXT NOT NULL,
              style       TEXT NOT NULL,
              count       INTEGER,
              price       INTEGER NOT NULL,
              img         TEXT,
              emoji       TEXT NOT NULL,
              page_count  INTEGER
        )
    ''')
    conn.commit()
    c.close()


def insert_book(book_name, author, style, count, price, img, emoji, page_count, id_book=None):
    c = conn.cursor()
    temp = (id_book, book_name, author, style, count, price, img, emoji, page_count)
    c.executemany('INSERT INTO books VALUES(?,?,?,?,?,?,?,?,?)', (temp,))
    conn.commit()
    print('books updated')
    c.close()


# init_db()
# insert_book('Книга_1', 'Автор_1', 'Любовынй роман', 4, 100, 'Book.png', 'Романтичные,Сексуальные,Трогательные', 888)
# insert_book('Книга_2', 'Автор_2', 'Фантастика', 5, 150, 'Book.png', 'Мистика,Экшн,Волнующие,Странные', 162)
# insert_book('Книга_3', 'Автор_3', 'Здоровье.Фитнес.Спорт', 6, 120, 'Book.png', 'Вдохновение,Молодежный', 362)
# insert_book('Книга_4', 'Автор_4', 'Фантастика', 7, 110, 'Book.png', 'Мистика,Научные,Экшн,Жестокие', 58)
# insert_book('Книга_5', 'Автор_1', 'Комиксы', 8, 200, 'Book.png', 'Смешные,Странные,Волнующие,Молодежные,Трогательные', 35)
# insert_book('Книга_6', 'Автор_2', 'Комиксы', 9, 250, 'Book.png', 'Жестокие,Страшные', 20)
# insert_book('Книга_7', 'Автор_3', 'Биография', 8, 100, 'Book.png', 'Вдохновение,Научные,Добрые', 97)
# insert_book('Книга_8', 'Автор_4', 'Детектив', 7, 130, 'Book.png', 'Странные,Мистика,Умные,Волнующие', 105)
# insert_book('Книга_9', 'Автор_1', 'Детектив', 6, 150, 'Book.png', 'Жестокие,Трогательные,Волнующие,Экшн', 85)
# insert_book('Книга_10', 'Автор_2', 'Энциклопедия', 5, 140, 'Book.png', 'Умные,Научные,Молодежные', 5000)


def search_by_author(author):
    conn()
    c = conn.cursor()
    temp = []
    c.execute('''SELECT * FROM books
                 WHERE author = (?)''', (author,))
    all_book = c.fetchall()
    print(len(all_book))
    l = len(all_book)
    for i in range(l):
        print(all_book[i][1])
        temp.append(
            {'book_name': all_book[i][1], 'author': all_book[i][2], 'style': all_book[i][3], 'count': all_book[i][4],
             'price': all_book[i][5], 'img': all_book[i][6], 'emoji': all_book[i][7], 'page_count': all_book[i][8],'description': all_book[i][9]})
    print(temp)
    return temp


def search_by_emoji(emoji):
    conection()
    temp = []
    c = conn.cursor()
    c.execute('''SELECT id_book FROM books''')
    l = len(c.fetchall())
    for i in range(l):
        c.execute('''SELECT emoji FROM books
                     WHERE id_book = (?)''', (i + 1,))
        temp_emoji = "".join(c.fetchone())
        if emoji in temp_emoji:
            c.execute(''' SELECT * FROM books
                          WHERE id_book = (?)''', (i + 1,))
            book = c.fetchone()
            temp.append({'book_name': book[1], 'author': book[2], 'style': book[3],
                         'count': book[4], 'price': book[5], 'img': book[6],
                         'emoji': book[7], 'page_count': book[8],'description': book[9]})
    print(temp)
    c.close()
    return temp


def search_by_style(style):
    c = conn.cursor()
    temp = []
    c.execute('''SELECT * FROM books
                 WHERE style = (?)''', (style,))
    all_book = c.fetchall()
    l = len(all_book)
    for i in range(l):
        temp.append({'book_name': all_book[i][1], 'author': all_book[i][2], 'style': all_book[i][3],
                     'count': all_book[i][4], 'price': all_book[i][5], 'img': all_book[i][6],
                     'emoji': all_book[i][7], 'page_count': all_book[i][8], 'description': all_book[i][9]})
    print(temp)
    return temp
