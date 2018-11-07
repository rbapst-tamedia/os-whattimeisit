'''Simple web page which display the date'''
import datetime
from flask import Flask

APP = Flask(__name__)

@APP.route("/")
def hello():
    '''Simple page which shows date, time, week number and TZ'''
    my_date = datetime.datetime.now().strftime('Hello World! It''s %Y-%m-%d %H:%M:%S Week=%V TZ=%Z')
    return my_date

if __name__ == "__main__":
    APP.run()
