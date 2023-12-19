from flask import Flask

# an app is simply an object of class Flask
app = Flask(__name__)  #__name__ is the name of the current module


@app.route(
    "/"
)  #this registers a route, which is the part of the url after the domain name; @ means a decorator. Here, the route is simply to the home page.
def hello_world():
  # when the route "/" is accessed, this function is ran.
  return "Hello, world"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
