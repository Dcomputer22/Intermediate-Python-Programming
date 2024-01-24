import requests
from datetime import datetime

USERNAME = "dcomputer"
TOKEN = "abcdefuvwxyz1234"
GRAPH_ID = "mygraph1"

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

graph_constant = {
    "id": GRAPH_ID,
    "name": "Regulating Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_constant, headers=headers)
# print(graph_response.text)

pixel_formation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": '8.5',
}

# pixel_response = requests.post(url=pixel_formation_endpoint, json=pixel_config, headers=headers)
# print(pixel_response.text)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
pixel_data_dict = {
    "quantity": input("How many kilometers did you run today?: ")
}
update_response = requests.put(url=update_endpoint, json=pixel_data_dict, headers=headers)
print(update_response.text)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# delete_response = requests.delete(delete_endpoint, headers=headers)
#
# print(delete_response.text)
