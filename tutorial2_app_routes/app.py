from flask import Flask, request

app = Flask(__name__)



# This is the route decorator. It tells Flask that the function below should be executed
# default route "/" is the root of the website
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/hello')
def hello(name):
    return 'Hello, World!'

# this is a url processer. It will take the name from the url and pass it to the function¨
# for example: http://127.0.0.1:8080/greet/Sodiq
@app.route('/greet/<name>')
def greet(name):
    return 'Hello, ' + name + '!'

# we can pass in integers as well. This will calculate the sum of the two numbers
# for example: http://127.0.0.1:8080/add/10/20
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f'The sum of {num1} + {num2} is {num1 + num2}'


# This is the route decorator. It tells Flask that the function below should be executed
# for example: http://127.0.0.1:8080/handle_url_params?name=Sodiq&age=20
@app.route('/handle_url_params')
def handle_url_params():
    return str(request.args)

# This is the route decorator. It tells Flask that the function below should be executed
# debug=True will automatically reload the server when you make changes to the code
# host='0.0.0.0' will make your server available from any device in your network
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
