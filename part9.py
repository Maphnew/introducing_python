#!

# HTTP

# * client

# - basic
# import urllib.request as ur
# url = 'http://quotesondesign.com/wp-json/posts'
# conn = ur.urlopen(url)
# print(conn)
# data = conn.read()
# print(data)
# print(conn.status)
# print(conn.getheader('Content-Type'))
# for key, value in conn.getheaders():
# 	print(key, value)

# - requests
# import requests
# url = 'http://quotesondesign.com/wp-json/posts'
# resp = requests.get(url)
# print(resp)
# print(resp.text)

# * server
# 

# * framework
# bottle
# flask
# 

# from bottle import route, run, static_file

# @route('/')
# def main():
# 	return static_file('index.html', root='.')
# run(host='localhost', port=9999)

# from bottle import route, run, static_file

# @route('/')
# def main():
# 	return static_file('index.html', root='.')

# @route('/echo/<thing>')
# def echo(thing):
# 	return "Say hello to my little friend: %s!"% thing

# run(host='localhost', port=9999)

# import requests
# resp = requests.get('http://localhost:9999/echo/Mothra')

# if resp.status_code == 200 and \
# 	resp.text == 'Say hello to my little friend: Mothra!':
# 	print('It worked!')
# else:
# 	print('Argh, got this:', resp.text)

# 9.2.5 Flask

# from flask import Flask, render_template

# app = Flask(__name__, static_folder='.', static_url_path='')

# @app.route('/')
# def home():
# 	return app.send_static_file('index.html')

# @app.route('/echo/<thing>')
# def echo(thing):
# 	return render_template('flask2.html', thing=thing)

# app.run(port=9999, debug=True)

# 9.2.6 비파이썬 웹서버
# 아파치와 mod_wsgi 모듈
# 엔진엑스와 uWSGI 앱 서버
import os
pid = os.getpid()
print(pid)
cwd = os.getcwd()
print(cwd)