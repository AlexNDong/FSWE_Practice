# This lesson needs to install FastAPI and Uvicorn for quickly code a RestAPI
# conda install fastapi (https://fastapi.tiangolo.com/tutorial/)
# conda install "uvicorn[standard]"

### PRACTICE 1 ###
# from fastapi import FastAPI

# # Make an instance representing our web
# app = FastAPI()

# @app.get("/") # @ means "decorator" to specify this is for restapi
# def read_root():
#     return {"message": "Hello K9"}
# # dictionary is like json {key:value} and RestAPI also uses json
# # to run this: we use "uvicorn" to host that on a server
# # /uvicorn main:app --host 0.0.0.0 --port 8000/ host it as in the server
# # "main is my python file", "app is the function", "host 0.0.0.0 is my local host", "port 8000"
# # This is representing 

### PRACTICE 2 ###
# Make an instance representing our web
from fastapi import FastAPI # fastapi allow to create webAPI (services that clients can call over HTTP)
from fastapi import HTTPException

app = FastAPI() # app instance represents web server, it will receive HTTP request, route HTTP request to Python function, send back response
# Define a route
@app.get("/add") # This "app" webserver has "GET" http method with URL path "/add"
# Define function that handle the request 
def add(a: float, b:float): # Fast API treat it as route handler
    result = a+b
    return {"operation": "add", "result": result} # in web, we always return the text json file (in form of dictionary)
# Note: one route "@app.get(/add)" ONLY take one route handler/function "def add()"
# We can have several route with the same @app instance of web server
@app.get("/")
def root():
    return {"message": "wellcome!"}
@app.get("/multiply")
def multiply(a: float, b:float):
    result = a*b
    return {"operation": "multiply", "result": result}
# Above example of "/add" or "/multiply" when we enter a and b are considered as "QUERY PARAMETERS"
# NOw, we will study "PATH PARAMETERS"
@app.get("/substract/{a}/{b}") # a and b are path parameters
def substraction(a:float, b:float):
    result = a - b
    return {"operation": "substract", "result": result}
# Use both PATH and QUERY together
@app.get("/devide/{a}")
def deviding(a:float,b:float): # a is as PATH, b is as query (http://0.0.0.0:8000/devide/10?b=5) [a is 10 "path", b is 5 "quert"]
    result = a/b
    return {"operation": "devide", "result": result}


# Example of POST method (send data to the server database, for example to create user information)
# However, we need to define Data model to use POST method (as we send our data to server system)
from pydantic import BaseModel

class User(BaseModel): # we need to define the base model in order to part using "POST" method
    name:str
    age:int

@app.post("/users")
def create_user(user: User):
    return {
        "message": f"User {user.name} with {user.age} years old created!",
        "user": user
    }

class Item(BaseModel):
    name: str
    price: float
@app.post("/items/")
def create_item(item: Item):
    return item.dict()

if __name__ == "__main__": # if we are running the file of itself -> it will return the name of the file
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # run server "app" in host "0.0.0.0" with port = "8000"


### Note
# To run server in uvicorn: use command  (uvicorn main:app --host 0.0.0.0 --port 8000 --reload) with (main) is a code file, (app) is server name initiated by FastAPI

### AFTER API ###
# After we finish writing our API, we need to test it, for example the amount of time needed to complete one request, how many request the API can execute at the same time ?
### LOCUST PYTHON ### - use to test request
# conda install locust