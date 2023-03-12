from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask import flash

# Credetials Of Database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Model 
class MyEmail(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.srno} - {self.email}"


# Retrive The All Record
@app.route("/",)
def home():

    all_detail = MyEmail.query.all()
    return render_template("index.html", all_detail=all_detail)


# Add The Record
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        mail = MyEmail(name=name, email=email)

        db.session.add(mail)
        db.session.commit()
        flash("Successfull inserted")
    return redirect("/")


# Delete The Record
@app.route("/delete/<int:srno>")
def delete(srno):

    data = MyEmail.query.filter_by(srno=srno).first()

    db.session.delete(data)

    db.session.commit()
    return redirect("/")


# Update The Record
@app.route("/update/<int:srno>", methods=["GET", "POST"])
def update(srno):

    if request.method == "POST":
        data = MyEmail.query.filter_by(srno=srno).first()
        data.name = request.form["name"]
        data.email = request.form["email"]

        db.session.commit()
        flash("Successfull Update")
        return redirect("/")


# Run The Code 
if __name__ == "__main__":
    app.secret_key = '12345'
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
