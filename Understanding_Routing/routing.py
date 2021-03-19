from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!!"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/<int:number>/<thing>')
def repeat(number, thing):
    print(thing)
    return f"{thing} "* number


@app.route('/<something>')
def hello(something):
    return redirect("/error")

@app.route('/error')
def hi():
    return render_template('index.html')

if __name__ =="__main__":
    app.run(debug=True)