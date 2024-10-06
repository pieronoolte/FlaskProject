from flask import Flask, render_template

#Create a Flask Instance
app= Flask(__name__)

# Create a rtoute decorator
@app.route('/')
# def index():
#     return "<h1>Hello Word!</h1>"
def index():
    stuff= "This is bold Text"
    favorite_pizza=["Pepeproni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", 
                           stuff = stuff,
                           favorite_pizza = favorite_pizza)

#localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

#Inalid URL
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

#Internal server Error
@app.errorhandler(500)
def page_server_error(error):
    return render_template("500.html"), 500

