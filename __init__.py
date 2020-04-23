import Game
from flask import Flask, render_template


app = Flask(__name__)

"""@brief This is a flask route for the first page

This routes the user to a login page that renders
login.html. The user will have to submit a username and password.
@param : none
"""
@app.route('/')
def login():
    return render_template('login.html')

"""@brief This is a flask route for the homepage

Once the user is logged in, it will route them to the home screen
which renders the home.html page.
@param : none
"""
@app.route('/home')
def home():
    return render_template('home.html')

"""@brief This is a flask route for the play page

If the user selects the play tab in the navbar, they will be
routed to the play page which renders play.html.
@param : none
"""
@app.route('/play')
def play():
    return render_template('play.html')

"""@brief This is a flask route for the about page

If the user selects the about tab in the navbar they will be routed
to the about page which renders about.html.
@param : none
"""
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
    ourgame = Game.Game()
    ourgame.gameloop()
