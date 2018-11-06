'''Simple web page which display the date'''
from flask import Flask
import datetime

app = Flask(__name__)
 
@app.route("/")
def hello():
    myDate = datetime.datetime.now().strftime('Hello World! It''s %Y-%m-%d %H:%M:%S Week=%V TZ=%Z')
    return myDate
 
if __name__ == "__main__":
    app.run()
