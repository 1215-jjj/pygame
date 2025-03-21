from flask import Flask, render_template

app = Flask(__name__, template_folder='game/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/love')
def love():
    return render_template('love.html')

if __name__ == "__main__":
    app.run(debug=True)