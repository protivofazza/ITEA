import shelve
from datetime import datetime

FILENAME = 'DBSHELVE'


class Post:

    posts = []

    def __init__(self, author, title, data):
        self._author = author
        self._title = title
        self._data = data
        self._date = datetime.now()


def create_user(id_, data):
    with shelve.open(FILENAME) as users:
        users[str(id_)] += [1]


def get_user(id_):
    with shelve.open(FILENAME) as users:
        print(users["posts"])


Post.posts.append(Post("Viktor", "Title1", "Data1"))
Post.posts.append(Post("Andrii", "Title2", "Data2"))
create_user("posts", Post.posts)
print(get_user(4))
