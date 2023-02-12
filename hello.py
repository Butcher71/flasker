from flask import Flask, render_template

# create a Flask Instance

app = Flask(__name__)


#Create a route decorator
@app.route('/')

def index():
	first_name = "Alex"
	stuff = "This is <strong>Bold</strong> Text"
	favorite_pizza =  ["Pepperoni", "Cheese", "Mushrooms", 41]
	return render_template("index.html", first_name=first_name, stuff = stuff, favorite_pizza=favorite_pizza)


#FILTERS!!:
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags

#localhost:5000/user/Alex so this allows us to name the page so in browser type localhost:5000/user/Alex will generate Hello Alex!!! type localhost:5000/user/pete will will generate Hello Pete!!! 
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", user_name=name)
