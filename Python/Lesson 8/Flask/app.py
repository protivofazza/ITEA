from flask import Flask
from flask import render_template
from db import posts

app = Flask(__name__)


@app.route('/')
def index():
    page_title = "MyPage"
    name = 'Viktor'
    return render_template('index.html', page_title=page_title, name=name)


@app.route('/hi')
def hola():
    names = ['Anton', 'Max', 'John', 'Mike', 'Louiz', 'Ann']
    return render_template('greetings.html', names=names)


@app.route('/posts/<int:post_id>')
@app.route('/posts')
def posts_(post_id=None):
    if post_id:
        return render_template('post_body.html', post=posts[post_id-1])
    return render_template('posts.html', posts=posts)




if __name__ == '__main__':
    app.run(port=5001, debug=True)
