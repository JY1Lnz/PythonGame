from flask import Flask
from flask import render_template
from jinja2 import Template

app = Flask(__name__)


@app.route('/user/<username>')
def helloworld(username):
    # show the user profile for that user
    return 'User %s' % username
# 变量规则 通过在URL中的一部分标记为<variable_name>就可以在URL中添加变量


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/')
def entrance():
    return 'The first page'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
    )
