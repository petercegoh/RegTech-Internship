from flask import Flask
from board import pages

#packages represent physical directories
#A directory becomes a package when it contains a special file named __init__.py

# application factory lets us scale projects. 
# Instead of having all our code at this file, have func that inits and returns my app. 
def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)
    return app

# # app object
# app = Flask(__name__)

# # default route, when we go to this location, the home function is called.
# # these functions are called views.
# @app.route("/")
# def home():
#     return "Hello, World!"

# if __name__ == "__main__":
#     # Flask dev server defaults to port 5000. 
#     # We change to 8000 bc AirPlay Reciever uses this port.
#     app.run(host="0.0.0.0", port=8000, debug=True)

    