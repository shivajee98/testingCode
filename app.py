from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Redirect to index.html
    return redirect(url_for('index'))

@app.route('/index.html')
def index():
    # Render the index.html template
    return render_template('index.html')

@app.route('/data')
def data():
    return 'Data endpoint!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
