import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    # Call the render template in return passing in the
    # file name of the html page you want to open as a string.
    # From there, create a directory called "templates" and create the HTML
    # files within that directory. MUST BE CALLED TEMPLATES.


@app.route("/about")
def about():
    return render_template("about.html")
# Here we create another route which this time calls
# the about parameter see "/about". Then, in the HTML files
# in the hrefs for the nev links associated with the pages
# we need to user the follwoing syntax in the src attributes
# to activate the links {{url_for('file name - no extension')}}


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# DEBUG SHOULD NOT BE SET TO TRUE ON SUBMITTED WEBSITES AS IT IS
# A SECURITY FLAW, ALWAYS SET TO FALSE WHEN SUBMITTING.
