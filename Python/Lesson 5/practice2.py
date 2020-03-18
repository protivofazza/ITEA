from datetime import datetime
import shelve
import sys


FILENAME = "SOCIAL_SHELVE"


class Post:

    posts = []

    def __init__(self, author, title, data):
        self._author = author
        self._title = title
        self._data = data
        self._date = datetime.now()
        with shelve.open(FILENAME) as database:
            database["posts"] += [self]

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @property
    def text(self):
        return self._data

    @property
    def date(self):
        return self.date

    def print_info(self):
        print(f"Title: {self._title}\nAuthor: {self._author}\nDate: {self._date}\n    {self._data}"
              f"\n**********")

    @classmethod
    def load_posts(cls):
        with shelve.open(FILENAME) as database:
            cls.posts = database["posts"]


class Login:
    _instances = None

    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super().__new__(cls)
        return cls._instances

    def __init__(self):
        self._logged = None

    @property
    def logged(self):
        return self._logged

    def login(self, login, password):
        for user in User.users:
            if login == user.login and password == user.password:
                self._logged = user
                break
        if not self._logged:
            print("Such combination of the login and password does not exist. Try one more time")

    def logout(self):
        self._logged = None
        print("Successfully logged out")


class Registration:
    _instances = None

    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super().__new__(cls)
        return cls._instances

    def _password_validation(self, password, password_verification):
        try:
            if password != password_verification:
                print("The passwords do not match")
                return False
            is_char = False
            is_digit = False
            for i in password:
                if 48 <= ord(i) <= 57:
                    is_digit = True
                elif 65 <= ord(i) <= 90:
                    is_char = True
                elif 97 <= ord(i) <= 122:
                    is_char = True
            if is_char and is_digit:
                return True
            print("The password must contain characters and digits")
            return False
        except TypeError:
            print("Type Error: your password must be of the 'str' type")
            return False
        except:
            print("Unknown Error")
            return False

    def _login_validation(self, login):
        if type(login) == str:
            for i in User.users:
                if i.login == login:
                    print("This login already exists")
                    return False
            return True
        else:
            print("Type Error: your password must be of the 'str' type")
            return False

    def register(self, login, password, password_verification, is_admin=False):
        if self._login_validation(login) and self._password_validation(password, password_verification):
            User.users.append(User(login, password, is_admin))
            print(f"Successfully registered the user '{login}'")
        else:
            print("Not registered. Try one more time")


class User:

    users = []

    def __init__(self, login, password, admin):
        self._login = login
        self._password = password
        self._registration_time = datetime.now()
        self._admin = admin
        with shelve.open(FILENAME) as database:
            database["users"] += [self]

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @property
    def admin(self):
        return self._admin

    def print_info(self):
        _posts = [post for post in Post.posts if post.author == self.login]
        print(f"Login: {self._login}. Registration Time: {self._registration_time}. Is This User An Admin:"
              f" {self._admin}. Total posts: {len(_posts)}")
        for post in _posts:
            post.print_info()
        print("*" * 30)

    def create_post(self, title, data):
        Post.posts.append(Post(self.login, title, data))

    @classmethod
    def load_users(cls):
        with shelve.open(FILENAME) as database:
            cls.users = database["users"]


registration_object = Registration()
login_object = Login()

Post.load_posts()
User.load_users()

while True:
    code = input("0: Exit. 1: Login. 2: Register\n")
    try:
        code = int(code)
    except TypeError:
        continue
    if code == 0:

        break
    elif code == 1:
        login = input("Login: ")
        password = input("Password: ")
        login_object.login(login, password)
        if login_object.logged:
            while True:
                if login_object.logged.admin:
                    code = input("0: Logout. 1: New Post. 2: All My Posts. 3: All Posts By Users. 4: All Users Info\n")
                else:
                    code = input("0: Logout. 1: New Post. 2: All My Posts\n")
                try:
                    code = int(code)
                except TypeError:
                    continue
                if code == 0:
                    login_object.logout()
                    break
                elif code == 1:
                    title = input("Title: ")
                    data = input("Post: ")
                    login_object.logged.create_post(title, data)
                elif code == 2:
                    _posts = [post for post in Post.posts if post.author == login_object.logged.login]
                    for post in _posts:
                        post.print_info()
                elif code == 3 and login_object.logged.admin:
                    for post in Post.posts:
                        post.print_info()
                elif code == 4 and login_object.logged.admin:
                    for user in User.users:
                        user.print_info()
            continue
        else:
            continue
    elif code == 2:
        login = input("Login: ")
        password = input("Password: ")
        password_verification = input("Password Verification: ")
        registration_object.register(login, password, password_verification)


"""
Admin user: 1 1q
User1: test test1
User2: test_2 test2
"""