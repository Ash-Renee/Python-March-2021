from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect('/play')

@app.route('/play')
def hello():
    return render_template('index.html')

@app.route('/play/<int:num_box>')
def times(num_box):
    return render_template('index.html', num = num_box)

@app.route('/play/<int:num_box>/<color>')
def color(num_box, color):
    return render_template('index.html', num = num_box, tempColor = color)







if __name__=="__main__":
    app.run(debug=True)