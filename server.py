from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/<input>')
def say(input):
    return f'Hi {input}!'
@app.route('/repeat/<int:number>/<string:word>')
def repeat(number, word):
    return (word + " ") * number
@app.errorhandler(404)
def error(error):
    return 'Sorry! No response. Try again.'
if __name__=="__main__":
    app.run(debug=True)