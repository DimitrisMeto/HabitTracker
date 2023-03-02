import requests
import datetime as dt

USERNAME = "USERNAME"
TOKEN = "TOKEN"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

new_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = dt.datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today? "),
}

response = requests.post(url=new_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_pixel_endpoint = f"{new_pixel_endpoint}/20230111"

update_data = {
    "quantity": "4"
}

# response = requests.put(url=update_pixel_endpoint, json=update_data, headers=headers)
# print(response.text)

delete_endpoint = f"{new_pixel_endpoint}/20230111"

# response = requests.delete(delete_endpoint, headers=headers)
# print(response.text)
