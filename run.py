"""
Import OS module
"""
import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env
# Must import request module from flask, import
# flash module must be imported to show feedback
# flash needs secret key


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")
    # Call the render template in return passing in the
    # file name of the html page you want to open as a string.
    # From there, create a directory called "templates" and create the HTML
    # files within that directory. MUST BE CALLED TEMPLATES.


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html",
                           page_title="About", company=data)
# Here we create another route which this time calls
# the about parameter see "/about". Then, in the HTML files
# in the hrefs for the nev links associated with the pages
# we need to user the follwoing syntax in the src attributes
# to activate the links {{url_for('file name - no extension')}}


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# DEBUG SHOULD NOT BE SET TO TRUE ON SUBMITTED WEBSITES AS IT IS
# A SECURITY FLAW, ALWAYS SET TO FALSE WHEN SUBMITTING.
