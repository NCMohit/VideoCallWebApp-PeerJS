from flask import Flask, redirect, url_for, request, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'password12345'

db = SQLAlchemy(app)

class User(db.Model):
   user = db.Column(db.String(120), unique=True, nullable=False,primary_key=True)
   password_hash = db.Column(db.String(128))
   def set_password(self, password):
      self.password_hash = generate_password_hash(password)
   def check_password(self, password):
      return check_password_hash(self.password_hash, password)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login',methods=["POST","GET"])
def login():
   if(request.method == "POST"):
      user = request.form["user"]
      password = request.form["pass"]
      if(User.query.filter_by(user=user).first() is not None):
         if(User.query.filter_by(user=user).first().check_password(password)):
            session['user'] = user
            return redirect(url_for("main"))
         else:
            flash("Wrong password! Please try again")
            return redirect(url_for("login"))
      else:
         flash("Username dosen't exist! Make sure you typed the username correctly")
         return redirect(url_for("login"))
   else:
      return render_template('login.html')

@app.route('/register',methods=["POST","GET"])
def register():
   if(request.method == "POST"):
      user = request.form["user"]
      password = request.form["pass"]
      secondpass = request.form["secondpass"]
      if(password == secondpass):
         if(User.query.filter_by(user=user).first() is None):
            newuser = User(user=user)
            newuser.set_password(password)
            db.session.add(newuser)
            db.session.commit()
            return redirect(url_for("login"))
         else:
            flash("Error username already exists")
            return redirect(url_for("register"))
      else:
         flash("Error passwords do not match")
         return redirect(url_for("register"))
   else:
      return render_template('register.html')

@app.route('/main')
def main():
	if("email" not in session):
		flash("Please log in first to use the dashboard !")
		return redirect(url_for("login"))
	else:
		return render_template('main.html')

@app.route('/forgotpass')
def forgotpass():
   return render_template('forgotpassword.html')

@app.route('/logout')
def logout():
   session.clear()
   return redirect(url_for("index"))

if(__name__ == "__main__"):
	app.run(debug = True,host="0.0.0.0")