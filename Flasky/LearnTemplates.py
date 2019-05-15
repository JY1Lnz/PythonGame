from flask import Flask
from flask import render_template
import Flasky.datafile

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<name>')
def Hello(name=None):
    return render_template('hello.html', name=name, digits=[1,2,3,4,5], users=Flasky.datafile.users)

if __name__ == '__main__':
    app.run()
