from flask import Flask,render_template,redirect
app=Flask(__name__) #creating new flask class object

@app.route("/")
def main():
	return "My First Flask Web App"

@app.route("/demo")
def demo1():
	return "Demo Page"

@app.route("/admin")
def demo2():
	return "Admin Page"

@app.route("/user")
def demo3():
	return "User Page"

@app.route("/user/<name>")
def demo4():
	return "Hello %s"%name  # %s is parameter marker ie string

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/stock_manager_login")
def stock_manager():
	return render_template("stock_manager_login.html")

@app.route("/shop_owner_login")
def shop_owner():
	return render_template("shop_owner_login.html")

@app.route("/customer_registration")
def customerregistration():
	return render_template("customer_registration.html")

@app.route("/customer_login")
def customerlogin():
	return render_template("customer_login.html")

if __name__=='__main__':
	app.run(debug=True)