import requests 
import time 

MY_STUDENT_ID = "6710301034"
url = f"http://172.16.2.117:8088" 

def get_light(light_id):
    api_url = f"{url}/api/{MY_STUDENT_ID}/lights/{light_id}"
    
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        sorted_items = sorted(data.item(), key=lambda item:[1]['delay'])
        sorted_light_ids = [item[0] for item in sorted_items]

        print(f"{sorted_light_ids} Success!")
        return sorted_light_ids 
    else:
        print(f"(Code: {response.status_code})")
        return [] 
    
def turn_on_light(light_id):
    api_url = f"{url}/api/{MY_STUDENT_ID}/lights/{light_id}"
    payload = {"status": "ON"}

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        print(f"{light_id} Success!")
    else:
        print(f"(Code: {response.status_code})")

def main():
    start_time = time.time() 

    lights_to_turn = get_light()

    if lights_to_turn:
        for light in lights_to_turn:
            turn_on_light() 

    end_time = time.time()
    print(f"\nTotal time: {end_time - start_time:.2f} seconds.")

if __name__=="__main__":
    main()
