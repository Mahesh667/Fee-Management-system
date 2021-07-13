#!/usr/bin/python3
import os

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
##postgress
engine = create_engine("mysql+pymysql://root:mahesh@localhost:3306/fee_management")


db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")
@app.route("/insert", methods=['GET'])
def insert():
    return render_template("insert.html")

@app.route("/view", methods=['POST', 'GET'])
def view():
    if request.method == "POST":

        fname = request.form.get("fname")
        lname = request.form.get("lname")
        session = request.form.get("session")
        sub_fee = request.form.get("sub_fee")
        due_fee = request.form.get("due_fee")
        tot_fee = request.form.get("tot_fee")
        db.execute("INSERT into student(firstname, lastname, session, submittedfee, duefee, totalfee) VALUES (:firstname, :lastname, :session, :submittedfee, :duefee, :totalfee)",
                {"firstname": fname, "lastname": lname, "session": session, "submittedfee": sub_fee, "duefee": due_fee, "totalfee": tot_fee})
        db.commit()

        # Get all records again
        students = db.execute("SELECT * FROM student").fetchall()
        return render_template("view.html", students=students)
    else:
        students = db.execute("SELECT * FROM student").fetchall()
        return render_template("view.html", students=students)




if __name__ == "__main__":
    app.run(debug=True)
