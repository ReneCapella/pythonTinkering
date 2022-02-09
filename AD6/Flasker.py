# python3 -m venv venv
# . venv/bin/activate
# pip install Flask
# export FLASK_APP=Flasker

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello_user/<user>')
def hello_name(user):
   return render_template('hello_user.html', name = user)

@app.route('/hello/<int:score>')
def hello_score(score):
   return render_template('hello.html', marks = score)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)


if __name__ == '__main__':
   app.run(debug = True)
