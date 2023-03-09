from flask import Flask, render_template, request, redirect
from report import report_post

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'GET':
        return redirect('/')

    url = request.form.get('url')
    success = report_post(url)
    if success:
        return render_template('success.html')
    else:
        return render_template('failure.html')


app.run()
