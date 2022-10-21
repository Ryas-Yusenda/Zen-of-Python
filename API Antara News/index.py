from src import Code
from flask import Flask, request
from src import res
app = Flask(__name__)

# import module from ./src


@app.route('/')
def home():
    response = Code.index()
    return res.success(response)


@app.route('/search/')
def search():
    param = request.args.get('q')
    print(param)
    response = Code.search(param)
    return res.success(response)


if __name__ == "__main__":
    app.run(debug=True)
