from flask import *
import os
from hashlib import *
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
                os.system('echo "I am {}" > {}'.format(str(username), str(username)))
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
        file1=open('broadcast.txt', 'rb')
        broadcast=file1.read()
        if 'username' in request.cookies:
            user = request.cookies.get('username')
        else:
            user = "Anonymous"
        return render_template('index.html', user=render_template_string(user), text=str(file.read().decode()), memo=str(broadcast.decode()))
    elif request.method == 'POST':
        if 'username' in request.cookies:
            user = request.cookies.get('username')
        else:
            user = "Anonymous"
        msg=request.form['msg']
        os.system(f'echo "{str(user)} 說：{str(msg)}" >> msg.txt')
        response = make_response(redirect('/'))
        return response


@app.route("/admin-login", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'GET':
        return render_template('admin-login.html')
    elif request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        os.system(f'./check {username} {password}')
        file=open('admincheck.txt', 'rb')
        list_f=file.read()
        if 'True' not in str(list_f):
            return "<h1>Error</h1><br></br><h2>帳號密碼錯誤</h2>"
        else:
            response = make_response(redirect('/admin'))
            response.set_cookie('admin_auth', str(md5(username.encode()).hexdigest()))
        return response

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        if 'admin_auth' not in request.cookies:
            response = make_response(redirect('/admin-login'))
            return response
        else:
            file=open('userlist.txt', 'rb')
            list_f=file.read()
            file=open('broadcast.txt', 'rb')
            broadcast=file.read()
            return render_template('admin.html', pwd=str(list_f.decode()), memo=str(broadcast.decode()))
    else:
        memo=request.form['memo']
        os.system(f'echo "{memo}" > broadcast.txt')
        response = make_response(redirect('/admin'))
        return response

    
@app.route("/hackers")
def hackers():
    return "No hacker currently"

@app.route("/user/<user>", methods=['GET', 'POST'])
def user(user):
    if request.method == 'GET':
        if 'username' not in request.cookies:
            response = make_response(redirect('/login'))
            return response
        else:
            if request.cookies.get('username')!=user:
                response = make_response(redirect('/login?msg=登入錯誤：你不是該使用者無法操作該內容'))
                return response
            file=open(user, 'rb')
            list_f=file.read()
            return render_template('user.html', memo=str(list_f.decode()), user=user)
    else:
        user=request.cookies.get('username')
        memo=request.form['memo']
        os.system(f'echo "{memo}" > {user}')
        response = make_response(redirect(f'/user/{user}'))
        return response
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=30003)
