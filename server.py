from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if not 'count' in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/incrementTwo')
def incrementTwo():
    if 'count' in session:
        session['count'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/incrementCustom')
def customIncrement():

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)