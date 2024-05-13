from flask import Flask, request, jsonify

app = Flask(__name__)

# to create a route: an endpoint, location on API we can go to get data
# @app.route("/")   # the path we want to access, the default root
# def home():
#     return "Home"  #some data we want to be available to the user when they reach 

# routes are GET by default
@app.route("/get-user/<user_id>") #path parameter <> its a dynamic value in the url
    # when they reach this ^ route, they will have access to this data
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "JOhn Doe",
        "email" :"john.doe@example.com"
    }

#query parameter, an extra param after the main path on the browser
    #get-user/123?extra="hello"

    # you trying to access a value called extra. 
    #   (could have been passed in the route as query param) 
    extra = request.args.get("extra")
    # if extra exists and was loaded,
    if extra:
        # add an extra key, and its value.
        user_data["extra"] = extra
    
    # flask parses the data to return as json.
    return jsonify(user_data), 200

# specify accepted methods for this route (in this case, POST)
@app.route("/create-user", methods = ["POST"])
def create_user():
    #we wna recieve some data from the body of the  request thats in json format
    # what is request in the first place??
    #data = request.get_json()

    params = request.form # get data from post type requests, in form format

    return jsonify(params), 201
    # we proabbly want to add this data to a DB, but for now just demo




# to run our flask application, runs the flask server
if __name__ == "__main__":
    app.run(debug=True)