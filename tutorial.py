from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

class FLaskOpen:
    def __init__(self):
        self.zar = 88

    def suma_zarurilor(self):
        if 3 == 3:
            return self.zar




if __name__ == '__main__':
    app.run(host='0:0:0:0')
