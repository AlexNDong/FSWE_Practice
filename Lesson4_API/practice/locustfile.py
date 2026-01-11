### LOCUST ### to test performance of request API
from locust import HttpUser, task, between
# HttpUser plays a role of user/client - who request API http
# task: plays a role of actions the user request
# between: the time interval that user request
 
class WebsiteUser(HttpUser): # inheriate all attributes and methods of class HttpUser
    wait_time = between(1, 5) # simulate each request randomly from 1 to 5 seconds

    @task
    def create_item(self):
        data = {"name":"Item 1", "price":10.0} 
        self.client.post("/items/", json=data) # POST method (simulating the post request from client to server)
        # simulate the request from client
        # it will start another server named "http://0.0.0.0:8089" as testing server
        # in which we can simulate different user/client requesting API to server of "0.0.0.0:8000"

## To test performance of the RestAPI {main.app} in the main.py file, first we run the server using uvicorn: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
## To run locust in command: "locust" as the name is already "locustfile.py", when you run "locust" it will automatically run 