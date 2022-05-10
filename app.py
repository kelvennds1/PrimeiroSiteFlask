# Importing Flask
from flask import Flask, render_template
import conversor
#Initalize app
app = Flask(__name__)

#Create pages
#Index:
@app.route('/')
def index():
    return render_template('index.html')

#Sign Up:
@app.route('/signup')
def signup():
    return render_template('signup.html')

#Bid
#@app.route('/bid')
#def bid():
#    value = conversor.cotacao()
#    usdbrl = value.bid()
#    return render_template('bid.html', usdbrl=usdbrl)

#Contacts
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)