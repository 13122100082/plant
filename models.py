from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
mysql = MySQL()
app.config['SQLALCHEMY_DATABASE_URI'] = 'plant'
app.config['MYSQL_DATABASE_PASSWORD'] = '123qwe'
app.config['MYSQL_DATABASE_DB'] = 'plant'
app.config['MYSQL_DATABASE_HOST'] = '192.168.65.200'
mysql.init_app(app)
"""

class Duty(db.Model):
    __tablename__ = 'tb_duty'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.String(1024), nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)
    is_show = db.Column(db.SmallInteger, nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, category_id, user_id, title, content, status, is_show, create_time):
        self.category_id = category_id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.status = status
        self.is_show = is_show
        self.create_time = create_time    

    def __repr__(self):
        return self.title


class Category(db.Model):
    __tablename__ = 'tb_category'

    category_id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(64), nullable=False, index=True)
    status = db.Column(db.SmallInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, category_id, name, status, create_time):
        self.category_id = category_id
        self.name = name
        self.status = status
        self.create_time = create_time    

    def __repr__(self):
        return self.name


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=True, index=True)
    password = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    role_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, password, phone, email, role_id,status, create_time):
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.role_id = role_id
        self.status = status
        self.create_time = create_time    

    def __repr__(self):
        return self.username



"""
https://github.com/lalor/todolist
https://github.com/ifwenvlook/blog
https://github.com/iamzcr/daily-duty-list
"""