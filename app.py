from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def features():
    return render_template('feature-requests.html')


@app.route('/request')
@app.route('/request/<request_id>')
def editrRequest(request_id=None):
    return render_template('request.html',request_id=request_id)


if __name__ == '__main__':
    app.run(debug=True)
