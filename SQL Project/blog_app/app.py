# handles database interactions, migrations, and functionalities
from flask import Flask
# this lets us grab a html file and user it as our template
from flask import render_template
from models import BlogPost, SessionLocal
# uses my BlogPost Class. SessionLocal helps link my python and the engine. 

# Function to add a new blog post
def create_post(title, content):
    session = SessionLocal()
    new_post = BlogPost(title=title, content=content)
    session.add(new_post)
    session.commit()
    session.close()
    print(f"Successfully created a new blog post: {title}")

# Example usage
create_post("My First Post", "This is the content of my first blog post!")

app = Flask(__name__)

@app.route("/")
def index():
    session = SessionLocal()
    # Get all blog posts from the database
    posts = session.query(BlogPost).all()  # Replace BlogPost with your model name
    session.close()
    # so you can pass dynamic information to the template. 
    # so like, this is what is happening when i pass a location to gmaps api url. 
    return render_template("index.html", posts=posts)  # Pass posts to the template

if __name__ == "__main__":
    app.run(debug=True)

# Additional functionalities can be added here, like
# retrieving posts, updating posts, deleting posts etc.
