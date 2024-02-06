from flask import *
import os
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('reg.html')
    elif request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        repassword=request.form['re-password']
        if password!=repassword:
            return "<h1>Error</h1><br></br><h2>註冊密碼需相同喔~</h2>"
        else:
            file=open('userlist.txt', 'rb')
            if f"{username}:" in str(file.read()):
                return "<h1>Error</h1><br></br><h2>帳號已被註冊</h2>"
            else:
                os.system('./createaccount {} {}'.format(username, password))
                os.system('echo "<h1>{}</h1>" > {}'.format(str(username), str(username)))
            return "<h1>註冊成功</h1><br></br><a href='login'> 點此登入帳號 </a>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        file=open('userlist.txt', 'rb')
        list_f=file.read()
        if f"{username}:" not in str(list_f):
            return "<h1>Error</h1><br></br><h2>帳號不存在</h2>"
        elif f"{username}:{password}" not in str(list_f):
            return "<h1>Error</h1><br></br><h2>密碼錯誤</h2>"
        else:
            response = make_response(redirect('/'))
            response.set_cookie('username', username)
        return response

@app.route("/home", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        file=open('msg.txt', 'rb')
        if 'username' in request.cookies:
            user = request.cookies.get('username')
        else:
            user = None
        return render_template('index.html', user=render_template_string(user), text=str(file.read().decode()))
    elif request.method == 'POST':
        if 'username' in request.cookies:
            user = request.cookies.get('username')
        else:
            user = "Anonymous"
        msg=request.form['msg']
        os.system(f'echo "<p>{str(user)}said:{str(msg)}</p>" >> msg.txt')
        response = make_response(redirect('/'))
        return response


@app.route("/admin")
def admin():
    return "<h1>開發中，請之後再對我下手 >///< </h1>"

@app.route("/hackers")
def hackers():
    return "No hacker currently"

@app.route("/user/<user>")
def user(user):
    return f"<h1>{user}</h1><br>開發中，請之後再對我下手 >///< </br>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=30003)