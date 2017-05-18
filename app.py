from flask import Flask, render_template, url_for, redirect, request, flash
from models import *
import time

app = Flask(__name__)
app.secret_key = 'my is  some_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://plant:123qwe@192.168.65.200:3306/plant'
db.init_app(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/booklist')
def showbookname():
    """dsadkasl"""
    books = db.session.execute("SELECT id, title FROM todolist").fetchall()
 #   books = [dict(id=row[0], title=row[1]) for row in cursor.fetchall()]
    return render_template('book.html', books=books)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username or password:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                if user.password != password:
                    flash("密码错误")
                    return redirect(url_for('login'))
                else:
                    session['user_id'] = user.user_id
                    session['username'] = user.username
                    return redirect(url_for('duty'))
            else:
                flash("用户不存在")
                return redirect(url_for('login'))
        else:
            flash("请输入用户名或密码")
            return redirect(url_for('login'))

    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        if username or phone or email or password:
            res = User.query.filter_by(phone=phone).first()
            if res:
                flash("手机号已被注册")
                return redirect(url_for('register'))
            res = User.query.filter_by(username=username).first()
            if res:
                flash("用户名已被注册")
                return redirect(url_for('register'))

            user = User(username, password, phone, email, 1, 1, time.time())
            res = db.session.add(user)
            db.session.commit()

            if user.user_id:
                flash('注册成功，立即登录')
                return redirect(url_for('login'))
            else:
                flash('注册失败，请重试!')
                return redirect(url_for('register'))
        else:
            flash("field can not be empty")
            return redirect(url_for('register'))
    else:
        return render_template('register.html')       


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



"""
https://github.com/lalor/todolist
https://github.com/ifwenvlook/blog
https://github.com/iamzcr/daily-duty-list
"""