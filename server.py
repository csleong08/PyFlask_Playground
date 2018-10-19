from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def playground():
    return 'Playground!'

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<times>/<color>')
def play2(times,color):
    return render_template('play2.html', boxes=int(times),myColor=color)

app.run(debug=True)