import requests 
import time 

MY_STUDENT_ID = "6710301034"
url = f"http://172.16.2.117:8088" 
LIGHTS = ["light_1", "light_2", "light_3", "light_4"]

def turn_on_light(light_id):
    api_url = f"{url}/api/{MY_STUDENT_ID}/lights/{light_id}"
    payload = {"status": "ON"}

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        data = response.json()
        print(f"{light_id} success!")
    else:
        print(f"{light_id} (Code: {response.status_code})")
def main():
    start_time = time.time()

    for light in LIGHTS:
        turn_on_light(light)

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2} seconds.")

if __name__=="__main__":
    main()