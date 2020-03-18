from threading import Thread
import requests


# 1-2


thread_number = 0
image_number = 0


def new_thread(name, daemon):
    def decorator(func):
        def wrapper(url):
            global thread_number
            thread_number += 1
            t = Thread(target=func, args=(url,), daemon=daemon, name=name+str(thread_number))
            t.start()
        return wrapper
    return decorator


@new_thread("download_image", False)
def download_image(url):
    global image_number
    response = requests.get(url)
    f = open("Animal"+str(image_number)+".jpg", "wb")
    image_number += 1
    if response.ok:
        for block in response.iter_content(1024):
            if not block:
                break
            f.write(block)


urls = [
    "https://besplatka.ua/aws/31/94/62/90/xomyachki-photo-cbef.jpg",
    "https://dl1.eduget.com/get/news/348526ea8b5b392a3ebe3082c761f225.jpg?bx=0&by=13&bw=449&bh=337",
    "https://www.meme-arsenal.com/memes/4ab9b67a0fcbc211e26408af2d3fd811.jpg",
    "https://i.pinimg.com/originals/a9/53/66/a95366ce365d4b8c70515d9310ec1866.jpg",
    "https://tayniymir.com/wp-content/uploads/2016/12/k-chemu-snyatsya-malenkie-sobachki2.jpg",
    "https://bipbap.ru/wp-content/uploads/2017/10/2015-10-15_175403ya.jpg",
    "https://pesikmal.ru/wp-content/uploads/2017/01/Foto1.jpg",
    "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
    "https://cs7.pikabu.ru/post_img/big/2019/01/22/10/1548178639131425422.jpg",
    "https://lapo4ka.com/uploads/product/3500/3591/homjak.jpg"
]

for url_ in urls:
    download_image(url_)


# 3

class MyFileManager:

    def __init__(self, path, mode='r'):
        self._path = path
        self._mode = mode

    def __enter__(self):
        return open(self._path, self._mode)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with MyFileManager("test.txt", 'r') as file:
    line = file.readline()
    print("Text in the file:" + line)