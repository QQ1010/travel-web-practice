from flask import Flask,url_for,render_template,request,redirect,flash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST': 
        if login_check(request.form['username'],request.form['password']):
            flash('Login Success!')
            return redirect(url_for('menu',username=request.form.get('username')))        
    return render_template('login.html')
def login_check(username,password):
    if username == 'test' and password == '0000':
        return True
    else:
        return False

@app.route('/menu/<username>',methods=['GET', 'POST'])
def menu(username):
    return render_template('menu.html',username=username)

@app.route('/prepare',methods=['GET', 'POST'])
def prepare():
    return render_template('prepare.html')
@app.route('/implement' ,methods=['GET','POST'])
def implement():
    return render_template('implement.html')
@app.route('/review' ,methods=['GET','POST'])
def review():
    return render_template('review.html')
if __name__ == '__main__':
    app.debug = True
    app.secret_key = '123456'
    app.run()