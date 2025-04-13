from flask import Flask
app=Flask(__name__)

@app.route('/Hello')
def foo():
    return 'Welcome to Flask'
app.run(host='localhost',port=5000)