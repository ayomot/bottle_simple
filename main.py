#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bottle
from bottle import run, template, request, response, redirect
from bottle import route, get, post ,static_file, HTTPError, TEMPLATE_PATH
import os
TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSS_DIR = os.path.join(BASE_DIR, 'htdocs/css')
JS_DIR = os.path.join(BASE_DIR, 'htdocs/js')

@get('/')
def index():
    return template('index')

@post('/')
def post_data():
    return request.forms.get("ex_text")


@get('/example')
def example():
    return template('example')

@route('/css/<filename>')
def recoad_static(filename):
    return static_file(filename, root=CSS_DIR)

@route('/js/<filename>')
def recoad_static(filename):
    return static_file(filename, root=JS_DIR)

if __name__ == '__main__':
    run(host='localhost', post=8080, debug=True, reloader=True)
