from flask import Flask, render_template

app = Flask(__name__)

# how to pass values into the index.html file
@app.route('/')
def index():
    # these are the values i pass into the index.html file
    myValue = "sodiq"
    myResult = 10+30
    myList = [1,2,3,4,5]
    # render the index.html file inside the templates folder and pass the values
    return render_template('index.html', myValue=myValue, myResult=myResult, myList=myList)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

