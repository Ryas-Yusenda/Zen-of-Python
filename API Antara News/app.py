from src import Code
from flask import Flask, request
from src import res
app = Flask(__name__)


@app.route('/')
def home():
    param = request.args.get('q')
    if param is None:
        response = Code.index()
        return res.success(response)
    
    response = Code.search(param)
    return res.success(response)


if __name__ == "__main__":
    app.run(debug=False)
