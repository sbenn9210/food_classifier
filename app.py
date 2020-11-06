from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base.html', list_of_names=['chris', "Shawn", "Jackson"])

@app.route('/shawn')
def hello_shawn():
    return 'Hello Shawn'

@app.route('/<name>')
def greet(name):
    return f'Hello {name}'

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

# TODO: {print __name__}