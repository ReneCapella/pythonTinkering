# python3 -m venv venv
# . venv/bin/activate
# pip install Flask
# export FLASK_APP=Flasker
# flask run

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/portfolio')
def portfolio():
   return render_template('portfolio.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact')
def result():
   return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug = True)
