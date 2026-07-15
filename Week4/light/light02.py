import requests 
import time 

MY_STUDENT_ID = "6710301034"
url = f"http://172.16.2.117:8088" 
LIGHTS = ["light_1", "light_2", "light_3", "light_4"]

def turn_on_light(light_id):
    api_url = f"{url}/api/{MY_STUDENT_ID}/lights/{light_id}"
    payload = {"status": "ON"} 

    
