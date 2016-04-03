from flask import Flask, session, render_template, redirect, url_for, request
import json, requests

app = Flask(__name__)
app.secret_key = 'asdf'

@app.route('/')
def index():
    if session['books']:
        return redirect(url_for('home'))
    session['books'] = []
    session['friends'] = []
    return render_template('index.html')

@app.route('/home')
def home():
    if not session['books']:
        session['books']= []
    return render_template('home.html', books=session['books'], friends=session['friends'])

@app.route('/add', methods=['POST'])
def add_book():
    r = json.loads(requests.get('http://openlibrary.org/search.json',
            params={'title':request.form['title'],'author':request.form['author']}))
    book = r['docs'][0]
    session['books'].push({book['isbn'][0]:{'title':book['title_suggest'],'author':book['author_name'][0],
        'cover':'http://covers.openlibrary.org/b/isbn/%s-M.jpg'%book['isbn'][0],
        'pages':int(request.form['pages']),'read':0}})
    return redirect(url_for('home'))

@app.route('/friends', methods=['POST'])
def friends():
    if request.form:
        session['friends'] = request.form['friends'].split(',')
        #return redirect(url_for('home'))
    return session['friends']

def send_sms():
    return

@app.route('/update', methods=['POST'])
def update_progress():
    book = session['books'][request.form['isbn']]
    book['read'] = int(request.form['read'])
    if book['read'] >= book['pages']:
        send_sms()
    #return redirect(url_for('home'))

@app.route('/progress')
def get_progress():
    return str(session['books'])

@app.route('/delete')
def delete():
    return

if __name__ == '__main__':
    app.run(debug=True)
