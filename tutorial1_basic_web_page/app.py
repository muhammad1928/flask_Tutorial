from flask import Flask

app = Flask(__name__)



# This is the route decorator. It tells Flask that the function below should be executed
# default route "/" is the root of the website
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


# This is the route decorator. It tells Flask that the function below should be executed
# debug=True will automatically reload the server when you make changes to the code
# host='0.0.0.0' will make your server available from any device in your network
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


# run python app.py in the terminal and click on the link to see the output to see the website