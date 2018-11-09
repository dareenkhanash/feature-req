from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def features():
    return render_template('feature-requests.html')


@app.route('/request')
def request():
    return render_template('add-request.html')


if __name__ == '__main__':
    app.run(debug=True)
