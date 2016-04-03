from flask import Flask, session, render_template, redirect, url_for, request
import json, requests

account_sid = "ACe1b841114bb532eab845e83995f2ab3c"
auth_token = "29851e1d4546574268457ff09472f807"

client = TwilioRestClient(account_sid, auth_token)

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
    return render_template('home.html')

@app.route('/personal', methods=['POST'])
def personal_info():
    session['name'] = request.form['name']
    session['number'] = request.form['number']
    return render_template('home.html')

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

def send_sms(progCount):
    contactNumber = session['number']
    userMessage = ""
    if progCount == 0:
        userMessage = "Good job! "
    elif progCount == 1:
        userMessage = "You're 25% of the way there!"
    elif progCount == 2:
        userMessage = "Wow! You're halfway through the book!"
    elif progCount == 3:
        userMessage = ""
    elif progCount == 4:
        userMessage = "Congratulations on finishing the book! Keep up the good work!"
        for friend in session['friends']:
            friendMessage = "Your friend " + session['name'] + " has finished a book!"
            client.messages.create(to="+1" + contactNumber, from_="+12015089231", body=friendMessage)
            
    client.messages.create(to="+1" + contactNumber, from_="+12015089231", body=userMessage)
    return

@app.route('/update', methods=['POST'])
def update_progress():
    book = session['books'][request.form['isbn']]
    lastpages = book['read']
    book['read'] = int(request.form['read'])
    if book['read'] >= book['pages']:
        send_sms(4)
    elif book['read'] >= book['pages'] * 0.75 and lastpages < book['pages'] * 0.75:
        send_sms(3)
    elif book['read'] == book['pages'] * 0.5 and lastpages < book['pages'] * 0.5:
        send_sms(2)
    elif book['read'] == book['pages'] * 0.25 and lastpages < book['pages'] * 0.25:
        send_sms(1)
    elif book['read'] == 0:
        send_sms(0)
    #return redirect(url_for('home'))

@app.route('/progress')
def get_progress():
    return str(session['books'])

@app.route('/delete')
def delete():
    return

if __name__ == '__main__':
    app.run(debug=True)
