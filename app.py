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
	
@app.route('/cart')
def cart():
	cart_products=[]
	products=query_all()
	cart_DB=session.query(Cart).all()
	for p in products:
		for c in cart_DB:
			if p.id == c.ProductID:
				cart_products.append(p)

	return render_template("cart.html",products=cart_products)

@app.route('/control')
def control ():
return redirect(url_for("control.html"))

@app.route('/login', methods=["POST", "GET"])
def log_in():
	if (request.method=="POST"):
		username=request.form['username']
		password=request.form['password']
		if (username=='shir') and (password=='1234'):
			return redirect(url_for('control'))
		else:
			return redirect(url_for('hello_world'))
return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)