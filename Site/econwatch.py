import os
from csv_vars import *
from flask import Flask, render_template


US_data_dir = "/home/cane/Documents/dev/Econ-Watch/Data/US"

app = Flask(__name__)

test = "Hello World!!"

data = csv_line1(os.path.join(US_data_dir,'BASE.csv'))

@app.route("/")
def home():
    return render_template('home.html', test=test, data=data)


if __name__=='__main__':
    app.run(debug=True)


