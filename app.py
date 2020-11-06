from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/shawn')
def hello_shawn():
    return 'Hello Shawn'

@app.route('/<name>')
def greet(name):
    return f'Hello {name}'


if __name__ == '__main__':
    app.run(debug=True)