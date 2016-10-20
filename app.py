from flask import Flask
from twilio import twiml


app = Flask(__name__)

@app.route('/')
def hello():
    """test"""

    return "Hello World"


@app.route('/sms', methods = ['GET', 'POST'])
def sms():
    """Responding to incoming text messages"""

    response = response = twiml.Response()
    response.message('Hello from SF Python! :smiley_cat:')

    return str(response)





if __name__ == "__main__":
    app.run()