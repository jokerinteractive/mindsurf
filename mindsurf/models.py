# -*- coding: utf-8 -*-
from datetime import datetime
from flask.ext.login import UserMixin
from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.Unicode(100))
    last_name = db.Column('last_name', db.Unicode(100))
    username = db.Column('username', db.Unicode(80), unique=True, index=True)
    email = db.Column('email', db.Unicode(120), unique=True, index=True)
    password = db.Column(db.Unicode(100))
    registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return '<User %r>' % (self.username)


class UserInfo(db.Model):
    __tablename__ = 'users_info'
    id = db.Column(db.Integer, primary_key=True)

    key = db.Column(db.String(64), nullable=False)
    value = db.Column(db.String(64))

    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    user = db.relationship(User, backref='info')

    def __unicode__(self):
        return '%s - %s' % (self.key, self.value)


post_tags_table = db.Table('post_tags', db.Model.metadata,
                           db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
                           db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
                           )


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    user = db.relationship(User, backref='posts')

    tags = db.relationship('Tag', secondary=post_tags_table)

    def __unicode__(self):
        return self.title


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))

    def __unicode__(self):
        return self.name


class Tree(db.Model):
    __tablename__ = 'tree'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    parent_id = db.Column(db.Integer, db.ForeignKey('tree.id'))
    parent = db.relationship('Tree', remote_side=[id], backref='children')

    def __unicode__(self):
        return self.name


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.Unicode)
    title = db.Column(db.Unicode(66))
    description = db.Column(db.UnicodeText())
    text = db.Column(db.UnicodeText())
    date = db.Column(db.DateTime)

    def __unicode__(self):
        return self.title
