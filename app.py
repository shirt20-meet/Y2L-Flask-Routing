from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route('/')
def hello_world():
	return render_template("home.html")

@app.route('/store')
def store_world():
	return render_template("store.html",products=query_all())

@app.route('/about')
def about_world():
	return render_template("about.html")

@app.route('/add_to_cart/<int:productID>')
def add_cart(productID):
	add_to_cart((productID))
	return redirect(url_for("store_world"))



if __name__ == '__main__':
    app.run(debug=True)