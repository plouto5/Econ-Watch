from flask import Flask, render_template
app = Flask(__name__)

test = "Hello World!!"

@app.route("/")
def home():
    return render_template('home.html', test=test)


if __name__=='__main__':
    app.run(debug=True)


