from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, my dear viewer/recuiter! It is just example on Flask for docker'

if __name__ == '__main__':
    app.debug = True
    app.run()
    