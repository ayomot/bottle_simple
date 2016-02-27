#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bottle
from bottle import run, template, request, response, redirect, html_escape
from bottle import route, get, post, static_file, TEMPLATE_PATH
import random
import string
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSS_DIR = os.path.join(BASE_DIR, 'htdocs/css')
JS_DIR = os.path.join(BASE_DIR, 'htdocs/js')
UPLOADS_DIR = os.path.join(BASE_DIR, 'htdocs/uploads')

@get('/')
def index():
    db = sqlite3.connect('db/post.db')
    conn = db.cursor()
    conn.execute("SELECT * FROM posts ORDER BY id DESC")
    posts = conn.fetchall()
    return template('index', posts = posts)

@post('/')
def post_data():
    ex_text = request.forms.get("ex_text")
    upload  = request.files.get('file')
    if not upload:
        return '画像は必須です'
    name, ext = os.path.splitext(upload.filename)

    if ext not in ('.png', '.jpg', '.jpeg'):
        return '投稿できる画像形式はjpgとpngだけです'

    st = string.digits + string.ascii_letters
    file_name = ''.join(random.choice(st) for i in range(16)) + ext
    save_path = os.path.join(UPLOADS_DIR, file_name)
    upload.save(save_path, True)

    db = sqlite3.connect('db/post.db')
    conn = db.cursor()
    conn.execute("INSERT INTO posts (text, img_file_name) VALUES (?, ?)",
            (ex_text, file_name))
    db.commit()
    redirect('/')

@get('/star/<post_id:int>')
def star(post_id):
    db = sqlite3.connect('db/post.db')
    conn = db.cursor()
    conn.execute("SELECT star_count FROM posts WHERE id = ?", (post_id,))
    post = conn.fetchall()
    if not post:
        return "error"
    new_star_count = post[0][0] + 1
    conn.execute("UPDATE posts SET star_count = ? WHERE id = ?", (new_star_count, post_id))
    db.commit()
    response.content_type = 'application/json'
    return {'star_count' : new_star_count}

def nl2br(s):
    """改行文字をbrタグに変換する
    """
    return html_escape(s).replace('\n','<br />')

@get('/example')
def example():
    return template('example')

@route('/css/<filename>')
def recoad_static(filename):
    return static_file(filename, root=CSS_DIR)

@route('/js/<filename>')
def recoad_static(filename):
    return static_file(filename, root=JS_DIR)
@route('/uploads/<filename>')
def recoad_static(filename):
    return static_file(filename, root=UPLOADS_DIR)

if __name__ == '__main__':
    run(host='localhost', post=8080, debug=True, reloader=True)
