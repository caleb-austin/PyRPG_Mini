import Game
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
    ourgame = Game.Game()
    ourgame.gameloop()
