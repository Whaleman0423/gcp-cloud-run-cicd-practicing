from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    """測試 flask api"""
    return 'Hello, World! Second'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)