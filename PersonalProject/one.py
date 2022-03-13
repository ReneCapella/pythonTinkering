# python3 -m venv venv
# . venv/bin/activate
# pip install Flask
# export FLASK_APP=one
# flask run

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def begin():
   return render_template('begin.html')

@app.route('/intro')
def intro():
   return render_template('intro.html')

@app.route('/one', methods=['POST', 'GET'])
def one():
    try:
        lonliest = '1'
        dict = request.form.to_dict()
        values = list(dict.values())
        keys = list(dict.keys())
        guess = values[0]
        which_guess = keys[0]
        if which_guess == 'guess':
            if guess == '1':
                return render_template('/one.html')
            else:
                error = 'nope'
                return render_template('/intro.html')
        elif which_guess == 'next_guess':
            if guess == '2':
                return render_template('/two.html')
            else:
                return render_template('/intro.html')
        elif which_guess == 'third_guess':
            print("we're here")
            if guess == 'no':
                return render_template('no.html')
            else:
                return render_template('/intro.html')
        elif which_guess == 'fourth_guess':
            if guess == 'yes':
                return render_template('yes.html')
            else:
                return render_template('/intro.html')
        elif which_guess == 'fifth_guess':
            if guess == lonliest:
                return render_template('/one2.html')
            else:
                return render_template('/intro.html')
        elif which_guess == 'sixth_guess':
            if guess == lonliest:
                return render_template('/one3.html')
            else:
                return render_template('/intro.html')
        elif which_guess == 'seventh_guess':
            if guess == lonliest:
                return render_template('/one4.html')
            else:
                return render_template('/intro.html')
        elif which_guess == 'eigth_guess':
            if guess == lonliest:
                return render_template('/one5.html')
            else:
                return render_template('/intro.html')
        elif which_guess == 'ninth_guess':
            if guess == lonliest:
                return render_template('/one6.html')
            else:
                return render_template('/intro.html')
        elif which_guess == 'tenth_guess':
            if guess == lonliest:
                return render_template('/one7.html')
            else:
                return render_template('/intro.html')
    except:
        return render_template('begin.html')


@app.route('/bridge')
def bridge():
    return render_template('/bridge.html')




if __name__ == '__main__':
   app.run(debug = True)
