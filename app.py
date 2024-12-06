from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.getenv('MY_NAME', 'World')
    return f'Hello, my name is {name}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
