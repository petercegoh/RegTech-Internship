from flask import Blueprint, render_template

# blueprints are modules (just reusable containers for functions, classes, variables)
# here, it contains related view functions that conveniently imports in __init__.py

# instance of Blueprint. stores the main pages of my project
# first arg is name of bp. 
bp = Blueprint("pages", __name__)

# two routes here.
# default route, the content on the page is hello home. 
# flask expects template to be in a templates/ directory. do no need to specify in path
@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")